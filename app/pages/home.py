import streamlit as st
# import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
# import time
# import base64
from streamlit_theme import st_theme

st.set_page_config(layout="wide")



# def to_rgba(hex_code):
#     hex_code = hex_code.lstrip("#")
#     return f"rgba{tuple(int(hex_code[i:i+2], 16)/x for i, x in zip((0,2,4,6), (1,1,1,255)))}"
# # st.image("static/background.jpg")

# def set_background(colour1, colour2, image_path):
#     with open(image_path, "rb") as img_file:
#         encoded_img = base64.b64encode(img_file.read()).decode()
#     bg_style = f"""
#     <style>
#     .stApp {{
#         background: linear-gradient(90deg, {colour1} 70%, {colour2} 95%), url("data:image/jpeg;base64,{encoded_img}");
#         background-size: cover;
#         background-attachment: fixed;
#     }}
#     </style>
#     """
#     st.markdown(bg_style, unsafe_allow_html=True)

# image_path = "static/background.jpg" if theme["base"] == "dark" else "static/l_background.jpg"
# colours = (to_rgba(theme["backgroundColor"] + "FF"), to_rgba(theme["backgroundColor"] + "33"))# if theme["base"] == "dark" else ("rgba(249, 249, 235, 1)", "rgba(249, 249, 235, 0.2))")

# set_background(*colours, image_path)

col1, col2 = st.columns([2,1])

# with col1:
st.title("Marco Bianchi")
st.markdown("""**Applied Data Scientist & Machine Learning Engineer**<br><br>

## Working on large-scale complex systems<br>From particle collisions to urban traffic<br>Using data, simulation, and machine learning""",
unsafe_allow_html=True)
theme = st_theme(adjust=True)
# Modeling complex systems through data, simulation and scientific rigor.

# with col2:
    # with open("assets/data_animation.json") as f:
    #     st_lottie(json.load(f), height=220)
# with col2:
#     st.image("static/CV.jpg", width=200)


# primaryColor='#ffc000'
# backgroundColor='#FBF8E9'
# secondaryBackgroundColor='#483248'
# textColor='hsl(0, 0%, 10%)'

# from streamlit_extras.card import card

# c1, c2, c3 = st.columns(3)

# with c1:
#     card(
#         title="Data Science",
#         text="Predictive modeling, ML pipelines, uncertainty-aware analysis",
#         image="https://img.icons8.com/ios-filled/100/brain.png"
#     )

# with c2:
#     card(
#         title="Simulation & Systems",
#         text="Multi-agent models, Monte Carlo, complex systems",
#         image="https://img.icons8.com/ios-filled/100/network.png"
#     )

# with c3:
#     card(
#         title="Research to Product",
#         text="From scientific validation to deployable models",
#         image="https://img.icons8.com/ios-filled/100/rocket.png"
#     )

# from streamlit_extras.metric_cards import style_metric_cards

st.header("Featured Projects")

tab1, tab2 = st.tabs([
    "ALICE Experiment -- CERN",
    "Turin Traffic Lights",
    # "Curriculum Vitae"
    ])

with tab1:
    # st.markdown("### 🧪 CERN – ALICE Experiment")
    st.markdown("""## ALICE -- CERN\n### Anisotropic Flow of $^3$He nuclei in Pb-Pb collisions\nExtracting collective behavior from petabyte-scale particle collision data
                """)
    # st.write("Large-scale experimental data analysis & ML")

    m1, m2, m3 = st.columns(3)

    kpi = [1.1, 155.2, 6]
    np1 = m1.empty()
    np2 = m2.empty()
    np3 = m3.empty()

    # for i in range(11):
    #     np1.markdown(f"## :violet[${kpi[0]/(11-i):.1f}$ PB]\n**Raw experimental data**")
    #     np2.markdown(f"## :violet[${kpi[1]/(11-i):.1f}$ GB]\n**Physics-selected data**")
    #     np3.markdown(f"## :violet[$O(10^{kpi[2]/(11-i):.0f})$]\n**Collision event analyzed**")
    #     time.sleep(0.001)

    np1.markdown(f"## :primary[${kpi[0]:.1f}$ PB]\n**Raw experimental data**")
    np2.markdown(f"## :primary[${kpi[1]:.1f}$ GB]\n**Physics-selected data**")
    np3.markdown(f"## :primary[$O(10^{kpi[2]:.0f})$]\n**Collision events analyzed**")
    ## Plot v3 e v4 con centralità e pT selezionabile

    centrality_options = ["0-20%", "20-40%", "40-60%"]
    selected_centralities = []

    # x = []
    # df3 = pd.DataFrame({'pT': [x for _ in range(len(centrality_options)) for x in [2, 2.8, 4, 5.6]], 'centrality': [x for x in centrality_options for _ in range(4)], 'v3': [8.545e-4, 1.828e-2, 2.900e-2, 6.316e-2,
                                                                                                                                                                            # 3.980e-3, 1.217e-2, .3981e-2, 5.559e-2,
                                                                                                                                                                            # 2.366e-3, 6.250e-3, 3.966e-2, 3.863e-2],
                                                                                                                                                                            # 'v4': [8.545e-4, 1.828e-2, 2.900e-2, 6.316e-2,
                                                                                                                                                                            # 3.980e-3, 1.217e-2, .3981e-2, 5.559e-2,
                                                                                                                                                                            # 2.366e-3, 6.250e-3, 3.966e-2, 3.863e-2]})

    df3 = pd.read_csv('static/out_v3.csv')
    df4 = pd.read_csv('static/out_v4.csv')

    df3["cent"][df3["cent"].str.contains('0_20')] = centrality_options[0]
    df3["cent"][df3["cent"].str.contains('20_40')] = centrality_options[1]
    df3["cent"][df3["cent"].str.contains('40_60')] = centrality_options[2]

    df4["cent"][df4["cent"].str.contains('0_20')] = centrality_options[0]
    df4["cent"][df4["cent"].str.contains('20_40')] = centrality_options[1]
    df4["cent"][df4["cent"].str.contains('40_60')] = centrality_options[2]

    with st.container(border=True):
        st.caption("Select centrality")
        cols = st.columns(len(centrality_options))
        for col, cent in zip(cols, centrality_options):
            with col:
                if st.checkbox(cent, value=True):
                    selected_centralities.append(cent)

        filtered_df3 = df3[df3['cent'].isin(selected_centralities)]
        filtered_df4 = df4[df4['cent'].isin(selected_centralities)]
        COLOR_MAP = {
        "0-20%": "#E69F00",
        "20-40%": "#56B4E9",
        "40-60%": "#009E73",
        }
        col1, col2 = st.columns(2)

        with col1:
            fig_v3 = px.scatter(
                filtered_df3,
                x="xlow",
                y="value",
                error_y="error",
                color="cent",
                title=r"v₃ vs pₜ",
                labels={"xlow": r"pₜ", "value": r"v₃"},
                color_discrete_map=COLOR_MAP
            )
            fig_v3.update_layout(legend_title_text="Centrality")
            st.plotly_chart(fig_v3, use_container_width=True, theme="streamlit")

        with col2:
            fig_v4 = px.scatter(
                filtered_df4,
                x="xlow",
                y="value",
                error_y="error",
                color="cent",
                title=r"v₄ vs pₜ",
                labels={"xlow": r"pₜ", "value": r"v₄"},
                color_discrete_map=COLOR_MAP,
                
            )
            fig_v4.update_layout(legend_title_text="Centrality")
            st.plotly_chart(fig_v4, use_container_width=True)


    st.subheader("Tech Stack")
    cols = st.columns([3, 4, 3.5, 5.5], width=400, gap="xxsmall")
    cols[0].button(":primary[C++]")
    cols[1].button(":primary[Python]")
    cols[2].button(":primary[ROOT]")
    cols[3].button(":primary[Pandas]")
    # st.markdown("| :primary[C++] | :primary[Python] | :primary[ROOT] | :primary[Pandas] |\n|---|---|---|---|")

    # tile = m1.container(border=True)
    # tile.markdown("""Data volume:\n* **1.1 PB** raw data\n* **155.2 GB** selected data""")
    
    # df = pd.DataFrame({'label': ["Selected Data", "Discarded Data"], 'value': [155.2, 1_100_000]})
    # fig = px.pie(df, values='value', names='label', hole=0.7, title="Data Selection", hover_name='label', hover_data='value')
    # fig.update_traces(texttemplate='%{value} GB')
    # tile.plotly_chart(fig, theme=None)

    # tile = m2.container(border=True)
    # tile.markdown("""Tech Stack:\n* **C++**\n* **Python**\n\t* Pandas""")
    # tile = m2.container(border=True)
    # df = pd.read_csv("/home/marco/flow/csv/df_pass5_long_v3_SP.csv", nrows=20)
    # tile.markdown("Data sample:")
    # tile.dataframe(df, height=348)
    # m2.metric("Tech Stack", "Python / C++")

    # st.page_link('pages/flow.py', label="Explore this project", icon=':material/matter:')

def get_lat_lon(geom):
    while not geom[0].isdecimal:
        geom = geom[1:]
    return [float(x) for x in geom.strip(")").split()]


with tab2:
    # st.markdown("### 🚦 Urban Traffic Modeling")
    st.markdown("### Agent-based Traffic Light Network")
    st.write("Simulation-driven data science for smart mobility")
    m = st.columns(3)
    m[0].markdown("## :primary[$15k+$ agents]\n**Multi-agent AI apporoach**")
    m[0].markdown("## :primary[$+30\%$]\n**Average vehicle speed**")
    m[1].markdown("## :primary[$10k+$]\n**FIPA messages per hour**") # how many messages per hour?
    m[1].markdown("## :primary[$-43\%$]\n**Stopped vehicles**") # how many messages per hour?
    m[2].markdown("## :primary[$3734$]\n**Simulated traffic lights**")
    m[2].markdown("## :primary[$-15\%$]\n**Mean absolute acceleration\***")
    st.caption("\* Mean absolute acceleration was used as a proxy for vehicle emissions")
    import geopandas as gpd

    gdf = gpd.read_file("static/junctions_fium5.shp", encoding="utf-8")
    with st.container(border=True):
        st.map(
            gdf.get_coordinates(), 
            latitude='y', 
            longitude='x', 
            size=1, 
            color=theme["primaryColor"], 
            zoom=12.5,
            # width=900
            )
    
    st.subheader("Tech Stack")
    cols = st.columns([3, 2.8, 3.5, 5.5], width=400, gap="xxsmall")
    cols[0].button(":primary[Gama]")
    cols[1].button(":primary[QGIS]")
    cols[2].button(":primary[Python]", key="pippo")
    # cols[3].button(":primary[Pandas]")
    # m1.metric("Agents", "1k+")
    # m2.metric("Approach", "Multi-agent AI")
    # st.page_link('pages/lights.py', label="Explore this project", icon=':material/traffic:')

# style_metric_cards()

# from streamlit_extras.stylable_container import stylable_container

# with stylable_container(
#     key="timeline",
#     css_styles="""
#     {
#         border-left: 3px solid #4F8BF9;
#         padding-left: 1rem;
#     }
#     """
# ):
#     st.markdown("""
#     **2022–2024** – Experimental physics & data analysis  
#     **2024–2025** – ML, simulation, applied research  
#     **Now** – Applied Data Science & ML deployment
#     """)

# st.warning("🚧 Work in progress")
 
# st.markdown("""
# - Deep learning with PyTorch (structured & spatio-temporal data)
# - ML model benchmarking and interpretability
# - Production-ready dashboards
# """)
st.divider()
st.space()
st.subheader("Get in touch")
col1, col2, col3 = st.columns([5, 5.65, 10], width=350, gap="xxsmall")

col1.link_button("GitHub", "https://github.com/marcobianchi463", type="primary")
col2.link_button("LinkedIn", "https://linkedin.com/in/marco-bianchi-373327327", type="primary")
# col2.markdown("[![Title]('https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg')](https://linkedin.com/in/marco-bianchi-373327327)")
col3.link_button("Email", "mailto:marco.bianchi411@gmail.com", type="primary")

with st.expander(":primary[**My Curriculum Vitae**]", width=770):
    st.pdf("static/CV.pdf")
# with tab2:
#     col3.pdf(
#         # "Download CV",
#         "static/CV.pdf"
#         )