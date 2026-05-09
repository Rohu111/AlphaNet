import os
import shutil
import streamlit as st

# ─── Config ───────────────────────────────────────────────────────────────────
DOWNLOADS_DIR = os.path.join(os.path.dirname(__file__), "..", "downloads")
DOWNLOADS_DIR = os.path.abspath(DOWNLOADS_DIR)

# ─── Page Setup ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Bulk Downloader", layout="wide")

st.markdown("""
<style>
    :root { --mono: 'Courier New', Courier, monospace; }
    .panel-title {
        font-family: var(--mono);
        font-size: 13px;
        font-weight: bold;
        color: #00ff88;
        letter-spacing: 2px;
        padding: 8px 0;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ─── Downloads folder viewer ──────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    '<div class="panel-title">📁 DOWNLOADS FOLDER</div>',
    unsafe_allow_html=True
)

files = [
    f for f in os.listdir(DOWNLOADS_DIR)
    if os.path.isfile(os.path.join(DOWNLOADS_DIR, f))
]

if files:

    for f in sorted(files)[:20]:

        fpath = os.path.join(DOWNLOADS_DIR, f)
        size  = os.path.getsize(fpath)

        col1, col2, col3, col4 = st.columns([5, 2, 2, 2])

        # ── File Name ─────────────────────────────────────────────────────────
        with col1:
            st.markdown(f"""
            <div style="
                padding:12px;
                background:rgba(255,255,255,0.03);
                border-radius:10px;
                font-family:var(--mono);
                font-size:12px;
                color:white;
                margin-bottom:8px;
            ">
                📄 {f}
            </div>
            """, unsafe_allow_html=True)

        # ── File Size ─────────────────────────────────────────────────────────
        with col2:
            st.markdown(f"""
            <div style="
                padding-top:12px;
                font-family:var(--mono);
                font-size:11px;
                color:#00ff88;
            ">
                {round(size / 1024, 1)} KB
            </div>
            """, unsafe_allow_html=True)

        # ── Browser Download (Save) Button ────────────────────────────────────
        with col3:
            with open(fpath, "rb") as file:
                st.download_button(
                    label="⬇ Save",
                    data=file,
                    file_name=f,
                    mime="application/octet-stream",
                    use_container_width=True,
                    key=f"download_{f}"
                )

        # ── Save to Local Downloads Folder ────────────────────────────────────
        with col4:
            LOCAL_DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")
            dest_path = os.path.join(LOCAL_DOWNLOADS, f)

            if st.button("💾 Save to Downloads", key=f"local_{f}", use_container_width=True):
                try:
                    os.makedirs(LOCAL_DOWNLOADS, exist_ok=True)
                    shutil.copy2(fpath, dest_path)
                    st.success(f"✅ Saved → {dest_path}")
                except Exception as e:
                    st.error(f"❌ Failed: {e}")

else:

    st.markdown("""
    <div style="
        font-family:var(--mono);
        font-size:12px;
        color:rgba(255,255,255,0.25);
        text-align:center;
        padding:30px;
    ">
        No files downloaded yet.
    </div>
    """, unsafe_allow_html=True)