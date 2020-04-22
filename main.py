from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, TwoLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons

import client_api as api
import uuid


current_uuid='7de9581e439311ea91659cb70dd0e9ca'
 


KV = '''

<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
    
    AnchorLayout:
        anchor_x: "center"
        size_hint_y: None
        height: avatar.height
        
        Image:
            id: avatar
            size_hint: None, None
            size: "400dp", "200dp"
            source: "img.jpg"

    MDLabel:
        text: "Cool menu"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "kivydevelopment@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Главная"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "main_screen"

            OneLineListItem:
                text: "Текущий лист"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "current_list"

<ListItemWithCheckbox>:

    IconLeftWidget:
        icon: root.icon

    RightCheckbox:

NavigationLayout:
    x: toolbar.height
    ScreenManager:
        id: screen_manager
        Screen:
            name: "main_screen"
            title: "test"
            BoxLayout:
                orientation: "vertical"
                MDToolbar:
                    id: toolbar
                    pos_hint: {"top": 1}
                    elevation: 10
                    title: "none"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                BoxLayout:

                    BoxLayout:

                        ScrollView:

                            MDList:
                                id: scroll_list_main
                                    
                MDBottomAppBar:       
                    MDToolbar:


        Screen:
            name: "current_list"

            BoxLayout:
                orientation: "vertical"
                MDToolbar:
                    id: toolbar
                    pos_hint: {"top": 1}
                    elevation: 10
                    title: "none"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                BoxLayout:

                    BoxLayout:

                        ScrollView:

                            MDList:
                                id: scroll_list_current
                                    
                MDBottomAppBar:       
                    MDToolbar:
                        icon: "plus-box"
                        type: "bottom"
                        on_action_button: app.open_screen_with_current_list()

    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer              

'''


class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    '''Custom list item.'''
    icon = StringProperty("android")
    

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Current_List(MDApp):
    def build(self):
        #self.theme_cls.primary_palette = ""
        return Builder.load_string(KV)
    
    def on_start(self):
        pass


    def open_screen_with_current_list(self):
        icons = list(md_icons.keys())
        user_list = api.getlistobj(uuid.UUID(current_uuid))
        self.root.ids.toolbar.title = user_list['name']
        for it in user_list["items"]:
            self.root.ids.scroll_list_current.add_widget(
                ListItemWithCheckbox(text=it["label"],secondary_text=it.get("descriprion"," "),icon=icons[5])
            )    
    
    def create_new_part_of_list(self):
        icons = list(md_icons.keys())
        self.root.ids.scroll_list.add_widget(
            ListItemWithCheckbox(text=f"New item", icon=icons[5])
        )

    def delete_all_items(self):
        pass



Current_List().run()