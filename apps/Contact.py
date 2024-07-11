import streamlit as st

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
        .contact-container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: #f0f2f6;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .contact-container .contact-info {
            margin-bottom: 20px;
            padding-bottom: 20px;
            border-bottom: 1px solid #dcdde1;
        }
        .contact-container .contact-info p {
            margin: 10px 0;
            font-size: 18px;
            color: #2C3E50;
        }
        .contact-container .social-links {
            display: flex;
            justify-content: space-around;
            align-items: center;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .contact-container .social-links .social-item {
            text-align: center;
            margin-bottom: 20px;
            flex: 0 0 calc(25% - 20px);
        }
        .contact-container .social-links img {
            width: 50px;
            height: 50px;
            margin-bottom: 10px;
            transition: transform 0.3s ease;
        }
        .contact-container .social-links img:hover {
            transform: scale(1.1); /* Zoom effect on hover */
        }
        .contact-container .social-links p {
            font-size: 14px;
            color: #555555;
            margin: 0;
            line-height: 1.2;
        }
        .contact-container .social-links a {
            text-decoration: none;
            transition: color 0.3s ease;
            display: block; /* Make the entire link clickable */
        }
        .contact-container .social-links a:hover {
            color: #E74C3C;
        }
        .contact-container .social-links .description {
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
            color: #34495E; /* Darker shade of blue for better contrast */
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.markdown('<div class="title">Contact Me</div>', unsafe_allow_html=True)

    st.markdown('<div class="contact-container">', unsafe_allow_html=True)

    st.markdown('<div class="contact-info">', unsafe_allow_html=True)
    st.write("Mobile: +91 9810767910")
    st.write("Email: shivanshm2001@gmail.com")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="social-links">', unsafe_allow_html=True)

    # GitHub
    st.markdown('<div class="social-item">', unsafe_allow_html=True)
    st.write('[![GitHub](https://img.icons8.com/ios-filled/50/000000/github.png)](https://github.com/ShivanshMaCoder)')
    st.markdown('<p class="description" style="font-size: 18px; font-weight: bold;">View my projects and hoping for feedback</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # LinkedIn
    st.markdown('<div class="social-item">', unsafe_allow_html=True)
    st.write('[![LinkedIn](https://img.icons8.com/ios-filled/50/000000/linkedin.png)](https://www.linkedin.com/in/mathur-shivansh/)')
    st.markdown('<p class="description" style="font-size: 18px; font-weight: bold;">Let\'s connect on LinkedIn and explore more about me :)</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # LeetCode
    st.markdown('<div class="social-item">', unsafe_allow_html=True)
    st.write('[![LeetCode](https://img.icons8.com/external-tal-revivo-color-tal-revivo/24/000000/external-level-up-your-coding-skills-and-quickly-land-a-job-logo-color-tal-revivo.png)](https://leetcode.com/u/CoderShivuu/)')
    st.markdown('<p class="description" style="font-size: 18px; font-weight: bold;">I am a problem solver and love coding</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # GeeksforGeeks
    st.markdown('<div class="social-item">', unsafe_allow_html=True)
    st.write('[![GeeksforGeeks](https://upload.wikimedia.org/wikipedia/commons/4/43/GeeksforGeeks.svg)](https://www.geeksforgeeks.org/user/shivanshm2001/)')
    st.markdown('<p class="description" style="font-size: 18px; font-weight: bold;">I am a problem solver and love coding</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
