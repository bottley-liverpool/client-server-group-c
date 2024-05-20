"""
Main module for running the server and client app
"""
import threading
import subprocess
import os
import time

def run_server():
    """
    Run the local server.
    """
    subprocess.run(["python", "server_app/local_server.py"], env=os.environ, check=False)

def run_streamlit_app():
    """
    Run the Streamlit app.
    """
    subprocess.run(["streamlit", "run", "client_app/app.py"], env=os.environ, check=False)

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.environ['PYTHONPATH'] = project_root

    server_thread = threading.Thread(target=run_server)
    streamlit_thread = threading.Thread(target=run_streamlit_app)

    server_thread.start()

    time.sleep(2)

    streamlit_thread.start()

    server_thread.join()
    streamlit_thread.join()
