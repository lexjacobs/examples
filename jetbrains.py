# from talon.voice import Context, Key
#
# ides = ['com.jetbrains.PhpStorm', 'com.jetbrains.intellij']
# ctx = Context('phpstorm', func=lambda app, win: any(
#     i in app.bundle for i in ides))
#
# keymap = {
#     'comment declaration': ['/**', Key('space')],
#     'comment block': ['/**', Key('enter')],
#     # annotation command
#
#     '(next tab | goneck)': Key('cmd-shift-['),
#     '(last tab | gopreev)': Key('cmd-shift-]'),
#     'last file': Key('ctrl-tab'),
#
#     'jolt': Key('cmd-d'),
#     'comply': Key('tab'),
#     'import class': Key('alt-enter enter'),
#     'quickfix': Key('alt-enter'),
#     'go class': Key('cmd-o'),
#     'go file': Key('cmd-shift-o'),
#     '(go implement | go definition)': Key('cmd-b'),
#     'preev method': Key('ctrl-up'),
#     'neck method': Key('ctrl-down'),
#     'refactor': Key('shift-f6'),
#     'generate': Key('cmd-n'),
#     'recent': Key('cmd-e'),
#     'trundle': Key('cmd-/'),
#     '(fix imports | remove unused imports)': Key('ctrl-alt-o'),
#     'complete [statement]': Key('cmd-shift-enter'),
# }
#
# ctx.keymap(keymap)
