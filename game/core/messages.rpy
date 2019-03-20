# in-game messages and logs
init python:
    class Messages(object):

        def __init__(self):
            self.messages = []
            # max number of messages to show
            self.num_to_show = 10

        def show(self, txt):
            '''Adds message to the list and shows it'''
            self.messages.append(txt)
            # hides and shows messages screen (reseting screen's timer)
            if config.developer:
                renpy.hide_screen('messages')
                renpy.show_screen('messages')


    msgs = Messages()
