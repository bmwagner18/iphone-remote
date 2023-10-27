import pyautogui as pag

def switcher(command:str):
    print(command)
    if command == '/next':
        print('Next channel')
        pag.keyDown('altleft')
        pag.press(['tab', 'tab'])
        pag.keyUp('altleft')
        pag.hotkey('alt','shiftleft','a') # mute all other tabs
        pag.hotkey('alt','shiftleft','n') # unmute this tab
    elif command == '/recent':
        print('Recent channel')
        pag.hotkey('altleft','tab') # alt-tab forwards
        pag.hotkey('alt','shiftleft','a') # mute all other tabs
        pag.hotkey('alt','shiftleft','n') # unmute this tab
    elif command == '/startPIP':
        print('Starting PIP')
        pag.hotkey('altleft','tab') # alt-tab forwards
        pag.hotkey('ctrl', 'shiftleft', ']') # create PIP
        pag.hotkey('altleft','tab') # alt-tab forwards
    elif command == '/stopPIP':
        print('Stopping PIP')
        pag.hotkey('altleft','shiftleft') # alt-tab forwards
        pag.hotkey('ctrl', 'shiftleft', ']') # close PIP
        pag.hotkey('altleft','tab') # alt-tab forwards
    elif command == '/switchPIP':
        print('Switching PIP')
        pag.hotkey('altleft','tab') # alt-tab forwards
        pag.hotkey('ctrl', 'shiftleft', ']') # close PIP
        pag.hotkey('altleft','tab') # alt-tab forwards
        pag.hotkey('ctrl', 'shiftleft', ']') # create PIP
        pag.hotkey('altleft','tab') # alt-tab forwards
        pag.hotkey('alt','shiftleft','a') # mute all other tabs
        pag.hotkey('alt','shiftleft','n') # unmute this tab
    elif command == '/switchaudio':
        print('Switching Audio')
        pag.hotkey('altleft','tab') # alt-tab forwards
        pag.hotkey('alt','shiftleft','a') # mute all other tabs
        pag.hotkey('alt','shiftleft','n') # unmute this tab
        pag.hotkey('altleft','tab') # alt-tab forwards        
    elif command == '/close': return 'QUIT'
    elif command =='/': return ''
    else: print(command)
    return command