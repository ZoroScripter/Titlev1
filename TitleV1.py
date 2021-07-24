import os
import time

#Colors
#\033[1;30m Branco
#\033[1;31m Vermelho
#\033[1;32m Verde
#\033[1;33m Amarelo
#\033[1;34m Azul
#\033[1;35m Roxo
#\033[1;36m Ciano
#\033[1;37m Cinza Claro


##################
os.system("clear")
os.system("pkg install figlet")
os.system("clear")
print("\033[1;31m")
os.system("figlet TitleV1")
##################
print("""\033[1;36m
l-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-l
l            TitleV1            l
l-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-l\033[1;35m
l       [1]Install Update       l
l       [2]Install Upgrade      l
l       [3]Install Git          l
l       [4]Install Python3      l
l       [5]Install Python2      l
l       [6]Install Python       l
l       [7]Install Wget         l
l       [8]Install Sl           l
l       [9]Install Libaca       l
l       [10]Install Cmatrix     l
l       [11]Update Reporitorys  l
l       [12]Install Ruby        l
l       [13]Install Php         l
l       [14]Instlal proot       l
l       [15]Install Black       l
l       [16]Install bc          l
l       [17]Somar               l
l       [18]Multiplicar         l
l       [19]Creditos            l
l       [20]Sair                l\033[1;36m
l-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-l
""")
op = input("\033[1;32m>>> ")

if op == "1":
    os.system("""
    clear
    pkg update
    python3 TitleV1.py
    """)
elif op == "2":
    os.system("""
    clear
    pkg upgrade
    python3 TitleV1.py
    """)
elif op == "3":
    os.system("""
    clear
    pkg install git
    python3 TitleV1.py
    """)
elif op == "4":
    os.system("""
    clear
    pkg install python3
    python3 TitleV1.py
    """)
elif op == "5":
    os.system("""
    clear
    pkg install python2
    python3 TitleV1.py
    """)
elif op == "6":
    os.system("""
    clear
    pkg install python
    python3 TitleV1.py
    """)
elif op == "7":
    os.system("""
    clear
    pkg install wget
    python3 TitleV1.py
    """)
elif op == "8":
    os.system("""
    clear
    pkg install sl
    python3 TitleV1.py
    """)
elif op == "9":
    os.system("""
    clear
    pkg install libaca
    python3 TitleV1.py
    """)
elif op == "10":
    os.system("""
    clear
    pkg install cmatrix
    python3 TitleV1.py
    """)
elif op == "11":
    os.system("""
    clear
    apt update
    apt upgrade
    python3 TitleV1.py
    """)
elif op == "12":
    os.system("""
    clear
    pkg install ruby
    python3 TitleV1.py
    """)
elif op == "13":
    os.system("""
    clear
    pkg install php
    python3 TitleV1.py
    """)
elif op == "14":
    os.system("""
    clear
    pkg install proot
    python3 TitleV1.py
    """)
elif op == "15":
    os.systen("""
    clear
    pkg install black
    python3 TitleV1.py
    """)
elif op == "16":
    os.system("""
    clear
    pkg install bc
    python3 TitleV1.py
    """)
elif op == "17":
    n1 = int(input("Num1: "))
    n2 = int(input("Num2: "))
    somar = n1 + n2
    print("A soma entre {} + {} é de {}".format(n1, n2, somar))
    time.sleep(9)
    os.system("python3 TitleV1.py")
elif op == "18":
    n1 = int(input("Num1: "))
    n2 = int(input("Num2: "))
    produto = n1*n2
    print("O Resultado Entre {} × {} = {}".format(n1, n2, res))
    time.sleep(9)
    os.system("python3 TitleV1.py")
elif op == "19":
    os.system("clear")
    print("""\033[1;36m
    Oque vc Deseja Saber sobre esse Script\033[1;31m
    ===========================l
    1 Para que foi criado      l
    2 Quem Criou               l
    3 Se teve ajudantes        l
    4 Sair                     l
    5 Voltar ao menu           l
    ===========================l
    """)
    op = input(">>>")
    
    if op == "1":
        os.system("clear")
        print("""\033[1;31m
        Bem...
        Este Script foi criado para vc que esta sem comandos para 
        instalar Que vc talvez ñ conheca!!
        """)
        time.sleep(10)
        os.system("python3 TitleV1.py")
    elif op == "2":
        os.system("clear")
        print("O criador deste Script Foi ZoroScripter")
        time.sleep(9)
        os.system("python3 TitleV1.py")
    elif op == "3":
        os.systen("clear")
        print("Ñ teve ajuda de Ninguém!!")
        time.sleep(6)
        os.system("python3 TitleV1.py")
    elif op == "4":
        os.system("clear")
        print("Saindo....")
        time.sleep(5)
        exit()
    elif op == "5":
        os.system("python3 TitleV1.py")
    else:
        os.system("python3 TitleV1.py")
elif op == "20":
    os.system("clear")
    print("Saindo....")
    time.sleep(5)
    exit()
else:
    os.system("python3 TitleV1.py")