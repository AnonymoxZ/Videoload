# Version Videoload 0.1.4
from os import system
import PySimpleGUI as tela
import baixador_mp4 as dwd
import settings as sett

# configuraçoes de tela
titulo = 'Videoload'
rodar = True
tela.theme(f'{sett.tema_aleatorio}')

# Interface principal
definiçoes_tela = [[tela.Text('Insira o link para download:')],
                  [tela.InputText(),tela.Button('Baixar')],
                  [tela.Button('Encerrar'),tela.Text('Click aqui para sair')]]

janela = tela.Window(titulo, definiçoes_tela)
# loop da janela
while rodar:
    event, values = janela.read()
    if event == tela.WIN_CLOSED or event == "Encerrar":
        sett.NotaFim()
        rodar = False
        quit()
        exit()
    elif event == 'Baixar':
        system('cls')
        # Baixando mp4 com sucesso
        if values[0] == '':
            sett.Tutorial()
        else:
            link = values[0]
            dwd.BaixarMP4(link)
   
janela.close()
