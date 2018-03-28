def get_selection():
    old = clip.get()
    serial = clip.serial()
    press('cmd-c', wait=0)
    sel = clip.await_change(after=serial)
    clip.set(old)
    return sel
