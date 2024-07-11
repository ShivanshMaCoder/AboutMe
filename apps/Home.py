import streamlit as st
from PIL import Image

def app():
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f2f6;
            background-image: url('https://www.transparenttextures.com/patterns/white-wall.png');
            background-size: cover;
        }
        .title {
            font-size: 50px;
            font-weight: bold;
            color: #2C3E50;
            text-align: center;
            margin-top: 20px;
        }
        .content {
            font-size: 20px;
            color: #34495E;
            text-align: justify;
            margin: 20px;
        }
        .hyperlink {
            color: #1ABC9C;
            text-decoration: none;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<div class="title">Welcome to My Personal Website</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="content">
        Hello! I'm Shivansh Mathur, a passionate developer with a strong foundation in Computer Science and Engineering, 
        having completed my Bachelors from 
        <a class="hyperlink" href="https://www.thapar.edu/" target="_blank">Thapar Institute of Engineering and Technology</a>. 
        I am a quick learner with excellent grasping power, consistently seeking to expand my knowledge and skills.
        <br><br>
        I have developed and contributed to numerous projects in Data Engineering, Data Science, LLM, Gen AI, and Backend Development. 
        Additionally, I have solved over 700 LeetCode problems, showcasing my problem-solving abilities and dedication to continuous learning.
        <br><br>
        My hobbies include playing and watching football, staying updated with the latest technology trends, and building prototypes to explore new technological advancements.
        <br><br>
        I hold certifications as a 
        <a class="hyperlink" href="https://credentials.databricks.com/a59a06cc-4653-42be-9910-5bf7b1557c35#gs.c1opeu" target="_blank">Databricks Certified PySpark 3.0 Developer</a> 
        and a 
        <a class="hyperlink" href="https://google.accredible.com/a86de99b-0ac7-4518-8b63-3e182628abe8" target="_blank">Google Certified Associate Cloud Engineer</a>.
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
