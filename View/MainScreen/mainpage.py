from kivymd.uix.screen import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.factory import Factory
from kivy.properties import StringProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.widget import Widget
from kivymd.uix.list import OneLineListItem
import sqlite3

class Event(OneLineListItem):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(args)!=0:
            # self.ids.title.text=  args[0]
            # self.ids.date.text=    args[1]
            # self.ids.describe.text=args[2]
            
            print()


class MainScreenView(Screen):
    def __init__(self):
        super().__init__()
        Factory.register('Event',cls=Event) 
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
        for event in self.events:
            print(event[1],event[2],event[3])
            self.ids.list.add_widget(Factory.Event(text=f'[size=32][b]{event[1]}[/b][/size] {event[2]}'))


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