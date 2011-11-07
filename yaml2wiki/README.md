# yaml2wiki

Parses a YAML file and creates corresponding wiki pages on a
Wikimedia-powered wiki.

A username or password can be specified on the commandline or in the file. If
no password is specified, you will be prompted for one.

Tested on OS X 10.6 with Python 2.7.

## Install

1. `pip install -r requirements.txt`
2. `chmod +x yaml2wiki.py`
3. `./yaml2wiki.py --help`

## Sample input file

```yaml
url: http://test2.wikipedia.org/w/api.php
username: testuser
password: asdf1234
pages:
  -
    title: Page Title
    body: |
      Content of your wiki page in [[wiki markup]].
  -
    title: Another Page Title
    body: |
      The bar above makes every newline significant.
      Without it there would be no newline between this line and the last.

      Without it there would be one newline between this line and the last.
```
