#!/bin/sh

set -e

# shellcheck disable=SC2039
if [[ -n "${RUN_MIGRATIONS}" ]]; then
  alembic upgrade head
fi

exec python -O -m app