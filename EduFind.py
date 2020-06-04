import wikipedia
import PySimpleGUI as sg
import wolframalpha


client = wolframalpha.Client('AWJVTA-U9A7QXPGV8') #getting client for Wolfram|Alpha API

sg.theme('LightGreen2')	# Add a touch of color

# All the stuff inside the window.

layout = [[sg.Text('Welcome to EduFind!')],
				 [sg.Text('Enter a command'), sg.InputText()], 
		         [sg.Button('Ok'), sg.Button('Cancel')] ]



window = sg.Window('EduFind- Your Educational Digital Assistant', layout) #Create window object

# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	if event in (None, 'Cancel'):
		break
	try:
		wiki_res = wikipedia.summary(values[0], sentences=2)
		wolfram_res = next(client.query(values[0]).results).text
		sg.Popup(wolfram_res, wiki_res)
	except wikipedia.exceptions.DisambiguationError:
		wolfram_res = next(client.query(values[0]).results).text
		sg.Popup(wolfram_res)
	except wikipedia.exceptions.PageError:
		wolfram_res = next(client.query(values[0]).results).text
		sg.Popup(wolfram_res)
	except:
		wiki_res = wikipedia.summary(values[0], sentences=2)
		sg.Popup(wiki_res)


window.close() #Close the window application
