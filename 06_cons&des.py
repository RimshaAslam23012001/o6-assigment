#6. Constructors and Destructors
#Assignment:
#Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")
#Test the Logger class
logger: Logger = Logger()
# The message "Logger object created." will be printed when the object is created.
# The message "Logger object destroyed." will be printed when the object is destroyed.