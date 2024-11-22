# --------------------------------------------
# Imports at the top - PyShiny EXPRESS VERSION
# --------------------------------------------

# From shiny, import just reactive and render
from shiny import reactive, render

# From shiny.express, import just ui
from shiny.express import ui

# Imports from Python Standard Library to simulate live data
import random
from datetime import datetime

# Optional: Import Font Awesome icons as you like
from faicons import icon_svg

# --------------------------------------------
# Set constants and define reactive calculation
# --------------------------------------------

UPDATE_INTERVAL_SECS: int = 1

@reactive.calc()
def reactive_calc_combined():
    """Generate a fake temperature and timestamp every N seconds."""
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    temp = round(random.uniform(-18, -16), 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {"temp": temp, "timestamp": timestamp}

# --------------------------------------------
# Define the UI Layout - Page Options
# --------------------------------------------

ui.page_opts(title="PyShiny Express: Live Data (Basic)", fillable=True)

# --------------------------------------------
# Define the UI Layout - Sidebar
# --------------------------------------------

with ui.sidebar(open="open"):
    ui.h2("Antarctic Explorer", class_="text-center")
    ui.p(
        "A demonstration of real-time temperature readings in Antarctica.",
        class_="text-center",
    )

# --------------------------------------------
# Define the UI Layout - Main Section
# --------------------------------------------

ui.h2("Current Temperature")

@render.text
def display_temp():
    """Display the latest temperature reading."""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['temp']} C"

ui.p("Warmer than usual")
icon_svg("sun")
ui.hr()

ui.h2("Current Date and Time")

@render.text
def display_time():
    """Display the latest timestamp."""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['timestamp']}"
