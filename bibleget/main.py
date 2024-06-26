from pathlib import Path
from os import environ
from sys import argv
from pandas import read_csv
from referenceparser import parse
from .select import select


def main():
    reference = parse(" ".join(argv[1:]))
    directory = Path(environ["BIBLE_HOME"]) / "data"
    book = reference.book.replace(" ", "-")
    filepath = next(directory.glob(f"*/*-{book}.csv"))
    dataframe = select(read_csv(filepath), reference)
    print(" ".join(dataframe["word"]))
