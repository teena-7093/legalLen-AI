import streamlit as st
import fitz

st.set_page_config(
    page_title="LegalLens AI",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ LegalLens AI")
st.subheader("AI-Powered Contract Risk Assessment")

st.write(
    "Upload a legal contract to begin preliminary contract analysis."
)

uploaded_file = st.file_uploader(
    "Upload your contract",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Contract uploaded successfully!")

    document = fitz.open(
        stream=uploaded_file.resad(),
        filetype="pdf"
    )

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    st.subheader("Extracted Contract Text")

    if extracted_text.strip():
        st.text_area(
            "Contract content",
            extracted_text,
            height=500
        )
    else:
        st.warning(
            "No text was detected. This may be a scanned PDF. "
            "OCR will be added in the next stage."
        )