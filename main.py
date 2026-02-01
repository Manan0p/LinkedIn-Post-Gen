import streamlit as st
from few_shot import FewShotPosts

def main():
    st.title("LinkedIn Post Generator")
    col1, col2, col3 = st.columns(3)
    fs = FewShotPosts()
    with col1:
        st.selectbox("Topic", options=fs.get_tags())

    with col2:
        st.selectbox("Language", options=["English", "Hinglish", "Hindi"])

if __name__ == "__main__":
    main()