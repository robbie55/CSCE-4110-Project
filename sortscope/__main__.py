import argparse

from sortscope.benchmark import benchmark
from sortscope.sorts import ALGORITHMS
from sortscope.visualize import visualize


def main() -> None:
    parser = argparse.ArgumentParser(prog="sortscope")
    commands = parser.add_subparsers(dest="command", required=True)

    vis = commands.add_parser("visualize", help="animate a sort in the terminal")
    vis.add_argument("algorithm", choices=ALGORITHMS)
    vis.add_argument("--size", type=int, default=15)

    commands.add_parser("benchmark", help="time every sort and save a plot")

    args = parser.parse_args()
    if args.command == "visualize":
        visualize(args.algorithm, args.size)
    else:
        benchmark()


if __name__ == "__main__":
    main()
