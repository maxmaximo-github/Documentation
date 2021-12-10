#!/usr/bin/env  python3


from pathlib import Path


cwd = Path.cwd()
Path(f"{cwd}/tmp3").mkdir(parents=True, exist_ok=True)
print(cwd)