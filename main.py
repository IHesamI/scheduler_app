from pickle import NONE
from kivymd.app import MDApp
from View.ManagerScreen.manager import ManagerScreen
from kivymd.icon_definitions import md_icons
class Calender(MDApp):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.manager_screen=ManagerScreen()
    def build(self) -> ManagerScreen:
        self.manager_screen.add_widget(self.manager_screen.create_screen('main'))
        return self.manager_screen

    
if __name__ == '__main__':
    Calender().run()
    
