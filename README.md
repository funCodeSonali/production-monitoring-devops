# Production-Grade Monitoring & Alerting Stack  
### DevOps / SRE Portfolio Project

---

## 📌 Overview

This project demonstrates a **production-like monitoring and alerting system** built using modern **DevOps and SRE best practices**.

It showcases **end-to-end observability** for a real application stack, covering:
- Application-level metrics
- Database-level metrics
- Host-level metrics
- Actionable alerting
- Meaningful Grafana dashboards
- Containerized deployment
- Optional cloud deployment (AWS EC2)

The objective of this project is to show **how production systems are monitored, diagnosed, and protected**, not just how tools are installed.

---

## 🏗️ High-Level Architecture

Client Requests
│
▼
Flask Application (Python)
│
▼
PostgreSQL Database
│
│ Metrics
▼
| Prometheus |
| - Scrapes application metrics |
| - Scrapes database metrics |
| - Scrapes host metrics |
| - Evaluates alert rules |
│
▼
Grafana Dashboards

---

## 🧰 Tech Stack

| Layer | Technology |
|----|----|
| Application | Flask (Python) |
| Database | PostgreSQL |
| Metrics Collection | Prometheus |
| Visualization | Grafana |
| Exporters | Node Exporter, Postgres Exporter |
| Alerting | Prometheus Alert Rules |
| Containerization | Docker, Docker Compose |
| Infrastructure (optional) | Terraform (AWS EC2) |

---

## 📊 Metrics Covered

### 🔹 Application Metrics (Flask)

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


**Why these matter**
- Traffic visibility
- Latency analysis using percentiles (P95)
- Backend pressure detection

---

### 🔹 PostgreSQL Metrics (Postgres Exporter)
Key database metrics:
- Database availability (`pg_up`)
- Active vs idle connections
- Max connections & free connections
- Transaction rate (commit / rollback)
- Cache hit ratio
- Database-level activity

**Use cases**
- Detect DB outages
- Identify connection saturation
- Analyze DB performance bottlenecks

---

### 🔹 Host Metrics (Node Exporter)

- CPU usage
- Memory usage
- Disk usage
- Network metrics
- Swap usage
- Load averages

---

**Use cases**
- Capacity planning
- Detect resource pressure
- Identify host-level failures

---

## 📈 Grafana Dashboards

Dashboards are built using **multiple visualization types** to reflect real production usage.

---

### 1️⃣ Flask Application Dashboard

**Panels included**
- Time-series:
  - Request rate per endpoint
  - Database write rate
- Latency:
  - 95th percentile request latency
- Stats:
  - Total requests
  - Total DB writes

**Demonstrates**
- Application traffic patterns
- Latency behavior
- Backend load correlation

---

### 2️⃣ Node / Host Metrics Dashboard

**Panels included**
- Gauge:
  - CPU usage %
  - Memory usage %
  - Disk usage %
- Stat:
  - Total memory (GiB)
  - Available memory (GiB)
  - CPU core count
  - Swap memory
- Time-series:
  - System load
  - CPU trends
  - Memory usage trends

**Demonstrates**
- At-a-glance host health
- Capacity visibility
- Resource pressure detection

---

### 3️⃣ PostgreSQL Metrics Dashboard

**Panels included**
- Active vs idle connections (grouped by database)
- Remaining connection capacity
- Transaction throughput
- Cache hit ratio
- Database activity breakdown

**Demonstrates**
- Database health monitoring
- Connection pool awareness
- Performance diagnostics

---

## 🚨 Alerting Strategy

Prometheus evaluates alert rules defined in `alerts.yml`.  
Alerts are grouped by **application**, **database**, **host**, and **infrastructure** layers.

### 🔔 Alert Design Principles
- Actionable thresholds
- Time-based stability using `for`
- Reduced noise
- Multi-signal correlation for infrastructure failures

---

## Alert Groups

### Application Alerts (`app_alerts`)

| Alert | Description | Severity |
|------|------------|----------|
| **FlaskAppDown** | Flask app cannot be scraped for 2 minutes | Critical |
| **HighRequestRate** | Request rate exceeds 20 req/min | Warning |
| **HighRequestLatency** | 95th percentile latency > 1s | Warning |
| **HighDBWrites** | More than 20 DB writes per minute | Warning |

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

## ▶️ Running the Project Locally

### Prerequisites
- Docker
- Docker Compose

### Start the stack
```bash
docker compose up --build

### Access Services

| Service     | URL                    |
|------------|------------------------|
| Flask App  | http://localhost:5000  |
| Prometheus | http://localhost:9090  |
| Grafana    | http://localhost:3000  |

### Grafana default login
Username: admin
Password: admin

---

## ☁️ AWS EC2 Demo (Optional)

- Terraform configuration provided for one-time AWS EC2 demo  
- Designed to work within AWS Free Tier  
- Instance can be terminated after demo to avoid costs  

---

## 🎯 What This Project Demonstrates

- ✅ Real-world monitoring architecture  
- ✅ Prometheus instrumentation & PromQL  
- ✅ Grafana dashboard design (Gauge, Stat, Time-series)  
- ✅ Alert design & correlation  
- ✅ Docker & Compose orchestration  
- ✅ DevOps & SRE mindset  

---


## 👩‍💻 Author

**Sonali Mittal**  
Software Engineer | DevOps & SRE Enthusiast  
AWS Certified Cloud Practitioner


