import re
import os
import hashlib

COMMENT_RE = re.compile(r'\/\/.*')

def simplify(lines):
    s = ""
    for l in lines:
        if COMMENT_RE.match(mod):
            continue

        mod = l.strip(' \t\n\r')
        s += mod

    return hashlib.sha224(s).hexdigest()

def get_time_stamp(path):
    return os.path.getmtime(path)

def set_time_stamp(path, stamp):
    os.utime(path, (os.path.getatime(path), stamp))

