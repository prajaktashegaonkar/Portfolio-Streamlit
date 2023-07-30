import streamlit as st
from pathlib import Path
from PIL import Image

# Setting up the path for the root files
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir/ "assets" / "Prajakta Shegaonkar Resume.pdf"
profile_pic = current_dir/"assets"/ "Profile_photo.png"


# General Details of Person
PAGE_TITLE = "Digital CV | Prajakta Shegaonkar"
PAGE_ICON = ":wave:"
NAME = "Prajakta Shegaonkar"
DESCRIPTION = """
Student at S.B.Jain Institute of Technology,Management and Research,Nagpur.
"""
Address="Nagpur,Maharashtra,India"
# Email
EMAIL = "prajaktashegaonkar3@gmail.com"
# Setting the page configuration of the default streamlit page
st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)
# st.title("Hello There ")



# Loading the resume file in binary format
with open(resume_file,"rb") as PDF_FILE :
 PDF_BYTE = PDF_FILE.read()


# Loading the profile picture
PROFILE_PIC = Image.open(profile_pic)


# HERO-SECTION
col1, col2 = st.columns(2,gap="small")
with col1:
 st.image(PROFILE_PIC,width=230)
with col2:
 st.title(NAME)
 st.write(DESCRIPTION)
 st.download_button(
 label="Download Resume",
 data=PDF_BYTE,
 file_name=resume_file.name,
 mime="application/octet-stream",
 )
st.write("Email:",EMAIL)


#About
st.write("#")
st.subheader("About")
st.write(""" As a passionate Web Developer with expertise in front-end and back-end
 technologies, I deliver high-quality projects that drive business growth
 and enhance user experience. With a strong foundation in HTML/CSS,
 JavaScript and various web frameworks I create responsive, efficient, and scalable web applications. I am committed to continuous learning
 and staying up-to-date with industry trends to deliver cutting-edge
 solutions. As an enthusiastic learner I am looking to expand my knowledge
 in the field of modern web development."
 """)


# Experience And Qualifications
st.markdown("---")
st.write("#")
st.subheader("Education")
st.write("S.B.Jain Institute of Technology,Management & Research, Nagpur")
st.markdown("Bachelor of Technology-BTech,Electronics and Telecommunication Engineering")
st.markdown("Year:2020-2024")
st.markdown("CGPA:9.36")


# Skills
st.markdown("---")
st.write("#")
st.subheader("Technical Skills")
st.write("""- C/C++ Programming
 - HTML
 - CSS
 - Python3
 - Javascript
 - MySQL
""")


# Projects and Accomplolishments
st.write("#")
st.subheader("Projects")
st.markdown("1)Book store Website")
st.write("""
 Role: Web Develepor
 --Designed website using HTML,CSS,Bootstrap,Javascript
 """)
st.markdown("2)Healthcare system using C++")
st.write("""
 Role: Programmer
 --Designed System based application for hospitals to manage staff data and patient data effectively. Also Designed the schema of database and Provided validation at the
user end.
end.
 """)
st.markdown("3)Currency Converter Using Python")
st.write(""" Role: Programmer
 --Designed an GUI based application that allows for the quick conversion of any
 currency and developed user friendly application.
 """)
         