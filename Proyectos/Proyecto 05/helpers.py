from pathlib import Path


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


def existsFile(file):
    return Path(file).is_file()
