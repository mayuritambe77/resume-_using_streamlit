import streamlit as st
from PIL import Image

# --- PAGE SETUP ---
st.set_page_config(page_title="Mayuri Tambe - Resume", layout="wide")

# --- PROFILE SECTION ---
col1, col2 = st.columns([1, 5])

with col1:
    image = Image.open("C:\\Users\\mayur\\Desktop\\project R\\streamlit library\\Mayuri Tambe.jpg")  # Replace with your actual image path
    st.image(image, width=120)

with col2:
    st.title("Mayuri Ashok Tambe")
    st.write("📧 mayuritambe777@gmail.com | 📞 6363472360")
    st.markdown("---")

# --- CAREER OBJECTIVE ---
st.header("🎯 Career Objective")
st.write("""
To work in an enthusiastic and supportive environment that provides opportunities to explore my knowledge and contribute meaningfully to the organization. 
Eager to apply my skills, learn continuously, and add value through innovation and dedication.
""")

# --- EXPERIENCE ---
st.header("💼 Experience")
st.subheader("CoCreate Ventures | Research Intern")
st.write("📍 Bangalore, Karnataka | 🗓️ Feb 2025 (Ongoing)")
st.markdown("""
- Developing automated cloud infrastructure provisioning and deployment using Terraform, RabbitMQ, and cost estimation services.
""")

st.subheader("Elewayte | AI Intern")
st.write("📍 Belagavi, Karnataka | 🗓️ May 2024 – June 2024")
st.markdown("""
- Specialized in Data Analysis and Healthcare AI, skilled in Machine Learning, Data Visualization, and Agile Project Management.
""")

st.subheader("Dlithe | IoT Intern")
st.write("📍 Belagavi, Karnataka | 🗓️ Oct 2023 – Nov 2023")
st.markdown("""
- Developed expertise in sensors and actuators while building the ‘Smart Gas’ project.
""")

st.subheader("Coached | Python Intern")
st.write("📍 Belagavi, Karnataka | 🗓️ Oct 2022 – Nov 2022")
st.markdown("""
- Strengthened Python programming and data visualization skills.
""")

# --- PROJECTS ---
st.header("🚀 Projects")

st.subheader("SmartSort – Municipal Waste Categorization")
st.markdown("""
- Created dataset with 5000 images across 9 categories and trained CNN and DenseNet201 models.
- Achieved 92% accuracy in automated waste categorization.
""")

st.subheader("Plant Leaf Disease Detection Using Deep Learning")
st.markdown("""
- Developed disease detection using CNN and Random Forest.
- Used HOG for feature extraction to enhance classification.
""")

st.subheader("License Plate Detection Using Image Processing")
st.markdown("""
- Implemented recognition using Python, OpenCV, and Tesseract OCR.
- Optimized for toll and traffic enforcement systems.
""")

# --- EDUCATION ---
st.header("🎓 Education")
st.subheader("Jain College of Engineering and Research")
st.write("📍 Belgaum | 🧑‍🎓 B.E. in Computer Science Engineering (8th Sem, Graduation: 2025)")
st.write("CGPA: 9.3")

# --- SKILLS ---
st.header("🧠 Skills")
st.subheader("Programming")
st.markdown("- Python\n- C/C++")

st.subheader("Technology")
st.markdown("- Git/GitHub\n- AWS\n- Linux\n- DevOps\n- Artificial Intelligence")

# --- CERTIFICATIONS ---
st.header("📜 Certifications")
st.markdown("""
- IIWCS-2024 by Springer and NIT Rourkela  
- 100 Days of Code: The Complete Python Bootcamp by Udemy
""")

# --- EXTRACURRICULAR ---
st.header("🎖️ Extracurricular Activities")
st.markdown("""
- Presented research paper at National Conference at NIT Rourkela (Feb 2024)  
- Organizer at BelPy 2024 (Python Conference)  
- Review paper under process: "Brain Controlled Cars Using AI"
""")

# --- LINKS ---
st.header("🔗 Links")
st.markdown("""
- [GitHub](https://github.com/mayuritambe77)  
- [LinkedIn](https://linkedin.com/in/mayuri-tambe-69736b27b)
""")

st.markdown("---")
st.write("Made with ❤️ using Streamlit")
st.write("© 2024 Mayuri Ashok Tambe")