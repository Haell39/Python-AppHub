import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

# Função para obter a taxa de câmbio de uma moeda para outra
def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/2455ec50180ebd6e570c33f1/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'conversion_rates' in data:
            exchange_rate = data['conversion_rates'].get(target_currency)
            if exchange_rate:
                return exchange_rate
            else:
                messagebox.showerror("Erro", "A moeda de destino não é válida.")
        else:
            messagebox.showerror("Erro", "Erro ao acessar a API de taxas de câmbio.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erro", f"Erro ao acessar a API: {e}")
    return None

# Função chamada ao pressionar o botão de conversão
def convert_currency():
    base_currency = base_currency_entry.get().upper()  # Moeda base
    target_currency = target_currency_entry.get().upper()  # Moeda de destino
    amount = amount_entry.get()  # Quantia a ser convertida
    
    try:
        amount = float(amount)
        exchange_rate = get_exchange_rate(base_currency, target_currency)
        if exchange_rate:
            result = amount * exchange_rate
            result_label.config(text=f"{amount} {base_currency} = {result:.2f} {target_currency}",
                                font=("Arial", 12), fg="lightyellow", bg="#000000", relief="solid", bd=3, padx=10, pady=10)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

# Configuração da interface gráfica com Tkinter
root = tk.Tk()
root.title("Conversor de Moeda")
root.geometry("500x600")  # Tamanho da janela
root.resizable(False, False)

# Carregar a imagem de fundo
bg_image = Image.open("ExchangeApp\\img\\imageA.jpg")  # Coloque o caminho da sua imagem
bg_image = bg_image.resize((500, 600), Image.Resampling.LANCZOS)  # Ajustar o tamanho da imagem
bg_photo = ImageTk.PhotoImage(bg_image)

# Criando o canvas para mostrar a imagem de fundo
canvas = tk.Canvas(root, width=500, height=600)
canvas.pack(fill="both", expand=True)

# Colocando a imagem no canvas
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Estilo dos widgets
widget_bg = "#3b3b3b"  # Cor de fundo para os widgets
button_bg = "#4CAF50"  # Cor do botão
button_fg = "white"  # Cor do texto do botão

# Label de título
label = tk.Label(root, text="Conversor de Moeda", font=("Arial", 16, "bold"), fg="white", bg=widget_bg, relief="flat", padx=10, pady=10)
label.place(relx=0.5, rely=0.1, anchor="center")

# Campo de entrada de valor
amount_label = tk.Label(root, text="Valor:", font=("Arial", 12), fg="white", bg=widget_bg)
amount_label.place(relx=0.5, rely=0.2, anchor="center")
amount_entry = tk.Entry(root, font=("Arial", 14), width=20, bd=2, relief="solid", borderwidth=2)
amount_entry.place(relx=0.5, rely=0.25, anchor="center")

# Campo de entrada para a moeda base
base_currency_label = tk.Label(root, text="Moeda Base (ex: USD):", font=("Arial", 12), fg="white", bg=widget_bg)
base_currency_label.place(relx=0.5, rely=0.35, anchor="center")
base_currency_entry = tk.Entry(root, font=("Arial", 14), width=20, bd=2, relief="solid", borderwidth=2)
base_currency_entry.place(relx=0.5, rely=0.4, anchor="center")

# Campo de entrada para a moeda de destino
target_currency_label = tk.Label(root, text="Moeda de Destino (ex: EUR):", font=("Arial", 12), fg="white", bg=widget_bg)
target_currency_label.place(relx=0.5, rely=0.5, anchor="center")
target_currency_entry = tk.Entry(root, font=("Arial", 14), width=20, bd=2, relief="solid", borderwidth=2)
target_currency_entry.place(relx=0.5, rely=0.55, anchor="center")

# Botão para fazer a conversão
convert_button = tk.Button(root, text="Converter", command=convert_currency, font=("Arial", 14, "bold"), fg=button_fg, bg=button_bg, relief="raised", bd=5, width=20)
convert_button.place(relx=0.5, rely=0.65, anchor="center")

# Label para mostrar o resultado da conversão
result_label = tk.Label(root, text="", font=("Arial", 12), fg="white", bg=widget_bg, wraplength=450)
result_label.place(relx=0.5, rely=0.75, anchor="center")

# Rodando o loop principal do Tkinter
root.mainloop()
