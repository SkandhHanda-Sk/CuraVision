import streamlit as st

def apply_custom_css():
    """
    Applies professional CSS styling to the Streamlit application.
    Focuses on branding, responsive layout, and custom UI components.
    """
    st.markdown("""
    <style>
        /* Hide default Streamlit elements for a cleaner dashboard look */
        #MainMenu, footer, header {visibility: hidden;}
        
        /* Main container layout constraints */
        .block-container {
            padding-top: 1.5rem; 
            padding-bottom: 0rem;
            height: 100vh;
            overflow: hidden;
        }
        
        /* Gradient title styling with modern typography */
        .main-title {
            background: linear-gradient(90deg, #38bdf8, #818cf8, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            font-size: 2.2rem;
            margin-bottom: -10px;
        }
        
        /* Image container aesthetics */
        [data-testid="stImage"] {
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.1);
            overflow: hidden;
        }
        
        /* Custom upload dropzone styling */
        [data-testid="stFileUploadDropzone"] {
            border: 1px dashed rgba(255,255,255,0.2) !important;
            border-radius: 12px;
            background: rgba(255,255,255,0.02);
        }
        
        [data-testid="stFileUploadDropzone"]:hover {
            border-color: #38b8f8 !important;
            background: rgba(255,255,255,0.06);
        }
        
        /* Interactive button animations and shadows */
        .stButton > button {
            border-radius: 8px;
            transition: all 0.2s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(56, 189, 248, 0.25);
        }
        
        /* Responsive scrollable block management */
        [data-testid="stVerticalBlockBorderWrapper"] {
            height: calc(100vh - 230px) !important;
        }
        
        /* Global app scroll management */
        .stApp {
            overflow: hidden;
        }
    </style>
    """, unsafe_allow_html=True)
