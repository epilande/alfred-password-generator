#!/usr/bin/python3

import os
import sys
import secrets
import json

defaultLength = os.environ['defaultLength']
punctuation = os.environ['punctuation']
digits = os.environ['digits']
letters = os.environ['letters']

length = int(sys.argv[1]) if len(sys.argv) > 1 else int(defaultLength)
password = ''.join(secrets.choice(letters + digits + punctuation)
                   for i in range(length))

print(json.dumps({'items': [
    {
        'title': f"Generate password {length} characters",
        'subtitle': f"{password}",
        'arg': f"{password}",
    }
]}))
