# --------------------------------------------
# Imports - PyShiny EXPRESS VERSION
# --------------------------------------------

# From shiny, import just reactive and render
from shiny import reactive, render

# From shiny.express, import just ui and inputs 
from shiny.express import input, ui

# Imports for live data simulation and processing
import random
from datetime import datetime
from collections import deque
import pandas as pd
import plotly.express as px
from shinywidgets import render_plotly
from scipy import stats

# Font Awesome icons for styling
from faicons import icon_svg

# --------------------------------------------
# Constants and Reactive Content
# --------------------------------------------

UPDATE_INTERVAL_SECS: int = 1
DEQUE_SIZE: int = 10  # Store the last 10 readings

# Reactive value wrapper around a deque
reactive_value_wrapper = reactive.Value(deque(maxlen=DEQUE_SIZE))

@reactive.calc()
def reactive_calc_combined():
    """
    Generate fake temperature data in multiple units and a timestamp every UPDATE_INTERVAL_SECS.
    """
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # Generate random temperature in Celsius
    temp_celsius = round(random.uniform(-10, 35), 1)
    temp_fahrenheit = round((temp_celsius * 9 / 5) + 32, 1)  # Convert to Fahrenheit
    temp_kelvin = round(temp_celsius + 273.15, 1)  # Convert to Kelvin
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_data = {
        "temp_celsius": temp_celsius,
        "temp_fahrenheit": temp_fahrenheit,
        "temp_kelvin": temp_kelvin,
        "timestamp": timestamp,
    }

    # Update deque with new data
    reactive_value_wrapper.get().append(new_data)

    # Convert deque to DataFrame for display and processing
    df = pd.DataFrame(reactive_value_wrapper.get())

    # Return required values
    return df, new_data


# --------------------------------------------
# Define UI Layout
# --------------------------------------------

ui.page_opts(title="Moses' Custom Live Data Dashboard", fillable=True)

# Sidebar
with ui.sidebar(open="open"):
    ui.h2("Real-Time Data Explorer", class_="text-center")
    ui.p("A custom dashboard to simulate and display live temperature readings.", class_="text-center")
    ui.input_radio_buttons(
        "temp_unit",
        label="Select Temperature Unit",
        choices=["Celsius", "Fahrenheit", "Kelvin"],
        selected="Celsius",
    )
    ui.hr()
    ui.h6("Links:")
    ui.a("GitHub Source", href="https://github.com/moseskoroma/cintel-05-cintel", target="_blank")
    ui.a("Deployed App", href="https://moseskoroma.github.io/cintel-05-cintel/", target="_blank")

# Main Panel
with ui.navset_card_tab(id="main_panel"):
    with ui.nav_panel("Live Data"):
        # Value Box for Current Temperature
        with ui.value_box(
            showcase=icon_svg("thermometer"),
            theme="bg-gradient-green-blue",
        ):
            "Live Temperature"

            @render.text
            def display_temp():
                """Display the latest temperature in the selected unit."""
                df, latest_data = reactive_calc_combined()
                selected_unit = input.temp_unit()

                if selected_unit == "Celsius":
                    temp = latest_data["temp_celsius"]
                    unit = "°C"
                elif selected_unit == "Fahrenheit":
                    temp = latest_data["temp_fahrenheit"]
                    unit = "°F"
                else:
                    temp = latest_data["temp_kelvin"]
                    unit = "K"

                return f"{temp} {unit}"

        # Value Box for Timestamp
        with ui.value_box(
            showcase=icon_svg("clock"),
            theme="bg-gradient-blue-purple",
        ):
            "Current Date and Time"

            @render.text
            def display_time():
                """Display the current timestamp."""
                _, latest_data = reactive_calc_combined()
                return latest_data["timestamp"]

    with ui.nav_panel("Recent Readings"):
        with ui.card():
            ui.card_header("Recent Data Table")

            @render.data_frame
            def display_data_table():
                """Display the recent readings as a DataFrame."""
                df, _ = reactive_calc_combined()
                return df

    with ui.nav_panel("Temperature Trends"):
        with ui.card():
            ui.card_header("Temperature Trend Chart")

            @render_plotly
            def display_plot():
                """Display a temperature trend chart with a regression line."""
                df, _ = reactive_calc_combined()

                if not df.empty:
                    fig = px.scatter(
                        df,
                        x="timestamp",
                        y="temp_celsius",
                        title="Temperature Trends with Regression Line",
                        labels={"temp_celsius": "Temperature (°C)", "timestamp": "Time"},
                        color_discrete_sequence=["blue"],
                    )

                    # Add regression line
                    x_vals = range(len(df))
                    slope, intercept, _, _, _ = stats.linregress(x_vals, df["temp_celsius"])
                    df["regression_line"] = [slope * x + intercept for x in x_vals]

                    fig.add_scatter(x=df["timestamp"], y=df["regression_line"], mode="lines", name="Regression Line")

                    fig.update_layout(
                        xaxis_title="Time",
                        yaxis_title="Temperature (°C)",
                        template="plotly_white",
                    )
                    return fig

                return px.scatter(title="No Data Available Yet")
