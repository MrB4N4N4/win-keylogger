import pythoncom, pyHook

FILE_NAME = "result.txt"

def CombinationKeys(key):
    if key in ["Lshift", "Rshift"]:
        return True
    if key in ["Space", "Return", "Back", "Tab"]:
        return "\n"

def OnKeyboardEvent(event):
    # functional keys to filter. Available to add other key.
    func_keys = ["Space", "Return", "Back", "Tab", "Lshift", "Lcontrol", "Lmenu"]
    try:
        key = str(event.Key)
        if key in func_keys:
            # restart point

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