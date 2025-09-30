
# 🕒 Habit Tracker with Pixela API

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Build](https://img.shields.io/badge/Build-Pass-brightgreen)
![Pixela Graph](https://img.shields.io/badge/View-Graph-orange?logo=graphql)

A **Python script** to track your daily habits and visualize them with [Pixela](https://pixe.la/). Log your activities like coding hours, reading, workouts, or anything else you want to track, and watch your progress over time!

---

## 🚀 Features

* Log daily habits with **just one function call**.
* Store quantity as **float values** (e.g., 1.5 hours, 3.2 km).
* Automatically formats the date in Pixela-compatible format (`YYYYMMDD`).
* Fully configurable via **environment variables** (keep your token safe!).
* Error handling for smooth execution and debugging.
* Ready for extensions: add graphs, multiple habits, or automated logging.

---

## 🛠️ Setup

1. **Clone the repository**

```bash
git clone https://github.com/VasilisKokotakis/Python-Script-to-Log-Habits-with-the-Pixela-API.git
cd Python-Script-to-Log-Habits-with-the-Pixela-API
```

2. **Install dependencies**

```bash
pip install requests
```

3. **Set environment variables** (replace with your Pixela info)

```bash
export PIXELA_USERNAME="your_username"
export PIXELA_TOKEN="your_secure_token"
export PIXELA_GRAPH_ID="graph1"   # optional, default is "graph1"
```

4. **Run the script**

```bash
python habit_tracker.py
```

---

## ⚡ Usage

```python
from habit_tracker import log_habit

# Log 10 hours of coding
log_habit(10.0)

# Log 1.5 hours of reading
log_habit(1.5)
```

Open your graph in a browser:

```
https://pixe.la/v1/users/<username>/graphs/<graph_id>.html
```

---

## 🌈 Customization

* Change the **graph color**, **unit**, or **graph name** in the Pixela dashboard.
* Add **multiple habit graphs** by creating new `GRAPH_ID`s.
* Schedule logging automatically with **cron** or **Windows Task Scheduler**.

---

## 💡 Tips

* Use `float` values for precise tracking.
* Keep your `TOKEN` secret—**never commit it to GitHub**.
* Combine with scripts or apps for a fully automated habit dashboard.

---

## 📚 Resources

* [Pixela Official Site](https://pixe.la/)
* [Pixela API Docs](https://docs.pixe.la/)
* [Your Graph Example](https://pixe.la/v1/users/kokotovasilis/graphs/graph1.html)

---

## 📝 License

This project is **MIT Licensed** — feel free to use, modify, and share!
