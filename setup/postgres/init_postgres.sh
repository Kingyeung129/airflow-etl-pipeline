#!/bin/bash
set -e

# # Create the crypto database
psql -v ON_ERROR_STOP=1 -U $POSTGRES_USER <<-EOSQL
  CREATE DATABASE airflow;
  CREATE DATABASE crypto;
EOSQL

# Restore the crypto database from the dump file
psql -v ON_ERROR_STOP=1 -U $POSTGRES_USER -d "crypto" < /docker-entrypoint-initdb.d/crypto.sql