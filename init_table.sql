CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    lat FLOAT,
    long FLOAT,
    event_type TEXT,
);

CREATE TABLE tweets (
    id SERIAL PRIMARY KEY,
    text TEXT,
    is_processed BOOL
);
