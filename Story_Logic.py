from PyQt6.QtWidgets import *
from Story_Screen1 import *
from Story_Screen2 import *
from Story_Screen3 import *
import csv

class Screen1(QMainWindow, Ui_MainWindow21):
    def __init__(self) -> None:
        """Initializes the first screen of the story program"""
        super().__init__()
        self.setupUi(self)

        self.button_s_new_entry.clicked.connect(self.open_new_entry_page)
        self.button_s_view_entries.clicked.connect(self.open_view_entries_page)

    def open_new_entry_page(self) -> None:
        """Opens the 'new entry' screen of the story program and closes the starting page"""
        self.window2 = Screen2()
        self.window2.show()
        self.close_current_window()

    def open_view_entries_page(self) -> None:
        """Opens the 'view entry screen ofthe story program and closes the starting page"""
        self.window3 = Screen3()
        self.window3.show()
        self.close_current_window()

    def close_current_window(self) -> None:
        """Closes the currently open window"""
        self.close()

class Screen2(QMainWindow, Ui_MainWindow22):
    def __init__(self) -> None:
        """Initializes the second screen of the story program"""
        super().__init__()
        self.setupUi(self)

        self.button_s_finish.clicked.connect(self.done_with_entry)
        
    
    def done_with_entry(self) -> None:
        """Checks there is a valid title and story entry, saves story to csv file, opens main screen and closes new entry screen"""
        if self.text_s_title.text() == '' or self.text_s_title.text() == 'Please enter a title':
            self.text_s_title.setText('Please enter a title')
        elif self.text_s_story.toPlainText() == '' or self.text_s_story.toPlainText() == 'Please enter a story':
            self.text_s_story.setPlainText('Please enter a story')
        else:
            story_title = self.text_s_title.text()
            story_content = self.text_s_story.toPlainText()

            with open('stories.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([story_title, story_content])

            self.window = Screen1()
            self.window.show()
            self.close_current_window()

    def close_current_window(self) -> None:
        """Closes the currently open window"""
        self.close()

class Screen3(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """Initializes the third screen of the story program and loads the titles into a list for the comboBox"""
        super().__init__()
        self.setupUi(self)

        self.button_s_finish.clicked.connect(self.open_starter_page)

        self.titles = []

        with open('stories.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                if row:
                    self.titles.append(row[0])

        if self.titles:
            self.comboBox.addItems(self.titles)
            self.comboBox.currentIndexChanged.connect(self.change_story)


    def change_story(self) -> None:
        """Updates the story when the title is changed"""
        if self.titles:
            with open('stories.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                self.current_title = self.comboBox.currentText()

                for row in reader:
                    if row:
                        if row[0] == self.current_title:
                            self.textBrowser.setPlainText(row[1])
                    

    def open_starter_page(self) -> None:
        """Opens the main page of the story program and closes the current window"""
        self.window = Screen1()
        self.window.show()
        self.close_current_window()
    

    def close_current_window(self) -> None:
        """Closes the currently open window"""
        self.close()

