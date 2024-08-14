import streamlit as st
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import pandas as pd
import time

import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots



def printCostumTitleAndContenth3(title, context):
    return f"""
        <div class="jumbotron">
        <h3>{title}</h3>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """

def printCostumTitleAndContenth2(title, context):
    return f"""
        <div class="jumbotron">
        <h2>{title}</h2>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """


def printCostumTitleAndContenth1(title, context):
    return f"""
        <div class="jumbotron">
        <h1>{title}</h1>
        <h5>{context}</h5>
        </div>
        <div class="container">
        </div>
        """


def animated_linear_progress_bar(label, value, color='green'):
    progress_html = f"""
        <svg width="300" height="30" style="background-color: #f1f1f1; border-radius: 5px;">
            <rect id="progress-rect" width="0%" height="100%" fill="{color}">
                <animate attributeName="width" from="0%" to="{value}%" dur="2s" fill="freeze" />
            </rect>
            <text x="50%" y="50%" fill="black" font-size="14" font-weight="bold" text-anchor="middle" dy=".3em">{label}</text>
        </svg>

        <script>
            const progressRect = document.getElementById('progress-rect');
            progressRect.setAttribute('width', '{value}%');
        </script>
    """
    st.markdown(progress_html, unsafe_allow_html=True)

# Example usage with animated linear progress bar

def animated_circular_progress_bar(label, value, max_value, color='red', max_size=150):
    normalized_value = min(value / max_value, 1.0)  # Normalize value to be between 0 and 1
    progress_html = f"""
        <div id="progress-container" style="width: {max_size}px; height: {max_size}px; position: relative; border-radius: 50%; overflow: hidden;">
            <div id="progress-circle" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></div>
            <div id="animated-circle" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></div>
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; color: {color}; font-size: 11px; font-weight: bold;">{label}<br>{value} </div>
        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/progressbar.js/1.0.1/progressbar.min.js"></script>
        <script>
            const container = document.getElementById('progress-container');
            const bar = new ProgressBar.Circle(container, {{
                strokeWidth: 13,
                easing: 'easeInOut',
                duration: 2000,
                color: '{color}',
                trailColor: '#e0e0e0',
                trailWidth: 10,
                svgStyle: null
            }});

            bar.animate({normalized_value});
        </script>
    """
    return progress_html

def animated_linear_progress_bar_with_metric(metric_value, label, value, color='green', width=200, height=20):
    progress_html = f"""
        <div style="display: flex; align-items: center; text-align: left;">
            <div style="font-size: 14px; font-weight: bold; margin-right: 10px;">{metric_value}</div>
            <div style="position: relative; width: {width}px;">
                <svg width="{width}" height="{height}" style="background-color: #f1f1f1; border-radius: 5px;">
                    <rect id="progress-rect" x="0" y="0" width="0%" height="100%" fill="{color}">
                        <animate attributeName="width" from="0%" to="{value}%" dur="2s" fill="freeze" />
                    </rect>
                    <text x="50%" y="50%" fill="black" font-size="14" font-weight="bold" text-anchor="middle" dy=".3em">{label}</text>
                </svg>
            </div>
        </div>

        <script>
            const progressRect = document.getElementById('progress-rect');
            progressRect.setAttribute('width', '{value}%');
        </script>
    """
    st.markdown(progress_html, unsafe_allow_html=True)

def printWithTitleAndBoarder1(title, context):
    return f"""
        <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
            <h3 style="color:#333333;">{title}</h3>
            <h5>{context}</h5>
        </div>
        """
# HTML and CSS for animated line
animated_line_html = """
<style>
    @keyframes drawLine {
        to {
            stroke-dashoffset: 0;
        }
    }

    .animated-line {
        width: 100%;
        height: 12px;
        background-color: black;
        position: relative;
        overflow: hidden;
    }

    .line-path {
        stroke-dasharray: 1000;
        stroke-dashoffset: 1000;
        animation: drawLine 2s forwards;
        stroke: #3498db;
        stroke-width: 2px;
    }
</style>

<div class="animated-line">
    <svg width="100%" height="100%">
        <line class="line-path" x1="0" y1="1" x2="100%" y2="1"/>
    </svg>
</div>
"""

def ConstructorConfig():
    option2 = option_menu(None, ["Pak choy", "Rice", "Aqua"],
                          menu_icon="forward", default_index=0, orientation="horizontal",
                          styles={
                              "container": {"padding": "0!important", "background-color": "#fafafa"},
                              "icon": {"color": "orange", "font-size": "15px"},
                              "nav-link": {"font-size": "15px", "text-align": "right", "margin": "0px",
                                           "--hover-color": "#eee", },
                              "nav-link-selected": {"background-color": "green"},
                          }
                          )


    if option2 == "Pak choy":
        st.markdown(printWithTitleAndBoarder1('Configuration', """Define your goal for pak choy traits during harvesting time.""") , unsafe_allow_html=True)
        st.write('')
        st.header('Crop Traits')
        data_edited = pd.DataFrame()
        data_df = pd.DataFrame(
            {
                "Crop Traits": ["Plant Height", "Longest Leaf", "Leaf Count"],
                "Is it Important Trait": [False, True, False],
                "Goal": ["260", "150", "11"],  # New column for text input
            }
        )


        col1, col2 = st.columns(2)
        with col1:
            genre = st.radio(
            "",
            ["Default: Table show that which trait is important and what is the goal value of the traits.",
             "Customize: Select the important traits and put the for the value of the goal."],
            index=0,
            )

        with col2:
            if genre == "Default: Table show that which trait is important and what is the goal value of the traits.":
                st.write(data_df)

            elif genre == "Customize: Select the important traits and put the for the value of the goal.":
                data_edited = st.data_editor(
                    data_df,
                    column_config={
                        "favorite": st.column_config.CheckboxColumn(
                            "Which ones are important?",
                            help="which crop traits is important for the Scoring?",
                            default=False,
                        ),
                        "text_input": st.column_config.TextColumn("Your Estimation of the Amount of the Crop traits when you want to harvest.", help="Put a number that show the amount of the IDEAL crop traits "),
                    },
                    disabled=["widgets"],
                    hide_index=True,
                )

        st.header('Yeild')
        yeild_pakchoy = 1100
        col1 , col2 = st.columns(2)
        with col1:
            genre = st.radio(
                "",
                ["Default : Weight of the Pak Choy farm when you want to harvest: 1100grams", "Put your Estimation of the yield of the Pak choy"],
                index=0,
            )
        with col2:
            if genre == "Put your Estimation of the yield of the Pak choy":
                text_input = st.text_input('Put your Estimation.')
                yeild_pakchoy = text_input


        data_edited['Crop Traits'] = ['plantheight', 'longestleaf', 'leavescount']

        if st.button('Submit'):
            data_edited['yeild'] = yeild_pakchoy
            data_edited.to_csv("Dataset/Benchmark/Pakchoyparameter.csv", index=False)
