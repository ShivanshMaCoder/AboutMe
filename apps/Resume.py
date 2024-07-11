import streamlit as st

def app():
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f2f6;
            background-image: url('https://www.transparenttextures.com/patterns/white-wall.png');
            background-size: cover;
            padding: 20px;
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
        .resume-container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: #f0f2f6;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .resume-container .resume-links {
            text-align: center;
            margin-bottom: 20px;
        }
        .resume-container .resume-links a {
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            font-size: 18px;
            font-weight: bold;
            color: #ffffff; /* Text color */
            background-color: #3498db; /* Button background color */
            border-radius: 5px;
            text-decoration: none;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        .resume-container .resume-links a:hover {
            background-color: #2980b9; /* Darker shade on hover */
            transform: translateY(-3px); /* Move up on hover */
        }
        .resume-container .resume-iframe {
            margin: auto;
            width: 100%;
            height: 1200px; /* Increased height */
            border: none;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        </style>
        """
    , unsafe_allow_html=True)

    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.markdown('<div class="title">My Resume</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-container">', unsafe_allow_html=True)

    st.markdown('<div class="resume-links">', unsafe_allow_html=True)
    resume_url = "https://drive.google.com/file/d/1CEC14r8vaghOmlHsADLqp7y7Bp3uMNvJ/view?usp=sharing"
    resume_download_url = "https://drive.google.com/uc?export=download&id=1CEC14r8vaghOmlHsADLqp7y7Bp3uMNvJ"
    st.write(f'<a href="{resume_url}" target="_blank">View Resume</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-iframe">', unsafe_allow_html=True)
    st.write('<iframe src="https://drive.google.com/file/d/1CEC14r8vaghOmlHsADLqp7y7Bp3uMNvJ/preview" width="100%" height="100%" style="border: none;"></iframe>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="resume-links">', unsafe_allow_html=True)
    st.write(f'<a href="{resume_download_url}" target="_blank">Download Resume</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
