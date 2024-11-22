# **Moses' Custom Live Data Dashboard**

## **Description**
This project is a **real-time data dashboard** built using PyShiny. It simulates live temperature readings in Celsius, Fahrenheit, and Kelvin, dynamically updates at a specified interval, and provides insightful visualizations such as trend charts with regression lines.

---

## **Features**
- **Real-Time Data Simulation**:
  - Generates live temperature readings in Celsius, Fahrenheit, and Kelvin.
  - Updates every second.
- **Interactive Temperature Unit Selection**:
  - Choose between Celsius, Fahrenheit, or Kelvin via radio buttons.
- **Dynamic Value Boxes**:
  - Displays the latest temperature and timestamp with attractive styling.
- **Recent Data Table**:
  - Shows the last 10 readings, including temperature in all units and timestamps.
- **Temperature Trend Chart**:
  - Scatter plot of recent temperature readings.
  - Includes a regression line to indicate trends over time.
- **Responsive Design**:
  - Fully responsive layout optimized for desktop and mobile views.

---

## **Screenshots**
| **Feature**          | **Screenshot**             |
|-----------------------|----------------------------|
| **Value Boxes**       | *(![alt text](<Screenshot 2024-11-22 at 1.55.02 PM.png>))*    |
| **Recent Data Table** | *(![alt text](<Screenshot 2024-11-22 at 1.55.24 PM.png>) )*    |
| **Temperature Chart** | *(![alt text](<Screenshot 2024-11-22 at 1.54.24 PM.png>))*    |

---

## **Technologies Used**
- **Python Libraries**:
  - `shiny`
  - `shiny.express`
  - `pandas`
  - `plotly`
  - `scipy`
- **Frontend Framework**: PyShiny (Express version)
- **Icons**: Font Awesome free icons (`faicons`)

---

## **Getting Started**

### **Online**
Access the deployed dashboard here:  
[**Live Dashboard**](https://mokeyzz1.github.io/cintel-05-cintel/l/)

---

### **Local Development**
To run the project locally, follow these steps:

1. Clone the repository:source .venv/bin/activate

   ```bash
   git clone https://github.com/moseskoroma/cintel-05-cintel.git
```
2. Navigate to the project directory:
    ```
cd cintel-05-cintel
```

3. Create a virtual environment:

python -m venv .venv

4. Activate the virtual environment:
    ```
Mac/Linux:

source .venv/bin/activate
Windows:

.venv\Scripts\activate
```

5. Install dependencies:
    ```
pip install -r requirements.txt
```
6. Run the app:
````
shiny run --reload --launch-browser dashboard/app.py
```
