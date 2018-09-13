import re
import os
import md5

COMMENT_RE = re.compile("\/\/.*")

def simplify(lines):
    s = ""
    for l in lines:
        mod = l.strip(' \t\n\r')
        if not COMMENT_RE.match(mod):
            s += mod

    return md5.new(s).digest()

def get_time_stamp(path):
    return os.path.getmtime(path)

def set_time_stamp(path, stamp):
    os.utime(path, (os.path.getatime(path), stamp))

