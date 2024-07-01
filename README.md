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

Como executar: 

No arquivo ```baixador_mp4.py``` onde é definido o diretorio para saída de download, é nescessário alterar para seu próprio caminho de diretório de sua maquina, segundo o padrão de seu sistema operacional.
A execução por definição ordenada é instruída ser feita pelo arquivo principal, como: ```py main.py```.
O programa possuí duas telas, uma do próprio prompt terminal onde serão descritas saídas de interação, e a principal GUI.
Os downloads são realizados um por vez, e por automatização são transferidos para o diretório específicado no caminho definido em sua própria máquina.
