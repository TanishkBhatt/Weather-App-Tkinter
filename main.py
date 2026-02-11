from fetchAPI import getData
from tkinter import *

# ---------------- WINDOW ----------------
window = Tk()
window.title("WEATHER APPLICATION")
window.geometry("1024x560")
window.resizable(False, False)
window.configure(bg="#EAF6FF") 

# ---------------- MAIN CARD ----------------
main_frame = Frame(
    window,
    bg="white",
    highlightthickness=1,
    highlightbackground="#CBD5E1"
)
main_frame.place(x=20, y=20, width=984, height=520)

# ---------------- TITLE ----------------
title = Label(
    main_frame,
    text="WEATHER APPLICATION",
    font=("Segoe UI", 26, "bold"),
    bg="white",
    fg="#1E3A8A"
)
title.place(relx=0.5, y=35, anchor="center")
Frame(main_frame, bg="#CBD5E1", height=1).place(x=40, y=75, width=900)

# ---------------- WEATHER ICON ----------------
weather_icon = Label(
    main_frame,
    text="🌥️",
    bg="white"
)
weather_icon.config(font=("Segoe UI", 110))
weather_icon.place(x=90, y=150)

# ---------------- CITY INPUT ----------------
city = Entry(
    main_frame,
    font=("Segoe UI", 14),
    bd=0,
    justify="center",
    bg="#F1F5F9",
    fg="#0F172A"
)
city.place(x=380, y=120, width=360, height=42)

city.insert(0, "ENTER CITY NAME...")
city.config(fg="#64748B")

def focus_in(event):
    if city.get() == "ENTER CITY NAME...":
        city.delete(0, END)
        city.config(fg="#0F172A")

def focus_out(event):
    if city.get() == "":
        city.insert(0, "ENTER CITY NAME...")
        city.config(fg="#64748B")

city.bind("<FocusIn>", focus_in)
city.bind("<FocusOut>", focus_out)

# ---------------- SEARCH BUTTON ----------------
search_btn = Button(
    main_frame,
    text="🔍",
    bg="#38BDF8",
    fg="white",
    bd=0,
    cursor="hand2",
    activebackground="#0EA5E9"
)
search_btn.config(font=("Segoe UI", 17))
search_btn.place(x=760, y=120, width=45, height=45)

# ---------------- WEATHER INFO ----------------
value_font = ("Segoe UI", 15)
label_font = ("Segoe UI", 15)

label_color = "#334155"
value_color = "#0F172A"

Label(main_frame, text="Weather".upper(), bg="white", fg=label_color, font=label_font).place(x=420, y=200)
Label(main_frame, text="Temperature".upper(), bg="white", fg=label_color, font=label_font).place(x=420, y=240)
Label(main_frame, text="Feels Like".upper(), bg="white", fg=label_color, font=label_font).place(x=420, y=280)
Label(main_frame, text="Humidity".upper(), bg="white", fg=label_color, font=label_font).place(x=420, y=320)
Label(main_frame, text="Wind Speed".upper(), bg="white", fg=label_color, font=label_font).place(x=420, y=360)

weather_val = Label(main_frame, text="—", bg="white", fg=value_color, font=value_font)
temp_val = Label(main_frame, text="—", bg="white", fg=value_color, font=value_font)
feels_val = Label(main_frame, text="—", bg="white", fg=value_color, font=value_font)
humidity_val = Label(main_frame, text="—", bg="white", fg=value_color, font=value_font)
wind_val = Label(main_frame, text="—", bg="white", fg=value_color, font=value_font)

weather_val.place(x=600, y=200)
temp_val.place(x=600, y=240)
feels_val.place(x=600, y=280)
humidity_val.place(x=600, y=320)
wind_val.place(x=600, y=360)

# ---------------- SEARCH ACTION ----------------
def fetch_weather():
    city_name = city.get().strip()
    if city_name == "" or city_name == "ENTER CITY NAME...":
        return

    data = getData(city_name)

    if data:
        weather_val.config(text=data["WEATHER"].upper())
        temp_val.config(text=f'{data["TEMPERATURE"]} °C')
        feels_val.config(text=f'{data["FEELS_LIKE"]} °C')
        humidity_val.config(text=f'{data["HUMIDITY"]} %')
        wind_val.config(text=f'{data["WIND_SPEED"]} m/s')

        condition = data["WEATHER"].lower()
        if "cloud" in condition:
            weather_icon.config(text="☁️")
        elif "rain" in condition:
            weather_icon.config(text="🌧️")
        elif "clear" in condition:
            weather_icon.config(text="☀️")
        elif "snow" in condition:
            weather_icon.config(text="❄️")
        else:
            weather_icon.config(text="🌥️")

search_btn.config(command=fetch_weather)

# ---------------- MAIN LOOP ----------------
window.mainloop()