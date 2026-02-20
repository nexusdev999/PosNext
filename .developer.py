# import
import subprocess, os, time

clear = os.system("clear")

print("""

______________________________________________

LISTA DE APPS PARA DOWNLOAD V1
-cachyos

______________________________________________

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

[20]xamp                | [21]netbeans

[22]sublime text        | [23]laucher studio
      
==============================================
""")

select = int(input("Digite o numero da opção escolhida: "))
print("boa escolha para seu workspace")

if select == 1:
    os.system("clear")
    os.system("curl -fsSL https://linux.toys/install.sh | bash")
    os.system("clear")
    os.system("python .developer.py")
elif select == 2:
    os.system("clear")
    os.system("sudo pacman -S --needed base-devel git nodejs npm python python-pip gcc gdb cmake clang valgrind")
    os.system("clear")
    os.system("python .developer.py")
elif select == 3:
    os.system("clear")
    os.system("sudo pacman -S github-desktop")
    os.system("clear")
    os.system("python .developer.py")
elif select == 4:
    os.system("clear")
    os.system("sudo pacman -S code")
    os.system("clear")
    os.system("python .developer.py")
elif select == 5:
    os.system("clear")
    os.system("sudo pacman -S kitty")
    os.system("clear")
    os.system("python .developer.py")
elif select == 6:
    os.system("clear")
    os.system("sudo pacman -S geany")
    os.system("clear")
    os.system("python .developer.py")
elif select == 7:
    os.system("clear")
    os.system("sudo pacman -S ghidra")
    os.system("clear")
    os.system("python .developer.py")
elif select == 8:
    os.system("clear")
    os.system("sudo pacman -S devtools")
    os.system("clear")
    os.system("python .developer.py")
elif select == 9:
    os.system("clear")
    os.system("sudo pacman -S qtcreator")
    os.system("clear")
    os.system("python .developer.py")
elif select == 10:
    os.system("clear")
    os.system('curl -f https://zed.dev/install.sh | sh')
    os.system("clear")
    os.system("python .developer.py")
elif select == 11:
    os.system("clear")
    os.system("sudo pacman -S postman-bin")
    os.system("clear")
    os.system("python .developer.py")
elif select == 12:
    os.system("clear")
    os.system("sudo pacman -S unityhub")
    os.system("clear")
    os.system("python .developer.py")
elif select == 13:
    os.system("clear")
    os.system("yay -S gamemaker2-bin")
    os.system("clear")
    os.system("python .developer.py")
elif select == 14:
    os.system("clear")
    os.system("sudo pacman -S meld")
    os.system("clear")
    os.system("python .developer.py")
elif select == 15:
    os.system("clear")
    os.system("sudo pacman -S docker")
    os.system("clear")
    os.system("python .developer.py")
elif select == 16:
    os.system("clear")
    os.system("sudo pacman -S ghostwriter")
    os.system("yay -S typora")
    os.system("clear")
    os.system("python .developer.py")
elif select == 17:
    os.system("clear")
    os.system("sudo pacman -S --needed ghostwriter")
    os.system("yay -S --needed typora")
    os.system("clear")
    os.system("python .developer.py")
elif select == 18:
    os.system("clear")
    os.system('bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"')
    os.system("clear")
    os.system("python .developer.py")
elif select == 19:
    os.system("clear")
    os.system("sudo pacman -S warp")
    os.system("clear")
    os.system("python .developer.py")
elif select == 20:
    os.system("clear")
    os.system("sudo pacman -S xampp")
    os.system("clear")
    os.system("python .developer")
elif select == 21:
    os.system("clear")
    os.system("sudo pacman -S netbeans")
    os.system("clear")
    os.system("python .developer.py")
elif select == 22:
    os.system("clear")
    os.system("sudo pacman -S sublime-text-4")
    os.system("clear")
    os.system("python .developer.py")
elif select == 23:
    os.system("clear")
    os.system("flatpak install flathub fr.arnaudmichel.launcherstudio")
    os.system("clear")
    os.system("python .developer.py")
else:
    os.system("clear")
    print("não temos essa opção")
    time.sleep(2.0)
    os.system("clear")
    os.system("python .developer")
    os.system("para sair e só fechar o terminal")



