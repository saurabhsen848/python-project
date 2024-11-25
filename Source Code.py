from string import (
    ascii_uppercase,
    ascii_lowercase,
    digits,
    punctuation,
    ascii_letters,
    whitespace,
)  # Importing constants form string module
from random import choice as rand_ch  # Importing choice from random module

upper = list(
    ascii_uppercase
)  # Creating a list of all uppercase letters from string module
lower = list(
    ascii_lowercase
)  # Creating a list of all lowercase letters from string module
digits = list(digits)  # Creating a list of all digits from string module
punc = list(punctuation)  # Creating a list of all punctuations form string module
lett = list(ascii_letters)  # Creating a list of all letters from string modules
space = list(whitespace)  # Creating a list of all whitespaces from string modules

while True:  # Creating an infinite loop for menu driven program using while
    print(
        """
Hello guys, This program helps you to generate password on different basis and detect the strength of a password
    1. Generate password
    2. Detect password strength
    3. Exit
You can select either 1, 2 or 3 as per your choice"""
    )  # A set of menu for the user

    try:
        choice = int(input("Enter your choice: "))
    
        # When 'Generate Password' is selected
        if choice == 1:
            while True:  # Nesting the infinite loop
                print("""
I see.... You have chosen to generate a password 
Here also you will get different options
    1. Based on length
    2. Based on strength
    3. Back
You can choose either 1, 2 or 3 as per your choice"""
                )  # Another set of menu for the user
                
                ch1 = int(input("Enter your choice: "))
                # Creating a password based on length
                if ch1 == 1:
                    n = int(
                        input("Enter the length of the password: ")
                    )  # Getting the length of the password
                    all_list = []  # Creating an empty list
                    all_list.extend(
                        lett
                    )  # Extending the empty list with the list of letters
                    all_list.extend(digits)  # Extending the list with the list of digits
                    all_list.extend(
                        punc
                    )  # Extending the list with the list of punctuations

                    str1 = ""  # Creating an empty string
                    for i in range(n):
                        str1 = str1 + str(
                            rand_ch(all_list)
                        )  # Appending randomly the characters from all_list to the empty string using concatenation operator in a for loop
                    print(str1)  # Printing the password as per the length given by the user
                    print(
                        "----------------xxx----------------"
                    )  # Creating a divider to make the output look good

                # Getting password based on strength
                if ch1 == 2:
                    while True:  # Nesting the infinite loop
                        print(
                            """
I see.... You have chosen to generate password based on strength
Here also you will get few options
    1. Generate a weak password
    2. Generate a average password
    3. Generate a strong password
    4. Back
You can choose either 1, 2, 3 or 4 as per your choice"""
                        )  # Another set of menu to the user
                        ch2 = int(input("Enter your choice: "))
                        # Creating a weak password
                        if ch2 == 1:
                            num = 7  # Specifying the length of the password
                            fist = []  # Creating an empty list
                            fist.extend(
                                lett
                            )  # Extending the empty list with the list of letters

                            str1 = ""  # Creating an empty list
                            for i in range(num):
                                str1 = str1 + str(
                                    rand_ch(fist)
                                )  # Appending randomly the characters from 'fist' to the empty string using concatenation operator in a for loop
                            print(str1)  # Printing the weak password
                            print(
                                "----------------xxx----------------"
                            )  # Creating a divider to make the output look good

                        # Creating an average password
                        if ch2 == 2:
                            num = 10  # Specifying the length of the password

                            fist1 = []  # Creating an empty list
                            s_symbol = [
                                "@",
                                "_",
                                "#",
                                ".",
                                ",",
                            ]  # Creating a list of some specific special symbols which may be used in average passwords
                            fist1.extend(
                                lett
                            )  # Extending the empty list with the list of letters created
                            fist1.extend(
                                digits
                            )  # Extending the list with the list of digits created
                            fist1.extend(
                                s_symbol
                            )  # Extending the list with the list of special symbols created

                            str2 = ""  # Creating a empty string
                            for i in range(num):
                                str2 = str2 + str(
                                    rand_ch(fist1)
                                )  # Appending randomly the characters from 'fist1' to the empty string using concatenation operator in a for loop
                            print(str2)  # Printing the average password
                            print(
                                "----------------xxx----------------"
                            )  # Creating a divider to make the output look good

                        # Creating a strong password
                        if ch2 == 3:
                            num = 18  # Specifying the length of the password

                            fist = []  # Creating an empty list
                            fist.extend(
                                lett
                            )  # Extending the empty list with the list of letters
                            fist.extend(
                                digits
                            )  # Extending the list with the list of digits
                            fist.extend(
                                punc
                            )  # Extending the list with the list of punctuations

                            str2 = ""  # Creating an empty string
                            for i in range(num):
                                str2 = str2 + str(
                                    rand_ch(fist)
                                )  # Appending randomly the characters from 'fist' to the empty string using concatenation operator in a for loop
                            print(str2)  # Printing the strong password
                            print(
                                "----------------xxx----------------"
                            )  # Creating a divider to make the output look good

                        if ch2 == 4:
                            break  # Back option
                        
                        if ch2 > 4:
                            print("You can choose only from 1 to 4")
                            print("----------------xxx----------------")

                if ch1 == 3:
                    break  # Back option
                
                if ch1 > 3:
                    print("You can choose only from 1 to 4")
                    print("----------------xxx----------------")

        # Creating password strength detector
        if choice == 2:
            pa_wrd = str(
                input("Enter the password whose strength has to be detected: ")
            )  # Getting the password whose strength has to be detected

            weak = (
                []
            )  # Creating an empty list which will contain the elements of a weak password
            weak.extend(lett)  # Extending the list with list of letters

            average = (
                []
            )  # Creating an empty list which will contain the elements of a average password
            average.extend(lett)  # Extending the list with list of letters
            average.extend(digits)  # Extending the list with list of digits

            strong = (
                []
            )  # Creating an empty list which will contain the elements of a strong password
            strong.extend(lett)  # Extending the list with list of letters
            strong.extend(digits)  # Extending the list with list of digits
            strong.extend(punc)  # Extending the list with list of punctuations

            pass_wrd = set(pa_wrd)  # Creating the set of the password given by the user

            if pass_wrd.issubset(
                weak
            ):  # Checking is the password is weak by using the concept of subset
                print("Weak")
                print(
                    "----------------xxx----------------"
                )  # Creating a divider to make the output look good
            elif pass_wrd.issubset(
                average
            ):  # Checking is the password is average by using the concept of subset
                print("Average")
                print(
                    "----------------xxx----------------"
                )  # Creating a divider to make the output look good
            elif pass_wrd.issubset(
                strong
            ):  # Checking is the password is strong by using the concept of subset
                print("Strong")
                print(
                    "----------------xxx----------------"
                )  # Creating a divider to make the output look good

            for a in pass_wrd:
                if a in space:    
                    print("Please enter a password without whitespaces")
                    print("----------------xxx----------------")
                    break   # Removing the whitespace

        if choice == 3:
            print("Exiting the program.....")
            break  # Exiting the program
        
        if choice>3:
            print("You can choose only from 1 to 3")
            print("----------------xxx----------------")

    except ValueError:
        print("\nPlease enter a valid integer :( \n\
            restarting....")
        print("----------------xxx----------------")