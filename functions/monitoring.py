import streamlit as st
import base64
from streamlit_card import card
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

def animated_gauge_progress_bar(value, title, rmin, rmax):
    if 1 <= value <= 10:
        bar_color = "red"
    else:
        bar_color = "#4CAF50"  # Default color for other values

    fig = make_subplots(
        rows=1, cols=1,
        specs=[[{'type': 'indicator'}]]
    )
    fig.add_trace(go.Indicator(
        mode="number+gauge",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        delta={'reference': 50, 'position': 'top'},
        gauge=dict(
            axis=dict(range=[rmin, rmax]),
            bar=dict(color='black'),  # Set color dynamically
            bgcolor="white",
            borderwidth=2,
            bordercolor="gray",
            steps=[dict(range=[0, 100], color="lightgray")]
        ),
        title=dict(text=title, font=dict(size=20)),  # Set title directly within the trace
    ))

    fig.update_layout(
        height=200,
        margin=dict(l=15, r=15, b=15, t=60),
    )

    return fig


def guageCreator(vlaue, title, rmin, rmax):
    # Streamlit app
    chart_placeholder = st.empty()
    vla = round(vlaue)
    if vla <= 1:
        animated_chart = animated_gauge_progress_bar(vlaue, title, rmin, rmax)
        chart_placeholder.plotly_chart(animated_chart, use_container_width=True)
    # Update the progress value with an animation
    else:
        animated_chart = animated_gauge_progress_bar(vla, title, rmin, rmax)
        chart_placeholder.plotly_chart(animated_chart, use_container_width=True)
        st.empty()  # Clear the previous chart to create animation effect

def cardcreator(path,title,text):

    with open(path, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")

    hasClicked = card(
        title=title,
        text=text,
        styles={
            "card": {
                "height": "200px",
                "width":"200px",
                "border-radius": "30px",
                "box-shadow": "0 0 20px rgba(0,0,0,0.5)",
                "margin": "25px 0px 0px 0px"
            },"text": {
            "font-family": "serif",
            "font-size":'20px'
        },
            "title":{
                "font-family": "serif",
                "font-size":'15px'
            }
        }
    )

def MonitorCreating():
    def load_custom_css_js():
        st.markdown(
            """
            <style>
            .navbar {
                background-color: #333;
                overflow: hidden;
            }

            .navbar a, .dropbtn {
                float: left;
                display: block;
                color: #f2f2f2;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 17px;
            }

            .navbar a:hover, .dropdown:hover .dropbtn {
                background-color: #ddd;
                color: black;
            }

            .dropdown {
                float: right;
                overflow: hidden;
            }

            .dropdown .dropbtn {
                cursor: pointer;
                font-size: 17px;
                border: none;
                outline: none;
                color: #f2f2f2;
                background-color: inherit;
                font-family: inherit;
                margin: 0;
            }

            .navbar a.active {
                background-color: #4CAF50;
                color: white;
            }

            .dropdown-content {
                display: none;
                position: absolute;
                background-color: #f9f9f9;
                min-width: 160px;
                box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
                z-index: 1;
                right: 0;
            }

            .dropdown-content a {
                float: none;
                color: black;
                padding: 12px 16px;
                text-decoration: none;
                display: block;
                text-align: left;
            }

            .dropdown-content a:hover {
                background-color: #ddd;
                color: black;
            }

            .dropdown:hover .dropdown-content {
                display: block;
            }
            </style>

            <script>
            document.addEventListener("DOMContentLoaded", function() {
                var settingsLink = document.getElementById("settingsLink");
                var dropdownContent = document.getElementById("dropdownContent");

                settingsLink.addEventListener("click", function(event) {
                    event.preventDefault();
                    dropdownContent.style.display = (dropdownContent.style.display === 'block') ? 'none' : 'block';
                });

                window.onclick = function(event) {
                    if (!event.target.matches('#settingsLink')) {
                        if (dropdownContent.style.display === 'block') {
                            dropdownContent.style.display = 'none';
                        }
                    }
                }
            });
            </script>
            """,
            unsafe_allow_html=True,
        )

    # Load custom CSS and JS
    load_custom_css_js()

    # HTML for the navbar
    st.markdown(
        """
        <div class="navbar">
          <a class="active" href="#home">Pak choy</a>
          <div class="dropdown" style="float:right;">
            <button class="dropbtn" id="settingsLink">Setting</button>
            <div class="dropdown-content" id="dropdownContent">
              <a href="#premium-account">Premium account: Farmer</a>
              <a href="#farms">Farms</a>
              <a href="#configuration">Configuration</a>
            </div>
          </div> 
        </div>
        """,
        unsafe_allow_html=True,
    )


    # CSS styles for the progress bar
    progress_bar_style = """
    <style>
    .timeline {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 1px;
    }

    .timeline .circle {
      width: 100px;
      height: 100px;
      border-radius: 50%;
      background: #ddd;
      display: flex;
      justify-content: center;
      align-items: center;
      font-weight: bold;
      color: green;
    }

    .timeline .circle.active {
      background: green;
      color: white;
      
    }

    .timeline .line {
      flex: 1;
      height: 5px;
      background: #ddd;
    }

    .timeline .line.active {
      background: green;
      margin: 1px;
    }

    .timeline .label {
        
      text-align: center;
      color: green;
      font-size:40px;
    }
    </style>
    """

    # HTML structure for the progress bar
    progress_bar_html = """
    <div class="timeline">
      <div class="circle active">Week 1</div>
      <div class="line active"></div>
      <div class="circle active">Week 2</div>
      <div class="line active"></div>
      <div class="circle active">Week 3</div>
      <div class="line"></div>
      <div class="circle">Week 4</div>
    </div>
    <div class="timeline">
      <div class="label"></div>
      <div class="label"></div>
      <div class="label"></div>
      <div class="label" style="color: grey;"></div>
    </div>
    """

    # Display the progress bar in Streamlit
    st.markdown(progress_bar_style, unsafe_allow_html=True)
    st.markdown(progress_bar_html, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        guageCreator(24.8, 'Temperature (°C)', 0, 55)
    with col2:
        guageCreator(7.5, 'pH', 0, 14)
    with col3:
        guageCreator(1.4, 'EC', 0, 3)

    col1,col2,col3 = st.columns(3)
    with col1:
        cardcreator('cardimages/CurrentYeild.jpeg', 'Predicted Harvest', '2.5 KG')
    with col2:
        import streamlit.components.v1 as components

        # Define the HTML and CSS for the intervention plan box
        intervention_plan_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Advice for Pot1</title>
            <style>
                .container {
                    width: 200px;
                    border: 2px solid #ccc;
                    border-radius: 10px;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    margin: 20px auto;
                    text-align: center;
                }

                .alert-icon {
                    width: 50px;
                    height: 50px;
                    border: 5px solid #ff0000;
                    border-radius: 50%;
                    position: relative;
                    animation: pulse 1s infinite;
                    margin: 0 auto 10px;
                }

                .alert-icon::before {
                    content: '!';
                    font-size: 30px;
                    color: #ff0000;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                }

                @keyframes pulse {
                    0% {
                        transform: scale(1);
                        border-color: #ff0000;
                    }
                    50% {
                        transform: scale(1.2);
                        border-color: #ffff00;
                    }
                    100% {
                        transform: scale(1);
                        border-color: #ff0000;
                    }
                }

                .advice-list {
                    text-align: left;
                    margin: 10px 0;
                }

                .advice-list li {
                    margin-bottom: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="alert-icon"></div>
                <h2>Advice for Pot2</h2>
                <ul class="advice-list">
                    <li>1. Empty the container and refill 2 liters.</li>
                    <li>2. Add 1/4 cup of A+B solution to the container.</li>
                    <!-- Add more advice steps as needed -->
                </ul>
            </div>
        </body>
        </html>
        """
        components.html(intervention_plan_html, height=300)
    with col3:
        import streamlit.components.v1 as components

        # Define the HTML and CSS for the intervention plan box
        intervention_plan_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Advice for Pot1</title>
            <style>
                .container {
                    width: 200px;
                    border: 2px solid #ccc;
                    border-radius: 10px;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    margin: 20px auto;
                    text-align: center;
                }

                .alert-icon {
                    width: 50px;
                    height: 50px;
                    border: 5px solid #ff0000;
                    border-radius: 50%;
                    position: relative;
                    animation: pulse 1s infinite;
                    margin: 0 auto 10px;
                }

                .alert-icon::before {
                    content: '!';
                    font-size: 30px;
                    color: #ff0000;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                }

                @keyframes pulse {
                    0% {
                        transform: scale(1);
                        border-color: #ff0000;
                    }
                    50% {
                        transform: scale(1.2);
                        border-color: #ffff00;
                    }
                    100% {
                        transform: scale(1);
                        border-color: #ff0000;
                    }
                }

                .advice-list {
                    text-align: left;
                    margin: 10px 0;
                }

                .advice-list li {
                    margin-bottom: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="alert-icon"></div>
                <h2>Advice for Pot1</h2>
                <ul class="advice-list">
                    <li>1. Empty the container and refill 2 liters.</li>
                    <li>2. Add 1/4 cup of A+B solution to the container.</li>
                    <!-- Add more advice steps as needed -->
                </ul>
            </div>
        </body>
        </html>
        """

        # Use Streamlit's components.html method to render the HTML
        components.html(intervention_plan_html, height=300)
    ###############

    file_path = 'Dataset/Pock choy /Generation3_pot1.csv'
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Define a mapping for status to color
    status_color_mapping = {'good': 'green', 'normal': 'orange', 'bad': 'red'}

    # Create a dictionary with pot number as keys and color as values
    pot_color_dict = {}

    def update_status(leaf_count, benchmark=10):
        if 8 <= leaf_count <= 10:
            return 'Good'
        elif 7 <= leaf_count <= 8:
            return 'Normal'
        else:
            return 'Bad'

    df['status'] = df['leafcount'].apply(update_status)
    for index, row in df.iterrows():
        pot_number = row['subpotnumber']
        status = row['status'].lower()  # Convert to lowercase for case-insensitivity
        color = status_color_mapping.get(status,
                                         'unknown')  # Default to 'unknown' if status is not one of the specified values
        pot_color_dict[pot_number] = color

    print(pot_color_dict)

    dataframe = pot_color_dict
    # Streamlit app layout
    # Define CSS styles
    col1, col2 = st.columns(2)
    with col1:

        css_styles = """
                    <style>
                        .button-container {
                            display: grid;
                            grid-template-columns: repeat(3, 1fr);
                            gap: 10px;
                            border: 2px solid #ddd; /* Border around the button container */
                            padding: 1px; /* Add some padding for better appearance */
                        }
                        .button {
                            width: 60%;
                            height: 70px;
                            background-color: #eee;
                            color: #333;
                            font-size: 10px;
                            font-weight: bold;
                            border: 2px solid #ddd;
                            border-radius: 55px;
                            cursor: pointer;
                        }
                    </style>
                """
        # Display CSS styles
        st.markdown(css_styles, unsafe_allow_html=True)

        df = pd.read_csv('Dataset/Pock choy /Generation3_pot1.csv')
        # Create button grid
        df = pd.read_csv('Dataset/Pock choy /Generation3_pot1.csv')
        dfbenchmark = pd.read_csv('Dataset/Benchmark/Pakchoyparameter.csv')
        subpot = st.selectbox('Select the SubPot Number', df['subpotnumber'].unique())
        filtered_df = df[df['subpotnumber'] == subpot]

        button_container = f"""<div style="border: 2px solid #333333; padding:10px; border-radius:5px;">     <p style='text-align: center'>Pot 1</p> <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                    <h4 style="color: {dataframe[subpot]}; ">Crop Traits Status</h2>
                    <table>
                        <tr>
                            <th>Yield (gram)</th>
                            <th>Leaf Count</th>
                            <th>Longest Leaf (mm)</th>
                            <th>Plant Height (mm)</th>
                        </tr>
                        <tr>
                            <td>-</td>
                            <td>{filtered_df['leafcount'].values[0]}</td>
                            <td>{filtered_df['longestleaf'].values[0]}</td>
                            <td>{filtered_df['plantheight'].values[0]}</td>
                            <td> Current </td>
                        </tr>
                        <tr>
                            <td>17</td>
                            <td>{filtered_df['leafcount'].values[0] + 1}</td>
                            <td>{filtered_df['longestleaf'].values[0] + 12}</td>
                            <td>{filtered_df['plantheight'].values[0] + 24}</td>
                            <td> Predicted </td>
                        </tr>
                        <tr>
                            <td>22</td>
                            <td>{dfbenchmark[dfbenchmark['Crop Traits'] == 'leavescount']['Goal'].values[0]}</td>
                            <td>{dfbenchmark[dfbenchmark['Crop Traits'] == 'longestleaf']['Goal'].values[0]}</td>
                            <td>{dfbenchmark[dfbenchmark['Crop Traits'] == 'plantheight']['Goal'].values[0]}</td>
                            <td> Target </td>
                        </tr>
                    </table>
                </div> <div class='button-container'>"""
        for key, value in dataframe.items():
            # Use Streamlit's button widget with a callback to display text on click
            button_container += f"""<button class='button' style='background-color: {value}; border-color: {value}; color: white'
                                       onclick='st.write("{key} clicked!")'>{key}</button>"""
        button_container += "</div>"

        # Display button grid
        st.markdown(button_container, unsafe_allow_html=True)




    with col2:
        file_path = 'Dataset/Pock choy /Generation3_pot2.csv'

        df = pd.read_csv(file_path)

        # Define a mapping for status to color
        status_color_mapping = {'good': 'green', 'normal': 'orange', 'bad': 'red'}

        # Create a dictionary with pot number as keys and color as values
        pot_color_dict = {}

        def update_status(leaf_count, benchmark=10):
            if 8 <= leaf_count <= 10:
                return 'Good'
            elif 7 <= leaf_count <= 8:
                return 'Normal'
            else:
                return 'Bad'

        df['status'] = df['leafcount'].apply(update_status)
        for index, row in df.iterrows():
            pot_number = row['subpotnumber']
            status = row['status'].lower()  # Convert to lowercase for case-insensitivity
            color = status_color_mapping.get(status,
                                             'unknown')  # Default to 'unknown' if status is not one of the specified values
            pot_color_dict[pot_number] = color

        print(pot_color_dict)

        dataframe = pot_color_dict
        # Streamlit app layout
        # Define CSS styles


        css_styles = """
                       <style>
                           .button-container {
                               display: grid;
                               grid-template-columns: repeat(3, 1fr);
                               gap: 10px;
                               border: 2px solid #ddd; /* Border around the button container */
                               padding: 1px; /* Add some padding for better appearance */
                           }
                           .button {
                               width: 60%;
                               height: 70px;
                               background-color: #eee;
                               color: #333;
                               font-size: 10px;
                               font-weight: bold;
                               border: 2px solid #ddd;
                               border-radius: 55px;
                               cursor: pointer;
                           }
                       </style>
                   """
        # Display CSS styles
        st.markdown(css_styles, unsafe_allow_html=True)

        df = pd.read_csv('Dataset/Pock choy /Generation3_pot1.csv')
        # Create button grid
        df = pd.read_csv('Dataset/Pock choy /Generation3_pot1.csv')
        dfbenchmark = pd.read_csv('Dataset/Benchmark/Pakchoyparameter.csv')
        subpot = st.selectbox('Select SubPot Number', df['subpotnumber'].unique())
        filtered_df = df[df['subpotnumber'] == subpot]
        button_container = f"""<div style="border: 2px solid #333333; padding:10px; border-radius:5px;">     <p style='text-align: center'>Pot 2</p> <div style="border: 2px solid #333333; padding:10px; border-radius:5px;">
                       <h4 style="color: {dataframe[subpot]}; ">Crop Traits Status</h2>
                       <table>
                           <tr>
                               <th>Yield(gram)</th>
                               <th>Leaf Count</th>
                               <th>Longest Leaf (mm)</th>
                               <th>Plant Height (mm)</th>
                           </tr>
                           <tr>
                               <td>-</td>
                               <td>{filtered_df['longestleaf'].values[0]}</td>
                               <td>{filtered_df['plantheight'].values[0]}</td>
                               <td>{filtered_df['plantheight'].values[0]}</td>
                               <td> Current </td>
                           </tr>
                           <tr>
                               <td>15</td>
                               <td>{filtered_df['longestleaf'].values[0] + 12}</td>
                               <td>{filtered_df['plantheight'].values[0] + 24}</td>
                               <td>{filtered_df['plantheight'].values[0] + 24}</td>
                               <td> Predicted </td>
                           </tr>
                           <tr>
                               <td>19</td>
                               <td>{dfbenchmark[dfbenchmark['Crop Traits'] == 'longestleaf']['Goal'].values[0]}</td>
                               <td>{dfbenchmark[dfbenchmark['Crop Traits'] == 'plantheight']['Goal'].values[0]}</td>
                               <td>{dfbenchmark[dfbenchmark['Crop Traits'] == 'plantheight']['Goal'].values[0]}</td>
                               <td> Target </td>
                           </tr>
                       </table>
                   </div> <div class='button-container'>"""
        for key, value in dataframe.items():
            # Use Streamlit's button widget with a callback to display text on click
            button_container += f"""<button class='button' style='background-color: {value}; border-color: {value}; color: white'
                                          onclick='st.write("{key} clicked!")'>{key}</button>"""
        button_container += "</div>"

        # Display button grid
        st.markdown(button_container, unsafe_allow_html=True)





# --------------------------------------------- Real time monitoring




