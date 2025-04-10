import streamlit as st
from PIL import Image

# Hero Section
st.title('Mayuri Ashok Tambe')
st.write('Brief introduction about yourself')
image = Image.open('C:\\Users\\mayur\\Desktop\\project R\\streamlit library\\Mayuri Tambe.jpg')
st.image(image, caption='Mayuri Tambe', use_column_width=True)

# Contact Information
st.header('Contact Information')
st.write('Email: mayuritambe777@gmail.com')
st.write('Phone: 6363472360')
#st.write('[LinkedIn](https://www.linkedin.com/in/yourprofile)')

# Experience
st.header('Experience')
st.subheader('CoCreate Ventures')
st.write('Duration: Feb 2025 - May 2025')
st.write('Working on a cloud project')

# Education
st.header('Education')
st.subheader('Jain college of Engineering and Research')
st.write('Bachelor of Engineering in Computer Science')
st.write('Year of Graduation: 2025')
st.write('Remarks: 9.3 CGPA')

# Skills
st.header('Skills')
st.write('- Skill 1')
st.write('- Skill 2')
st.write('- Skill 3')

# Projects
st.header('Projects')
st.subheader('Project Name')
st.write('Description of the project.')
#st.write('[Project Link](https://github.com/yourusername/projectname)')
