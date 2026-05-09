import streamlit as st
import time

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AlphaNet — Secure Access",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── SHARED STYLE (imported on every page) ─────────────────────────────────────
def load_global_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@300;400;500;600;700&family=Orbitron:wght@400;700;900&display=swap');

    :root {
        --green:      #00ff88;
        --green-dim:  rgba(0,255,136,0.12);
        --green-glow: rgba(0,255,136,0.45);
        --cyan:       #00c8ff;
        --red:        #ff4d6a;
        --bg:         #030b14;
        --bg2:        #060f1e;
        --panel:      rgba(4,14,28,0.92);
        --border:     rgba(0,255,136,0.22);
        --white:      #e8f4f8;
        --mono:       'Share Tech Mono', monospace;
        --display:    'Orbitron', sans-serif;
        --body:       'Rajdhani', sans-serif;
    }

    /* ── Reset & base ── */
    html, body, [class*="css"] {
        font-family: var(--body) !important;
    }
    .stApp {
        background: #030b14 !important;
        color: var(--white) !important;
    }
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stSidebar"] { display: none; }

    /* ── Animated grid background ── */
    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        z-index: 0;
        background-image:
            linear-gradient(rgba(0,255,136,0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,255,136,0.04) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: gridMove 25s linear infinite;
        pointer-events: none;
    }
    @keyframes gridMove {
        0%   { background-position: 0 0; }
        100% { background-position: 50px 50px; }
    }

    /* ── Scanlines ── */
    .stApp::after {
        content: "";
        position: fixed;
        inset: 0;
        z-index: 1;
        background: repeating-linear-gradient(
            to bottom,
            transparent 0px, transparent 3px,
            rgba(0,0,0,0.05) 3px, rgba(0,0,0,0.05) 4px
        );
        pointer-events: none;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb { background: rgba(0,255,136,0.3); border-radius: 3px; }

    /* ── Neon text utilities ── */
    .neon-green { color: var(--green); text-shadow: 0 0 10px var(--green-glow); }
    .neon-cyan  { color: var(--cyan);  text-shadow: 0 0 10px rgba(0,200,255,0.5); }
    </style>
    """, unsafe_allow_html=True)


def login_page_css():
    st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none !important; }

    .login-wrap {
        display: flex;
        align-items: flex-start;
        justify-content: center;
        min-height: 80vh;
        padding-top: 40px;
        gap: 80px;
        position: relative;
        z-index: 10;
    }

    /* ── Left brand column ── */
    .brand-col { flex: 1.2; max-width: 600px; padding-top: 20px; }

    .terminal-block {
        background: rgba(0,0,0,0.55);
        border: 1px solid var(--border);
        border-left: 3px solid var(--green);
        border-radius: 8px;
        padding: 22px 26px;
        font-family: var(--mono);
        font-size: 13px;
        line-height: 2;
        color: rgba(0,255,136,0.75);
        margin-bottom: 40px;
        position: relative;
    }
    .terminal-block::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 100%;
        background: linear-gradient(180deg, rgba(0,255,136,0.06), transparent);
        border-radius: 8px;
        pointer-events: none;
    }
    .t-line { display: flex; align-items: center; gap: 10px; }
    .t-line::before { content: '›'; color: var(--cyan); font-size: 16px; }
    .t-ok {
        margin-left: auto;
        background: var(--green-dim);
        padding: 1px 8px;
        border-radius: 3px;
        border: 1px solid rgba(0,255,136,0.3);
        font-size: 11px;
        color: var(--green);
    }

    .logo-tag {
        font-family: var(--mono);
        font-size: 11px;
        color: var(--cyan);
        letter-spacing: 5px;
        margin-bottom: 10px;
    }
    .logo-main {
        font-family: var(--display);
        font-size: 76px;
        font-weight: 900;
        letter-spacing: -2px;
        line-height: 0.9;
        background: linear-gradient(135deg, var(--green) 0%, #00ffcc 50%, var(--cyan) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 0 18px var(--green-glow));
    }
    .logo-sub {
        font-family: var(--body);
        font-weight: 300;
        font-size: 14px;
        letter-spacing: 8px;
        color: rgba(0,200,255,0.65);
        margin-top: 14px;
        margin-bottom: 36px;
    }
    .logo-tagline {
        font-family: var(--mono);
        font-size: 13px;
        color: rgba(255,255,255,0.4);
        letter-spacing: 2px;
        margin-bottom: 30px;
    }

    .status-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
    }
    .sc {
        background: rgba(4,14,28,0.9);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 16px 18px;
        position: relative;
        overflow: hidden;
    }
    .sc::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--green), transparent);
    }
    .sc-lbl { font-family: var(--mono); font-size: 10px; color: rgba(255,255,255,0.35); letter-spacing: 2px; }
    .sc-val { font-family: var(--display); font-size: 12px; font-weight: 700; color: var(--green); margin-top: 4px; }
    .sc-dot {
        position: absolute; top: 14px; right: 14px;
        width: 7px; height: 7px; border-radius: 50%;
        background: var(--green); box-shadow: 0 0 8px var(--green);
        animation: blink 2s ease-in-out infinite;
    }
    @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.3} }

    /* ── Login card ── */
    .login-card {
        width: 400px;
        background: rgba(4,14,28,0.95);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 44px 38px;
        box-shadow:
            0 0 0 1px rgba(0,255,136,0.04),
            0 24px 60px rgba(0,0,0,0.65),
            0 0 60px rgba(0,255,136,0.06) inset;
        position: relative;
    }
    .corner { position: absolute; width: 18px; height: 18px; border-color: var(--green); border-style: solid; opacity: 0.55; }
    .tl { top:12px; left:12px;  border-width: 2px 0 0 2px; }
    .tr { top:12px; right:12px; border-width: 2px 2px 0 0; }
    .bl { bottom:12px; left:12px;  border-width: 0 0 2px 2px; }
    .br { bottom:12px; right:12px; border-width: 0 2px 2px 0; }

    .card-head { text-align: center; margin-bottom: 34px; }
    .card-icon {
        width: 54px; height: 54px;
        border-radius: 12px;
        background: var(--green-dim);
        border: 1px solid rgba(0,255,136,0.3);
        display: flex; align-items: center; justify-content: center;
        margin: 0 auto 18px;
        font-size: 26px;
        box-shadow: 0 0 20px rgba(0,255,136,0.18);
    }
    .card-title {
        font-family: var(--display);
        font-size: 17px; font-weight: 700;
        color: var(--white); letter-spacing: 3px;
    }
    .card-sub {
        font-family: var(--mono);
        font-size: 10px; color: rgba(0,200,255,0.55);
        letter-spacing: 3px; margin-top: 6px;
    }

    .field-lbl {
        font-family: var(--mono);
        font-size: 10px; color: rgba(0,255,136,0.65);
        letter-spacing: 3px; margin-bottom: 6px;
        display: block;
    }

    /* Style streamlit inputs */
    div[data-testid="stTextInput"] input {
        background: rgba(0,0,0,0.45) !important;
        border: 1px solid rgba(0,255,136,0.22) !important;
        border-radius: 8px !important;
        color: var(--white) !important;
        font-family: var(--mono) !important;
        font-size: 14px !important;
        letter-spacing: 1px !important;
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: var(--green) !important;
        box-shadow: 0 0 0 3px rgba(0,255,136,0.1) !important;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #00ff88, #00e07a) !important;
        color: #010d07 !important;
        font-family: var(--display) !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        letter-spacing: 4px !important;
        border: none !important;
        border-radius: 8px !important;
        width: 100% !important;
        height: 52px !important;
        box-shadow: 0 0 20px rgba(0,255,136,0.35) !important;
        transition: all 0.3s !important;
    }
    div.stButton > button:hover {
        box-shadow: 0 0 35px rgba(0,255,136,0.6) !important;
        transform: translateY(-1px) !important;
    }

    .alert-ok {
        background: rgba(0,255,136,0.08);
        border: 1px solid rgba(0,255,136,0.4);
        border-radius: 8px;
        padding: 12px 16px;
        font-family: var(--mono);
        font-size: 12px;
        color: var(--green);
        text-align: center;
        margin-top: 14px;
        letter-spacing: 1px;
    }
    .alert-err {
        background: rgba(255,77,106,0.08);
        border: 1px solid rgba(255,77,106,0.4);
        border-radius: 8px;
        padding: 12px 16px;
        font-family: var(--mono);
        font-size: 12px;
        color: var(--red);
        text-align: center;
        margin-top: 14px;
        letter-spacing: 1px;
    }

    .divider {
        display: flex; align-items: center; gap: 10px;
        font-family: var(--mono); font-size: 10px;
        color: rgba(255,255,255,0.18); letter-spacing: 2px;
        margin: 22px 0;
    }
    .divider::before, .divider::after {
        content: ''; flex: 1; height: 1px;
        background: rgba(0,255,136,0.1);
    }

    .card-footer {
        text-align: center;
        font-family: var(--mono);
        font-size: 10px;
        color: rgba(255,255,255,0.2);
        letter-spacing: 1px;
        line-height: 2;
        margin-top: 22px;
    }

    .top-bar {
        display: flex; align-items: center; justify-content: space-between;
        padding: 14px 0 30px;
        border-bottom: 1px solid var(--border);
        margin-bottom: 40px;
        position: relative; z-index: 10;
    }
    .tb-brand {
        font-family: var(--display);
        font-size: 13px; font-weight: 700;
        color: var(--green); letter-spacing: 4px;
        text-shadow: 0 0 10px var(--green-glow);
    }
    .tb-status {
        display: flex; gap: 20px;
        font-family: var(--mono); font-size: 11px;
        color: rgba(0,255,136,0.55);
    }
    .tb-s { display: flex; align-items: center; gap: 6px; }

    .footer-bar {
        margin-top: 60px;
        border-top: 1px solid var(--border);
        padding: 16px 0;
        display: flex; align-items: center; justify-content: space-between;
        font-family: var(--mono); font-size: 10px;
        color: rgba(0,255,136,0.3); letter-spacing: 2px;
        position: relative; z-index: 10;
    }
    </style>
    """, unsafe_allow_html=True)


# ─── LOGIN PAGE ───────────────────────────────────────────────────────────────
def show_login():
    load_global_css()
    login_page_css()

    # Top bar
    st.markdown("""
    <div class="top-bar">
        <div class="tb-brand">ALPHANET</div>
        <div class="tb-status">
            <div class="tb-s"><span class="sc-dot" style="position:static;margin:0"></span>MONITORING</div>
            <div class="tb-s"><span class="sc-dot" style="position:static;margin:0"></span>DOWNLOAD</div>
            <div class="tb-s"><span class="sc-dot" style="position:static;margin:0"></span>ANALYZER</div>
        </div>
        <div style="font-family:var(--mono);font-size:11px;color:var(--cyan);">v2.4.1-STABLE</div>
    </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1.3, 1], gap="large")

    # ── Left brand ──
    with col_left:
        st.markdown("""
        <div class="brand-col">
          <div class="terminal-block">
            <div style="font-family:var(--mono);font-size:11px;color:var(--cyan);letter-spacing:3px;margin-bottom:14px;">
              ALPHANET v2.4.1 — BOOT SEQUENCE
            </div>
            <div class="t-line">Initializing secure connection... <span class="t-ok">OK</span></div>
            <div class="t-line">Loading network modules... <span class="t-ok">OK</span></div>
            <div class="t-line">Establishing encrypted tunnel... <span class="t-ok">OK</span></div>
            <div class="t-line">Verifying system integrity... <span class="t-ok">OK</span></div>
            <div class="t-line">Ready for authentication. <span class="t-ok">STANDBY</span></div>
          </div>

          <div class="logo-tag">// NETWORK SECURITY PLATFORM</div>
          <div class="logo-main">ALPHA<br>NET</div>
          <div class="logo-sub">UTILITY &amp; MONITORING SUITE</div>
          <div class="logo-tagline">"Monitor. Analyze. Optimize."</div>

          <div class="status-grid">
            <div class="sc">
              <div class="sc-dot"></div>
              <div class="sc-lbl">MONITORING</div>
              <div class="sc-val">ONLINE</div>
            </div>
            <div class="sc">
              <div class="sc-dot"></div>
              <div class="sc-lbl">DOWNLOADER</div>
              <div class="sc-val">READY</div>
            </div>
            <div class="sc">
              <div class="sc-dot"></div>
              <div class="sc-lbl">ANALYZER</div>
              <div class="sc-val">ACTIVE</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Right login card ──
    with col_right:
        st.markdown("""
        <div class="login-card">
          <div class="corner tl"></div><div class="corner tr"></div>
          <div class="corner bl"></div><div class="corner br"></div>
          <div class="card-head">
            <div class="card-icon">🔐</div>
            <div class="card-title">SECURE ACCESS</div>
            <div class="card-sub">AUTHENTICATE TO CONTINUE</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<span class="field-lbl">IDENTIFIER</span>', unsafe_allow_html=True)
        username = st.text_input("username", placeholder="Enter username",
                                  label_visibility="collapsed", key="login_user")

        st.markdown('<span class="field-lbl">PASSPHRASE</span>', unsafe_allow_html=True)
        password = st.text_input("password", placeholder="Enter password",
                                  type="password", label_visibility="collapsed", key="login_pass")

        st.markdown("<br>", unsafe_allow_html=True)
        login_btn = st.button("ACCESS DASHBOARD", key="login_btn")

        if login_btn:
            if username == "admin" and password == "alpha123":
                with st.spinner("Authenticating..."):
                    time.sleep(1.2)
                st.markdown('<div class="alert-ok">✓ &nbsp; ACCESS GRANTED — WELCOME BACK</div>',
                            unsafe_allow_html=True)
                time.sleep(0.8)
                st.session_state["authenticated"] = True
                st.session_state["current_page"] = "home"
                st.rerun()
            elif not username or not password:
                st.markdown('<div class="alert-err">⚠ &nbsp; CREDENTIALS REQUIRED</div>',
                            unsafe_allow_html=True)
            else:
                st.markdown('<div class="alert-err">✕ &nbsp; INVALID CREDENTIALS — ACCESS DENIED</div>',
                            unsafe_allow_html=True)

        st.markdown("""
        <div class="divider">SECURED WITH AES-256</div>
        <div class="card-footer">
            Forgot credentials? &nbsp;·&nbsp; Request access<br>
            Protected by AlphaNet Security Protocol v2.4
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer-bar">
        <span>© 2025 TEAM ALPHA PAIR ⚡</span>
        <span>SESSION ENCRYPTED · TLS 1.3</span>
        <span>BUILD 2.4.1-STABLE</span>
    </div>
    """, unsafe_allow_html=True)


# ─── SESSION STATE INIT ───────────────────────────────────────────────────────
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "login"

# ─── ROUTER ──────────────────────────────────────────────────────────────────
if not st.session_state["authenticated"]:
    show_login()
else:
    # Redirect to dashboard
    st.switch_page("pages/1_Home.py")
