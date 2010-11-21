#!/usr/bin/env python
import gtk
window = gtk.Window()
window.connect('delete-event', gtk.main_quit)
window.show_all()
gtk.main()
