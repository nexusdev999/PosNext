# import
import subprocess, os, platform, time

#variaveis de sistema
limpar = os.system("clear")
sistema = platform.system()
arquitetura = platform.machine()

#lista de progamas
lista_gamer = ["steam", "discord", "vlc", "wine-cachyos", "wine-cachyos-opt", "wine-staging", "wine-gecko", "wine-mono", "winetricks", "govelay", "lutris", "heroic-games-laucher-bin", "protonup", "protonup-qt", "protontricks", "prismlaucher"]

print("carregando codigo aguarde...")
time.sleep(2.0)
print("    atenção!!!")
time.sleep(1.0)
print("SÓ FUNCIONA EM CACHYOS FDP")
time.sleep(1.0)

print(f"""

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
                                   
 [+] PosNext Gamer Mode Installer
 
 [+] Installing Gamer Mode Apps...

 [+] sistema: {sistema}
 
 [+] arquitetura: {arquitetura}

 [+] {lista_gamer}
 


    """)


def instalar_apps(app):
 subprocess.run(["sudo", "pacman", "-S", "--noconfirm", app])

for app in lista_gamer:
    instalar_apps(app)
    
print(" [+] Gamer Mode Apps Installed Successfully!")

