import argparse
from dundie.core import load
# from .core import load ---> Relative import

def main():
    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards CLI",
        epilog="Use with cautious"
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "send"),
        default="help",
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="File path to load",
        default=None,
    )
    args = parser.parse_args()
    globals()[args.subcommand](args.filepath)

