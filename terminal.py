from talon.voice import Word, Key, Context, Str
import string

terminals = ('com.apple.Terminal', 'com.googlecode.iterm2')
ctx = Context('terminal', func=lambda app, win: any(
    t in app.bundle for t in terminals))

keymap = {
    'cd': 'cd ',
    'cd back': 'cd -; ls -a;\n',
    'cd develop': 'cd ~/develop; ls -a;\n',
    'cd home': 'cd ~; ls -a;\n',
    'cd parent': 'cd ..; ls -a;\n',
    'run ellis': 'ls -a;\n',
    'run make (durr | dear)': 'mkdir ',
    'snipple': [Key('ctrl-a'), Key('ctrl-k')],
    'trough': [Key('ctrl-w')],

    'run git': 'git ',
    'run git clone': 'git clone ',
    'run git checkout': 'git checkout ',
    'run git diff': 'git diff \n',
    'run git initialize': 'git init \n',
    'run git commit': 'git commit ',
    'run git log': 'git log \n',
    'run git push': 'git push ',
    'run git push origin': 'git push origin ',
    'run git push origin master': 'git push origin master ',
    'run git pull': 'git pull ',
    'run git reset': 'git reset ',
    'run git status': 'git status ',
    'run git tag': 'git tag ',
    'run git add': 'git add ',
    'run git add dot': 'git add .\n',
    'run git amend': 'git add .; git commit --amend --no-edit\n',

    'tools oedipus': [Key('ctrl-x'), Key('ctrl-e')],
    'open sublime': Str('subl .\n'),
    'open adam': Str('atom .\n'),
}

ctx.keymap(keymap)
