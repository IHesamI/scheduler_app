from kivymd.uix.screen import Screen
from kivymd.uix.pickers import MDDatePicker
from kivymd.app import MDApp
import sqlite3
# TODO 
class EventScreenView(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def on_save(self, instance, value, date_range):
            self.date=value
    def on_cancel(self, instance, value):
        pass
    def show_datepicker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    def save_event(self):
        self.title=self.ids.title.text
        self.describe=self.ids.describe.text
        
        try:
            conn=sqlite3.connect(r'C:\Users\Eniac\Documents\Python\kivy_projects\Calender\Events.db')
            cursor=conn.cursor()
            query='CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY AUTOINCREMENT,title varchar(255),date DATE,describe varchar(255))'
            cursor.execute(query)
            query='INSERT INTO events (title,date,describe) VALUES(?,?,?)'
            cursor.execute(query,(self.title,self.date,self.describe))
            conn.commit()
            print('added successfully')
        except Exception as e:
            print(e.with_traceback())
            
        MDApp.get_running_app().manager_screen.switch_screen('main')


# TODO
class EventManager():
    pass
