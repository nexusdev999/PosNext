import os, time

limp = os.system("clear")

#carregamento animation

print('post next by nexus dev.')
time.sleep(2.0)
print('loading.')
time.sleep(2.0)
os.system('clear')
print('post next by nexus dev..')
print('loading..')
time.sleep(2.0)
os.system('clear')
print('post next by nexus dev...')
print('loading...')
time.sleep(2.0)
os.system('clear')
print('CARREGAMENTO FINALIZADO🚀')
time.sleep(2.0)
os.system('clear')

#tela inicial
print("""
________________________________________

          POSTNEXT V2.0 
      only for arch or based 
________________________________________

[1] developer    | [3] gamer

[2] home office  | [4] social

[5] extras       | [6] optimizations

[7] repositorios | [8] themes

========================================
""")

selecione = int(input("escolha a sua opção: "))
os.system('clear')
print('boa escolha estamos carregando pra você')

if selecione == 1:
    os.system('clear')
    print('carregando aplicativos')
    time.sleep(2.0)
    os.system('clear')
    os.system('python .developer.py')
elif selecione == 2:
    os.system('clear')
    print('carregando aplicativos')
    time.sleep(2.0)
    os.system('clear')
    os.system('python .office.py')
else:
    os.system('clear')
    print('não temos essa opção')