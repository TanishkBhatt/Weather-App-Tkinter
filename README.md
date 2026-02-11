# Weather App using Tkinter
  
A Python-based **desktop weather application** built with **Tkinter** that fetches real-time weather data using the **OpenWeather API**.  
The app allows users to search weather details for any city through a simple and interactive GUI.

---

## Introduction

This project demonstrates how a Python desktop application can interact with an external API and present live data through a graphical user interface.  
It focuses on clean code structure, API integration, and GUI-based user interaction.

---

## About the Project (In Depth)

The Weather App works by taking a city name as user input and sending a request to the OpenWeather API.  
The API returns weather data in JSON format, which is then parsed and displayed in the application window.

## Key Features
- City-based weather search
- Real-time weather data
- Simple and clean Tkinter GUI
- API error handling
- Modular code structure

## Project Structure

```bash
Weather-App-Tkinter/
│
├── main.py             # Main application and GUI logic
├── fetchAPI.py         # API request and response handling
├── config.py           # API key and configuration
└── README.md           # Project documentation
```

---


##  Technical Stack Used

- **Programming Language :** python  
- **GUI Framework :** tkinter  
- **API :** OpenWeather API  
- **HTTP Library :** requests

---

##  How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/TanishkBhatt/Weather-App-Tkinter.git
```

### Step 2: Install Dependencies
```bash
pip install requests
```

### Step 3: Add OpenWeather API Key

- Create an account at https://openweathermap.org/
- Generate your API key
- Open config.py and add:

```bash
API_KEY = "your_api_key_here"
```

### Step 4: Run the Application
```bash
python main.py
```

--- 

## About the Author

`Tanishk Bhatt`
Student and Python programmer with interests in API-based applications, GUI development, and backend logic.
This project represents hands-on learning in Python desktop app development.

---

## Links

- OpenWeather API : https://openweathermap.org/
- Request Library Documentation : https://docs.python-requests.org/
- Github : https://github.com/TanishkBhatt/
- Portfolio : https://tanishkbhatt.github.io/Portfolio/
- YouTube : https://youbute.com/@TanishkBhatt-x6w/

---