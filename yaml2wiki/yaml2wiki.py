#!/usr/local/bin/python
"""Parses a YAML file and creates corresponding wiki pages on a
Wikimedia-powered wiki.

A username or password can be specified on the commandline or in the file. If
no password is specified, you will be prompted for one.

Sample input file:

---
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
"""
import argparse
import sys
import wikitools
import yaml

parser = argparse.ArgumentParser(description=globals()['__doc__'],
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('input', type=argparse.FileType('r'), nargs='?',
                    help='Filename of YAML file.')
parser.add_argument('-u', '--url', help='URL to api.php on the wiki server.')
parser.add_argument('--username', help='Account username.')
parser.add_argument('--password', help='Account password.')
parser.add_argument('--create', choices=('nocreate', 'createonly'),
                    help='Control if pages are created or not.')


if __name__ == '__main__':
    args = parser.parse_args()

    # Input is file or standard input
    input_yaml = args.input
    if input_yaml is None:
        input_yaml = sys.stdin.read()

    input_data = yaml.load(input_yaml)

    try:
        url = args.url or input_data['url']
        username = args.username or input_data['username']
    except KeyError:
        sys.exit('URL and/or Username not specified.')
    password = args.password or input_data.get('password', False)

    wiki = wikitools.Wiki(url)
    wiki.login(username, password)

    edit_kwargs = {}
    if args.create is not None:
        edit_kwargs[args.create] = 'on'

    for page_data in input_data['pages']:
        print 'Creating page: %s' % page_data['title']
        page = wikitools.Page(wiki, page_data['title'])
        page.edit(text=page_data['body'], **edit_kwargs)

    print 'Pages created successfully.'
