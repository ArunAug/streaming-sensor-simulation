# Streaming Sensor Data Simulation 🚀

A real-time data engineering project that simulates sensor readings, ingests them into Kafka, and processes the stream using PySpark Structured Streaming.

---

## 📌 Overview

This project demonstrates an end-to-end **real-time streaming pipeline** using:

- A Python-based Kafka producer simulating IoT sensor data
- Apache Kafka as the message broker
- PySpark Structured Streaming to process and aggregate the sensor data
- Console sink for real-time monitoring (can be extended to Delta Lake, PostgreSQL, etc.)

---

## 🧱 Project Structure

<pre> streaming-sensor-simulation/ ├── simulator/ # Kafka producer sending fake sensor data │ └── sensor_producer.py │ ├── streaming/ # PySpark job consuming and processing the stream │ └── sensor_streaming_job.py │ ├── notebooks/ # Optional notebooks for visualization/EDA │ └── analysis.ipynb │ ├── .github/ │ └── workflows/ # CI/CD pipeline configuration │ └── python-ci.yml │ ├── docker-compose.yml # Kafka + Zookeeper setup ├── requirements.txt # Python dependencies ├── .gitignore # Git ignore rules └── README.md # Project documentation </pre>

---

## 🧰 Tech Stack

- **Kafka + Zookeeper** (via Docker)
- **PySpark Structured Streaming**
- **Kafka-Python** for producing messages
- **GitHub Actions** for CI
- **Docker Compose** for environment management

---

## ⚙️ Setup Instructions

### 🔧 1. Prerequisites

- Python 3.9+
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Apache Spark (locally installed or using Databricks)
- Git

### 🐳 2. Start Kafka Environment

```bash
docker compose up -d

### 🐳 3. nstall Dependencies

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 🐳 4.How to Run

🛰️ 1. Simulate Sensor Data
Run the Kafka producer:

python simulator/sensor_producer.py

🔄 2. Process Stream in PySpark
Run the PySpark structured streaming job:

spark-submit streaming/sensor_streaming_job.py

You will see aggregated temperature/humidity outputs in your terminal.

🧪 CI/CD - GitHub Actions
This project includes a basic CI pipeline that:

Installs dependencies

Lints Python code using flake8

File: .github/workflows/python-ci.yml

To trigger the pipeline:

Push to main branch Or open a Pull Request