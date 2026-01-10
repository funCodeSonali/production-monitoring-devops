# Production-Grade Monitoring & Alerting Stack (DevOps Portfolio Project)

## Overview

This project demonstrates a **production-like monitoring and alerting stack** for a real application using modern DevOps and SRE practices.

It includes:
- A Flask application with a PostgreSQL backend
- Custom application metrics
- Database and host-level metrics
- Prometheus alerting rules
- Grafana dashboards
- Fully containerized setup using Docker Compose
- Optional Terraform configuration for AWS EC2 demo

The goal of this project is to showcase **end-to-end observability**, not just metrics collection.

---

## Tech Stack

- **Application**: Flask (Python)
- **Database**: PostgreSQL
- **Metrics**: Prometheus
- **Dashboards**: Grafana
- **Exporters**:
  - PostgreSQL Exporter
  - Node Exporter
- **Containerization**: Docker & Docker Compose
- **Infrastructure (optional)**: Terraform (AWS EC2)

---

## Metrics Exposed

### Application Metrics (Flask)

Exposed via `/metrics` using `prometheus_client`:

- **`app_http_requests_total`**
  - Total HTTP requests
  - Labels: `method`, `endpoint`

- **`app_request_latency_seconds`**
  - Histogram of request latency per endpoint
  - Used for percentile-based latency alerts

- **`app_db_writes_total`**
  - Total number of database write operations

---

### Database Metrics (Postgres Exporter)

- Database availability (`pg_up`)
- Active connections
- Max connections
- Transaction statistics
- Cache and performance metrics

---

### Host Metrics (Node Exporter)

- CPU usage
- Memory usage
- Disk usage
- Network metrics

---

## Alerting Strategy

Prometheus evaluates alert rules defined in `alerts.yml`.  
Alerts are grouped by **application**, **database**, **host**, and **infrastructure** layers.

---

## Alert Groups

### Application Alerts (`app_alerts`)

| Alert | Description | Severity |
|------|------------|----------|
| **FlaskAppDown** | Flask app cannot be scraped for 2 minutes | Critical |
| **HighRequestRate** | Request rate exceeds 10 req/min | Warning |
| **HighRequestLatency** | 95th percentile latency > 1s | Warning |
| **HighDBWrites** | More than 5 DB writes per minute | Warning |

These alerts ensure **application availability, performance, and abnormal load detection**.

---

### PostgreSQL & Exporter Alerts (`postgres_alerts`)

| Alert | Description | Severity |
|------|------------|----------|
| **PostgresDatabaseDown** | Exporter cannot connect to DB | Critical |
| **PostgresExporterDown** | Exporter endpoint unreachable | Warning |
| **PostgresTooManyConnections** | Active connections > 50 | Warning |
| **PostgresLowFreeConnections** | Less than 10 free connections | Warning |

These alerts protect against **database outages and saturation scenarios**.

---

### Node / Host Alerts (`node_alerts`)

| Alert | Description | Severity |
|------|------------|----------|
| **NodeExporterDown** | Host metrics unavailable | Warning |
| **HighCPUUsage** | CPU usage > 80% | Warning |
| **HighMemoryUsage** | Memory usage > 80% | Warning |

These alerts monitor **host health and resource pressure**.

---

### Infrastructure Alerts (`infrastructure_alerts`)

| Alert | Description | Severity |
|------|------------|----------|
| **InstanceDown** | Flask, Postgres exporter, and Node exporter all unreachable for 3 minutes | Critical |

This alert uses **multi-signal correlation** to avoid false positives and indicates:
- Host down
- Docker daemon stopped
- Network isolation

---

## Running the Project Locally

### Prerequisites
- Docker
- Docker Compose

### Start the stack
```bash
docker compose up --build


