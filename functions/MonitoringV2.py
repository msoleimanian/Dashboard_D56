import streamlit as st
import dash
from dash import dcc, html
import dash_daq as daq
from dash.dependencies import Input, Output
import random
from threading import Thread
import time
import dash
from dash import dcc, html
import dash_daq as daq
from dash.dependencies import Input, Output
import random
from threading import Thread
import time
import streamlit.components.v1 as components
import streamlit as st
import random
import time
from threading import Thread
import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def creategauge():
    # Function to fetch real-time data
    def get_sensor_data():
        # Replace these random values with actual sensor data
        ec_value = random.uniform(1.65, 1.95)  # Simulated EC value
        ph_value = random.uniform(6.0, 7.0)  # Simulated pH value
        temp_value = random.uniform(20, 30)  # Simulated Temp value
        tds_value = random.uniform(500, 1500)  # Simulated TDS value
        return ec_value, ph_value, temp_value, tds_value

    # Create a Dash app
    app = dash.Dash(__name__)

    app.layout = html.Div([
        html.Div([
            html.Div([
                daq.Gauge(
                    id='ec-gauge',
                    label='EC Value',
                    min=0,
                    max=10,
                    showCurrentValue=True,
                    units='EC',
                    color={"gradient": True,
                           "ranges": {"green": [0, 1.95], "yellow": [1.0, 1.55], "red": [0, 1.0, 1.95, 10]}}
                ),
            ], style={'margin-bottom': '20px'}),
            html.Div([
                daq.Gauge(
                    id='ph-gauge',
                    label='pH Value',
                    min=4,
                    max=9,
                    showCurrentValue=True,
                    units='pH',
                    color={"gradient": True,
                           "ranges": {"red": [4, 5.5], "yellow": [5.5, 6.5, 7.5, 8.5], "green": [6.5, 9]}}
                ),
            ], style={'margin-bottom': '20px'}),
            html.Div([
                daq.Gauge(
                    id='temp-gauge',
                    label='Temp Value',
                    min=0,
                    max=40,
                    showCurrentValue=True,
                    units='°C',
                    color={"gradient": True,
                           "ranges": {"blue": [0, 15], "green": [15, 25], "red": [25, 40]}}
                ),
            ], style={'margin-bottom': '20px'}),
            html.Div([
                daq.Gauge(
                    id='tds-gauge',
                    label='TDS Value',
                    min=0,
                    max=2000,
                    showCurrentValue=True,
                    units='ppm',
                    color={"gradient": True,
                           "ranges": {"green": [0, 800], "yellow": [800, 1200], "red": [1200, 2000]}}
                ),
            ], style={'margin-bottom': '20px'}),
        ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
        dcc.Interval(
            id='interval-component',
            interval=5 * 1000,  # in milliseconds (5 seconds)
            n_intervals=0
        )
    ])

    @app.callback(
        [Output('ec-gauge', 'value'),
         Output('ph-gauge', 'value'),
         Output('temp-gauge', 'value'),
         Output('tds-gauge', 'value')],
        [Input('interval-component', 'n_intervals')]
    )
    def update_gauges(n):
        ec_value, ph_value, temp_value, tds_value = get_sensor_data()
        return ec_value, ph_value, temp_value, tds_value

    # Function to run the Dash app
    def run_dash_app():
        app.run_server(port=8060)

    # Run Dash app in a separate thread
    thread = Thread(target=run_dash_app)
    thread.start()

    # Streamlit app

    # Generate and display the CSS for the combined container
    def generate_combined_css():
        return """
        <style>
        .combined-container {
            border-radius: 10px;
            padding: 20px;
            border: 2px solid #333;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
            margin: 20px auto;
            text-align: center;
            max-width: 2000px;
            height: 900px;
            background-color: #f9f9f9;
        }
        .iframe-container {
            width: 100%;
            height: 800px;
            border: none;
        }
        </style>
        """

    # Generate and display the combined CSS
    st.markdown(generate_combined_css(), unsafe_allow_html=True)

    # Display the combined container
    st.markdown(f"""
        <div class="combined-container">
            <h2 style="font-size: 18px;">Real-Time Monitoring</h2>
            <iframe src="http://localhost:8060" class="iframe-container"></iframe>
        </div>
    """, unsafe_allow_html=True)

    # Ensure the thread is not closed immediately
    while True:
        time.sleep(2)


def createYeidl():
    # Function to fetch the predicted yield
    def get_predicted_yield():
        # Replace this with your actual logic for predicted yield
        predicted_yield = random.uniform(80, 100)  # Simulated predicted yield
        return predicted_yield

    # Function to determine the status color based on the predicted yield
    def get_status_color(predicted_yield):
        if predicted_yield < 50:
            return 'red'
        elif 50 <= predicted_yield < 75:
            return 'yellow'
        else:
            return 'green'

    # Generate and display the CSS for the combined container
    def generate_combined_css():
        return """
        <style>
        .combined-container2 {
            border-radius: 10px;
            padding: 5px;
            border: 2px solid #333;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
            margin: 10px auto;
            text-align: center;
            max-width: 600px;
            background-color: #f9f9f9;
        }
        .predicted-yield {
            padding: 5px;
            border: 2px solid #333;
            border-radius: 10px;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .container {
            border-radius: 10px;
            padding: 5px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
            margin: 0 auto;
            text-align: center;
            background-color: #f1f1f1;
        }
        .alert-icon {
            width: 30px;
            height: 30px;
            border: 2px solid #ff0000;
            border-radius: 50%;
            position: relative;
            animation: pulse 1s infinite;
            margin: 0 auto 5px;
        }
        .alert-icon::before {
            content: '!';
            font-size: 14px;
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
        .advice-container {
            display: flex;
            justify-content: space-around;
            margin: 5px 0;
        }
        .advice-list {
            background-color: #fff;
            padding: 5px;
            border: 2px solid #333;
            border-radius: 5px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
            width: 45%;
            font-size: 12px;
        }
        </style>
        """

    # Fetch the predicted yield
    predicted_yield = get_predicted_yield()

    # Determine the status color
    status_color = get_status_color(predicted_yield)

    # Generate and display the combined CSS
    st.markdown(generate_combined_css(), unsafe_allow_html=True)

    # Display the combined container
    st.markdown(f"""
        <div class="combined-container2">
            <div class="predicted-yield" style="background-color: {status_color};">
                <h2 style="font-size: 18px;">Predicted Yield</h2>
                <p style="font-size: 18px;">{predicted_yield:.2f}%</p>
            </div>
            <div class="container">
                <div class="alert-icon"></div>
                <div class="advice-container">
                    <div class="advice-list">
                        <h2 style="font-size: 16px;">Advice for Pot1</h2>
                        <p>1. Empty the container and refill 2 liters.</p>
                        <p>2. Add 1/4 cup of A+B solution to the container.</p>
                    </div>
                    <div class="advice-list">
                        <h2 style="font-size: 16px;">Advice for Pot2</h2>
                        <p>1. Empty the container and refill 2 liters.</p>
                        <p>2. Add 1/4 cup of A+B solution to the container.</p>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def createadvice1():
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


def MonitorCreating():


    #--------------------------------------------------------------------------
    def generate_menu_css():
        return """
        <style>
        .topnav {
            overflow: hidden;
            background-color: #333;
        }

        .topnav a {
            float: left;
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
            font-size: 17px;
        }

        .topnav a:hover {
            background-color: #ddd;
            color: black;
        }

        .topnav a.active {
            background-color: #04AA6D;
            color: white;
        }

        .topnav .icon {
            display: none;
        }

        .dropdown {
            float: left;
            overflow: hidden;
        }

        .dropdown .dropbtn {
            font-size: 17px;  
            border: none;
            outline: none;
            color: white;
            padding: 14px 16px;
            background-color: inherit;
            font-family: inherit;
            margin: 0;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
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
        }

        .dropdown:hover .dropdown-content {
            display: block;
        }
        </style>
        """

    # Generate and display the CSS for the menu
    st.markdown(generate_menu_css(), unsafe_allow_html=True)
    from datetime import datetime

    # Get the current date
    current_date = datetime.now().strftime("%B %d, 2024")

    # Display the top menu bar
    st.markdown(f"""
    <div class="topnav">
      <a class="active" href="#home">Pack Choy</a>
      <a href="#news">{current_date}</a>
      <div class="dropdown">
        <button class="dropbtn">Settings 
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
          <a href="#">Profile</a>
          <a href="#">Farms</a>
          <a href="#">Logout</a>
        </div>
      </div> 
    </div>
    """, unsafe_allow_html=True)
    def createpots():
        # Function to generate a random color for the crops
        def get_random_color():
            colors = ['#4CAF50', '#FFEB3B', '#F44336']  # Green, Yellow, Red
            return random.choice(colors)

        # Function to generate random crop data
        def generate_random_data():
            yield_gram = random.randint(10, 30)
            leaf_count = random.randint(5, 15)
            longest_leaf = random.randint(100, 200)
            plant_height = random.randint(100, 300)
            return yield_gram, leaf_count, longest_leaf, plant_height

        # Generate random data for the table
        data_current = generate_random_data()
        data_predicted = generate_random_data()
        data_target = generate_random_data()

        # HTML, CSS, and JavaScript for 2D visualization with popup
        html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>2D Visualization of Pak Choy Crops</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f9f9f9;
                }}
                .container {{
                   
                    text-align: center;
                }}
                .pots {{
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                }}
                .pot {{
                    border: 2px solid #333;
                    padding: 10px;
                    border-radius: 10px;
                    background-color: #fff;
                    width: 200px;
                }}
                .title {{
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 10px;
                }}
                .grid {{
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    grid-gap: 10px;
                    justify-items: center;
                }}
                .circle {{
                    width: 60px;
                    height: 60px;
                    border-radius: 50%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    cursor: pointer;
                    transition: transform 0.2s, box-shadow 0.2s;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    position: relative;
                }}
                .circle:hover {{
                    transform: scale(1.1);
                    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
                }}
                .circle p {{
                    margin: 0;
                    text-align: center;
                    font-size: 10px;
                    color: black;
                }}
                .circle p:last-child {{
                    font-size: 8px;
                }}
                .info {{
                    position: absolute;
                    bottom: 20px;
                    background: rgba(0, 0, 0, 0.7);
                    color: #fff;
                    padding: 10px;
                    border-radius: 5px;
                    display: none;
                }}
                .header {{
                    font-size: 24px;
                    font-weight: bold;
                    margin-bottom: 20px;
                }}
                .table-container {{
                    margin-top: 20px;
                    text-align: left;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-bottom: 20px;
                }}
                table, th, td {{
                    border: 1px solid #ddd;
                }}
                th, td {{
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                .popup {{
                    display: none;
                    position: fixed;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    border: 2px solid #333;
                    border-radius: 10px;
                    background-color: #fff;
                    z-index: 10;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    text-align: center;
                }}
                .popup table {{
                    margin: 0 auto;
                }}
                .popup button {{
                    margin-top: 10px;
                    padding: 5px 10px;
                    font-size: 14px;
                    cursor: pointer;
                }}
                .overlay {{
                    display: none;
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(0, 0, 0, 0.5);
                    z-index: 9;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">2D Visualization of Pak Choy Crops</div>
                <div class="pots">
                    <div class="pot">
                        <div class="title">Pot 1</div>
                        <div class="grid">
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>1</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>2</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>3</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>4</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>5</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>6</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>7</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>8</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>9</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>10</p></div>
                        </div>
                    </div>
                    <div class="pot">
                        <div class="title">Pot 2</div>
                        <div class="grid">
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>1</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>2</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>3</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>4</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>5</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>6</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>7</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>8</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>9</p></div>
                            <div class="circle" style="background-color: {get_random_color()};" onclick="showInfo()"><p>Pak Choy</p><p>10</p></div>
                        </div>
                    </div>
                </div>
                <div class="overlay" id="overlay"></div>
                <div class="popup" id="popup">
                    <table>
                        <tr>
                            <th>Yield (gram)</th>
                            <th>Leaf Count</th>
                            <th>Longest Leaf (mm)</th>
                            <th>Plant Height (mm)</th>
                            <th></th>
                        </tr>
                        <tr>
                            <td>{data_current[0]}</td>
                            <td>{data_current[1]}</td>
                            <td>{data_current[2]}</td>
                            <td>{data_current[3]}</td>
                            <td>Current</td>
                        </tr>
                        <tr>
                            <td>{data_predicted[0]}</td>
                            <td>{data_predicted[1]}</td>
                            <td>{data_predicted[2]}</td>
                            <td>{data_predicted[3]}</td>
                            <td>Predicted</td>
                        </tr>
                        <tr>
                            <td>{data_target[0]}</td>
                            <td>{data_target[1]}</td>
                            <td>{data_target[2]}</td>
                            <td>{data_target[3]}</td>
                            <td>Target</td>
                        </tr>
                    </table>
                    <button onclick="closePopup()">Close</button>
                </div>
            </div>
            <script>
                function showInfo() {{
                    const overlay = document.getElementById('overlay');
                    const popup = document.getElementById('popup');
                    overlay.style.display = 'block';
                    popup.style.display = 'block';
                }}

                function closePopup() {{
                    const overlay = document.getElementById('overlay');
                    const popup = document.getElementById('popup');
                    overlay.style.display = 'none';
                    popup.style.display = 'none';
                }}
            </script>
        </body>
        </html>
        """

        # Streamlit app content
        st.components.v1.html(html_code, height=500)


    #-----------------------------------------------

    # Sample data for plant growth
    growth_data = {
        "Week": [1, 2, 3, 4],
        "Plant Height (cm)": [random.randint(5, 15), random.randint(10, 20), random.randint(15, 25),
                              random.randint(20, 30)],
        "Leaf Count": [random.randint(3, 7), random.randint(5, 10), random.randint(8, 15), random.randint(10, 20)]
    }

    # Function to generate the HTML for the modal content
    def generate_modal_content(week):
        plant_height = growth_data["Plant Height (cm)"][week - 1]
        leaf_count = growth_data["Leaf Count"][week - 1]

        modal_content = f"""
        <div id="modal-week-{week}" class="modal">
            <div class="modal-content">
                <span class="close" onclick="closeModal({week})">&times;</span>
                <h2>Growth Information for Week {week}</h2>
                <p><strong>Plant Height:</strong> {plant_height} cm</p>
                <p><strong>Leaf Count:</strong> {leaf_count}</p>
            </div>
        </div>
        """
        return modal_content

    # Generate the HTML for the timeline and modals
    timeline_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .timeline {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin: 20px 0;
                padding: 0;
                list-style-type: none;
                font-family: 'Comic Sans MS', cursive, sans-serif;
            }}
            .timeline li {{
                position: relative;
                flex: 1;
                text-align: center;
            }}
            .timeline li::before {{
                content: '';
                position: absolute;
                top: 50%;
                left: -50%;
                width: 100%;
                height: 2px;
                background-color: #ddd;
                z-index: -1;
            }}
            .timeline li:first-child::before {{
                left: 50%;
            }}
            .timeline li:last-child::before {{
                width: 50%;
            }}
            .timeline li div {{
                padding: 10px 20px;
                border-radius: 20px;
                background-color: #ddd;
                border: 2px solid #ddd;
                display: inline-block;
                transition: background-color 0.3s, border-color 0.3s;
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                cursor: pointer;
            }}
            .timeline li.current div {{
                background-color: #4caf50;
                border: 2px solid #4caf50;
                color: white;
                font-weight: bold;
            }}
            .timeline li div:hover {{
                background-color: #f1f1f1;
                border-color: #bbb;
            }}
            .modal {{
                display: none;
                position: fixed;
                z-index: 1;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                overflow: auto;
                background-color: rgb(0,0,0);
                background-color: rgba(0,0,0,0.4);
            }}
            .modal-content {{
                background-color: #fefefe;
                margin: 5% auto;
                padding: 20px;
                border: 1px solid #888;
                width: 80%;
                max-width: 600px;
                transition: width 0.3s, height 0.3s;
            }}
            .modal-content.enlarge {{
                width: 90%;
                height: 90%;
            }}
            .close {{
                color: #aaa;
                float: right;
                font-size: 28px;
                font-weight: bold;
            }}
            .close:hover,
            .close:focus {{
                color: black;
                text-decoration: none;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <ul class="timeline">
            {''.join([f'<li class="{"" if i != 1 else "current"}"><div id="week-{i + 1}" onclick="showModal({i + 1})">Week {i + 1}</div></li>' for i in range(4)])}
        </ul>
        {''.join([generate_modal_content(i + 1) for i in range(4)])}
        <script>
            function showModal(week) {{
                const modal = document.getElementById('modal-week-' + week);
                modal.style.display = "block";
                setTimeout(() => {{
                    modal.querySelector('.modal-content').classList.add('enlarge');
                }}, 10);
            }}
            function closeModal(week) {{
                const modal = document.getElementById('modal-week-' + week);
                modal.querySelector('.modal-content').classList.remove('enlarge');
                setTimeout(() => {{
                    modal.style.display = "none";
                }}, 300);
            }}
        </script>
    </body>
    </html>
    """

    # Streamlit app content
    st.components.v1.html(timeline_html, height=100)




    col1, col2 = st.columns([7, 3])

    with col1:
        createYeidl()
        createpots()

    with col2:
        creategauge()




