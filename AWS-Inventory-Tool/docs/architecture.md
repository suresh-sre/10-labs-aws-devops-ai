# Architecture

## Overview
The AWS Inventory Tool is designed as a modular CLI utility.

## Layers
- `app.py`: entrypoint and command orchestration.
- `config.py`: environment loading and validation.
- `aws/`: AWS session helpers and service clients.
- `inventory/`: resource discovery and inventory gathering.
- `reports/`: report generation and export logic.
- `utils/`: common utilities for formatting and file handling.

## Runtime flow
1. Load `.env` settings.
2. Establish an AWS session.
3. Discover inventory across selected AWS services.
4. Render reports and save outputs under `output/`.
