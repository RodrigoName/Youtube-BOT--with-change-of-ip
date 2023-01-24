from tkinter import N
import webbrowser, time, os
import subprocess
import random

#Em Liste substitua pelos seus links do youtube
# instale o pycharm no seu computador e coloque o código para rodar
##############################


#Em duration, determine o tempo em segundos para os videos rodarem
#Se tudo der certo, abrirá 4 janelas do navegador e elas fecharam depois de 300 segundos
#Não se preocupe, elas irão abrir novamente, assim qualquer computador é capaz de rodar
#sem problemas de memória 


#----------------------------------------------------
#url = "https://www.youtube.com/watch?v=awnKl..."
#duration= "10"
#---------------------------------------------------------

Liste =  [

"https://www.youtube.com/watch?v=AviDWvQg6-I&ab_channel=%23Shorts_Rodrigo?autoplay=1",
"https://www.youtube.com/watch?v=w9fVeTOnI9E&ab_channel=%23Shorts_Rodrigo?autoplay=1",

   
          ]


duration= "10"


while True:
    Listagem = random.choice(Liste)
    webbrowser.open_new_tab("chrome://newtab")

    for i in range(1):
        webbrowser.open_new(Listagem)
        time.sleep(int(duration))
        break

    
    Listagem = random.choice(Liste)
    webbrowser.open_new_tab("chrome://newtab")

    for i in range(1):
        webbrowser.open_new(Listagem)
        time.sleep(int(duration))
        break

        
    subprocess.call("taskkill /IM chrome.exe /F")
    break
