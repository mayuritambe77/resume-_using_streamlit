import streamlit as st
from PIL import Image

# --- PAGE SETUP ---
# Set the page title and layout
st.set_page_config(page_title="Mayuri Tambe - Resume", layout="wide")

# --- CUSTOM CSS ---
# Add custom CSS for styling the resume
st.markdown("""
    <style>
        .title {
            color: #2E86C1;
            font-size: 36px;
            font-weight: bold;
        }
        .header {
            color: #117A65;
            font-size: 28px;
            font-weight: bold;
            margin-top: 20px;
        }
        .subheader {
            color: #D35400;
            font-size: 22px;
            font-weight: bold;
        }
        .text {
            color: #34495E;
            font-size: 18px;
        }
        .footer {
            color: #7D3C98;
            font-size: 16px;
            text-align: center;
            margin-top: 50px;
        }
        .divider {
            border-top: 2px solid #BDC3C7;
            margin: 20px 0;
        }
    </style>
""", unsafe_allow_html=True)

# --- PROFILE SECTION ---
# Display profile picture and basic contact information
col1, col2 = st.columns([1, 5])

with col1:
    # Load and display the profile image
    image = Image.open(r"C:\Users\mayur\Desktop\project R\streamlit library\Mayuri Tambe.jpg")
    st.image(image, width=120)

with col2:
    # Display name and contact details
    st.markdown('<div class="title">Mayuri Ashok Tambe</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">📧 mayuritambe777@gmail.com | 📞 6363472360</div>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- CAREER OBJECTIVE ---
# Display the career objective section
st.markdown('<div class="header">🎯 Career Objective</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        To work in an enthusiastic and supportive environment that provides opportunities to explore my knowledge 
        and contribute meaningfully to the organization. Eager to apply my skills, learn continuously, and add value 
        through innovation and dedication.
    </div>
""", unsafe_allow_html=True)

# --- EXPERIENCE ---
# Display the experience section
st.markdown('<div class="header">💼 Experience</div>', unsafe_allow_html=True)

# Experience 1
st.markdown('<div class="subheader">CoCreate Ventures | Research Intern</div>', unsafe_allow_html=True)
st.markdown('<div class="text">📍 Bangalore, Karnataka | 🗓️ Feb 2025 (Ongoing)</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        - Developing automated cloud infrastructure provisioning and deployment using Terraform, RabbitMQ, and cost estimation services.
    </div>
""", unsafe_allow_html=True)

# Experience 2
st.markdown('<div class="subheader">Elewayte | AI Intern</div>', unsafe_allow_html=True)
st.markdown('<div class="text">📍 Belagavi, Karnataka | 🗓️ May 2024 – June 2024</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        - Specialized in Data Analysis and Healthcare AI, skilled in Machine Learning, Data Visualization, and Agile Project Management.
    </div>
""", unsafe_allow_html=True)

# Experience 3
st.markdown('<div class="subheader">Dlithe | IoT Intern</div>', unsafe_allow_html=True)
st.markdown('<div class="text">📍 Belagavi, Karnataka | 🗓️ Oct 2023 – Nov 2023</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        - Developed expertise in sensors and actuators while building the ‘Smart Gas’ project.
    </div>
""", unsafe_allow_html=True)

# Experience 4
st.markdown('<div class="subheader">Coached | Python Intern</div>', unsafe_allow_html=True)
st.markdown('<div class="text">📍 Belagavi, Karnataka | 🗓️ Oct 2022 – Nov 2022</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        - Strengthened Python programming and data visualization skills.
    </div>
""", unsafe_allow_html=True)

# --- PROJECTS ---
# Display the projects section
st.markdown('<div class="header">🚀 Projects</div>', unsafe_allow_html=True)

# Project 1
st.markdown('<div class="subheader">SmartSort – Municipal Waste Categorization</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        - Created dataset with 5000 images across 9 categories and trained CNN and DenseNet201 models.<br>
        - Achieved 92% accuracy in automated waste categorization.
    </div>
""", unsafe_allow_html=True)

# Project 2
st.markdown('<div class="subheader">Plant Leaf Disease Detection Using Deep Learning</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        - Developed disease detection using CNN and Random Forest.<br>
        - Used HOG for feature extraction to enhance classification.
    </div>
""", unsafe_allow_html=True)

# Project 3
st.markdown('<div class="subheader">License Plate Detection Using Image Processing</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        - Implemented recognition using Python, OpenCV, and Tesseract OCR.<br>
        - Optimized for toll and traffic enforcement systems.
    </div>
""", unsafe_allow_html=True)

# --- EDUCATION ---
# Display the education section
st.markdown('<div class="header">🎓 Education</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Jain College of Engineering and Research</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        📍 Belgaum | 🧑‍🎓 B.E. in Computer Science Engineering (8th Sem, Graduation: 2025)<br>
        CGPA: 9.3
    </div>
""", unsafe_allow_html=True)

# --- SKILLS ---
# Display the skills section
st.markdown('<div class="header">🧠 Skills</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        <b>Programming:</b> Python, C/C++<br>
        <b>Technology:</b> Git/GitHub, AWS, Linux, DevOps, Artificial Intelligence
    </div>
""", unsafe_allow_html=True)

# --- CERTIFICATIONS ---
# Display the certifications section
st.markdown('<div class="header">📜 Certifications</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        - IIWCS-2024 by Springer and NIT Rourkela<br>
        - 100 Days of Code: The Complete Python Bootcamp by Udemy
    </div>
""", unsafe_allow_html=True)

# --- EXTRACURRICULAR ---
# Display the extracurricular activities section
st.markdown('<div class="header">🎖️ Extracurricular Activities</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        - Presented research paper at National Conference at NIT Rourkela (Feb 2024)<br>
        - Organizer at BelPy 2024 (Python Conference)<br>
        - Review paper under process: "Brain Controlled Cars Using AI"
    </div>
""", unsafe_allow_html=True)

# --- LINKS ---
# Display the links section
st.markdown('<div class="header">🔗 Links</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="text">
        - [GitHub](https://github.com/mayuritambe77)<br>
        - [LinkedIn](https://linkedin.com/in/mayuri-tambe-69736b27b)
    </div>
""", unsafe_allow_html=True)

# --- FOOTER ---
# Display the footer
st.markdown('<div class="footer">Made with ❤️ using Streamlit<br>© 2024 Mayuri Ashok Tambe</div>', unsafe_allow_html=True)