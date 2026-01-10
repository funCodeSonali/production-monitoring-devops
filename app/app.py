from flask import Flask, Response
import psycopg2
import time
from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST,
)

app = Flask(__name__)

# ---------------------------
# Prometheus Metrics
# ---------------------------


REQUEST_COUNT = Counter(
    "app_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request latency in seconds",
    ["endpoint"]
)

DB_WRITES = Counter(
    "app_db_writes_total",
    "Total database write operations"
)

# ---------------------------
# Database Connection
# ---------------------------

# Retry loop for Postgres
def get_postgres_connection(retries=10, delay=3):
    for attempt in range(retries):
        try:
            conn = psycopg2.connect(
                host="postgres",
                database="postgres",
                user="postgres",
                password="postgres"
            )
            print("Connected to Postgres!")
            return conn
        except psycopg2.OperationalError:
            print(f"Postgres not ready, retrying {attempt+1}/{retries}...")
            time.sleep(delay)
    raise Exception("Could not connect to Postgres after multiple attempts.")


# ---------------------------
# DB Initialization
# ---------------------------

def init_db():
    conn = get_postgres_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS hits (
            id SERIAL PRIMARY KEY,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("Database initialized (table ensured).")

# Run DB init at startup
init_db()

# ---------------------------
# Routes
# ---------------------------

@app.route("/")
def health():
    REQUEST_COUNT.labels("GET", "/").inc()
    return "Application is running\n"


@app.route("/write")
def write_to_db():
    start_time = time.time()

    conn = get_postgres_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO hits DEFAULT VALUES;")
    conn.commit()
    cur.close()
    conn.close()

    DB_WRITES.inc()
    REQUEST_COUNT.labels("GET", "/write").inc()
    REQUEST_LATENCY.labels("/write").observe(time.time() - start_time)

    return "Database write successful\n"


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

# ---------------------------
# App Entrypoint
# ---------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
