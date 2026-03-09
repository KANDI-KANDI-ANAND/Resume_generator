import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="AI Resume Optimizer",
    page_icon="📄",
    layout="wide"
)


st.markdown("""
<style>
/* Remove default streamlit padding */
.block-container {
    padding-top: 1rem !important;
    margin-bottom: 2rem !important;
    margin-left: 2rem !important;
    margin-right: 2rem !important;
    max-width: 100% !important;
}

/* Hide default header/footer */
[data-testid="stHeader"]     { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
#MainMenu, footer            { display: none !important; }

/* ── BUG 2 FIX: Fix left column, scroll right column independently ── */

/* Target the first column (left 30%) — make it fixed */
[data-testid="stHorizontalBlock"] > div:first-child {
    position: fixed !important;
    top: 2rem !important;
    left: 2rem !important;
    height: 90vh !important;
    overflow-y: auto !important;
    background: #ffffff !important;
    border-right: 1px solid #e8eaf0 !important;
    padding: 1.5rem 1.2rem !important;
    z-index: 100 !important;
    /* width is ~30% of viewport to match the column ratio */
    width: 30% !important;
}

/* Target the second column (right 70%) — push it right and allow scroll */
[data-testid="stHorizontalBlock"] > div:last-child {
    margin-left: 30% !important;
    height: 100vh !important;
    overflow-y: auto !important;
    padding: 1.5rem 1.5rem !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# SESSION STATE
# -------------------------

if "api_key" not in st.session_state:
    st.session_state.api_key = None

if "resume_path" not in st.session_state:
    st.session_state.resume_path = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "awaiting_jd" not in st.session_state:
    st.session_state.awaiting_jd = False

if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0


# -------------------------
# LAYOUT
# -------------------------

left, right = st.columns([3,7])

# =================================================
# LEFT PANEL
# =================================================

with left:

    st.markdown("## ⚙️ Setup")

    api_key = st.text_input(
        "Enter API Key",
        type="password"
    )

    if st.button("Save API Key"):

        if api_key.strip():

            st.session_state.api_key = api_key
            os.environ["GOOGLE_API_KEY"] = api_key.strip()
            st.success("API key saved")

        else:
            st.warning("Enter API key")

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"],
        key=f"resume_uploader_{st.session_state.uploader_key}"
    )

    if uploaded_file is not None:
        os.makedirs("uploads", exist_ok=True)
        path = os.path.join("uploads", uploaded_file.name)
        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.session_state.resume_path = path
        st.success("Resume uploaded")

        if st.button("Remove Resume"):
            st.session_state.resume_path = None
            st.session_state.awaiting_jd = False
            # Increment key → Streamlit renders a brand new empty uploader
            st.session_state.uploader_key += 1
            st.rerun()

    else:
        # KEY FIX: user clicked ✕ on uploader — sync session state immediately
        if st.session_state.resume_path is not None:
            st.session_state.resume_path = None
            st.session_state.awaiting_jd = False


# =================================================
# CHAT PANEL
# =================================================

with right:

    st.markdown("## 🤖 Resume Assistant")

    # display history
    for role, msg in st.session_state.chat_history:

        with st.chat_message(role):
            st.write(msg)


    if st.session_state.awaiting_jd:
        placeholder = "Paste Job Description here"
    else:
        placeholder = "Send a message"

    user_input = st.chat_input(placeholder)

    if user_input:

        if not st.session_state.awaiting_jd:
            # ── Normal message handling ──
            st.session_state.chat_history.append(("user", user_input))

            if not st.session_state.api_key:
                bot_msg = "Please enter your API key."
            elif not st.session_state.resume_path:
                bot_msg = "Please upload your resume."
            else:
                st.session_state.awaiting_jd = True
                bot_msg = "Please paste the **Job Description** below."

            st.session_state.chat_history.append(("assistant", bot_msg))
            st.rerun()

        else:
            # ── Job Description handling ──
            jd_text = user_input
            st.session_state.chat_history.append(("user", jd_text))

            with st.chat_message("assistant"):
                with st.spinner("Optimizing resume..."):

                    from graph import workflow

                    initial_state = {
                        "Old_Resume": st.session_state.resume_path,
                        "Job_JD": jd_text,
                        "iteration": 0,
                        "max_iteration": 4
                    }

                    result = workflow.invoke(initial_state)
                    pdf_path = result["pdf_path"]

                    st.success("Resume optimized!")
                    st.text(f"Generated resume ATS score: {result['optimized_resume_ats_score']}")

                    if result.get("reason"):
                        st.text(f"Reason: {result['reason']}")

                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            "Download Optimized Resume",
                            f,
                            file_name="optimized_resume.pdf",
                            mime="application/pdf"
                        )

            st.session_state.awaiting_jd = False