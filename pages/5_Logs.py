import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import check_auth, load_dashboard_css, render_sidebar
import pandas as pd
import datetime

st.set_page_config(page_title="AlphaNet — Logs", page_icon="📜",
                   layout="wide", initial_sidebar_state="expanded")

check_auth()
load_dashboard_css()
render_sidebar("logs")

st.markdown("""
<div class="page-header">
    <div>
        <div class="page-title">📜 &nbsp;ACTIVITY LOGS</div>
        <div style="font-family:var(--mono);font-size:11px;color:rgba(255,255,255,0.3);
                    letter-spacing:2px;margin-top:4px;">
            SESSION ACTIVITY HISTORY
        </div>
    </div>
    <div class="page-badge">● &nbsp;LOGGING ACTIVE</div>
</div>
""", unsafe_allow_html=True)

# ─── Seed default logs if empty ───────────────────────────────────────────────
if "logs" not in st.session_state or not st.session_state["logs"]:
    st.session_state["logs"] = [
        {"Time": "2025-07-10 09:00:00", "Module": "System",
         "Action": "Session started", "Result": "Login successful"},
        {"Time": "2025-07-10 09:01:12", "Module": "Website Monitor",
         "Action": "Checked 3 URLs", "Result": "3 live, 0 down"},
        {"Time": "2025-07-10 09:05:44", "Module": "Speed Test",
         "Action": "Speed test run", "Result": "↓85.2 ↑32.1 Mbps, Ping 18ms"},
    ]

logs = st.session_state["logs"]

# ─── Summary ──────────────────────────────────────────────────────────────────
modules = list({l["Module"] for l in logs})
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="mc-label">TOTAL EVENTS</div>
        <div class="mc-value">{len(logs)}</div>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="mc-label">MODULES USED</div>
        <div class="mc-value">{len(modules)}</div>
    </div>""", unsafe_allow_html=True)
with c3:
    last_time = logs[-1]["Time"] if logs else "—"
    st.markdown(f"""
    <div class="metric-card">
        <div class="mc-label">LAST ACTIVITY</div>
        <div class="mc-value" style="font-size:16px;">{last_time[-8:]}</div>
        <div class="mc-sub">{last_time[:10]}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─── Log stream ───────────────────────────────────────────────────────────────
st.markdown('<div class="panel-title">📋 LOG STREAM</div>', unsafe_allow_html=True)

module_icons = {
    "System": "⚙️", "Website Monitor": "🌐",
    "Speed Test": "🚀", "Bulk Downloader": "📥"
}
for log in reversed(logs):
    icon = module_icons.get(log["Module"], "📌")
    st.markdown(f"""
    <div style="background:rgba(4,14,28,0.8);border:1px solid rgba(0,255,136,0.12);
                border-left:3px solid rgba(0,255,136,0.4);border-radius:8px;
                padding:12px 18px;margin-bottom:6px;
                display:flex;align-items:center;gap:16px;">
        <div style="font-size:18px;">{icon}</div>
        <div style="flex:1;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
                <span style="font-family:var(--body);font-size:15px;font-weight:600;
                             color:var(--white);">{log['Module']}</span>
                <span style="font-family:var(--mono);font-size:10px;
                             color:rgba(255,255,255,0.3);">{log['Time']}</span>
            </div>
            <div style="font-family:var(--mono);font-size:11px;
                        color:rgba(255,255,255,0.4);margin-top:3px;letter-spacing:1px;">
                {log['Action']} &nbsp;·&nbsp; {log['Result']}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── Export ───────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
col_clear, col_export = st.columns([1, 1])

with col_clear:
    if st.button("🗑  Clear Logs", key="clear_logs", use_container_width=True):
        st.session_state["logs"] = []
        st.rerun()

with col_export:
    df = pd.DataFrame(logs)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇  Export CSV", data=csv,
                       file_name="alphanet_logs.csv", mime="text/csv",
                       use_container_width=True)
