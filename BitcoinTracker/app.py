from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import requests
import json

# Colors 
co0 = "#000000"  # black
co1 = "#ffffff"  # white
co2 = "#0000ff"  # blue

fundo = "#484f60"

# Janela
janela = Tk()
janela.title("Bitcoin Price Tracker")
janela.geometry("350x400")  
janela.configure(bg=fundo)


ico_path = "BitcoinTracker\\bitcoin.ico"
janela.iconbitmap(ico_path)


janela.resizable(False, False)


frame_cima = Frame(janela, width=350, height=50, bg=co1, pady=0, padx=0, relief="flat")
frame_cima.grid(row=0, column=0, sticky="nsew")

frame_baixo = Frame(janela, width=350, bg=fundo, pady=0, padx=0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky="nsew")


janela.grid_rowconfigure(0, weight=0)
janela.grid_rowconfigure(1, weight=1)
janela.grid_columnconfigure(0, weight=1)


# API
def info():
    api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CAOA%2CBRL%2CJPY"

    #  Request
    response = requests.get(api_link)

    
    dados = response.json()

    # USD 
    valor_usd = float(dados["USD"])
    valor_formatado_usd = "${:,.3f}".format(valor_usd)
    l_p_usd["text"] = f"Cotação Atual: 1₿ = {valor_formatado_usd}"

    # BRL 
    valor_real = float(dados["BRL"])
    valor_formatado_real = "R${:,.3f}".format(valor_real)
    l_p_real["text"] = f"Cotação Real: 1₿ = {valor_formatado_real}"

    # EUR 
    valor_euro = float(dados["EUR"])
    valor_formatado_euro = "€{:,.3f}".format(valor_euro)
    l_p_euro["text"] = f"Cotação Euro: 1₿ = {valor_formatado_euro}"

    # JPY 
    valor_jpy = float(dados["JPY"])
    valor_formatado_jpy = "¥{:,.3f}".format(valor_jpy)
    l_p_jpy["text"] = f"Cotação Iene: 1₿ = {valor_formatado_jpy}"

    frame_baixo.after(
        1000, info
    )  # Atualiza a cotação a cada 1 segundo


# Frames e image
imagem = Image.open(
    "BitcoinTracker\\bitcoin.png"
)
imagem = imagem.resize((30, 30), Image.Resampling.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image=imagem, bg=co1, relief="flat")
l_icon.place(x=10, y=10)

l_nome = Label(
    frame_cima,
    text="Bitcoin Price Tracker",
    bg=co1,
    relief="flat",
    anchor="center",
    font=("Arial", 20),
    fg=co2,
)
l_nome.place(x=50, y=10)


l_p_usd = Label(
    frame_baixo,
    text="",
    width=30,
    bg=fundo,
    relief="flat",
    anchor="center",
    font=("Arial", 15),
    fg=co1,
)
l_p_usd.grid(row=0, column=0, sticky="n", padx=10, pady=10)

# Adicionando um separator (uma linha divisória)
ttk.Separator(frame_baixo, orient=HORIZONTAL).grid(
    row=1, column=0, sticky="ew", padx=10, pady=10
)

# alinha as cotações à esquerda
frame_cotacoes = Frame(frame_baixo, bg=fundo)
frame_cotacoes.grid(row=2, column=0, sticky="n", padx=10, pady=5)

# Outras cotações
l_p_real = Label(
    frame_cotacoes,
    text="",
    bg=fundo,
    relief="flat",
    anchor="w",
    font=("Arial", 13),
    fg=co1,
)
l_p_real.grid(row=0, column=0, sticky="w", pady=5)

l_p_euro = Label(
    frame_cotacoes,
    text="",
    bg=fundo,
    relief="flat",
    anchor="w",
    font=("Arial", 13),
    fg=co1,
)
l_p_euro.grid(row=1, column=0, sticky="w", pady=5)

l_p_jpy = Label(
    frame_cotacoes,
    text="",
    bg=fundo,
    relief="flat",
    anchor="w",
    font=("Arial", 13),
    fg=co1,
)
l_p_jpy.grid(row=2, column=0, sticky="w", pady=5)

info()

# Chamando o mainloop
janela.mainloop()
