# import
import subprocess, os

clear = os.system("clear")

print("""

--------------------------------

LISTA DE APPS PARA DOWNLOAD V1
-cachyos

---------------------------------

            [1]linux toys

[2]base e depedencias   | [7]Ghidra

[3]github desktop       | [8]dev toolbox

[4]visual studio code   | [9]qt creator
|open souce

[5]kitty                | [10]zed

[6]geany                | [11]postman

[12]unity hub           | [13]gamemaker2

[14]Meld                | [15]docker
 
[16]Typora/Ghostwriter  | [17]Typora/Ghostwriter

[18]oh my bash          | [19]Warp


""")

select = int(input("Digite o numero da opção escolhida: "))
print("boa escolha para seu workspace")

if select == 1:
    os.system("clear")
    os.system("curl -fsSL https://linux.toys/install.sh | bash")
    os.system("clear")
    os.system("python developer_mode_install.py")
else:
    os.system("clear")
    print("não temos essa opção")
    os.system("python developer_mode_install.py")
    os.system("para sair e só fechar o terminal")



