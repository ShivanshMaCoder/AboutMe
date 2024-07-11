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

    
    
    st.markdown('<div class="title">Projects</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="content">
        <h3>Incedo Inc. - Software Engineer (Data and AI)</h3>
        <h4>Tech Stack: Flask, Reactjs, GCP, Git</h4>
        <ul>
            <li>Led the development and implementation of VeriTel, improving operational efficiency by 64% for Verizon.</li>
            <li>Integrated real-time Looker dashboards in Reactjs, increasing user engagement by 25%.</li>
            <li>Pioneered ML algorithms for data analysis, enhancing accuracy by 30%, and implemented RAG for RCA and MoP, reducing Mean Time To Resolve by 78% to 10.56 hours.</li>
            <li>Managed DevOps with Git for Versioning and GCP Compute Engine, ensuring 99.99% uptime and scalability of VeriTel platform.</li>
        </ul>

        <h3>Incedo Inc. - Software Engineer (Data and AI)</h3>
        <h4>Tech Stack: Python, Langchain, MongoDB, HuggingFace, Flask</h4>
        <ul>
            <li>Improved the Code Review process by 60% through streamlined workflows and best practices.</li>
            <li>Leveraged HuggingFace open-source Language Models (LLMs) to enhance natural language processing capabilities, reducing costs by 97%.</li>
            <li>Used Flask as the backend microservice framework and MongoDB as the database, reducing latency by 53% for swift data retrieval.</li>
        </ul>

        <h3>Incedo Inc. - Software Engineer Intern (Data and AI)</h3>
        <h4>Tech Stack: Pyspark, AWS, PowerBI, MySQL</h4>
        <ul>
            <li>Automated data importing on AWS S3 bucket using boto3, reducing manual effort by 90%.</li>
            <li>Utilized AWS Glue Catalog and AWS Glue Crawler to enhance database organization and metadata storage, improving data accessibility by 81%.</li>
            <li>Created efficient ETL jobs on AWS Glue using PySpark, automating processes and reducing processing time by 25.7%.</li>
            <li>Established tables in AWS Athena and optimized SQL queries, improving data retrieval speed by 2.9%.</li>
            <li>Integrated PowerBI with AWS Athena using ODBC connector, increasing efficiency by 20% and enhancing decision-making by 91%.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
