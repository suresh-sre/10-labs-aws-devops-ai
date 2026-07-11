# API Endpoints

The AWS Inventory Tool is currently a CLI-first utility. If an HTTP API is added later, keep it small and focused.

## Potential endpoints
- `GET /health` — basic liveness check
- `GET /status` — inventory generation status
- `POST /inventory` — trigger inventory collection
- `GET /reports` — list generated report files
