# Growth-Mindset-Challenge-Web-App-With-Giaic-Quarter-3-Project-1-

# Growth-Mindset-Challenge-Web-App-With-Giaic-Quarter-3-Project-1-
Ks trh project create krte streamlit pr kxh steps h use follow krte hue 


Step 1: Python Install Karein (Agar Pehle Se Nahi Hai)
Agar Python install nahi hai, to Python Download se install karein.
Confirm karein:
python --version

---

Step 2: Streamlit Install Karein
Directly install karein:
pip install streamlit
Check karein ke install ho gaya:
streamlit --version
---

Step 3: Python File Banayein
1. Ek naya folder banayein jisme aapka project hoga.
2. Usme ek Python file banayein, jaise app.py.
3. Yeh code paste karein:


import streamlit as st

st.title("🌱 Growth Mindset App")

st.write("Welcome to the Growth Mindset App! Here you can set goals, track progress, and stay motivated.")

# Goal Setting
goal = st.text_input("Set your goal:")
if st.button("Save Goal"):
    st.success(f"Goal Saved: {goal}")

# Progress Tracker
progress = st.slider("Track your progress:", 0, 100, 0)
st.progress(progress / 100)

# Daily Inspiration
st.subheader("🌟 Daily Inspiration")
st.write("Keep pushing forward! Every step counts.")
---

Step 4: Streamlit App Run Karein
1. Terminal ya CMD open karein.
2. Us folder me chalein jisme app.py hai.
3. Yeh command likhein aur enter karein:

streamlit run HERE YOUR FILE NAME
#LIKE 
streamlit run app.py


---

Step 5: Browser Me Dekhein
Jab aap command run karenge, web browser open hoga aur aapka Growth Mindset App show hoga! 🚀
