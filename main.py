from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.network.urlrequest import UrlRequest
import requests
#import re
from kivy.uix.textinput import TextInput
from kivymd.uix.label import MDLabel
# 
KV = '''
MDScreen:
    # 
    MDRaisedButton:
        id: searchbutton
        text: "Search"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}  
        on_release: app.predict()
    # 
    MDTextField:
        id: verseview
        pos_hint: {'center_x': .5, 'center_y': .6}
        size_hint_x: None
        width: "200dp"
        hint_text: "Eg: John 3 16"
        mode: "line"
        required: True
        helper_text: "You don't have to use colon"
        helper_text_mode: "on_error"
    
    MDLabel:
        pos_hint: {'center_y':0.3}
        halign: 'center'
        text: ''
        id: output_text
        theme_text_color: "Custom"
        text_color: 0, 1, 0, 1
        
'''
# 
class App(MDApp):   
    def build(self):
        #self.help_string = Builder.load_string(Builder_string)
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)
    # 
    def predict(self):
        self.stringvalue = self.root.ids.verseview.text
        self.urlstring = "https://getbible.net/json?passage=%s"%self.stringvalue.strip()   #For Eg: https://getbible.net/json?passage=1Jn3:16
        
        try:
            self.r = requests.get(self.urlstring)
            self.r.raise_for_status()
            self.res = self.r.text
            self.start = self.res.find('"verse":"') + len('"verse":"')
            self.end = self.res.find(',"direction":"')
            self.substring = self.res[self.start:self.end-9]
            self.root.ids.output_text.text = self.substring        
            
        except Exception as err:
            print(f"Error: {err}")                       

# 
App().run()















































