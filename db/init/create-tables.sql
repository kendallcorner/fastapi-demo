-- shows sql commands
\set ECHO all

CREATE TABLE IF NOT EXISTS demo (
    created_timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    info TEXT,
    modified_timestamp TIMESTAMPTZ
);
