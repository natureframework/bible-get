from referenceparser.classes.reference import Reference
from pandas import DataFrame


def select(book: DataFrame, reference: Reference) -> DataFrame:
    chapters = book["chapter"].astype(str)
    verses = book["verse"].astype(str)
    width = max(chapters.str.len().max(), verses.str.len().max())
    chapters = chapters.str.zfill(width)
    verses = verses.str.zfill(width)
    index = chapters.str.cat(verses).astype(int)
    start = int(
        str(reference.start.chapter).zfill(width)
        + str(reference.start.verse).zfill(width)
    )
    end = int(
        str(reference.end.chapter).zfill(width) + str(reference.end.verse).zfill(width)
    )
    return book[index.between(start, end)]
