
import streamlit as st
import pandas as pd

st.title("Upload CSV and Analyze")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Download CSV")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="data.csv",
        mime="text/csv"
    )
