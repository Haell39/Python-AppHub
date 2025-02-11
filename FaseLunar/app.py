import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime
from PIL import Image, ImageTk

# Função para obter a fase da lua para uma data específica
def get_moon_phase(date):
    url = f"https://api.ipgeolocation.io/astronomy?apiKey=b17d58398b214afa859599a34d88ad9b&date={date}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        moon_phase = data['moon_phase']
        return moon_phase
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro", f"Erro ao acessar a API: {e}")
        return None

# Função chamada ao pressionar o botão
def show_moon_phase():
    date = date_entry.get()  # Pega a data inserida pelo usuário
    try:
        # Valida se a data está no formato correto
        datetime.strptime(date, "%Y-%m-%d")
        moon_phase = get_moon_phase(date)  # Chama a função para pegar a fase da lua
        if moon_phase:
            result_label.config(text=f"Fase da Lua em {date}: {moon_phase}", 
                                font=("Georgia", 14, "italic"),  # Fonte mística
                                fg="lightyellow",  # Cor suave para o texto
                                bg="#000000",  # Cor de fundo escura sem transparência
                                relief="solid",  # Borda sólida
                                bd=3,  # Espessura da borda
                                borderwidth=2,  # Borda mais suave
                                padx=10, pady=10,  # Espaçamento interno
                                wraplength=350)  # Texto ajustável
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira a data no formato YYYY-MM-DD.")

# Configuração da interface gráfica com Tkinter
root = tk.Tk()
root.title("Fases da Lua")
root.geometry("400x500")  # Tamanho da janela

# Carregar a imagem de fundo
bg_image = Image.open("FaseLunar\\Images\\MoonImg.jpg")  # Substitua pelo caminho da sua imagem
bg_image = bg_image.resize((400, 500), Image.Resampling.LANCZOS)  # Ajustar tamanho da imagem
bg_photo = ImageTk.PhotoImage(bg_image)

# Criando o canvas para mostrar a imagem de fundo
canvas = tk.Canvas(root, width=400, height=500)
canvas.pack(fill="both", expand=True)

# Colocando a imagem no canvas
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Label de instruções centralizada
label = tk.Label(root, text="Digite a data (Ano-Mês-Dia):", font=("Arial", 12, "bold"), fg="white", bg="#3b3b3b")
label.place(relx=0.5, rely=0.15, anchor="center")

# Campo de entrada de data centralizado
date_entry = tk.Entry(root, font=("Arial", 12), width=15)
date_entry.place(relx=0.5, rely=0.25, anchor="center")

# Botão para obter a fase da lua centralizado
check_button = tk.Button(root, text="Ver Fase da Lua", command=show_moon_phase, font=("Arial", 12, "bold"), fg="white", bg="#4CAF50", relief="raised", bd=5)
check_button.place(relx=0.5, rely=0.35, anchor="center")

# Label para mostrar o resultado centralizado e ajustável
result_label = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="#3b3b3b", wraplength=350)
result_label.place(relx=0.5, rely=0.50, anchor="center")

# Rodando o loop principal do Tkinter
root.mainloop()
