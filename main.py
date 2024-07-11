import streamlit as st
from PIL import Image

# Set a custom theme
custom_theme = """
<style>
body {
    background-color: #f0f2f6; /* Match the background color of Home.py */
}
.sidebar .sidebar-content {
    background-color: #34495E;
    color: white;
    font-size: 18px;
}
.sidebar .sidebar-content a {
    color: #E74C3C;
    text-decoration: none;
}
.sidebar .sidebar-content a:hover {
    color: #FFFFFF;
}
</style>
"""
st.markdown(custom_theme, unsafe_allow_html=True)

# Load and resize passport photo
passport_photo = Image.open('images/Shivansh_PassportPic.jpg')  # Replace with your actual path
new_width = int(passport_photo.width * 0.8)
new_height = int(passport_photo.height * 0.8)
passport_photo_resized = passport_photo.resize((new_width, new_height))

# Function to generate HTML for sidebar
def sidebar_content():
    html = f'<a href="https://www.linkedin.com/in/mathur-shivansh/" target="_blank" rel="noopener noreferrer">'
    html += f'<img src="data:image/jpeg;base64,{image_to_base64(passport_photo_resized)}" style="cursor:pointer; border-radius: 50%;" width="80%" height="auto">'
    html += '</a>'
    return html

# Function to convert image to base64 format
def image_to_base64(image):
    import base64
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Sidebar navigation and global elements
st.sidebar.markdown(sidebar_content(), unsafe_allow_html=True)

# Import and run your app modules
from apps import Home, Contact, Projects, Resume

# Sidebar navigation
app = st.sidebar.selectbox(
    'Navigation',
    ('Home', 'Contact', 'Projects', 'Resume')
)

if app == 'Home':
    Home.app()
elif app == 'Contact':
    Contact.app()
elif app == 'Projects':
    Projects.app()
elif app == 'Resume':
    Resume.app()
