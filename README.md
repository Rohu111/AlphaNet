# 🛡️ AlphaNet — Network Utility & Monitoring Suite

> **"Monitor. Analyze. Optimize."**  
> A cyber-themed Streamlit network utility platform by **Team Alpha Pair ⚡**

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/AlphaNet.git
cd AlphaNet

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

Then open **http://localhost:8501** in your browser.

**Login credentials:**
- Username: `admin`
- Password: `alpha123`

---

## 📄 Project Structure

```
AlphaNet/
├── app.py                    # Entry point — Login page
├── utils.py                  # Shared CSS, auth guard, sidebar
├── requirements.txt
├── README.md
├── downloads/                # Downloaded files saved here
└── pages/
    ├── 1_Home.py             # Dashboard overview
    ├── 2_Website_Monitor.py  # URL uptime checker
    ├── 3_Bulk_Downloader.py  # Multi-URL downloader
    ├── 4_Speed_Test.py       # Network speed analyzer
    ├── 5_Logs.py             # Activity history
    └── 6_About.py            # Team & project info
```

---

## 🎨 Features

| Module | Description |
|---|---|
| 🔐 Login | Cyber hacker-style secure login with animated terminal |
| 🏠 Dashboard | Metrics, quick actions, activity table, system health |
| 🌐 Website Monitor | Multi-URL uptime + response time checker |
| 📥 Bulk Downloader | Download multiple files from URLs at once |
| 🚀 Speed Test | Download/upload speed & ping via speedtest-cli |
| 📜 Logs | Session activity log with CSV export |
| ℹ️ About | Team info, tech stack, future scope |

---

## ⚙️ Tech Stack

- **Frontend/UI:** Streamlit + Custom CSS (Orbitron, Rajdhani, Share Tech Mono)
- **Backend:** Python 3.10+
- **Libraries:** `requests`, `pandas`, `speedtest-cli`

---

## 👥 Team

**TEAM ALPHA PAIR ⚡** — Hackathon 2025
