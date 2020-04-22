from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivymd.uix.toolbar import MDBottomAppBar, MDToolbar, MDIconButton
from kivy.properties import ObjectProperty


class MDToolbarMain(MDToolbar):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    screen_name="main_screen"
    icon = StringProperty()






class DrawerList(ThemableBehavior, MDList):


    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""
        
        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

    def remove_all_widgets_inside(self, count):
        for i in range(count):
            self.remove_widget(self.children)
