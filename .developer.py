import subprocess, os, time

# Limpa a tela ao iniciar
os.system("clear")

# Listas de programas (nomes corrigidos para pacotes Arch/AUR)
aur_list = ["ghidra", "code", "qtcreator", "kitty", "zed", "geany", "meld", "docker", "netbeans", "ghostwriter"]
helpers_list = ["github-desktop-bin", "devtoolbox-bin", "postman-bin", "unityhub", "gamemaker-beta-bin", "typora", "oh-my-bash-git", "warp-terminal", "xampp", "sublime-text-4"]

def reiniciar():
    os.system("python .developer.py")

print("""
______________________________________________

██████╗  ██████╗ ███████╗████████╗ 
██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝ 
██████╔╝██║   ██║███████╗   ██║    
██╔═══╝ ██║   ██║╚════██║   ██║    
██║     ╚██████╔╝███████║   ██║    
╚═╝      ╚═════╝ ╚══════╝   ╚═╝    
                                   
███╗   ██╗███████╗██╗  ██╗████████╗
████╗  ██║██╔════╝╚██╗██╔╝╚══██╔══╝
██╔██╗ ██║█████╗   ╚███╔╝    ██║   
██║╚██╗██║██╔══╝   ██╔██╗    ██║   
██║ ╚████║███████╗██╔╝ ██╗   ██║   
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ╚═╝   
                                   
 [+] PosNext developer Installer
 
 [+] Installing developer Apps...

 [+] sistema: {sistema}
 
 [+] arquitetura: {arquitetura}

______________________________________________
            [1] linux toys
[2] base e depedencias   | [7] Ghidra
[3] github desktop       | [8] dev toolbox
[4] visual studio code   | [9] qt creator
[5] kitty                | [10] zed
[6] geany                | [11] postman
[12] unity hub           | [13] gamemaker2
[14] Meld                | [15] docker
[16] Typora              | [17] Ghostwriter
[18] oh my bash          | [19] Warp
[20] xampp               | [21] netbeans
[22] sublime text        | [23] launcher studio
==============================================
""")

try:
    select = int(input("Digite o numero da opção escolhida: "))
except ValueError:
    reiniciar()

print("Boa escolha para seu workspace!")

# Dicionário que mapeia o número ao nome real do pacote
apps = {
    3: "github-desktop-bin", 4: "code", 5: "kitty", 6: "geany",
    7: "ghidra", 8: "dev-toolbox", 9: "qtcreator", 10: "zed",
    11: "postman-bin", 12: "unityhub", 13: "gamemaker-bin", 14: "meld",
    15: "docker", 16: "typora", 17: "ghostwriter", 19: "warp-terminal",
    20: "xampp", 21: "netbeans", 22: "sublime-text-4"
}

if select == 1:
    os.system("curl -fsSL https://linux.toys/install.sh | bash")
    reiniciar()

elif select == 2:
    os.system("sudo pacman -Syu --needed base-devel git curl wget zenity python python-requests python-gobject gtk3 vte3 jdk-openjdk pkg-config libx11 libxkbcommon wayland fontconfig freetype2 alsa-lib libsecret nspr nss unzip libxtst libxss mesa libglvnd")
    reiniciar()

elif select == 18:
    os.system('bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"')
    reiniciar()

elif select == 23:
    os.system("flatpak install flathub fr.arnaudmichel.launcherstudio")
    reiniciar()

elif select in apps:
    os.system("clear")
    # No CachyOS, usamos yay para cobrir Repos Oficiais e AUR de uma vez
    subprocess.run(["yay", "-S", "--needed", "--noconfirm", apps[select]])
    reiniciar()

else:
    print("Não temos essa opção")
    time.sleep(2)
    reiniciar()

    




