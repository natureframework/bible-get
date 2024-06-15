# bible-get

A command line tool to get Bible verses.

## Example #1

```sh
bible-get genesis 1 1
```

Output

```txt
בראשית ברא אלהים את השמים ואת הארץ
```

## Example #2

```sh
bible-get john 1 1
```

Output

```txt
ΕΝ ΑΡΧΗΙ ΗΝ Ο ΛΟΓΟΣ ΚΑΙ Ο ΛΟΓΟΣ ΗΝ ΠΡΟΣ ΤΟΝ ΘΕΟΝ ΚΑΙ ΘΕΟΣ ΗΝ Ο ΛΟΓΟΣ
```

## Requirements

1. Python 3.9 or above
2. Git

## Install

```sh
pip install git+https://github.com/natureframework/bible-get.git
```

## Bible Data

Download or clone the [bible](https://github.com/ivandustin/bible) repository.
Create `BIBLE_HOME` environment variable and set its value to the path of the bible repository.

## Reference Format

See the [reference-parser](https://github.com/natureframework/reference-parser) repository for the supported reference format.
