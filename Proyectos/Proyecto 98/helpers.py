from pathlib import Path


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)
