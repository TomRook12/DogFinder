from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        #Connect before kivy loads
        conn = sqlite3.connect("Test.db")

        #Create a Cursor
        c = conn.cursor()

        # Create a table
        c.execute("""Create TABLE if not exists customers(
            name text,
            last_name text)         
            """)

        conn.commit()

        conn.close()

        return Builder.load_file("first_db.kv")

    def submit(self):
        conn = sqlite3.connect("Test.db")

        c = conn.cursor()

        # Create a table
        c.execute("INSERT INTO customers VALUES(:first)",
                  {
                      'first': self.root.ids.word_input.text,
                  })
        self.root.ids.word_label.text = f"{self.root.ids.word_input.text} Added"


        conn.commit()

        conn.close()

    def show_records(self):
        pass

MainApp().run()
