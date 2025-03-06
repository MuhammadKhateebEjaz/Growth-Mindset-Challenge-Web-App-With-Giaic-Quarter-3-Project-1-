#streamlit
# Imports

import streamlit as st
import pandas as pd
import os
from io import BytesIO

#set up our App


st.set_page_config(page_title="💿 Data sweeper", layout="wide")

#custom css
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: black;
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.title("💿 Data sweeper")
st.write("Transfrom your filesbetween CSV and Excel fromats with build-in data cleaning and visualization!")

uploaded_files = st.file_uploaded("Upload your files (CSV or Excle): " , tyoe  = ["csv , "xlsx"],"
"accept_multiple_files = True)"
"if uploaded_files :"
"for file in uploaded_files :"
"file_ext = os.path.splitext(file.name)[-1].lower()"
"if file_ext == ".csv" :"" 
"df = pd.read_csv(file)"
"elif file_ext == ".xlsx" :"            
"df = pd.read_excel(file)"
"else : "
"st.error(f"Unsupported file type : {file_ext}" )"
"continue"


#display info about the file
"st.write(f"💿 Data sweeper : {💿 Data sweeper}")"
st.write(f"File name : {file.name}")
st.write(f"File type : {file_size/1024:})
         

        #  show 5 rows of our df 

st.write("Preview the Head of the Dataframe"))
st.dataframe(df.head())

#option for data cleaning
st.subheader("Data Cleaning Options")
if st.checknox(f"Remove Duplicates From {file.name}"):
col1, col2 = st.columns(2)


with col1 :
if st.button(f"Remove Duplicates for {file.name}"):
    df.drop_duplicates(inplace = True)
    st.write("Duplicates Removed!")

with col2 :
if st.button(f"Fill Missing Valuesa for {file.name}"):
    numeric_cols = de.select_dytype(include = "number").columns
    df{numeric_cols} = df{numeric_cols}.fillna(df{numeric_cols}.mean())
    st.write("Missing values filled!")
     



# choose the file format to download
st.subheader(select colums to convert")"
colums = st.multiselect(f"Colums to convert for {file.name}", df.columns)
df = df{colums}


#Createsome Visualization
st.subheader("Data Visualization")
if st.checkbox("Show Visualization for {file.name}"):
st.bar_Chart(df.selct_dtypes(include = "number"). iloc {: ,:2}


#converting the file --> csv or excel
st.subheader("Conversion Options")  
coversions_type = st.radio(f"Convert {file.name} to :", ("CSV", "Excel"), key =file.name)   

if st.button(f"Convert {file.name}"):
buffer = BytestIO()
if conversions_type == "CSV":
df.to_csv(buffer, index = False)
file_name = file.name.replace("filr_ext", ".csv")
mime_type = "text/csv"
else:
converions_type == "Excel"
df.to_excel(buffer, index = False)
file_name = file.name.replace("file_ext", ".xlsx")
mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" 
buffer.seek(0)


#download button
st.download_button(label = f"Download {file.name} as {conversions_type},
                   data = buffer,
                   file_name = file_name,   
                     mime = mime_type)

st.success("All files processed successfully!") 









































# "file.seek(0)"
# "df = pd.read_csv(file)"
# "st.write(df)"
# "st.write("File uploaded successfully")"

# "if st.button("Download"):"
# "output = BytesIO()"
# "writer = pd.ExcelWriter(output, engine='xlsxwriter')"  
# "df.to_excel(writer, sheet_name='Sheet1')"
# "writer.save()"
# "output.seek(0)"
# "st.download_button(label="Download", data=output, file_name='output.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')"
# "else:"
# "st.write("Please upload a file")"
# The code above is a simple Streamlit app that allows users to upload a file, read the file, and display the data in the file. The app also allows users to download the data in the file in Excel format.
# To run the app, you can use the following command:    streamlit run App.py
# When you run the app, you will see a page that looks like this:   
# Conclusion
# In this article, we have shown you how to create a simple Streamlit app that allows users to upload a file, read the file, and display the data in the file. We have also shown you how to allow users to download the data in the file in Excel format.  
# We hope you found this article helpful. If you have any questions or comments, please let us know in the comments below.
# Happy coding!

# Peer Review Contributions by:  Lalithnarayan C
# The author read and approved the final manuscript.
# The code above is a simple Streamlit app that allows users to upload a file, read the file, and display the data in the file. The app also allows users to download the data in the file in Excel format.
# To run the app, you can use the following command:    streamlit run App.py

# The code above is a simple Streamlit app that allows users to upload a file, read the file, and display the data in the file. The app also allows users to download the data in the file in Excel format.
# To run the app, you can use the following command:    streamlit run App.py
# When you run the app, you will see a page that looks like this:
# Conclusion
# In this article, we have shown you how to create a simple Streamlit app that allows users to upload a file, read the file, and display the data in the file. We have also shown you how to allow users to download the data in the file in Excel format.
# We hope you found this article helpful. If you have any questions or comments, please let us know in the comments below.
# Happy coding!











