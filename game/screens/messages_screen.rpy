# screen to show in-game messages (similar to notify)
transform _msg_transform:
    # These control the position.
    xalign .97 yalign .015

    # These control the actions on show and hide.
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


screen messages():
    zorder 99
    # show up to 5 last messages
    frame:
        background '#2328'
        at _msg_transform
        vbox:
            for txt in msgs.messages[-min(len(msgs.messages), msgs.num_to_show):]:
                text txt #at _msg_transform
    # hide this screen after a short time
    timer 3.25 action Hide('messages')
