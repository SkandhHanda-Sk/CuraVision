import streamlit as st
from ocr_engine import stream_ocr
from analysis_engine import stream_analysis


from styles import apply_custom_css

# --- 1. SETUP & STYLE ---
st.set_page_config(page_title="CuraVision", page_icon="🏥", layout="wide")
apply_custom_css()


# --- 2. STATE ---
if "res" not in st.session_state:
    st.session_state.update(res=None, ocr=None)


# --- 3. TOP HEADER ---
st.markdown("<h1 class='main-title'>🏥 CuraVision</h1>", unsafe_allow_html=True)
st.caption("Local OCR + Smart Analysis")
st.markdown("<div style='margin-bottom: -15px;'></div>", unsafe_allow_html=True)
st.divider()

# --- 4. THREE-COLUMN UI ---
col_img, col_ocr, col_res = st.columns([0.8, 1, 1.2], gap="medium")

with col_ocr:
    st.subheader("🔍 Raw Text")
    ocr_container = st.container(height=500) 
    if st.session_state.ocr:
        ocr_container.code(st.session_state.ocr)
    else:
        ocr_container.info("Raw text will appear here.")

with col_res:
    st.subheader("📋 Smart Analysis")
    res_container = st.container(height=500)
    if st.session_state.res:
        res_container.markdown(st.session_state.res)
        st.download_button(
            label="📄 Download Analysis",
            data=st.session_state.res,
            file_name="curavision_analysis.md",
            mime="text/markdown"
        )
    else:
        res_container.info("Analysis will appear here.")


with col_img:
    up_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    
    if up_file:
        b1, b2 = st.columns(2)
        analyze = b1.button("🚀 Analyze", type="primary", width="stretch")
        if b2.button("🗑️ Clear", width="stretch"):
            st.session_state.update(res=None, ocr=None)
            st.rerun()

        st.image(up_file, width='stretch')

        if analyze:
            # 1. Stream OCR in Middle Column
            with ocr_container:
                placeholder = st.empty()
                full_ocr = ""
                for chunk in stream_ocr(up_file.getvalue()):
                    full_ocr += chunk
                    placeholder.code(full_ocr)
                st.session_state.ocr = full_ocr
            
            # 2. Stream Analysis in Right Column
            with res_container:
                full_res = st.write_stream(stream_analysis(full_ocr))
                st.session_state.res = full_res
            st.rerun()