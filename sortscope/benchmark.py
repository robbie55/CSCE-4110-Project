"""Benchmark table and plot (saved to figures/). Owner: Robbie."""

import random
import time

import matplotlib

matplotlib.use("Agg")  # save to file only; no window
import matplotlib.pyplot as plt

from sortscope.sorts import ALGORITHMS
from sortscope.stats import Stats

SIZES = [100, 500, 1000, 2000]
REPEATS = 3
INPUT_TYPES = ["random", "sorted", "reversed"]
PLOT_PATH = "figures/benchmark.png"


def make_inputs(n: int) -> dict[str, list[int]]:
    """Return the three input lists of size n."""
    return {
        "random": random.Random(0).sample(range(n), n),
        "sorted": list(range(n)),
        "reversed": list(range(n, 0, -1)),
    }


def benchmark() -> None:
    # times[input_type][algorithm] = fastest time (ms) for each size in SIZES
    times = {}
    for input_type in INPUT_TYPES:
        times[input_type] = {}
        for name in ALGORITHMS:
            times[input_type][name] = []

    print(f"{'Algorithm':<10} {'Input':<9} {'n':>5} {'Time (ms)':>10} {'Comparisons':>12} {'Swaps/Moves':>12}")
    print("-" * 63)

    for name, sort in ALGORITHMS.items():
        for input_type in INPUT_TYPES:
            for n in SIZES:
                data = make_inputs(n)[input_type]
                best_ms = float("inf")
                stats = Stats()
                for _ in range(REPEATS):
                    stats = Stats()
                    start = time.perf_counter()
                    sort(data, stats)
                    elapsed_ms = (time.perf_counter() - start) * 1000
                    best_ms = min(best_ms, elapsed_ms)

                times[input_type][name].append(best_ms)
                print(
                    f"{name:<10} {input_type:<9} {n:>5} {best_ms:>10.3f} "
                    f"{stats.comparisons:>12} {stats.swaps:>12}"
                )

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
    for ax, input_type in zip(axes, INPUT_TYPES):
        for name in ALGORITHMS:
            ax.plot(SIZES, times[input_type][name], marker="o", label=name)
        ax.set_title(f"{input_type} input")
        ax.set_xlabel("n")
        ax.set_ylabel("time (ms)")
        ax.set_yscale("log")
        ax.legend()
    fig.tight_layout()
    fig.savefig(PLOT_PATH)
    plt.close(fig)
    print(f"\nSaved plot to {PLOT_PATH}")
