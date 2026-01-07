# 🚀 Jenkins–Prometheus–Grafana Monitoring

**Jenkins Performance, Health & Security Monitoring using Prometheus and Grafana**

This project demonstrates a complete **DevOps monitoring setup** where Jenkins is monitored using Prometheus metrics and visualized through Grafana dashboards. It also includes a **custom Python-based scoring system** to evaluate Jenkins health and security.

---

## 📌 Project Overview

Modern CI/CD pipelines require continuous monitoring to ensure reliability and performance.  
This project focuses on:

- Monitoring Jenkins jobs and executors  
- Collecting JVM and system metrics using Prometheus  
- Visualizing real-time metrics in Grafana  
- Analyzing job success, failures, and queue behavior  
- Calculating Jenkins **Health & Security Score** using Python  

---

## 🛠️ Tools & Technologies

- Jenkins  
- Prometheus  
- Grafana  
- Python  
- JVM Metrics  
- REST API  
- Time-Series Monitoring  

---

## 🏗️ Architecture

Jenkins
↓ (Metrics /prometheus)
Prometheus
↓ (Queries)
Grafana Dashboards
↓
Health & Security Analysis (Python)



## 📂 Repository Structure
Jenkins-Prometheus-Grafana-Monitoring/
│
├── Report/
│ └── jenkins_score_report.json
│
├── screenshots/
│ ├── Jenkins Dashboard
│ ├── Grafana Dashboard
│ ├── Prometheus Targets
│ └── Prometheus Metrics
│
├── scripts/
│ └── jenkins_scoring_system_visual.py
│
├── Project_ppt.pptx
├── LICENSE
└── README.md



---

## 📊 Metrics Monitored

- Jenkins job status (Success / Failed / Unstable)  
- Job execution duration  
- Jenkins queue size  
- Executor availability & usage  
- JVM memory usage  
- Garbage Collection metrics  
- CPU utilization  
- Jenkins node health  

---

## 📈 Jenkins Health & Security Scoring

The project includes a Python script that computes Jenkins scores based on collected metrics.

| Metric Type | Score |
|------------|-------|
| Health Score | 50 |
| Security Score | 60 |
| **Final Score** | **54** |

✔ Scores are generated programmatically and visualized using bar charts.

---

## ▶️ How to Run the Project

### 1️⃣ Start Jenkins

Access Jenkins in browser:

http://localhost:8080


Install and enable:
- **Prometheus Metrics Plugin**

---

### 2️⃣ Start Prometheus

Ensure Jenkins is added as a scrape target.

Access Prometheus:
http://localhost:9090

Verify targets:
Status → Targets


---

### 3️⃣ Start Grafana

Access Grafana:

http://localhost:3000




Steps:
- Add Prometheus as a Data Source  
- Import Jenkins dashboard  
- Visualize real-time metrics  

---

### 4️⃣ Run Jenkins Scoring Script

python scripts/jenkins_scoring_system_visual.py


This will:
- Analyze Jenkins metrics  
- Generate health & security scores  
- Create visual charts  
- Produce a JSON report  

Output file:
Report/jenkins_score_report.json


---

## 📸 Screenshots

All screenshots related to:
- Jenkins dashboard  
- Grafana monitoring dashboard  
- Prometheus metrics & targets  

📁 Available here:  
https://github.com/Bijayakumar2005/Jenkins-Prometheus-Grafana-Monitoring/tree/main/screenshots

---

## 📑 Project Presentation

📊 PowerPoint Presentation:  
https://github.com/Bijayakumar2005/Jenkins-Prometheus-Grafana-Monitoring/blob/main/Project_ppt.pptx

---

## 🎯 Use Cases

- DevOps monitoring & observability  
- CI/CD pipeline health tracking  
- Jenkins performance analysis  
- Interview-ready DevOps project  
- Academic / college submission  

---

## 🚀 Future Enhancements

- Alerting using Alertmanager  
- Email / Slack notifications  
- Dockerized Jenkins–Prometheus–Grafana stack  
- Kubernetes monitoring  
- Advanced security scoring  

---

## 👤 Author

**Bijaya Kumar Rout**  
GitHub: https://github.com/Bijayakumar2005  

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!
