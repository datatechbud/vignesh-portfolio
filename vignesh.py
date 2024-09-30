import streamlit as st
from PIL import Image
import pandas as pd

# Customizing page configurations and layout
st.set_page_config(page_title="Vignesh Murugesan - Data Specialist Portfolio", layout="wide", initial_sidebar_state="expanded")

# Load external CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply CSS from external file
local_css("style.css")

# Sidebar for navigation with optimized spacing and image
st.sidebar.title("Vignesh Murugesan")
st.sidebar.image("https://media.licdn.com/dms/image/v2/D4E35AQEEYrxb1rKquA/profile-framedphoto-shrink_400_400/profile-framedphoto-shrink_400_400/0/1719440752616?e=1728126000&v=beta&t=abkbP0Q90Yl5HyUekGCIzpF54z2L8Itnubnw4u1804c", width=150)  # Use your uploaded image
st.sidebar.markdown("### Data Specialist Portfolio")
section = st.sidebar.radio("Navigate to:", ["About Me", "Skills", "Experience", "Education", "Projects", "Contact"])

# About Me Section
if section == "About Me":
    st.markdown("<h1 class='main-title'>Vignesh Murugesan</h1>", unsafe_allow_html=True)
    st.subheader("Data Specialist | SQL | Power BI | Databricks | Data-Driven Solutions")
    st.write("""
    I am a dedicated Data Specialist with expertise in analyzing data, creating visualizations, and implementing data solutions. With strong experience across industries such as retail, HR systems, and software development, I thrive on turning raw data into actionable insights. My primary goal is to help businesses optimize processes and drive revenue growth through data-driven strategies.
    """)

    st.write("Connect with me:")
    st.markdown("""
    - [LinkedIn](https://www.linkedin.com/in/vigneshmurugesan14/)
    - Email: vigneshmv1498@gmail.com
    - Location: Hoofddorp, Netherlands
    """)

# Skills Section
elif section == "Skills":
    st.markdown("<h2 class='section-title'>Skills</h2>", unsafe_allow_html=True)
    
    skills = {
        "SQL": 85,
        "Python": 75,
        "Data Visualization (Power BI, Tableau)": 90,
        "Javascript": 70,
        "Google BigQuery": 75,
        "Azure Databricks": 70,
        "Version Control (Git)": 80,
        "Splunk": 65
    }

    st.write("### Core Technical Skills")
    cols = st.columns(3)
    idx = 0
    for skill, level in skills.items():
        cols[idx].markdown(f"**{skill}**")
        cols[idx].progress(level)
        idx = (idx + 1) % 3  # Cycle through columns for better layout

    st.write("### Tools and Technologies")
    tools = {
        "Google BigQuery": 85,
        "Databricks": 80,
        "Microsoft Azure": 75,
        "Splunk": 60,
        "Postman & JSON": 70,
        "Looker Studio": 75,
    }
    st.dataframe(pd.DataFrame(list(tools.items()), columns=["Tool", "Proficiency Level"]))

# Experience Section
elif section == "Experience":
    st.markdown("<h2 class='section-title'>Professional Experience</h2>", unsafe_allow_html=True)

    st.subheader("Data Analyst | Akshayapatram B.V. (2024 - Present)")
    st.write("""
    - Spearheaded dynamic sales dashboards to analyze trends, leading to improved targeted marketing.
    - Boosted system efficiency by 2% through POS enhancements.
    - Reduced system downtime by 5% through improved monitoring and operations.
    """)

    st.subheader("Associate Software Application Engineer | Tesla (2023 - 2024)")
    st.write("""
    - Managed implementation and support of HR application, providing Level II & III support.
    - Coordinated data transformations using SQL for international teams.
    - Designed and executed test plans, ensuring robust software releases.
    """)

    st.subheader("Sales Data Analyst | Akshayapatram B.V. (2022 - 2023)")
    st.write("""
    - Analyzed sales trends, driving a 5% revenue increase and reducing food waste by 18%.
    - Developed Power BI dashboards, automating reports and reducing manual workload by 30%.
    """)

# Education Section
elif section == "Education":
    st.markdown("<h2 class='section-title'>Education</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Master of Science | Vrije Universiteit Amsterdam")
        st.write("**Major**: Computer Science (Software Engineering and Green IT)")
        st.write("**Dates**: 2019 - 2023")
        st.write("**Location**: Amsterdam, Netherlands")

    with col2:
        st.subheader("Bachelor of Engineering | Anna University, India")
        st.write("**Major**: Computer Science & Engineering")
        st.write("**Dates**: 2015 - 2019")
        st.write("**Location**: Erode, India")

# Projects Section
elif section == "Projects":
    st.markdown("<h2 class='section-title'>Notable Projects</h2>", unsafe_allow_html=True)

    st.subheader("1. Dynamic Sales Dashboard (2024)")
    st.write("""
    Developed a dynamic sales dashboard using Power BI, which visualized key performance indicators. This dashboard was instrumental in improving sales strategies and targeted marketing.
    """)

    st.subheader("2. HR Application Support (2023)")
    st.write("""
    Managed testing and deployment of an HR application at Tesla, ensuring a seamless user experience and improving system reliability.
    """)

    st.subheader("3. Carbon Footprint Reduction Project (2022)")
    st.write("""
    Collaborated with Accenture’s Data Delivery team to reduce the carbon emissions of leased cars, resulting in a 6% reduction in the overall carbon footprint.
    """)

# Contact Section
elif section == "Contact":
    st.markdown("<h2 class='section-title'>Get in Touch</h2>", unsafe_allow_html=True)
    
    st.write("You can contact me via:")
    st.markdown("""
    - **Email**: vigneshmv1498@gmail.com
    - **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/vigneshmurugesan14/)
    """)

    st.write("Feel free to reach out for data analysis or engineering-related opportunities!")

# Footer
st.markdown("""
    <hr style="border: 0; height: 2px; background-color: #f0f0f0;">
    <div class='footer'>© 2024 Vignesh Murugesan. All rights reserved.</div>
""", unsafe_allow_html=True)
