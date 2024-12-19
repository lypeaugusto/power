#1 entrar no sistema https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas 
import os

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('google chrome')
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x=535, y=61)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
time.sleep(2)
pyautogui.press('enter')

pyautogui.click(x=697, y=411)
pyautogui.write('kakaroto@gmail.com')

time.sleep(1)
pyautogui.press('tab')
pyautogui.write('123456789')

pyautogui.click(x=949, y=565)

time.sleep(1)
pyautogui.click(x=1129, y=359)



file_path = r"C:\estudos\python\power\produtos.csv"

if os.path.exists(file_path):
    print("Arquivo encontrado:", file_path)
    tabela = pandas.read_csv(file_path)
    print(tabela)
else:
    print("Arquivo não encontrado. Verifique o caminho:", file_path)





time.sleep(1)
pyautogui.click(x=1013, y=358)

row = 0
colm = 0

for row in tabela.index:
    

    codigo = tabela.loc[row,'codigo']

    time.sleep(1)
    pyautogui.click(x=614, y=302)
    pyautogui.write(str(codigo))

    marca = tabela.loc[row,'marca'] 
    pyautogui.press('tab')
    pyautogui.write(str(marca))

    tipo = tabela.loc[row,'tipo']
    pyautogui.press('tab')
    pyautogui.write(str(tipo))

    categoria = tabela.loc[row,'categoria']
    pyautogui.press('tab')
    pyautogui.write(str(categoria))

    preco = tabela.loc[row,'preco_unitario']
    pyautogui.press('tab')
    pyautogui.write(str(preco))

    custo = tabela.loc[row,'custo']
    pyautogui.press('tab')
    pyautogui.write(str(custo))

    obs = tabela.loc[row,'obs']
    pyautogui.press('tab')
    pyautogui.write(str(obs))
    pyautogui.press('enter')
    pyautogui.scroll(10000)


#4 cadastrar
#5 cadastrar todos produtos 
 
