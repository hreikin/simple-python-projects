# Importing required libraries.
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import random
import sys

# Initialize main window.
class MainWindow(QMainWindow):
  
    def __init__(self):
        super().__init__()

        # Set the title of the window.
        self.setWindowTitle("Number Guessing Game")

        # Set the window location and size.
        self.setGeometry(300, 300, 340, 350)

        # Calling the UI method.
        self.app_ui()

        # Show the "app_ui".
        self.show()

        # Set the random number.
        self.random_number = 0

        # Set the current and max try values.
        self.current_try = 1
        self.max_tries = 2

    def app_ui(self):

        # Set the title heading for the game.
        title = QLabel("Number Guessing Game", self)

        # Set the title heading geometry.
        title.setGeometry(20, 10, 300, 60)

        # Set the font to be used.
        font = QFont("Times", 14)
        font.setBold(True)
        font.setUnderline(True)
        title.setFont(font)

        # Set the title alignment.
        title.setAlignment(Qt.AlignCenter)

        # Create a label for game info.
        self.info = QLabel("Welcome, click start to begin.", self)

        # Set the location and size of the label.
        self.info.setGeometry(40, 85, 260, 60)

        # Set word wrap to True so the label is multi line
        self.info.setWordWrap(True)

        # Set the labels font and alignment.
        self.info.setFont(QFont("Times", 14))
        self.info.setAlignment(Qt.AlignCenter)

        # Create a style for the label.
        self.info.setStyleSheet("QLabel"
								"{"
								"border : 2px solid black;"
								"background : lightgrey;"
								"}")

        # Create spin box for user input and set the range from 1 to 10.
        self.guess_number = QSpinBox(self)
        self.guess_number.setRange(1, 10)

        # Set location of spin box.
        self.guess_number.move(120, 170)

        # Setting font and alignment.
        self.guess_number.setAlignment(Qt.AlignCenter)
        self.guess_number.setFont(QFont("Times", 14))

        # Create a button to check if the entered number is correct and then set its location and size. 
        # Set the button to be disabled until the player starts the game.
        global check_button
        check_button = QPushButton("Check", self)
        check_button.setGeometry(130, 235, 80, 30)
        check_button.setDisabled(True)

        # Add a signal to the check button so it checks the players guess against the answer when clicked.
        check_button.clicked.connect(self.check_answer)

        # Create a button to start the game and set its location and size.
        global start_button
        start_button = QPushButton("Start Game", self)
        start_button.setGeometry(65, 280, 100, 40)

        # Add a signal to the start button so it starts the game when clicked.
        start_button.clicked.connect(self.start_game)

        # Create a reset button and set its location and size.
        # Set the button to disabled until the player starts the game.
        global reset_button
        reset_button = QPushButton("Reset Game", self)
        reset_button.setGeometry(175, 280, 100, 40)
        reset_button.setDisabled(True)

        # Add a signal to the reset button so it resets the game when clicked.
        reset_button.clicked.connect(self.reset_game)

    def start_game(self):

        # Make the label blue.
        self.info.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid blue;"
                                "background : lightblue;"
                                "}")

        # Enable the check button when the game starts.
        check_button.setDisabled(False)

        # Enable the reset button when the game starts.
        reset_button.setDisabled(False)

        # Disable the start button when the game starts
        start_button.setDisabled(True)

        # Set the random number.
        self.random_number = random.randint(1, 10)

        # Set current try value.
        self.current_try = 1

        # Change the info labels text to explain the game.
        self.info.setText("Try to guess the number between 1 and 10. You get 3 tries.")

    def check_answer(self):

        # If current try is less than or equal to max tries run through the following "if, else" statement, 
        # if not disable the button and print the game over text.
        if self.current_try <= self.max_tries:

            # Get the players guess from the input box.
            guess_number = self.guess_number.value()

            # Check the value of the players guess against the answer.
            if guess_number == self.random_number:

                # Change the info label to let the player know they were correct and change the colour to green.
                self.info.setText("Well done, that is correct!")
                self.info.setStyleSheet("QLabel"
                                        "{"
                                        "border : 2px solid black;"
                                        "background : lightgreen;"
                                        "}")

                # Disable the check button when the game is complete.
                check_button.setDisabled(True)

            elif guess_number < self.random_number:

                # Give the player a hint.
                self.info.setText("Sorry, try a little higher.")
                self.current_try = self.current_try + 1

            else:

                # Give the player a hint.
                self.info.setText("Sorry, try a little lower.")
                self.current_try = self.current_try + 1

        else:

            # Set game over message.
            self.info.setText("Game Over!")
            check_button.setDisabled(True)

    def reset_game(self):

        # Make the label grey again.
        self.info.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black;"
                                "background : lightgrey;"
                                "}")

        # Set check button to disabled when game is reset.
        check_button.setDisabled(True)

        # Set reset button to disabled when game is reset.
        reset_button.setDisabled(True)

        # Set start button to enabled when game is reset.
        start_button.setDisabled(False)

        # Reset the info label text.
        self.info.setText("Welcome, click start to begin.")

        # Reset current try value.
        self.current_try = 1

# Create the PyQt5 app and the instance of our window.
app = QApplication(sys.argv)
window = MainWindow()
  
# Start the app.
sys.exit(app.exec())