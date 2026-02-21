import os, time, sys

pasta_do_programa = os.path.dirname(os.path.abspath(sys.argv[0]))

def limpar():
    os.system('clear')

limpar()
print('POSTNEXT BY NEXUS DEV.')
print('CARREGANDO...')
time.sleep(1.0)
limpar()
print('CARREGAMENTO FINALIZADO🚀')
time.sleep(0.5)

while True:
    limpar()
    print("""
________________________________________
          POSTNEXT V2.0 
      only for arch or based 
________________________________________
[1] developer    | [3] gamer
[2] home office  | [4] social
[5] extras       | [6] optimizations
[7] repositorios | [8] themes
[0] sair
========================================
""")

    try:
        selecione = int(input("escolha a sua opção: "))
        if selecione == 0:
            break
            
        abas_arquivos = {
            1: ".developer.py", 2: ".office.py", 3: ".gamer.py", 
            4: ".social.py", 5: ".extras.py", 6: ".optimize.py", 
            7: ".repositorios.py", 8: ".themes.py"
        }

        if selecione in abas_arquivos:
            nome_arquivo = abas_arquivos[selecione]
            caminho_completo = os.path.join(pasta_do_programa, nome_arquivo)

            if os.path.exists(caminho_completo):
                print(f'Boa escolha! Iniciando {nome_arquivo}...')
                # RODA NA MESMA JANELA
                os.system(f"sudo python {caminho_completo}")
                input("\n✅ Instalação finalizada! Aperte ENTER para voltar ao menu...")
            else:
                print(f"\n❌ ERRO: O arquivo {nome_arquivo} não está nesta pasta!")
                print(f"Procurei em: {caminho_completo}")
                time.sleep(3)
        else:
            print("Opção inválida!")
            time.sleep(1)

    except ValueError:
        print("ERRO: DIGITE APENAS NÚMEROS")
        time.sleep(1)