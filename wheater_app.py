import requests
from tkinter import *
from tkinter import ttk
from wheater import Wheater


def main():
    root = Tk()
    root.title("Weather App")
    root.geometry("400x300")
    root.grid()

    def clean_frame(frame):
        if frame:
            for widget in frame.winfo_children():
                widget.destroy()

    # Asignar los frames correctamente sin aplicar grid en la misma línea
    mainframe = ttk.Frame(root, padding=5)
    mainframe.grid(row=1, column=1)  # Aplica grid en una línea separada

    wheater_frame = ttk.Frame(root, padding=5)
    wheater_frame.grid(row=2, column=1)  # Aplica grid en una línea separada

    def view_wheater(city):
        clean_frame(wheater_frame)  # Limpia el contenido del frame
        if city:
            city_info = Wheater()
            try:
                city_info.get_city(city)

                name_city = ttk.Label(wheater_frame, text=city_info.city)
                name_country = ttk.Label(wheater_frame, text=city_info._country)
                celcius_city = ttk.Label(wheater_frame, text=f"{city_info._celcius}° C")
                feelslike_c = ttk.Label(
                    wheater_frame,
                    text=f"Sensacion Terminca: {city_info._feelslike_c}° C",
                )
                clouds_city = ttk.Label(
                    wheater_frame, text=f"Nubes: {city_info._clouds}%"
                )
                humidity = ttk.Label(
                    wheater_frame, text=f"Humedad: {city_info._humidity}%"
                )
                name_city.grid(row=4, column=1)
                name_country.grid(row=4, column=2)
                celcius_city.grid(row=5, column=1)
                feelslike_c.grid(row=6, column=1)
                clouds_city.grid(row=7, column=1)
                humidity.grid(row=8, column=1)

            except requests.exceptions.RequestException as e:
                error_msg = ttk.Label(wheater_frame, text=e)
                error_msg.grid(row=4, column=1)

    city_entry = ttk.Entry(mainframe, width=20)
    city_entry.grid(row=2, column=1)

    city_entry_label = ttk.Label(mainframe, text="Search city")
    city_entry_label.grid(row=1, column=1)

    search_btn = ttk.Button(
        mainframe,
        text="Search",
        command=lambda: view_wheater(city_entry.get()),
    )
    search_btn.grid(row=3, column=1)

    root.mainloop()


if __name__ == "__main__":
    main()
