#!/usr/bin/python3

import sys
import secrets
import string
import json

length = int(sys.argv[1]) if len(sys.argv) > 1 else 16
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(length))

print(json.dumps({'items': [
    {
        'title': f"Generate password {length} characters",
        'subtitle': f"{password}",
        'arg': f"{password}",
    }
]}))
