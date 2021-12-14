import ui
import os
import console
import Image
import random
import time
from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress



#tela / screen
v = ui.load_view()
x,y=ui.get_screen_size()
v.frame=(0,0,x,y)


#coloca um wallpaper aleatorio na variavel img / puts a random wallpaper on the variable img
imagens = ('img/fundo.png', 'img/fundo1.png', 'img/fundo2.jpeg')
wallpaper = random.choice(imagens)
img = ui.Image.named(wallpaper)


#A imagem aleatorio da variavel img é definida na view da interface de usuario / The random image of the img variable is defined in the user interface view
v['imageview1'].image = img


#posicoes / positions
#botao1 / button1
v['button1'].center = (v.width * 0.5, v.height * 0.5)
v['label3'].center = (v.width * 0.5, v.height * 0.502)
#botao2 / button2
v['button2'].center = (v.width * 0.5, v.height * 0.6)
v['label4'].center = (v.width * 0.5, v.height * 0.601)
#botao3 / button3
v['button3'].center = (v.width * 0.5, v.height * 0.701)
v['label5'].center = (v.width * 0.5, v.height * 0.702)
#botao4 / button4
v['button4'].center = (v.width * 0.5, v.height * 0.801)
v['label6'].center = (v.width * 0.5, v.height * 0.802)

#versao / version
v['label7'].center = (v.width * 0.5, v.height * 0.98)


#view present
v.present(
	'fullscreen',
	hide_title_bar=True,
	title_bar_color='black',
	orientations='portrait'
)



#definicoes dos botoes / button difinitions 
@ui.in_background
def button1(self):
	
	
	link = console.input_alert('Insira uma URL')
	yt = Playlist(link)
	
	
	for link in yt.video_urls:
		
		ys = YouTube(link, on_progress_callback = on_progress)
		
		v['textview1'].text = f'Baixando: {ys.title}\n\n Canal: {ys.author}'
		
		stream = ys.streams.get_highest_resolution()
		stream.download(output_path='downloads/videos playlist', skip_existing=True)
		
		

@ui.in_background
def button2(self):
	
	
	link = console.input_alert('Insira uma URL')
	yt = YouTube(link)
	
	
	v['textview1'].text = f'Baixando: {yt.title}\n\n Canal: {yt.author}'
	
	ys = yt.streams.get_highest_resolution()
	ys.download(output_path='downloads/videos', skip_existing=True)



@ui.in_background
def button3(self):
	
	
	link = console.input_alert('Inira uma URL')
	yt = Playlist(link)
	
	
	for url in yt.video_urls:
		ys = YouTube(url, on_progress_callback = on_progress)
		
		v['textview1'].text = f'Baixando: {ys.title}\n\n Canal: {ys.author}'
		
		z = ys.streams.get_audio_only()
		
		out_file = z.download(output_path='downloads/musicas playlist', skip_existing=True, timeout=1)
		
		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)



@ui.in_background
def button4(self):
	
	
	link = console.input_alert('Insira uma URL')
	yt = YouTube(link)
	
	
	v['textview1'].text = f'Baixando: {yt.title}\n\n Canal: {yt.author}'
	
	ys = yt.streams.get_audio_only()
	
	out_file = ys.download(output_path='downloads/musicas', skip_existing=True)
	
	base, ext = os.path.splitext(out_file)
	new_file = base + '.mp3'
	os.rename(out_file, new_file)


#acoes dos botoes / button actions
v['button1'].action = button1
v['button2'].action = button2
v['button3'].action = button3
v['button4'].action = button4
