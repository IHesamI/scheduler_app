from kivymd.uix.screen import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers.datepicker import MDDatePicker
from kivy.metrics import dp
import sqlite3
# from kivymd.uix.pickers.

class MainScreenView(Screen):
    def __init__(self):
        super().__init__()
        items_title=['Settings','Sync Now','Search']
        menu_items=[
            {'text':f'{item}',
             'viewclass':'OneLineListItem',
             'height':dp(40),
             'on_release':lambda x:x,
            }for item in items_title
            ]
        self.menu=MDDropdownMenu(
            caller=self.ids.toolbar,
            items=menu_items,
            width_mult=2,
            # pos_hint={'x':1,'y':1}
            position="bottom",
        )
        self.events=self.get_events()
        print([event for event in self.events])

    def get_events(self):
        path=r'C:\Users\Eniac\Documents\Python\kivy_projects\Calender\Events.db'
        try:
            connect=sqlite3.connect(path)
            cursor=connect.cursor()
            query='SELECT * \
            FROM events '
            events=cursor.execute(query)
            connect.commit()
            return events
        except Exception as e :
            print(e.with_traceback())
        

    def menu_callback(self):
        pass