# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A CLI quiz tool for students of the Chudokai Aikido Federation International studying Dan Koto Shitsumon (DKS). It presents random questions from a JSON file and accepts user answers via the terminal.

## Running

```bash
python3 main.py
```

## Architecture

- **main.py** — Entry point. Loads questions from `questions.json` and presents a random question interactively via stdin/stdout.
- **convertCSV.py** — Standalone utility to convert a `dks.csv` file into `dks.json` (reads/writes files relative to its own directory). Run with `python3 convertCSV.py`.
- **questions.json** — Question bank. Array of objects with a `"question"` key.

## Notes

- Python 3, no external dependencies (uses only `json`, `random`, `csv`, `os`, `sys`).
- `main.py` hardcodes the filename `questions.json` (relative path, expects to be run from the repo root).
- `convertCSV.py` outputs to `dks.json`, not `questions.json` — these are separate files.
