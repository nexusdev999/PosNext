# import
import subprocess

print("""


    PosNext Developer Mode Installer
    Installing Developer Mode Apps...



    """)
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


def instalar(app):
    subprocess.run(["sudo", "pacman", "-S", "--noconfirm", app])


for app in apps_dev:
    instalar(app)

    print("Developer Mode Apps Installed Successfully!")
