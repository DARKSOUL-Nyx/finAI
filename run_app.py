import os
import sys
import streamlit
# Add the project root directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, project_root)
print(project_root)
# Now run the Streamlit app
if __name__ == "__main__":
    import streamlit.web.bootstrap
    streamlit.web.bootstrap.run("frontend/app.py", "", [], [])