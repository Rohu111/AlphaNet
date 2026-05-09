import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import check_auth, load_dashboard_css, render_sidebar

st.set_page_config(page_title="AlphaNet — About", page_icon="ℹ️",
                   layout="wide", initial_sidebar_state="expanded")

check_auth()
load_dashboard_css()
render_sidebar("about")

st.markdown("""
<div class="page-header">
    <div>
        <div class="page-title">ℹ️ &nbsp;ABOUT ALPHANET</div>
        <div style="font-family:var(--mono);font-size:11px;color:rgba(255,255,255,0.3);
                    letter-spacing:2px;margin-top:4px;">
            PROJECT OVERVIEW & TEAM
        </div>
    </div>
    <div class="page-badge">v2.4.1-STABLE</div>
</div>
""", unsafe_allow_html=True)

# ─── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:40px 20px;">
    <div style="font-family:var(--display);font-size:64px;font-weight:900;
                background:linear-gradient(135deg,#00ff88,#00ffcc,#00c8ff);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                background-clip:text;filter:drop-shadow(0 0 20px rgba(0,255,136,0.4));
                line-height:1;margin-bottom:16px;">
        ALPHANET
    </div>
    <div style="font-family:var(--mono);font-size:13px;
                color:rgba(0,200,255,0.6);letter-spacing:6px;margin-bottom:20px;">
        NETWORK UTILITY & MONITORING SUITE
    </div>
    <div style="font-family:var(--mono);font-size:14px;color:rgba(255,255,255,0.4);
                letter-spacing:3px;">
        "Monitor. Analyze. Optimize."
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Description ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="panel-card">
    <div class="panel-title">📌 PROJECT DESCRIPTION</div>
    <div style="font-family:var(--body);font-size:16px;color:rgba(255,255,255,0.6);
                line-height:1.8;">
        AlphaNet is a <strong style="color:#00ff88;">cyber-themed network utility platform</strong>
        built with Python & Streamlit. It combines multiple networking tools into one
        centralized dashboard — designed to feel like a real network operations center.<br><br>
        Whether you need to check website uptime, bulk-download files, or run a network speed
        analysis, AlphaNet provides all of this through a sleek, professional interface.
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Modules ──────────────────────────────────────────────────────────────────
st.markdown('<div class="panel-title">🔧 MODULES</div>', unsafe_allow_html=True)

modules = [
    ("🌐", "Website Monitor",  "Real-time uptime checker. Monitors HTTP status, response time, and availability for multiple URLs simultaneously."),
    ("📥", "Bulk Downloader",  "Multi-URL file downloader. Downloads files from multiple URLs, tracks progress, and logs all activity."),
    ("🚀", "Speed Test",       "Network performance analyzer. Measures download/upload speed and ping using the speedtest-cli library."),
    ("📜", "Activity Logs",    "Full session history. Records all module usage, actions, and results — exportable as CSV."),
]

cols = st.columns(2)
for i, (icon, name, desc) in enumerate(modules):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="action-card" style="text-align:left;margin-bottom:14px;">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
                <span style="font-size:28px;">{icon}</span>
                <span class="ac-title">{name}</span>
            </div>
            <div class="ac-desc" style="text-align:left;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ─── Tech Stack ───────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="panel-title">⚙️ TECH STACK</div>', unsafe_allow_html=True)

stack = [
    ("🖥️", "Frontend / UI",  "Streamlit"),
    ("🐍", "Backend",         "Python 3.10+"),
    ("🌐", "HTTP Client",     "requests"),
    ("📊", "Data Processing", "pandas"),
    ("🚀", "Speed Testing",   "speedtest-cli"),
    ("🎨", "Styling",         "Custom CSS + Google Fonts"),
]

tc = st.columns(3)
for i, (icon, category, tech) in enumerate(stack):
    with tc[i % 3]:
        st.markdown(f"""
        <div class="metric-card" style="margin-bottom:14px;">
            <div class="mc-icon">{icon}</div>
            <div class="mc-label">{category}</div>
            <div style="font-family:var(--body);font-size:15px;font-weight:600;
                        color:var(--green);">{tech}</div>
        </div>
        """, unsafe_allow_html=True)

# ─── Team ─────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="panel-title">👥 TEAM</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;padding:30px 20px;">
    <div style="font-family:var(--display);font-size:28px;font-weight:900;
                color:var(--green);letter-spacing:4px;margin-bottom:10px;">
        TEAM ALPHA PAIR ⚡
    </div>
    <div style="font-family:var(--mono);font-size:12px;
                color:rgba(255,255,255,0.3);letter-spacing:3px;">
        HACKATHON PROJECT · 2025
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Future Scope ─────────────────────────────────────────────────────────────
st.markdown('<div class="panel-title">🔭 FUTURE SCOPE</div>', unsafe_allow_html=True)
future = [
    "Real-time network packet analyzer",
    "Port scanner & vulnerability checker",
    "DNS lookup & WHOIS integration",
    "Automated scheduling for monitoring tasks",
    "Email/SMS alerts for downtime events",
    "Cloud storage integration for downloads",
    "Multi-user authentication system",
    "Advanced data visualization with Plotly",
]
cols2 = st.columns(2)
for i, item in enumerate(future):
    with cols2[i % 2]:
        st.markdown(f"""
        <div style="font-family:var(--mono);font-size:12px;
                    color:rgba(255,255,255,0.45);padding:8px 0;
                    border-bottom:1px solid rgba(0,255,136,0.06);
                    letter-spacing:1px;">
            <span style="color:rgba(0,255,136,0.5);">›</span> &nbsp; {item}
        </div>
        """, unsafe_allow_html=True)
