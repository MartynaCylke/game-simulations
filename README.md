# Game Simulations

[![CI](https://github.com/MartynaCylke/game-simulations/actions/workflows/ci.yml/badge.svg)](https://github.com/MartynaCylke/game-simulations/actions/workflows/ci.yml)

A modular Python toolkit for simulating and analysing slot-game mechanics. The
project covers line, ways, scatter, cluster and tumbling-reel calculations and
includes automated unit and integration tests.

## Highlights

- separate calculation modules for the main win mechanics;
- configurable game and simulation parameters;
- generation and analysis of lookup tables and RTP data;
- deterministic unit tests plus end-to-end integration coverage;
- CI across multiple supported Python versions.

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
