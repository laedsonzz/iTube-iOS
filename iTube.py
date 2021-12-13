import ui
from pytube import YouTube
from pytube import Playlist
import console
from pytube.cli import on_progress
import Image



#tamanho da tela
v = ui.load_view()
x,y=ui.get_screen_size()
v.frame=(0,0,x,y)
img = ui.Image.named('fundo1.png')
imagem1 = v['imageview1']
imagem1.image = img


#ajustes posições
v['button1'].center = (v.width * 0.5, v.height * 0.5)
v['label3'].center = (v.width * 0.5, v.height * 0.501)
v['label4'].center = (v.width * 0.5, v.height * 0.98)

#delegate view
v.present(
	'fullscreen',
	hide_title_bar=True,
	title_bar_color='#1a1a1a',
	orientations='portrait'
)



#função
@ui.in_background
def bot1(self):
	
	link = console.input_alert('Digite uma URL')
	yt = Playlist(link)
	
	for link in yt.video_urls:
		ys = YouTube(link)
		v['textview1'].text = f'Baixando: {ys.title}'
		stream = ys.streams.get_highest_resolution()
		stream.download()
	

def teste(self):
	link = console.input_alert('teste')
	v['textview1'].text = link
	v['label1'].center

	
v['button1'].action = bot1
