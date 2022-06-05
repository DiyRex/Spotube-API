import tempfile
from pathlib import Path

def tmpf():
    tempdir = tempfile.mkdtemp()
    path = Path(tempdir)
    print(path)
    return path
