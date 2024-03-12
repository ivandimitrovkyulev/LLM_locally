from argparse import ArgumentParser

from src import __version__


# Create CLI interface
parser = ArgumentParser(
    usage="python3 %(prog)s <command> [<args>] \n",
    description="Run Large Language Model (LLM) locally.",
    epilog=f"Version - {__version__}",
)

parser.add_argument(
    "-d",
    "--directory-path",
    default="/data",
    help=f"Directory path containing documents to be loaded."
)
parser.add_argument(
    "-v",
    "--version",
    action="version",
    version=__version__,
    help="Prints the program's current version."
)
