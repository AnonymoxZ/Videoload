# Videoload

**NOTE:** *This is a legacy project; this repository now exists only for archiving purposes. This was my first project, created as a prototype for another download program.*


Desktop app for download MP4 media from YouTube.

Requiriments:
- pytube
- PySimpleGUI

pip installing commands:

Windows:
-  pip install pysimplegui
-  pip install pytube

Linux:
- pip3 install pysimplegui
- pip3 install pytube

# What each file does:
```main.py```: Main file, where call the program.

```baixador_mp4.py```: Where the function download request the MP4 media, and transfer for directory specified. 

```Soft_UI.py```: GUI configurations file, use PySimpleGUI. Integrate download function from ```baixador_mp4.py```

```settings.py```: File with utils functions, like clear screen, and random themes of GUI.

# How to execute:

```py main.py```
