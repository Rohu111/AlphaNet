import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import check_auth, load_dashboard_css, render_sidebar
import datetime

st.set_page_config(page_title="AlphaNet — Home", page_icon="🏠",
                   layout="wide", initial_sidebar_state="expanded")

check_auth()
load_dashboard_css()
render_sidebar("home")

# ─── Page header ──────────────────────────────────────────────────────────────
now = datetime.datetime.now().strftime("%d %b %Y  |  %H:%M:%S")
st.markdown(f"""
<div class="page-header">
    <div>
        <div class="page-title">🏠 &nbsp;DASHBOARD</div>
        <div style="font-family:var(--mono);font-size:11px;color:rgba(255,255,255,0.3);
                    letter-spacing:2px;margin-top:4px;">
            WELCOME BACK, ADMIN
        </div>
    </div>
    <div>
        <div class="page-badge">● &nbsp;ALL SYSTEMS OPERATIONAL</div>
        <div style="font-family:var(--mono);font-size:10px;
                    color:rgba(255,255,255,0.25);text-align:right;
                    letter-spacing:1px;margin-top:6px;">{now}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Metric Cards ─────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
metrics = [
    (c1, "🌐", "MONITORED SITES", "12", "+3 today"),
    (c2, "📥", "DOWNLOADS",        "48", "1.2 GB total"),
    (c3, "🚀", "AVG SPEED",        "94<span style='font-size:14px'>Mbps</span>", "Last tested"),
    (c4, "⏱️", "UPTIME",           "99.8<span style='font-size:14px'>%</span>", "30-day avg"),
]
for col, icon, label, value, sub in metrics:
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="mc-icon">{icon}</div>
            <div class="mc-label">{label}</div>
            <div class="mc-value">{value}</div>
            <div class="mc-sub">{sub}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── Quick Actions ─────────────────────────────────────────────────────────────
st.markdown('<div class="panel-title">⚡ QUICK ACTIONS</div>', unsafe_allow_html=True)
a1, a2, a3 = st.columns(3)

with a1:
    st.markdown("""
    <div class="action-card">
        <div class="ac-icon">🌐</div>
        <div class="ac-title">WEBSITE MONITOR</div>
        <div class="ac-desc">Check uptime & response<br>time for multiple URLs</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Monitor", key="qa_monitor", use_container_width=True):
        st.switch_page("pages/2_Website_Monitor.py")

with a2:
    st.markdown("""
    <div class="action-card">
        <div class="ac-icon">📥</div>
        <div class="ac-title">BULK DOWNLOADER</div>
        <div class="ac-desc">Download multiple files<br>from URLs at once</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Downloader", key="qa_bulk", use_container_width=True):
        st.switch_page("pages/3_Bulk_Downloader.py")

with a3:
    st.markdown("""
    <div class="action-card">
        <div class="ac-icon">🚀</div>
        <div class="ac-title">SPEED TEST</div>
        <div class="ac-desc">Measure download, upload<br>speed & ping latency</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Speed Test", key="qa_speed", use_container_width=True):
        st.switch_page("pages/4_Speed_Test.py")

st.markdown("<br>", unsafe_allow_html=True)

# ─── Recent Activity ──────────────────────────────────────────────────────────
import pandas as pd

st.markdown('<div class="panel-title">📋 RECENT ACTIVITY</div>', unsafe_allow_html=True)

activity_data = {
    "Timestamp":  ["2025-07-10 14:22", "2025-07-10 13:45", "2025-07-10 12:30",
                   "2025-07-10 11:15", "2025-07-10 10:00"],
    "Module":     ["Website Monitor", "Speed Test", "Bulk Downloader",
                   "Website Monitor", "Speed Test"],
    "Action":     ["Checked 5 URLs", "Speed test run", "Downloaded 3 files",
                   "Checked 8 URLs", "Speed test run"],
    "Status":     ["✅ Success", "✅ Success", "⚠️ Partial", "✅ Success", "✅ Success"],
    "Duration":   ["2.3s", "12.4s", "34.7s", "4.1s", "11.8s"],
}
df = pd.DataFrame(activity_data)
st.dataframe(df, use_container_width=True, hide_index=True)

# ─── System Health mini bar ────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="panel-title">🔧 SYSTEM HEALTH</div>', unsafe_allow_html=True)
h1, h2, h3 = st.columns(3)

with h1:
    st.markdown('<div style="font-family:var(--mono);font-size:11px;'
                'color:rgba(255,255,255,0.4);letter-spacing:2px;margin-bottom:6px;">'
                'MONITORING ENGINE</div>', unsafe_allow_html=True)
    st.progress(1.0)
    st.markdown('<span style="font-family:var(--mono);font-size:11px;'
                'color:#00ff88;">100% — ONLINE</span>', unsafe_allow_html=True)

with h2:
    st.markdown('<div style="font-family:var(--mono);font-size:11px;'
                'color:rgba(255,255,255,0.4);letter-spacing:2px;margin-bottom:6px;">'
                'DOWNLOADER MODULE</div>', unsafe_allow_html=True)
    st.progress(0.85)
    st.markdown('<span style="font-family:var(--mono);font-size:11px;'
                'color:#ffd700;">85% — READY</span>', unsafe_allow_html=True)

with h3:
    st.markdown('<div style="font-family:var(--mono);font-size:11px;'
                'color:rgba(255,255,255,0.4);letter-spacing:2px;margin-bottom:6px;">'
                'SPEED ANALYZER</div>', unsafe_allow_html=True)
    st.progress(0.92)
    st.markdown('<span style="font-family:var(--mono);font-size:11px;'
                'color:#00ff88;">92% — ACTIVE</span>', unsafe_allow_html=True)
