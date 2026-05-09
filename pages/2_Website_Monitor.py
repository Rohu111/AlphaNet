import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import check_auth, load_dashboard_css, render_sidebar
import requests
import time
import pandas as pd

st.set_page_config(page_title="AlphaNet — Website Monitor", page_icon="🌐",
                   layout="wide", initial_sidebar_state="expanded")

check_auth()
load_dashboard_css()
render_sidebar("monitor")

# ─── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div>
        <div class="page-title">🌐 &nbsp;WEBSITE MONITOR</div>
        <div style="font-family:var(--mono);font-size:11px;color:rgba(255,255,255,0.3);
                    letter-spacing:2px;margin-top:4px;">
            REAL-TIME UPTIME & RESPONSE CHECKER
        </div>
    </div>
    <div class="page-badge">● &nbsp;MONITOR ACTIVE</div>
</div>
""", unsafe_allow_html=True)

# ─── URL Input ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="panel-card">
    <div class="panel-title">🔗 TARGET URLS</div>
""", unsafe_allow_html=True)

url_input = st.text_area(
    "Enter URLs (one per line)",
    placeholder="https://google.com\nhttps://github.com\nhttps://example.com",
    height=140,
    label_visibility="collapsed",
    key="monitor_urls"
)
st.markdown("</div>", unsafe_allow_html=True)

col_btn, col_info = st.columns([1, 3])
with col_btn:
    run_btn = st.button("▶  RUN CHECK", key="run_monitor", use_container_width=True)
with col_info:
    st.markdown("""
    <div style="font-family:var(--mono);font-size:11px;color:rgba(255,255,255,0.3);
                padding:10px 0;letter-spacing:1px;">
        Checks HTTP status, response time, and availability for each URL.
    </div>
    """, unsafe_allow_html=True)

# ─── Run Check ────────────────────────────────────────────────────────────────
def check_url(url: str) -> dict:
    url = url.strip()
    if not url:
        return {}
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    try:
        start = time.time()
        resp = requests.get(url, timeout=8, allow_redirects=True)
        elapsed = round((time.time() - start) * 1000, 1)
        status = resp.status_code
        live = status < 400
        return {
            "URL": url,
            "Status": "🟢 LIVE" if live else "🔴 DOWN",
            "HTTP Code": status,
            "Response Time (ms)": elapsed,
            "Server": resp.headers.get("Server", "—"),
        }
    except requests.exceptions.ConnectionError:
        return {"URL": url, "Status": "🔴 DOWN", "HTTP Code": "Connection Error",
                "Response Time (ms)": "—", "Server": "—"}
    except requests.exceptions.Timeout:
        return {"URL": url, "Status": "🔴 TIMEOUT", "HTTP Code": "Timeout",
                "Response Time (ms)": ">8000", "Server": "—"}
    except Exception as e:
        return {"URL": url, "Status": "⚠️ ERROR", "HTTP Code": str(e),
                "Response Time (ms)": "—", "Server": "—"}


if run_btn:
    urls = [u.strip() for u in url_input.strip().splitlines() if u.strip()]
    if not urls:
        st.markdown('<div class="a-warn">⚠ &nbsp;Please enter at least one URL.</div>',
                    unsafe_allow_html=True)
    else:
        results = []
        prog = st.progress(0)
        status_text = st.empty()

        for i, url in enumerate(urls):
            status_text.markdown(f"""
            <div style="font-family:var(--mono);font-size:12px;
                        color:rgba(0,200,255,0.7);letter-spacing:1px;">
                › Checking: {url}
            </div>
            """, unsafe_allow_html=True)
            r = check_url(url)
            if r:
                results.append(r)
            prog.progress((i + 1) / len(urls))
            time.sleep(0.1)

        status_text.empty()
        prog.empty()

        if results:
            # Summary metrics
            live_count = sum(1 for r in results if "LIVE" in r["Status"])
            down_count = len(results) - live_count
            avg_time = [r["Response Time (ms)"] for r in results
                        if isinstance(r["Response Time (ms)"], (int, float))]
            avg_ms = round(sum(avg_time) / len(avg_time), 1) if avg_time else "—"

            sm1, sm2, sm3, sm4 = st.columns(4)
            with sm1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="mc-label">TOTAL CHECKED</div>
                    <div class="mc-value">{len(results)}</div>
                </div>""", unsafe_allow_html=True)
            with sm2:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="mc-label">LIVE</div>
                    <div class="mc-value" style="color:#00ff88;">{live_count}</div>
                </div>""", unsafe_allow_html=True)
            with sm3:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="mc-label">DOWN</div>
                    <div class="mc-value" style="color:#ff4d6a;">{down_count}</div>
                </div>""", unsafe_allow_html=True)
            with sm4:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="mc-label">AVG RESPONSE</div>
                    <div class="mc-value">{avg_ms}<span style="font-size:14px">ms</span></div>
                </div>""", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Individual status cards
            st.markdown('<div class="panel-title">📊 RESULTS</div>', unsafe_allow_html=True)

            for r in results:
                is_live = "LIVE" in r["Status"]
                border_color = "#00ff88" if is_live else "#ff4d6a"
                badge_class = "badge-live" if is_live else "badge-down"
                rt = r['Response Time (ms)']
                rt_str = f"{rt} ms" if isinstance(rt, (int, float)) else str(rt)

                st.markdown(f"""
                <div style="background:var(--panel);border:1px solid {border_color}33;
                            border-left:3px solid {border_color};border-radius:10px;
                            padding:16px 20px;margin-bottom:10px;
                            display:flex;align-items:center;justify-content:space-between;">
                    <div>
                        <div style="font-family:var(--mono);font-size:13px;
                                    color:var(--white);margin-bottom:4px;">
                            {r['URL']}
                        </div>
                        <div style="font-family:var(--mono);font-size:11px;
                                    color:rgba(255,255,255,0.3);">
                            HTTP {r['HTTP Code']} &nbsp;·&nbsp; {rt_str}
                            &nbsp;·&nbsp; Server: {r['Server']}
                        </div>
                    </div>
                    <div class="{badge_class}">
                        <span class="pulse">●</span> {r['Status'].split(' ', 1)[-1]}
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Full dataframe
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="panel-title">📋 FULL DATA</div>', unsafe_allow_html=True)
            df = pd.DataFrame(results)
            st.dataframe(df, use_container_width=True, hide_index=True)

            # Save to session logs
            if "logs" not in st.session_state:
                st.session_state["logs"] = []
            import datetime
            st.session_state["logs"].append({
                "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Module": "Website Monitor",
                "Action": f"Checked {len(results)} URLs",
                "Result": f"{live_count} live, {down_count} down"
            })
