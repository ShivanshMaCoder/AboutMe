import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def display_passport_photo(self):
        st.sidebar.image('images/Shivansh_PassportPic.jpg', use_column_width=True)
        st.sidebar.markdown(
            """
            [LinkedIn Profile](https://www.linkedin.com/in/mathur-shivansh/)
            """
        )

    def run(self):
        self.display_passport_photo()

        st.sidebar.markdown(
            """
            <style>
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
            """, unsafe_allow_html=True
        )

        app = st.sidebar.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()

