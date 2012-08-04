# -*- coding: utf-8 -*-
import os
from gi.repository import Gtk


class UILoader:
    instance = None
    
    UI_COUNT = 5

    (UI_MAINWINDOW,
     UI_INTROSPECTION,
     UI_BUSWATCH,
     UI_EXECUTEDIALOG,
     UI_ADDCONNECTIONDIALOG
    ) = range(UI_COUNT)

    # {ui_id: ((files,...), root widget)}
    _ui_map = {UI_MAINWINDOW           : (('mainwindow.ui',), 
                                          'appwindow1'),
               UI_INTROSPECTION        : (('introspection.ui',),
                                          'box_introspectview'),
               UI_BUSWATCH             : (('buswatch.ui',),
                                          'paned_buswatch'),
               UI_EXECUTEDIALOG        : (('executedialog.ui',),
                                          'executedialog1'),
               UI_ADDCONNECTIONDIALOG  : (('addconnectiondialog.ui',),
                                          'add_connection_dialog1')
              }

    def __init__(self, ui):
        ui_info = self._ui_map[ui]
        self.ui = Gtk.Builder()

        #load ui files
        for file in ui_info[0]:
            self.ui.add_from_file(self.ui_dir + '/' + file)

        self.root_widget_name = ui_info[1]

    def get_widget(self, name):
        return self.ui.get_object(name)

    def get_root_widget(self):
        return self.get_widget(self.root_widget_name)

    def connect_signals(self, obj_or_map):
        self.ui.connect_signals(obj_or_map)

    @property
    def ui_dir(self):
        try:
            ui_dir = os.environ['DFEET_DATA_PATH']
        except:
            ui_dir = "../ui"
            
        return ui_dir 

