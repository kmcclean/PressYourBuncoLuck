class ErrorHandling:

    def non_blank_string(self, check_text):
        while True:
            text = input(check_text)
            if text is not "":
                return text
            else:
                print("Blank entries are not accepted.")

    # This is the integer checking for the game. It makes sure that the data given is a positive integer.
    def positive_integer_input_checking(self, check_text):
        while True:
            try:
                check = int(input(check_text))

                if check > 0:
                    return check
                else:
                    print("You cannot use negative numbers.")

            except ValueError:
                print("The entry needs to be an integer.")

    # This is used when an integer between a certain range is required.
    def range_integer_input_checking(self, check_text, low, high):
        while True:
            try:
                check = int(input(check_text))
                if check >= low and check <= high:
                    return check
                else:
                    print("Choose a number between " + str(low) + " and " + str(high))

            except ValueError:
                print("The entry needs to be an integer.")