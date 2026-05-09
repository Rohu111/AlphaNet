import streamlit as st

VALID_USER = "admin"
VALID_PASS = "alpha123"

def check_auth():
    """Guard every page — redirects to login if not authenticated."""
    if not st.session_state.get("authenticated"):
        st.switch_page("app.py")

def load_dashboard_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@300;400;500;600;700&family=Orbitron:wght@400;700;900&display=swap');

    :root {
        --green:      #00ff88;
        --green-dim:  rgba(0,255,136,0.12);
        --green-glow: rgba(0,255,136,0.45);
        --cyan:       #00c8ff;
        --red:        #ff4d6a;
        --orange:     #ff9f43;
        --yellow:     #ffd700;
        --bg:         #030b14;
        --panel:      rgba(4,14,28,0.92);
        --border:     rgba(0,255,136,0.2);
        --white:      #e8f4f8;
        --mono:       'Share Tech Mono', monospace;
        --display:    'Orbitron', sans-serif;
        --body:       'Rajdhani', sans-serif;
    }

    html, body, [class*="css"] { font-family: var(--body) !important; }
    .stApp { background: #030b14 !important; color: var(--white) !important; }
    #MainMenu, footer, header { visibility: hidden; }

    /* Animated grid */
    .stApp::before {
        content: "";
        position: fixed; inset: 0; z-index: 0;
        background-image:
            linear-gradient(rgba(0,255,136,0.035) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,255,136,0.035) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: gridMove 25s linear infinite;
        pointer-events: none;
    }
    @keyframes gridMove {
        0%   { background-position: 0 0; }
        100% { background-position: 50px 50px; }
    }
    .stApp::after {
        content: "";
        position: fixed; inset: 0; z-index: 1;
        background: repeating-linear-gradient(
            to bottom, transparent 0px, transparent 3px,
            rgba(0,0,0,0.04) 3px, rgba(0,0,0,0.04) 4px
        );
        pointer-events: none;
    }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb { background: rgba(0,255,136,0.28); border-radius: 3px; }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(3,8,18,0.97) !important;
        border-right: 1px solid var(--border) !important;
    }
    [data-testid="stSidebarNav"] { display: none; }

    /* Sidebar content */
    .sidebar-logo {
        font-family: var(--display);
        font-size: 22px; font-weight: 900;
        background: linear-gradient(135deg, var(--green), var(--cyan));
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 2px; text-align: center;
        padding: 10px 0 4px;
    }
    .sidebar-tagline {
        font-family: var(--mono); font-size: 9px;
        color: rgba(0,200,255,0.5); letter-spacing: 3px;
        text-align: center; margin-bottom: 24px;
    }
    .nav-section {
        font-family: var(--mono); font-size: 9px;
        color: rgba(255,255,255,0.25); letter-spacing: 3px;
        padding: 10px 0 6px; margin-bottom: 4px;
        border-bottom: 1px solid rgba(0,255,136,0.08);
    }
    .nav-item {
        display: flex; align-items: center; gap: 10px;
        padding: 10px 12px; border-radius: 8px;
        font-family: var(--body); font-size: 15px; font-weight: 500;
        color: rgba(255,255,255,0.55);
        cursor: pointer; transition: all 0.2s;
        margin-bottom: 3px; text-decoration: none;
    }
    .nav-item:hover {
        background: var(--green-dim); color: var(--green);
    }
    .nav-item.active {
        background: rgba(0,255,136,0.15);
        color: var(--green);
        border-left: 3px solid var(--green);
    }

    /* Page header */
    .page-header {
        display: flex; align-items: center; justify-content: space-between;
        padding: 0 0 20px;
        border-bottom: 1px solid var(--border);
        margin-bottom: 28px;
        position: relative; z-index: 10;
    }
    .page-title {
        font-family: var(--display);
        font-size: 22px; font-weight: 900;
        color: var(--white); letter-spacing: 2px;
    }
    .page-badge {
        font-family: var(--mono); font-size: 10px;
        color: var(--green); letter-spacing: 3px;
        background: var(--green-dim); border: 1px solid rgba(0,255,136,0.28);
        padding: 4px 12px; border-radius: 4px;
    }

    /* Metric cards */
    .metric-card {
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 22px 24px;
        position: relative; overflow: hidden;
        transition: border-color 0.3s, transform 0.3s;
    }
    .metric-card:hover { border-color: var(--green); transform: translateY(-2px); }
    .metric-card::before {
        content: '';
        position: absolute; top: 0; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, transparent, var(--green), transparent);
    }
    .mc-icon { font-size: 28px; margin-bottom: 10px; }
    .mc-label {
        font-family: var(--mono); font-size: 10px;
        color: rgba(255,255,255,0.35); letter-spacing: 3px; margin-bottom: 6px;
    }
    .mc-value {
        font-family: var(--display); font-size: 28px; font-weight: 900;
        color: var(--green); line-height: 1;
    }
    .mc-sub {
        font-family: var(--mono); font-size: 11px;
        color: rgba(255,255,255,0.3); margin-top: 6px;
    }

    /* Panel cards */
    .panel-card {
        background: var(--panel);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 24px 26px;
        position: relative; overflow: hidden;
        margin-bottom: 20px;
    }
    .panel-title {
        font-family: var(--display); font-size: 13px; font-weight: 700;
        color: var(--white); letter-spacing: 2px; margin-bottom: 18px;
        display: flex; align-items: center; gap: 10px;
    }
    .panel-title::after {
        content: ''; flex: 1; height: 1px;
        background: linear-gradient(90deg, var(--border), transparent);
    }

    /* Status badge */
    .badge-live {
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(0,255,136,0.1); border: 1px solid rgba(0,255,136,0.35);
        color: var(--green); border-radius: 4px;
        padding: 3px 10px; font-family: var(--mono); font-size: 11px;
    }
    .badge-down {
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(255,77,106,0.1); border: 1px solid rgba(255,77,106,0.35);
        color: var(--red); border-radius: 4px;
        padding: 3px 10px; font-family: var(--mono); font-size: 11px;
    }
    .pulse { animation: blink 1.4s ease-in-out infinite; }
    @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.3} }

    /* Quick action cards */
    .action-card {
        background: var(--panel); border: 1px solid var(--border);
        border-radius: 12px; padding: 26px 24px; text-align: center;
        transition: all 0.3s; cursor: pointer; position: relative; overflow: hidden;
    }
    .action-card:hover {
        border-color: var(--green);
        box-shadow: 0 0 25px rgba(0,255,136,0.12);
        transform: translateY(-3px);
    }
    .action-card::before {
        content: ''; position: absolute; top:0; left:0; right:0; height:2px;
        background: linear-gradient(90deg, transparent, var(--cyan), transparent);
    }
    .ac-icon { font-size: 36px; margin-bottom: 12px; }
    .ac-title {
        font-family: var(--display); font-size: 13px; font-weight: 700;
        color: var(--white); letter-spacing: 2px; margin-bottom: 8px;
    }
    .ac-desc {
        font-family: var(--mono); font-size: 11px;
        color: rgba(255,255,255,0.35); line-height: 1.6;
    }

    /* Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, var(--green), #00e07a) !important;
        color: #010d07 !important;
        font-family: var(--display) !important;
        font-size: 11px !important; font-weight: 700 !important;
        letter-spacing: 3px !important;
        border: none !important; border-radius: 8px !important;
        box-shadow: 0 0 18px rgba(0,255,136,0.3) !important;
        transition: all 0.3s !important;
        padding: 10px 20px !important;
    }
    div.stButton > button:hover {
        box-shadow: 0 0 30px rgba(0,255,136,0.55) !important;
        transform: translateY(-1px) !important;
    }

    /* Text inputs */
    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea {
        background: rgba(0,0,0,0.4) !important;
        border: 1px solid rgba(0,255,136,0.2) !important;
        border-radius: 8px !important;
        color: var(--white) !important;
        font-family: var(--mono) !important;
        font-size: 13px !important;
    }
    div[data-testid="stTextInput"] input:focus,
    div[data-testid="stTextArea"] textarea:focus {
        border-color: var(--green) !important;
        box-shadow: 0 0 0 2px rgba(0,255,136,0.1) !important;
    }

    /* Dataframe */
    div[data-testid="stDataFrame"] {
        border: 1px solid var(--border) !important;
        border-radius: 10px !important;
        overflow: hidden;
        font-family: var(--mono) !important;
    }

    /* Divider */
    hr { border-color: var(--border) !important; }

    /* Sidebar buttons */
    .sidebar-nav-btn {
        width: 100%; text-align: left;
        background: transparent; border: none;
        padding: 10px 12px; border-radius: 8px;
        font-family: var(--body); font-size: 15px; font-weight: 500;
        color: rgba(255,255,255,0.55);
        cursor: pointer; transition: all 0.2s;
        display: flex; align-items: center; gap: 10px;
        margin-bottom: 3px;
    }

    /* Success / error alerts */
    .a-ok {
        background: rgba(0,255,136,0.07);
        border: 1px solid rgba(0,255,136,0.35);
        border-radius: 8px; padding: 12px 16px;
        font-family: var(--mono); font-size: 12px;
        color: var(--green); text-align: center;
        margin: 10px 0; letter-spacing: 1px;
    }
    .a-err {
        background: rgba(255,77,106,0.07);
        border: 1px solid rgba(255,77,106,0.35);
        border-radius: 8px; padding: 12px 16px;
        font-family: var(--mono); font-size: 12px;
        color: var(--red); text-align: center;
        margin: 10px 0; letter-spacing: 1px;
    }
    .a-warn {
        background: rgba(255,159,67,0.07);
        border: 1px solid rgba(255,159,67,0.35);
        border-radius: 8px; padding: 12px 16px;
        font-family: var(--mono); font-size: 12px;
        color: var(--orange); text-align: center;
        margin: 10px 0; letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)


def render_sidebar(active_page="home"):
    nav_items = [
        ("home",    "🏠", "Home"),
        ("monitor", "🌐", "Website Monitor"),
        ("bulk",    "📥", "Bulk Downloader"),
        ("speed",   "🚀", "Speed Test"),
        ("logs",    "📜", "Logs"),
        ("about",   "ℹ️",  "About"),
    ]
    page_map = {
        "home":    "pages/1_Home.py",
        "monitor": "pages/2_Website_Monitor.py",
        "bulk":    "pages/3_Bulk_Downloader.py",
        "speed":   "pages/4_Speed_Test.py",
        "logs":    "pages/5_Logs.py",
        "about":   "pages/6_About.py",
    }

    with st.sidebar:
        st.markdown('<div class="sidebar-logo">ALPHANET</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-tagline">MONITOR · ANALYZE · OPTIMIZE</div>', unsafe_allow_html=True)
        st.markdown('<div class="nav-section">NAVIGATION</div>', unsafe_allow_html=True)

        for key, icon, label in nav_items:
            is_active = (key == active_page)
            style = (
                "background:rgba(0,255,136,0.14);color:#00ff88;"
                "border-left:3px solid #00ff88;font-weight:600;"
                if is_active
                else "color:rgba(255,255,255,0.55);"
            )
            if st.button(f"{icon}  {label}", key=f"nav_{key}",
                         use_container_width=True):
                st.switch_page(page_map[key])

        st.markdown("---")
        st.markdown('<div class="nav-section">SYSTEM</div>', unsafe_allow_html=True)

        # Status indicators
        st.markdown("""
        <div style="font-family:var(--mono);font-size:11px;padding:8px 4px;line-height:2.2;">
            <div style="color:rgba(0,255,136,0.7);">● &nbsp;Monitoring — ONLINE</div>
            <div style="color:rgba(0,255,136,0.7);">● &nbsp;Downloader — READY</div>
            <div style="color:rgba(0,255,136,0.7);">● &nbsp;Speed Analyzer — ACTIVE</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        if st.button("🔒  Logout", key="logout_btn", use_container_width=True):
            st.session_state["authenticated"] = False
            st.switch_page("app.py")
