# import
import subprocess, os, platform, time

#variaveis de sistema
limpar = os.system("clear")
sistema = platform.system()
arquitetura = platform.machine()

# lista de apps
apps_dev = [
    "git",
    "visual-studio-code-bin",
    "zed",
    "github-desktop",
    "vim",
    "neovim",
    "kitty",
    "jetbrains-toolbox",
    "mise",
    "docker",
    "lazydocker",
    "lazygit",
]

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
                                   
 [+] PosNext Developer Mode Installer
 
 [+] Installing Developer Mode Apps...

 [+] sistema: {sistema}
 
 [+] arquitetura: {arquitetura}

 [+] {apps_dev}
 


    """)



def instalar(app):
    subprocess.run(["sudo", "pacman", "-S", "--noconfirm", app])


for app in apps_dev:
    instalar(app)

print(" [+] Developer Mode Apps Installed Successfully!")
