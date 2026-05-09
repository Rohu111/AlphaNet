import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import check_auth, load_dashboard_css, render_sidebar
import time
import datetime

st.set_page_config(page_title="AlphaNet — Speed Test", page_icon="🚀",
                   layout="wide", initial_sidebar_state="expanded")

check_auth()
load_dashboard_css()
render_sidebar("speed")

st.markdown("""
<div class="page-header">
    <div>
        <div class="page-title">🚀 &nbsp;SPEED TEST</div>
        <div style="font-family:var(--mono);font-size:11px;color:rgba(255,255,255,0.3);
                    letter-spacing:2px;margin-top:4px;">
            NETWORK PERFORMANCE ANALYZER
        </div>
    </div>
    <div class="page-badge">● &nbsp;ANALYZER ACTIVE</div>
</div>
""", unsafe_allow_html=True)

# ─── How to run ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="panel-card">
    <div class="panel-title">ℹ️ ABOUT SPEED TEST</div>
    <div style="font-family:var(--mono);font-size:12px;color:rgba(255,255,255,0.45);
                line-height:2;letter-spacing:1px;">
        › This module uses the <code>speedtest-cli</code> library to measure your real network speed.<br>
        › Make sure it is installed: <code>pip install speedtest-cli</code><br>
        › The test may take 15–30 seconds depending on your connection.<br>
        › Results include: Download speed, Upload speed, Ping, and ISP info.
    </div>
</div>
""", unsafe_allow_html=True)

run_btn = st.button("▶  RUN SPEED TEST", key="run_speed", use_container_width=False)

def run_speedtest():
    try:
        import speedtest
        st_obj = speedtest.Speedtest()
        st_obj.get_best_server()
        ping      = round(st_obj.results.ping, 2)
        download  = round(st_obj.download() / 1_000_000, 2)
        upload    = round(st_obj.upload()   / 1_000_000, 2)
        isp       = st_obj.results.client.get("isp", "Unknown")
        server    = st_obj.results.server.get("name", "—")
        country   = st_obj.results.server.get("country", "—")
        return {
            "download": download, "upload": upload,
            "ping": ping, "isp": isp,
            "server": server, "country": country,
            "error": None
        }
    except ImportError:
        return {"error": "speedtest-cli not installed. Run: pip install speedtest-cli"}
    except Exception as e:
        return {"error": str(e)}

if run_btn:
    with st.spinner("Running speed test — this may take 20–30 seconds..."):
        result = run_speedtest()

    if result.get("error"):
        st.markdown(f'<div class="a-err">⚠ &nbsp;{result["error"]}</div>',
                    unsafe_allow_html=True)
    else:
        d, u, p = result["download"], result["upload"], result["ping"]

        # ── Gauge-style display ──
        def speed_bar_color(mbps):
            if mbps >= 100: return "#00ff88"
            if mbps >= 50:  return "#ffd700"
            return "#ff4d6a"

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""
            <div class="metric-card" style="text-align:center;">
                <div style="font-size:40px;margin-bottom:10px;">⬇️</div>
                <div class="mc-label">DOWNLOAD</div>
                <div class="mc-value" style="color:{speed_bar_color(d)};font-size:36px;">{d}</div>
                <div class="mc-sub">Mbps</div>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="metric-card" style="text-align:center;">
                <div style="font-size:40px;margin-bottom:10px;">⬆️</div>
                <div class="mc-label">UPLOAD</div>
                <div class="mc-value" style="color:{speed_bar_color(u)};font-size:36px;">{u}</div>
                <div class="mc-sub">Mbps</div>
            </div>""", unsafe_allow_html=True)
        with c3:
            ping_color = "#00ff88" if p < 30 else "#ffd700" if p < 80 else "#ff4d6a"
            st.markdown(f"""
            <div class="metric-card" style="text-align:center;">
                <div style="font-size:40px;margin-bottom:10px;">📡</div>
                <div class="mc-label">PING</div>
                <div class="mc-value" style="color:{ping_color};font-size:36px;">{p}</div>
                <div class="mc-sub">ms</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Progress bars
        st.markdown('<div class="panel-title">📊 SPEED ANALYSIS</div>', unsafe_allow_html=True)

        for label, val, unit, max_val in [
            ("DOWNLOAD SPEED", d, "Mbps", 200),
            ("UPLOAD SPEED",   u, "Mbps", 200),
            ("PING LATENCY",   p, "ms",   200),
        ]:
            pct = min(val / max_val, 1.0)
            c = speed_bar_color(val) if unit == "Mbps" else (
                "#00ff88" if val < 30 else "#ffd700" if val < 80 else "#ff4d6a"
            )
            st.markdown(f"""
            <div style="margin-bottom:16px;">
                <div style="display:flex;justify-content:space-between;
                            font-family:var(--mono);font-size:11px;margin-bottom:6px;">
                    <span style="color:rgba(255,255,255,0.4);letter-spacing:2px;">{label}</span>
                    <span style="color:{c};">{val} {unit}</span>
                </div>
                <div style="background:rgba(255,255,255,0.06);border-radius:4px;height:8px;">
                    <div style="width:{pct*100:.1f}%;height:8px;border-radius:4px;
                                background:{c};
                                box-shadow:0 0 8px {c};transition:width 1s;">
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Server info
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="panel-card">
            <div class="panel-title">🖥️ SERVER INFO</div>
            <div style="font-family:var(--mono);font-size:12px;line-height:2.2;
                        color:rgba(255,255,255,0.5);">
                <span style="color:rgba(0,255,136,0.6);">ISP &nbsp;&nbsp;&nbsp;&nbsp;›</span>
                &nbsp; {result['isp']}<br>
                <span style="color:rgba(0,255,136,0.6);">SERVER &nbsp;›</span>
                &nbsp; {result['server']}, {result['country']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Log
        if "logs" not in st.session_state:
            st.session_state["logs"] = []
        st.session_state["logs"].append({
            "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Module": "Speed Test",
            "Action": "Speed test run",
            "Result": f"↓{d} ↑{u} Mbps, Ping {p}ms"
        })
