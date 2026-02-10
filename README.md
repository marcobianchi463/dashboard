# Personal Data Science Dashboard

A fully self‑hosted, containerized **Data Science & Machine Learning portfolio dashboard**, designed to communicate complex research and data‑driven projects through interactive visualizations and clear storytelling.

The dashboard is built as a production‑grade application, following modern **MLOps / DevOps best practices**, and is continuously deployed on a private Linux server via **Docker, GitHub Actions, and Cloudflare Tunnel**.

---

## ✨ Motivation

Traditional CVs and static portfolios struggle to convey:

* the scale of real datasets,
* the structure of complex analyses,
* and the engineering maturity behind data science projects.

This dashboard was created to bridge that gap, providing an **interactive, reproducible, and technically rigorous** way to present applied data science work — from academic research to system‑level simulations.

---

## 🧠 Featured Projects

### 🔬 Anisotropic Flow Analysis — ALICE (CERN)

**Large‑scale experimental data analysis & statistical modeling**

* Analysis of anisotropic transverse flow ($v_3$, $v_4$) of $^3$He nuclei in Pb–Pb collisions
* Petabyte‑scale experimental data reduction and selection
* Physics‑driven statistical analysis and visualization

**Data scale**

* Raw data: **1.1 PB**
* Selected analysis data: **155 GB**

**Highlights**

* Interactive flow observables vs $p_T$ and centrality
* Physics‑aware filtering and comparison
* Publication‑ready visual storytelling

---

### 🚦 Multi‑Agent Traffic Simulation (Work in progress)

**Complex systems modeling & simulation**

* Agent‑based model of traffic lights and intersections
* Local communication and distributed coordination strategies
* Performance evaluation under varying traffic conditions

**Highlights**

* Simulation‑driven data generation
* System‑level emergent behavior analysis
* Clear separation between model logic and analytics

---

## 🖥️ Dashboard Features

* Interactive visualizations (Plotly)
* Physics‑grade numerical data handling (NumPy, Pandas)
* Modular Streamlit architecture
* Clean scientific notation and Unicode math rendering
* Responsive layout for desktop and tablet

---

## 🏗️ Architecture Overview

```text
User Browser
     │
     ▼
Cloudflare Tunnel (Zero Trust)
     │
     ▼
Dockerized Streamlit App
     │
     ▼
Read‑only data volumes / media assets
```

---

## ⚙️ Tech Stack

**Application**

* Python 3.12
* Streamlit
* Plotly
* Pandas / NumPy

**Infrastructure & DevOps**

* Docker & Docker Compose
* GitHub Actions (CI)
* GitHub Container Registry (GHCR)
* Cloudflare Tunnel (Zero Trust)
* Linux self‑hosted server

---

## 🔁 CI/CD Pipeline

The project follows a fully automated CI/CD workflow:

1. **Code push to `main`**
2. **GitHub Actions** builds the Docker image
3. Image is pushed to **GitHub Container Registry**
4. Production server automatically pulls and redeploys the latest image

This guarantees:

* reproducible builds
* zero‑downtime updates
* full traceability between code and deployment

---

## 📦 Data Management Philosophy

* No large datasets are stored in the repository
* All heavy data and generated media are mounted as **external read‑only volumes**
* The repository contains only:

  * application code
  * configuration

This approach mirrors industry‑standard data governance practices.

---

## 🚀 Local Development

```bash
# create virtual environment
python -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run locally
streamlit run app/app.py
```

---

## 🐳 Docker Usage

```bash
# build image
docker build -t portfolio-dashboard .

# run container
docker run -p 8501:8501 portfolio-dashboard
```

---

## 📌 Project Status

The dashboard is actively evolving:

* new visualizations and projects are added incrementally
* ongoing focus on clarity, performance, and scientific rigor

---

## 👤 Author

**Marco Bianchi**
Applied Data Scientist & Machine Learning Engineer

Focused on:

* data‑driven modeling of complex systems
* large‑scale scientific data analysis
* production‑ready ML and analytics pipelines

---

## 📜 License

This project is released for portfolio and demonstration purposes.

---

If you are a recruiter or researcher and would like to discuss the technical or scientific aspects of this work, feel free to reach out.
