import streamlit as st
from streamlit_option_menu import option_menu
import functions.about as about
import functions.MonitoringV2 as monitor
import functions.ExploreMenue as expmenu
import functions.Simulation as sim
import functions.Config as config
import functions.Home as home


def menuconstructor():
    # Set page configuration
    st.set_page_config(layout="wide", page_title="AgroPulse TwinHub", page_icon="🌿")

    # Custom CSS for improved styling
    st.markdown("""
        <style>
            .sidebar .sidebar-content {
                background-color: #f0f0f5;
                padding: 10px;
                border-radius: 10px;
            }
            .css-1v3fvcr {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                border-radius: 10px;
            }
            .css-10trblm {
                color: #4CAF50;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # 1. Sidebar menu
    with st.sidebar:
        st.header("AgroPulse TwinHub")
        select = option_menu(
            menu_title=None,
            options=['Monitoring', 'Explore', 'Simulation', 'Configuration', 'About'],
            icons=['activity', 'search', 'bar-chart', 'settings', 'info-circle'],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#f0f0f5"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#4CAF50"},
            }
        )

    # Display content based on menu selection
    if select == 'Monitoring':
        monitor.MonitorCreating()
    elif select == 'Explore':
        expmenu.constructoemain()
    elif select == 'Simulation':
        sim.SimulationConstructor()
    elif select == 'Configuration':
        config.ConstructorConfig()
    elif select == 'About':
        about.homepageconstructor()
    else:
        home.homepageconstructor()


if __name__ == '__main__':
    menuconstructor()
