#!/usr/bin/env python3
"""
Client App Module
"""
import streamlit as st
from client_app.networking import send_dictionary, send_text_file

def main():
    """
    Main Streamlit Client Application
    """
    st.title("Client Application")

    action = st.selectbox("Action", ["Send Text File", "Send Dictionary"], key="action_select")

    if action == "Send Dictionary":
        key = st.text_input("Key", max_chars=50, key="dict_key")
        value = st.number_input("Value", min_value=0, max_value=100, step=1, key="dict_value")
        serialization_format = st.selectbox(
            "Serialization Format", 
            ["binary", "json", "xml"], 
            key="dict_serialize_format"
        )

        if st.button(
            "Send Dictionary", 
            key="send_dict_btn", 
            disabled=value < 1 or value > 100 or len(key) == 0 or len(key) > 50
            ):
            dictionary = {'key': key, 'value': value}
            send_dictionary(dictionary, serialization_format)
            st.success("Dictionary sent successfully!")

    elif action == "Send Text File":
        file = st.file_uploader("Choose a text file", type="txt", key="file_uploader")
        encrypt_data = st.checkbox("Encrypt File", value=True, key="encrypt_checkbox")

        if file and st.button("Send Text File", key="send_file_btn"):
            file_path = f"temp_{file.name}"
            with open(file_path, 'wb') as f:
                f.write(file.read())
            send_text_file(file_path, encrypt_data)
            st.success("Text file sent successfully!")

if __name__ == "__main__":
    main()
