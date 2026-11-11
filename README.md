# SortScope

Sorting algorithm visualizer and benchmark for CSCE 4110 (Algorithms).

**Team:** Robbie McLaughlin, Aisha Aloma, Hamidat Oloko

SortScope implements five sorting algorithms from scratch (bubble, insertion, selection, merge, quick), animates them in the terminal, and benchmarks their runtime, comparisons, and swaps on random, sorted, and reversed inputs.

## Setup

Requires Python 3.10+.

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python -m sortscope visualize bubble          # animate a sort
python -m sortscope visualize quick --size 20
python -m sortscope benchmark                 # table + plot in figures/
pytest                                        # run tests
```

## Project layout

| Path | Purpose | Owner |
|---|---|---|
| `sortscope/sorts/` | One file per algorithm | All |
| `sortscope/stats.py` | Counters and step-callback type | — |
| `sortscope/visualize.py` | Terminal animation | Aisha |
| `sortscope/benchmark.py` | Timing table and plot | Robbie |
| `tests/` | Correctness tests | Hamidat |
| `figures/` | Saved plots for the report | — |

## Adding a sort

Every sort has the same signature:

```python
def my_sort(data: list[int], stats: Stats, on_step: StepCallback | None = None) -> list[int]:
```

- Return a sorted **copy**; never modify `data`.
- Increment `stats.comparisons` and `stats.swaps` as you go.
- Call `on_step(current_list)` after each step if it's given (drives the visualizer).

Then register it in `ALGORITHMS` in `sortscope/sorts/__init__.py`. Tests pick it up automatically.
