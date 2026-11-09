"""
OpportunityBob Launcher
Unified single command launcher for Streamlit
"""
import os
import subprocess
import sys

def main():
    print("Launching OpportunityBob on http://localhost:8501 ...")
    cmd = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "streamlit_app.py",
        "--server.port=8501",
        "--server.headless=true"
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    main()
