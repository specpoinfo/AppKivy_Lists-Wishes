from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDTextButton, MDRaisedButton

from kivymd.app import MDApp

KV = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Screen 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Screen 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"


Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"
                BoxLayout:
                    orientation: "vertical"
                    MDLabel:
                        text: "Screen 1"
                        halign: "center"
                    
                    MDRaisedButton:
                        text: "press here"
                        pos_hint: {"center_x": .5, "center_y": .3}
                        on_press: app.new_page_screen()

            Screen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

new_kv = '''
BoxLayout:
    orientation: "vertical"
    MDTextButton:
        text: "Hello"
    MDTextButton:
        text: "world!"
'''

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def new_page_screen(self):
        KVTest_1().run()

class KVTest_1(MDApp):
    def build(self):
        return Builder.load_string(new_kv)


TestNavigationDrawer().run()
