import requests
import tkinter as tk
from tkinter import messagebox, PhotoImage

def get_weather():
    api_key = "6b73c40fda874e07a5f224736251002" 
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Entrada inválida", "Por favor, insira o nome da cidade.")
        return
    
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    try:
        response = requests.get(url)
        data = response.json()
        
        if "error" in data:
            messagebox.showerror("Erro", data["error"]["message"])
            return
        
        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        
        result_label.config(text=f"{location}, {country}\n{temp_c}°C\n{condition}", bg="#ffffff", fg="#333333")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao obter dados: {e}")

# << Interface
root = tk.Tk()
root.title("Weather App")
root.geometry("350x420") # Ajustar tamanho da janela
root.resizable(False, False) # Impedir redimensionamento pelo usuario
root.configure(bg="#87CEEB")  


background_image = PhotoImage(file="weatherApp\\Img\\image.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

tk.Label(root, text="Qual Cidade:", font=("Arial", 12, "bold"), bg="#87CEEB").pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12), width=20)
city_entry.pack(pady=5)

tk.Button(root, text="Analisar Clima", font=("Arial", 12, "bold"), bg="#ffcc00", fg="#000", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#ffffff", fg="#333333", relief="solid", bd=2, padx=10, pady=5)
result_label.pack(pady=15)

root.mainloop()
