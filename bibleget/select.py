from referenceparser.classes.reference import Reference
from pandas import DataFrame


def select(book: DataFrame, reference: Reference) -> DataFrame:
    chapters = book["chapter"]
    verses = book["verse"]
    start = (chapters >= reference.start.chapter) & (verses >= reference.start.verse)
    end = (chapters <= reference.end.chapter) & (verses <= reference.end.verse)
    return book[start & end]
