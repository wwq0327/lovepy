#!/usr/bin/python

import vte, gtk

window = gtk.Window()
window.set_default_size(480, 320)
window.set_title('Inception')
window.connect('destroy', lambda *w: gtk.main_quit())

sw = gtk.ScrolledWindow()
sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

term = vte.Terminal()
term.set_emulation('xterm')

sw.add(term)
window.add(sw)
window.show_all()

term.fork_command()
clipboard = gtk.Clipboard()

for i in range(1000):
   clipboard.set_text('echo $SHLVL \n bash \n')
   term.paste_clipboard()

gtk.main()
