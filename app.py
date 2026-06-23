import streamlit as st
from streamlit_option_menu import option_menu
import os

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Viniksan Portfolio",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background:
    radial-gradient(circle at 10% 20%, rgba(0,217,255,0.15) 0%, transparent 30%),
    radial-gradient(circle at 90% 80%, rgba(124,58,237,0.15) 0%, transparent 30%),
    #0E1117;
}

.hero{
    background:linear-gradient(135deg,#111827,#1F2937);
    padding:50px;
    border-radius:25px;
    text-align:center;
    border:1px solid #00D9FF;
    animation:float 4s ease-in-out infinite;
}

@keyframes float{
    0%{transform:translateY(0px);}
    50%{transform:translateY(-8px);}
    100%{transform:translateY(0px);}
}

.glow{
    color:white;
    text-shadow:
    0 0 10px #00D9FF,
    0 0 20px #00D9FF,
    0 0 40px #00D9FF,
    0 0 80px #00D9FF;
}

.card{
    background:#161B22;
    padding:25px;
    border-radius:20px;
    margin-bottom:20px;
    border:1px solid #2D3748;
    transition:0.4s;
}

.card:hover{
    transform:translateY(-5px);
    border:1px solid #00D9FF;
}

h1,h2,h3,h4,p{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    selected = option_menu(
        menu_title="VINIKSAN",
        options=[
            "Home",
            "About",
            "Skills",
            "Education",
            "Projects",
            "Contact"
        ],
        icons=[
            "house",
            "person",
            "cpu",
            "mortarboard",
            "code-square",
            "telephone"
        ],
        default_index=0
    )

# ---------------- HOME ---------------- #

if selected == "Home":

    st.markdown("""
    <div class="hero">

    <h1 class="glow">✦ VINIKSAN S</h1>

    <h3 style="color:#00D9FF;">
    AI Engineer | Machine Learning Engineer | Data Science Enthusiast | Cloud Practitioner
    </h3>

    <p style="font-size:18px;">
    Artificial Intelligence • Machine Learning • Advanced AI •
    Data Science • Cloud Computing • Full Stack Development
    </p>

    <p style="font-size:16px;">
    Passionate about building intelligent systems, developing
    innovative AI solutions, and solving real-world challenges
    through technology, automation, and data-driven insights.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🚀 Projects", "10+")

    with col2:
        st.metric("⚡ Skills", "15+")

    with col3:
        st.metric("🎓 Academic Year", "3rd Year")

    with col4:
        st.metric("☁️ Cloud", "AWS")

    st.write("")

    st.markdown("""
    <div class="card">

    <h3>💡 Professional Summary</h3>

    <p>
    I am a dedicated Artificial Intelligence and Data Science student
    with strong interests in Machine Learning, Advanced AI,
    Data Analytics, Cloud Computing, and Software Development.

    I continuously enhance my technical expertise through hands-on
    projects, practical implementations, and continuous learning.

    My objective is to become a highly skilled AI Engineer and
    contribute to innovative solutions that create meaningful
    impact across industries.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("🏆 Key Highlights")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("✓ Artificial Intelligence")

    with c2:
        st.success("✓ Machine Learning")

    with c3:
        st.success("✓ Cloud Computing")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.success("✓ Data Science")

    with c5:
        st.success("✓ Streamlit Development")

    with c6:
        st.success("✓ Flask Development")

# ---------------- ABOUT ---------------- #

elif selected == "About":

    st.title("👨‍💻 About Me")

    st.write("""
Hello, I am Viniksan S, a passionate and dedicated Artificial Intelligence and Data Science student currently pursuing a Bachelor of Technology (B.Tech) at PSV College of Engineering and Technology.

I have a strong interest in Artificial Intelligence, Machine Learning, Advanced AI, Data Science, Cloud Computing, and Software Development. I enjoy transforming innovative ideas into practical solutions and continuously expanding my knowledge through hands-on projects and real-world applications.

My academic journey has provided me with a strong foundation in programming, machine learning, data analytics, and intelligent system development. I actively work on projects that enhance my technical expertise and strengthen my problem-solving abilities.

I am highly enthusiastic about exploring new technologies and staying updated with the latest advancements in Artificial Intelligence and Cloud Computing. I believe continuous learning and practical implementation are the keys to professional growth.

My goal is to become a skilled AI Engineer who develops innovative solutions that create meaningful impact and contribute to the future of technology.
""")

    st.markdown("### 🌟 Personal Interests & Activities")

    st.info("""
🤖 Exploring emerging technologies, AI innovations, and future-focused solutions

📚 Learning new tools, frameworks, and modern development techniques

💡 Building intelligent applications and automation-driven systems

☁️ Following the latest advancements in Artificial Intelligence, Machine Learning, and Cloud Computing

🧠 Continuously enhancing technical, analytical, and problem-solving abilities

🎯 Discovering creative approaches to solve real-world challenges through technology

📈 Staying updated with emerging industry trends and digital transformation initiatives

🏋️ Passionate about fitness, strength training, and maintaining a healthy lifestyle

💪 Actively involved in bodybuilding and personal fitness development

🏆 Dedicated to powerlifting and strength progression, with a strong focus on deadlift training

⚡ Believer in discipline, consistency, determination, and continuous self-improvement

🚀 Enjoy setting ambitious goals and pushing beyond limits to achieve personal and professional growth

🌍 Committed to lifelong learning and exploring new opportunities for innovation and development

🔥 Always curious to explore new ideas, technologies, and challenges that contribute to personal and professional excellence
""")

    st.markdown("### 🎯 Career Vision")

    st.success("""
To become a highly skilled Artificial Intelligence Engineer specializing in Machine Learning, Advanced AI, and Cloud Technologies while building innovative solutions that solve real-world problems and create positive impact through technology.
""")

    st.markdown("### 🏆 Core Strengths")

    col1, col2 = st.columns(2)

    with col1:
        st.success("✅ Problem Solving")
        st.success("✅ Critical Thinking")
        st.success("✅ Fast Learner")
        st.success("✅ Team Collaboration")

    with col2:
        st.success("✅ Leadership Skills")
        st.success("✅ Adaptability")
        st.success("✅ Project Development")
        st.success("✅ Continuous Improvement")



# ---------------- SKILLS ---------------- #

elif selected == "Skills":

    st.title("⚡ Technical Skills")

    skills = {
        "Python":95,
        "Artificial Intelligence":95,
        "Advanced AI":92,
        "Machine Learning":90,
        "Data Science":90,
        "Cloud Computing":88,
        "Streamlit":90,
        "Flask":85,
        "Git & GitHub":88,
        "SQL":85
    }

    for skill,value in skills.items():

        st.markdown(f"### {skill} ({value}%)")
        st.progress(value)

    st.success(
        "🚀 Specialized In: Artificial Intelligence, Machine Learning, Advanced AI, Data Science & Cloud Computing"
    )

# ---------------- EDUCATION ---------------- #

elif selected == "Education":

    st.title("🎓 Educational Background")

    st.markdown("""
    <div class="card">

    <h2>PSV College of Engineering and Technology</h2>

    <p>

    <strong>Bachelor of Technology (B.Tech)</strong>

    <br><br>

    Major in <strong>Artificial Intelligence and Data Science</strong>

    <br><br>

    📍 Krishnagiri, Tamil Nadu – 635108

    <br><br>

    📅 Academic Tenure: 2024 – 2028

    <br><br>

    🎓 Currently in Third Year of Study

    <br><br>

    📚 Expected Year of Graduation: 2028

    <br><br>

    My academic journey has provided a strong foundation in
    Artificial Intelligence, Machine Learning, Data Science,
    Cloud Computing, and Software Engineering.

    <br><br>

    I continuously explore emerging technologies through
    hands-on projects, practical implementations, and
    real-world problem-solving initiatives.

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.info(
        "🚀 Dedicated to continuous learning, innovation, and building impactful AI solutions."
    )

# ---------------- PROJECTS ---------------- #

elif selected == "Projects":

    st.title("🚀 Featured Projects")

    projects = [

        ("AI Multi Tool",
         "Advanced AI application integrating multiple intelligent tools."),

        ("Resume Analyzer",
         "AI-powered resume analysis and candidate evaluation system."),

        ("Loan Approval Prediction",
         "Machine Learning model for loan approval prediction."),

        ("Student Score Prediction",
         "Predicts student academic performance using Machine Learning."),

        ("AI Powered Dashboard",
         "Interactive dashboard powered by AI analytics."),

        ("E-Commerce Website",
         "Online shopping platform built using Flask."),

        ("Task Management App",
         "Productivity and task management application."),

        ("Blog Platform",
         "Content publishing and blog management platform."),

        ("Portfolio Website",
         "Professional portfolio built using Streamlit."),

        ("AI Bot",
         "AI chatbot powered by Python and NLP.")
    ]

    for title,desc in projects:

        st.markdown(f"""
        <div class="card">

        <h3>{title}</h3>

        <p>{desc}</p>

        </div>
        """, unsafe_allow_html=True)

# ---------------- CONTACT ---------------- #

elif selected == "Contact":

    st.title("📞 Contact Information")

    st.info("📱 Mobile: 8807716083")

    st.info("📧 Email: viniksanop@gmail.com")

    st.info("📍 Location: Tirupattur, Tamil Nadu - 635601")

    st.link_button(
        "🔗 LinkedIn Profile",
        "https://www.linkedin.com/in/viniksan-op-ab0b502a1"
    )

    st.link_button(
    "💻 GitHub Profile",
    "https://github.com/viniksan"
)

st.link_button(
    "📄 View Resume",
    "https://drive.google.com/file/d/1wfddszzt5qmgihf__8ePe41s586mgY7G/view"
)

st.markdown("---")
st.caption("© 2026 Viniksan S | AI & Machine Learning Portfolio")