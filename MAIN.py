import tkinter as tk
from PIL import Image
import requests
import json
import geocoder
import credenciais_google
import googlemaps
from contextlib import suppress
import time



HEIGHT = 500
WIDTH = 600
r = ''
j= ''
ROW = 0
COLUMN = 0	
pesquisa = ''

def organizadora(resultados,c):
	
	gmaps = googlemaps.Client(key=credenciais_google.google_api_token)
	
	#print(resultados)
	
	place_id = ''
	name = ''
	address = ''
	number = ''
	website = ''
	rating = ''


	#sistemas pra varer arquivo jason solicitado pela api
	
	with suppress(Exception):
		place_id = resultados['results'][c]['place_id']
		name = resultados['results'][c]['name']
		address = resultados['results'][c]['vicinity']
		number1 = gmaps.place(place_id=place_id, fields=['formatted_phone_number'])
		number = number1['result']['formatted_phone_number']
		website1 = gmaps.place(place_id=place_id, fields=['website'])
		website = website['result']['website']
		rating = str(resultados['results'][c]['rating'])
		
		#print('=' * 60)
		#print("resultado nº", c)
		#print('Name: ' + name)
		#print('Address: ' + address)
		#print('Phone Number: ', number['result']['formatted_phone_number'])
		#print('Website: ', website['result']['website'])
		#print('Rating: ' + rating)
		#print('=' * 60)
		return str(c)+" "+str(name)+" "+str(address)+" "+str(number)+" "+str(website)+" "+str(rating)

def search(entry,options):
	i = 0
	c = -1
	#keyword
	palavrachave = entry
	print(palavrachave)

	#localização
	g = geocoder.ip('me')
	localizacao = "-12.9704,-38.5124" #str(g.latlng).replace('[','').replace(']','').strip().replace(' ','') #localização atual
	print(localizacao)

	#Raio
	raio = (options+"000").strip()
	print(raio)
	#testes
	#print(palavrachave+' / '+localizacao+' / '+raio)
	
	#autenticação
	gmaps = googlemaps.Client(key=credenciais_google.google_api_token)

	
	#request dados da pesquisa
	resultados = gmaps.places_nearby(location=localizacao, radius=raio, open_now=False, keyword=palavrachave)
	print(resultados)
	
	#retorno
	for c in range(0, 19):
		c += 1
		i += 1
		pesquisa = organizadora(resultados,c)

def blocks(row, column, c):
	block = tk.label(frame_2, relwidth=0.25, relheight=0.20)
	block.grid(row=row, column=column)
	label['text'] = pesquisa[]




root = tk.Tk()	


CheckVar1 = int

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
		
img = tk.PhotoImage(file='arriba.png')
logo_label = tk.Label(root, image=img)
logo_label.place(relwidth=1, relheight=1)

check = tk.Checkbutton(root, text="Usar localização atual", variable = CheckVar1,\
                onvalue = 1, offvalue = 0)

check.place(relx=0.22, rely=0.276, relwidth=0.22, relheight=0.050, anchor='n')

frame_1 = tk.Frame(root, bg='white', bd=5)
frame_1.place(relx=0.5, rely=0.20, relwidth=0.8, relheight=0.075, anchor='n')

button = tk.Button(frame_1, text='Pesquisar', command=lambda: search(entry.get(),options.get()))
button.place(relx=0.795, relheight=1, relwidth=0.2)

entry = tk.Entry(frame_1, bg='#eeeeee', font=12)
entry.place(relheight=1, relwidth=0.700)

options = tk.Spinbox(frame_1, from_=5, to=20)
options.place(relx=0.710, relheight=1, relwidth=0.080)

frame_2 = tk.Frame(root, bg='white', bd=5)
frame_2.place(relx=0.5, rely=0.34, relwidth=0.8, relheight=0.6, anchor='n')

label = tk.Label(frame_2, text="Results Here!", bg='white')
label.place(relheight=1, relwidth=1) 

for c in pesquisa:
	if ROW > 2:
		COLUMN += 1
		ROW = 0
	elif ROW == 2 and COLUMN == 2:
		pass
	else:
		ROW += 1
	blocks(ROW, COLUMN, c)	




root.mainloop()