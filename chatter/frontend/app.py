import clutter

script = clutter.Script()

def parseKeyPress(self, event):
    if event.keyval == clutter.keysyms.Escape:
        clutter.main_quit()
    elif event.keyval == clutter.keysyms.F11:
        stage.set_fullscreen(not stage.get_fullscreen())

def start():
    script.load_from_file("templates/signin.template")
    userinput = script.get_object("signin-user")
    userinput.set_editable(True)
    userinput.set_reactive(True)
    userinput.set_size(20,200)
    stage = script.get_object("main-stage")
    stage.connect('key-press-event', parseKeyPress)
    stage.show_all()
    clutter.main()

if __name__=="__main__":
    start()


