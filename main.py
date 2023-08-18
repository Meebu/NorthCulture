import streamlit as st
import glob
import webbrowser
import random



def open_whatsapp():
    whatsapp_url = "https://api.whatsapp.com/send?phone=+92 334 1441122&text=I'm interested in buying your product!"
    webbrowser.open(whatsapp_url)

my_files=glob.glob("images/*jpeg")


st.image("Logo/Logo.png")
info_text="""
Welcome to The North Culture, where history, beauty, and you converge in a harmonious celebration.
 Explore our curated collection and adorn yourself with jewelry that echoes tales of heritage. 
 Every piece is a testament to the artistry that transcends time, 
a fusion of cultures that finds its place in your story."""
st.info(info_text)
st.subheader("Items")
col3,empty,col4=st.columns([1.5,0.5,1.5])

with col3:
    for i, item in enumerate(my_files[:3]):
        st.image(item)
        random_float = random.randint(4000, 5000)
        st.markdown(f"**Price : {random_float}**")
        if st.button("Buy Now",key=f"key{i}"):
            open_whatsapp()
        st.write("")

with col4:
    for i, item in enumerate(my_files[3:]):
        st.image(item)
        random_float = random.randint(4000, 5000)
        st.markdown(f"**Price : {random_float}**")
        if st.button("Buy Now",key=f"key{i+4}"):
            open_whatsapp()








