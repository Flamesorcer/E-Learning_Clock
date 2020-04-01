import PySimpleGUI as sg
import datetime
import webbrowser
import playsound

sg.theme('DarkBrown1')
#Classes list goes Class name, beginning hour, beginning minute, end hour, end minute, zoom link, other link
classes = [ ["Engineering", 8, 30, 9, 21, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["Passing to Math", 9, 21, 9, 26, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["Math", 9, 26, 10, 13, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["Passing to P.E.", 10, 13, 10, 18, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["P.E.", 10, 18, 11, 5, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["Passing to Physics/Lunch", 10, 13 , 11, 37, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["Physics", 11, 37, 12, 49, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["Passing to Comp Sci.", 12, 49, 12, 54, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["Comp Sci.", 12, 54 , 13, 41, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["Passing to Ela", 13, 41 , 13, 46, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["Ela", 13, 46 , 14, 33, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["Passing to Chinese", 14, 33, 14, 38, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["Chinese", 14, 38, 15, 25, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"],
            ["Freedom", 15, 25, 8, 30, "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA", "https://www.youtube.com/channel/UC6nSFpj9HTCZ5t-N3Rm3-HA"]
]

layout = [  [sg.Text('None', size=(21, 1), justification='center', key='_Class_', font=(30))],
            [sg.Text('8:30 – 9:21', size=(29, 1), justification='center', key='Schedule')],
            [sg.Text('', size=(15, 1), font=('Helvetica', 20), justification='center', key='_Time_')],
            [sg.Text('', size=(15, 1), font=('Helvetica', 20), justification='center', key='time_left')],
            [sg.T(' ' * 15), sg.Button(button_text='Zoom', key = "Zoom"), sg.Button(button_text='Link', key = "Link")]]
count = -1
window = sg.Window('E-Learning', layout)
while True:          
    #displaying time                       
    event, values = window.read(timeout=1000)
    time1 = datetime.datetime.now()
    hour = time1.hour
    minute = time1.minute
    sec = time1.second
    time = hour*60 + minute
    allSeconds = hour*3600 + minute * 60 + sec
    window['_Time_'].update('{:02d}:{:02d}:{:02d}'.format(hour, minute, sec))
    left = 0
    
    #displaying the class and period, and setting links
    if event in (None, 'Quit'):             
        break
    for i in range (0, len(classes)):
        if (time >= (classes[i][1]*60 + classes[i][2]) and time < (classes[i][3]*60 + classes[i][4])):
            window['_Class_'].update(classes[i][0])
            window["Schedule"].update("{}:{:02d} – {}:{:02d}".format(classes[i][1], classes[i][2], classes[i][3], classes[i][4]))
            left = (classes[i][3]*60 + classes[i][4])*60 - allSeconds
            zoom, link = classes[i][5], classes[i][6]

            if (time == classes[i][1]*60 + classes[i][2] and count <= 0):
                playsound.playsound("alert.mp3")
                count = 100
            break

    window["time_left"].update('{:02d}:{:02d}'.format(int(left/60), int(left%60)))
    
    
    count -= 1
    #link events
    if event in ("Zoom"):
        webbrowser.open_new_tab(zoom)
    if event in ("Link"):
        webbrowser.open_new_tab(link)
    
window.close()