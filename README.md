# Videoload
DeskApp para baixar mídia MP4 do YouTube

Requisitos:
- pytube
- PySimpleGUI

pip instalaçoes:

Windows:
-  pip install pysimplegui
-  pip install pytube

Linux:
- pip3 install pysimplegui
- pip3 install pytube

# Oque cada arquivo faz:
```main.py```: É o arquivo principal, onde chamamos a função de execução que integra a API **pytube** e a GUI.

```baixador_mp4.py```: Esse é o arquivo backend, que faz uso da API pytube para requisição de download de mídia MP4 do YouTube, que além do funcionamento principal, faz também a transferência automatizada do arquivo baixado para um diretorio específicado.

```Soft_UI.py```: Arquivo de definição da interface gráfica.
Utiliza a biblioteca PySimpleGUI.

```settings.py```: Arquivo de configurações de interfaces Shell e GUI. Possui um array composto por todos o fundos background da GUI principal, onde o mesmo faz seleção aleatória do tema de fundo,l, como também exporta notas de interação para interface terminal.

# Como executar: 

No arquivo ```baixador_mp4.py``` onde é definido o diretorio para saída de download, é nescessário alterar para seu próprio caminho de diretório de sua maquina, segundo o padrão de seu sistema operacional.
A execução por definição ordenada é instruída ser feita pelo arquivo principal, como: ```py main.py```.
O programa possuí duas telas, uma do próprio prompt terminal onde serão descritas saídas de interação, e a principal GUI.
Os downloads são realizados um por vez, e por automatização são transferidos para o diretório específicado no caminho definido em sua própria máquina.
