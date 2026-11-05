from pathlib import Path


def get_directory_contents(dirpath: Path) -> list[str]:
    if not dirpath.is_dir():
        raise ValueError(f"{dirpath} is not a directory")

    return sorted(d.relative_to(dirpath).name for d in dirpath.glob("*"))
