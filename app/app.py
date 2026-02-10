# import streamlit as st

# st.set_page_config(
#     page_title="Marco Bianchi – Data Science Portfolio",
#     layout="wide"
# )

# # HERO
# st.title("Marco Bianchi")
# st.subheader("Applied Data Science & Machine Learning")

# st.write("""
# I design and validate data-driven models for complex systems,
# combining scientific rigor, machine learning, and applied research.
# """)

# st.divider()

# # RESEARCH TO IMPACT
# st.header("From Research to Impact")
# st.write("""
# My work sits at the intersection of scientific research and applied data science...
# """)

# st.divider()

# # PROJECTS
# st.header("Featured Projects")

# col1, col2 = st.columns(2)

# with col1:
#     st.subheader("Anisotropic Flow of ³He – CERN")
#     st.write("Large-scale experimental data analysis and ML...")
#     st.button("Explore thesis project")

# with col2:
#     st.subheader("Traffic Modeling & Multi-Agent Systems")
#     st.write("Simulation-driven data science for urban mobility...")
#     st.button("Explore traffic project")

# st.divider()

# # WIP
# st.header("Current Focus")
# st.info("🚧 Work in progress – actively updated")

# st.divider()

# # STACK
# st.header("Tools & Methodology")

# st.divider()

# # CTA
# st.header("Get in touch")
# st.markdown("""
# - [GitHub](https://github.com/marcobianchi463/)
# - [LinkedIn](https://linkedin.com/in/marco-bianchi-373327327)
# """)

# from streamlit_extras.colored_header import colored_header
# from streamlit_lottie import st_lottie
import streamlit as st

pages = [
    st.Page("pages/home.py", title="Home", icon=':material/home:'),
    # st.Page('pages/flow.py', title="Anisotropic Flow", icon=':material/matter:'),
    # st.Page('pages/lights.py', title="Traffic Lights", icon=':material/traffic:')
]

pg = st.navigation(pages, position='sidebar', expanded=True)
pg.run()
