# çç Instructions:

"""
1. Create/Import a CSV file to VSCode
2. Open browser
3. Access the system site with loguin and password
4. Insert all product info
5. Submit all info to the system
6. Repeat registration until all products are registered
"""

# Create/Import a CSV file to VSCode
import pyautogui
import time
import pandas as pd
import keyboard

pyautogui.FAILSAFE = (
    True  # Habilita o failsafe (padrão) para pausar a automação em caso de emergência
)


# Importing the CSV file
table = pd.read_csv("Projects/AutomationCSV/produtos.csv")
print(table)

# definir o tempo de espera entre cada ação do  PyAutoGUI
pyautogui.PAUSE = 0.6

# abrir navegador (librewolf)
pyautogui.press("win")
pyautogui.write("librewolf")  # 2. Open browser
pyautogui.press("enter")
time.sleep(3)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


# wait to load
time.sleep(5)

# Access the system site with loguin and password

pyautogui.write("IqZCZ@example.com")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.click(x=482, y=522)

time.sleep(2)


# 4. Insert all product info

for line in table.index:

    pyautogui.click(x=426, y=268)
    pyautogui.write(str(table.loc[line, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(table.loc[line, "obs"]):
        pyautogui.write(str(table.loc[line, "obs"]))
    pyautogui.click(x=409, y=864)
    pyautogui.scroll(5000)

# 6. Repeat registration until all products are registered
