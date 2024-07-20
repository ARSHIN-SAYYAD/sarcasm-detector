import streamlit as st
from detection import detect_sarcasm
import base64
    
st.set_page_config(
    page_title="Sarcasm Detector",
    page_icon="favicon.ico",  # Path to your favicon file
)

titleimg = "img.webp"
def set_bg_hack(main_bg):
# set bg name
    main_bg_ext = "png"

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-repeat: no-repeat;
            background-position: 40rem ;
            background-size: contain;
            background-attachment: scroll;
            
        }}
       
        </style>
        """,
        unsafe_allow_html=True,
    )
set_bg_hack(titleimg)

def main():
    st.title("Witty or Not?")
    
    st.write("Enter some text to check if it is sarcastic or not.")

    user_input = st.text_area("Enter your text here:")
    
    if st.button("Detect Sarcasm"):
        if user_input:
            result = detect_sarcasm(user_input)
            st.write(f"Prediction: {result}")
        else:
            st.write("Please enter some text.")

if __name__ == "__main__":
    main()
