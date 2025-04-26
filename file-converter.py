# Imports
import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up the app
st.set_page_config(page_title="💿 Data Sweeper", layout="wide")

# App title and description
st.title("💿 Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

# File upload
uploaded_files = st.file_uploader(
    "Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        # Display info about the file
        st.write(f"💿 Data Sweeper")
        st.write(f"File name: {file.name}")
        st.write(f"File size: {file.size / 1024:.2f} KB")

        # Show a preview of the data
        st.write("### Preview of the Data")
        st.dataframe(df.head())

        # Data cleaning options
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Remove Duplicates from {file.name}"):
            if st.button(f"Remove Duplicates for {file.name}"):
                df.drop_duplicates(inplace=True)
                st.write("Duplicates removed!")

        if st.checkbox(f"Fill Missing Values for {file.name}"):
            if st.button(f"Fill Missing Values for {file.name}"):
                numeric_cols = df.select_dtypes(include="number").columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.write("Missing values filled!")

        # Column selection for conversion
        st.subheader("Select Columns to Convert")
        columns = st.multiselect(f"Columns to convert for {file.name}", df.columns)
        if columns:
            df = df[columns]

        # Data visualization
        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        # File conversion options
        st.subheader("Conversion Options")
        conversion_type = st.radio(
            f"Convert {file.name} to:", ("CSV", "Excel"), key=file.name
        )

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            else:  # Excel
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            # Download button
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type,
            )

    st.success("All files processed successfully!")
