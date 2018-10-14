from talon.engine import engine

def listener(topic, m):
    if topic == 'cmd' and m['cmd']['cmd'] == 'g.load' and m['success'] == True:
        print('[grammar reloaded]')
    if topic == 'cmd':
        return
    else:
        print(topic, m)

engine.register('', listener)
