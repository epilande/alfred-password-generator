#!/usr/bin/python3

import os
import sys
import secrets
import json

defaultLength = os.environ['defaultLength']
letters = os.environ['letters']
digits = os.environ['digits']
punctuation = os.environ['punctuation']

length = int(sys.argv[1]) if len(sys.argv) > 1 else int(defaultLength)

combinations = [
    {
        'title': f"Generate password {length} characters",
        'combo': letters + digits + punctuation
    },
    {
        'title': f"{length} characters - Letters",
        'combo': letters
    },
    {
        'title': f"{length} characters - Letters + Digits",
        'combo': letters + digits
    },
    {
        'title': f"{length} characters - Letters + Punctuation",
        'combo': letters + punctuation
    }
]


def item(d):
    password = ''.join(secrets.choice(d['combo']) for i in range(length))
    return {
        'title': d['title'],
        'subtitle': f"{password}",
        'arg': f"{password}",
    }


items = list(map(item, combinations))

print(json.dumps({'items': items}))
