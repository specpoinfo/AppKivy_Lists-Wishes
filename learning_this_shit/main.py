from kivy.lang import Builder
from kivymd.uix.button import Button
from kivymd.uix.card import MDSeparator
from nav import ItemDrawer, MDToolbarMain, DrawerList

from kivymd.app import MDApp
from dict_lang import l

class MainApp(MDApp):
    lang = "eng"
    main_theme = "Green"
    
    def build(self):
        #return Builder.load_string(KV)
        self.theme_cls.primary_palette = self.main_theme
        self.theme_cls.theme_style = "Light" #"Dark"

        
    def on_start(self):
        self.change_lang_on(self.lang)

    def change_lang_other(self):
        if self.lang == "ru":
            self.lang = "eng"
        else:
            self.lang = "ru"
        self.change_lang_on(self.lang)

    def change_lang_on(self, lang):
        self.inicialize_lang(lang)
        self.inicialize_lang_menu(lang)


    def inicialize_lang_menu(self, lang):
        icons_item = [
            ['plus-circle',l[lang]["cr_ne_list"],'create_new_list'],
            ['basket',l[lang]["main"],'main_screen'],
            ['account-group',l[lang]["friends"],'friend_screen'],
            ['cogs',l[lang]["setting"],'setting_screen'],
        ]
        self.root.ids.content_drawer.ids.md_list.clear_widgets()
        for item in icons_item:   
            ItemDrawer.screen_name = item[2]
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(id=item[2],icon=item[0], text=item[1])
            )
        
        #for i in range(len(icons_item)):
        

    def inicialize_lang(self, lang):
        self.root.ids.main_screen_toolbar.title = l[lang]["main"]
        self.root.ids.friend_screen_toolbar.title = l[lang]["friends"]
        self.root.ids.setting_screen_toolbar.title = l[lang]["setting"]
        self.root.ids.create_new_list_toolbar.title = l[lang]["cr_ne_list"]
        

    
    def change_screen(self, instance):
        self.root.ids.screen_manager.current = instance.screen_name
    def change_screen_on(self, screen_name):
        self.root.ids.screen_manager.current = screen_name
        





MainApp().run()