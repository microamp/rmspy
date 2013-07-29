# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('rmspy')

from rmspy_lib import Window
from rmspy.AboutRmspyDialog import AboutRmspyDialog
from rmspy.PreferencesRmspyDialog import PreferencesRmspyDialog

# See rmspy_lib.Window.py for more details about how this class works
class RmspyWindow(Window):
    __gtype_name__ = "RmspyWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(RmspyWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutRmspyDialog
        self.PreferencesDialog = PreferencesRmspyDialog

    def on_one_click_released(self, builder):
        """Remove spyware"""
        print("'1-Click' released!")
