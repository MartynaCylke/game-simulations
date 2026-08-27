# Game Simulations

Python tools for simulating slot-game mechanics, including lines, ways,
scatter wins, clusters, and tumbling reels.

## Requirements

- Python 3.10 or newer
- `venv` (recommended)

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt -r requirements-dev.txt
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Running a simulation

Show the available command-line options:

```bash
python run.py --help
```

Generated books, lookup tables, and force files are written under `library/`.
These generated files are intentionally excluded from version control.

## Tests

```bash
python -m pytest
```

## Utility scripts

- `check_lookup_rtp.py` inspects lookup-table RTP data.
- `scale_lookup_tables.py` rescales generated lookup tables.
