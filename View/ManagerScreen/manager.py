from kivy.uix.screenmanager import ScreenManager,NoTransition
from kivymd.app import MDApp
import os
from View.screens import screens
from kivy.clock import Clock
class ManagerScreen(ScreenManager):
    _screen_names=[]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app=MDApp.get_running_app()
        self.transition=NoTransition()
        
    def refresh(self,screen_name):
        self._screen_names.remove(screen_name)
        self.remove_widget(self.get_screen(screen_name))
        self.switch_screen(screen_name)        
        print(self._get_screen_names())

    def create_screen(self,name_screen,*args):
        if name_screen not in self._screen_names:
            self._screen_names.append(name_screen)
            exec(f"import View.{screens[name_screen]}")
            self.app.load_all_kv_files(os.path.join(self.app.directory, "View", screens[name_screen].split(".")[0]))            
            view = eval(f'View.{screens[name_screen]}.{screens[name_screen].split(".")[0]}View()')
            view.name = name_screen
            return view

    def switch_screen(self, screen_name: str) -> None:
        def switch_screen(*args):
            if screen_name not in self._screen_names:
                screen = self.create_screen(screen_name,*args)
                self.add_screen(screen)
            self.current = screen_name

        if screen_name not in self._screen_names:
            Clock.schedule_once(switch_screen)
        else:
            self.current = screen_name
    def add_screen(self, view) -> None:
        self.add_widget(view)
        