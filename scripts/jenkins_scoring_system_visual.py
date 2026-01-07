import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt

PROM_URL = "http://localhost:9090/api/v1/query"


# -------------------------
# Query Prometheus Safely
# -------------------------
def prom_query(q):
    try:
        r = requests.get(PROM_URL, params={"query": q}, timeout=10)
        data = r.json()

        if data["status"] == "success" and len(data["data"]["result"]) > 0:
            total = 0.0
            for row in data["data"]["result"]:
                total += float(row["value"][1])
            return total
        return 0.0
    except:
        return 0.0


# -------------------------
# Collect Health Metrics
# -------------------------
def get_health_metrics():
    m = {}

    # Correct metric based on your screenshot!!!
    base = "default_jenkins_builds_last_build_result"

    m["successful_builds"] = prom_query(f"count({base} == 0)")
    m["failed_builds"]     = prom_query(f"count({base} == 1)")
    m["unstable_builds"]   = prom_query(f"count({base} == 2)")
    m["aborted_builds"]    = prom_query(f"count({base} == 3)")

    m["total_builds"] = (
        m["successful_builds"] +
        m["failed_builds"] +
        m["unstable_builds"] +
        m["aborted_builds"]
    )

    # Executors
    m["executor_busy"]  = prom_query("default_jenkins_executors_busy")
    m["executor_total"] = prom_query("default_jenkins_executors_defined")
    m["queue_size"]     = prom_query("default_jenkins_executors_queue_length")

    # JVM Memory
    m["memory_used"] = prom_query("jvm_memory_bytes_used")
    m["memory_max"]  = prom_query("jvm_memory_bytes_max")

    return m


# -------------------------
# Security (Simulated)
# -------------------------
def get_security_metrics():
    return {
        "outdated_plugins": 2,
        "critical_vulnerabilities": 1,
        "user_accounts_admin": 3,
        "missing_auth_settings": 0
    }


# -------------------------
# Health Score
# -------------------------
def calculate_health_score(m):
    if m["total_builds"] == 0:
        success_rate = 100
    else:
        success_rate = (m["successful_builds"] / m["total_builds"]) * 100

    executor_score = (
        100 if m["executor_total"] == 0 else
        100 - (m["executor_busy"] / m["executor_total"] * 100)
    )

    queue_score = max(0, 100 - (m["queue_size"] * 10))

    if m["memory_max"] > 0:
        mem_usage = m["memory_used"] / m["memory_max"] * 100
    else:
        mem_usage = 50

    mem_score = max(0, 100 - mem_usage)

    final = (
        success_rate * 0.40 +
        executor_score * 0.20 +
        queue_score * 0.10 +
        mem_score * 0.30
    )

    return round(min(max(final, 0), 100), 2)


# -------------------------
# Security Score
# -------------------------
def calculate_security_score(s):
    score = 100
    score -= s["outdated_plugins"] * 5
    score -= s["critical_vulnerabilities"] * 20
    score -= max(0, s["user_accounts_admin"] - 1) * 5
    score -= s["missing_auth_settings"] * 15
    return max(round(score, 2), 0)


# -------------------------
# Visualization
# -------------------------
def generate_visual(h, s, final):
    labels = ["Health", "Security", "Final"]
    values = [h, s, final]

    plt.figure(figsize=(7,5))
    bars = plt.bar(labels, values)

    for b in bars:
        y = b.get_height()
        plt.text(b.get_x()+b.get_width()/2, y+1, f"{y:.1f}", ha="center")

    plt.ylim(0, 110)
    plt.title("Jenkins Health & Security Score")
    plt.savefig("jenkins_score_visual.png")
    plt.close()


# -------------------------
# Main
# -------------------------
def generate_report():
    print("\n=== JENKINS HEALTH & SECURITY REPORT ===\n")

    health = get_health_metrics()
    sec = get_security_metrics()

    health_score = calculate_health_score(health)
    sec_score = calculate_security_score(sec)
    final_score = round(health_score * 0.6 + sec_score * 0.4, 2)

    print(json.dumps(health, indent=4))
    print("\n", json.dumps(sec, indent=4))

    print("\nScores:")
    print("Health Score  :", health_score)
    print("Security Score:", sec_score)
    print("Final Score   :", final_score)

    # save JSON
    output = {
        "timestamp": str(datetime.now()),
        "health_metrics": health,
        "security_metrics": sec,
        "health_score": health_score,
        "security_score": sec_score,
        "final_score": final_score
    }

    with open("jenkins_score_report.json", "w") as f:
        json.dump(output, f, indent=4)

    generate_visual(health_score, sec_score, final_score)
    print("\n📁 Saved: jenkins_score_report.json")
    print("📊 Saved: jenkins_score_visual.png")


generate_report()
