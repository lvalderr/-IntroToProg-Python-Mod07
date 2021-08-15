# -------------------------------------------------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: The script demonstrates the use of Try - Exception handling in a Menu
# ChangeLog (Who,When,What):
# LValderrama, 8.09.2021, Created started script
# LValderrama, 8.13.2021, Added Try/Catch to Menu, read from file, write to file, entering inventory values
# LValderrama, 8.14.2021, Added pickling/unpickling options
# -------------------------------------------------------------------------------------------------------------------- #

# Objective:
# The Assignment07.py script is designed to:
# 1. Present a menu of choices for the user to select from.
#       1) Display current inventory
#       2) Add a new inventory item
#       3) Remove an existing inventory item
#       4) Save data to file
#       5) Reload data from text file
#       6) Reload data from pickle file
#       5) Exit program
# 2. Execute the program based on the choice made by the user.
# 3. Use Try/Catch Error Handling.
# 4. The program has "pickle" and "unpickle" features.

# Improving my code: Entered a Try/Catch to:
# 1. The menu option selection. the user should only enter integers between 1 - 7.
# 2. Option 1 Read from file
# 3. Option 2 Value as the user should only enter integers.
# 4. Option 4 writing to file in case the file does not exit.

# Pseudo-Code:
# Data --------------------------------------------------------------------------------------------------------------- #
# Step 1 - Declare variables and constants --------------------------------------------------------------------------- #
import sys
pickle = ""
pickleFile = "BikeInventoryPickle.dat"  # This is the pickle file.
strFileName = "BikeInventory.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Bike, Value}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strBike = ""  # Captures the user inventory data


# Processing Data ---------------------------------------------------------------------------------------------------- #
# Step 2 - set up class processor functions--------------------------------------------------------------------------- #


class Processor:
    """ Performs Processing Bike"""

    @staticmethod
    def read_data_from_text_file(file_name):
        """ Reads data from BikeInventory.txt file into a list of dictionary rows

        :param file_name: (string) strFileName = BikeInventory.txt
        :return: (list) dictionary rows
        """
        try:
            lstTable = []
            objFile = open(file_name, "r")
        except IOError:
            print('\nThere is no file associated with this application. ')
            input("\nPress Enter to exit.")
            sys.exit()
        for row in objFile:
            if "," in row:
                lstRow = row.split(",")
                dicRow = {"Bike": lstRow[0].strip(), "Value": lstRow[1].strip()}
                lstTable.append(dicRow)
        objFile.close()
        return lstTable

    @staticmethod
    def read_data_from_pickle_file(pickling):
        """ Reads data from BikeInventoryPickle.dat file into a list of dictionary rows

        :param pickling: (string) pickleFile = BikeInventoryPickle.dat
        :return: (list) dictionary rows
        """
        import pickle
        print('\nUnpickling Bike Inventory.')
        pickleFile = open(pickling, "rb")
        pickleFileData = pickle.load(pickleFile)  # Error indicating 'str' object has no attribute 'load'
        print(pickleFileData)
        pickleFile.close()

    @staticmethod
    def add_data_to_list(list_of_rows, bike, value):
        """ Adds bikes and values to list

        :type list_of_rows:
        :param list_of_rows: (list) you want filled with file data
        :param bike: (string) to do item
        :param value: (string) the value of the bike
        :return: (list) of bikes and values
        """
        try:
            dicRow = {"Bike": str(bike), "Value": str(value)}
            list_of_rows.append(dicRow)
        except ValueError:
            print("Enter a number in Value")
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(list_of_rows):
        """ Removes bikes from list

        :param list_of_rows: (list) you want filled with file data
        :return" (List) of bikes removed
        """
        while len(lstTable) > 0:
            print("Current inventory list:\n", "\n".join([f"\t{item['Bike']}" for item in lstTable]))
            term = input("Enter the Bike you want to delete or type 'exit' to return to Menu of Options: ")
            if term.lower() == "exit":
                break
            for bike in lstTable:
                if term in bike["Bike"]:  # If the bike entered by the user matches the name in the list then proceed
                    print(f"Removing {bike['Bike']}...")  # Print a message "item found" and processing removal
                    list_of_rows.remove(bike)  # The item is removed from the table
                    break
            else:
                print(f"Bike not found in list: {term}")  # Displays message indicating the bike was not found!

    @staticmethod
    def write_data_from_list_to_text_file(file_name, list_of_rows):
        """ Writes data from list to text file

        :param file_name: (string) strFileName = BikeInventory.txt
        :param list_of_rows: (list) you want filled with file data
        """
        validFile = False
        while not validFile:
            try:
                objFile = open(file_name, 'w')
                print()
                validFile = True
            except IOError as e:
                print("Unable to open the file", file_name, "Ending program.\n", e)
                input("\nPress Enter to exit.")
                sys.exit()
            for row in list_of_rows:
                objFile.write(row["Bike"] + "," + str(row["Value"]) + "\n")
            objFile.close()

    @staticmethod
    def write_data_from_list_to_pickle_file(pickling, list_of_rows):
        """ Writes data from list to text file

        :param pickling: (string) strFileName = BikeInventory.txt
        :param list_of_rows: (list) you want filled with file data
        """
        import pickle
        pickleFile = open(pickling, "wb")
        pickle.dump(list_of_rows, pickleFile)
        pickleFile.close()


# Input/Output ------------------------------------------------------------------------------------------------------- #
# Step 3 - set up presentation, IO functions ------------------------------------------------------------------------- #


class IO:
    """    Performs Input and Output   """

    @staticmethod
    def print_menu_of_Options():
        """ Display a menu of choices to the user

        :return: Nothing
        """
        print('''
        Menu of Options
        1) Display current inventory
        2) Add a new inventory item
        3) Remove an existing inventory item
        4) Save data to file
        5) Reload data from text file
        6) Reload data from pickle file
        7) Exit program
        ''')
        print()  # Adding extra line

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = int(input("Which option would you like to perform? [1 to 7] - "))
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message: An optional message to display
        :return: Nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def print_current_inventory_in_list(list_of_rows):
        """ Shows the current bikes in the list of dictionaries rows

        :param list_of_rows: (list) split data into list
        :return: Nothing
        """
        print("******* The current inventory: *******")
        for row in lstTable:
            print(row["Bike"] + ',' + row["Value"])  # Unpacking
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_inventory_and_value():
        """ Adds new bike and value entered by the user
        :return: (string) Bike and its corresponding value
        """
        try:
            bike = str(input("Enter a new bike inventory: ")).strip()
            value = int(input("Enter value: "))
            print()
            return bike, value
        except ValueError:
            print("Enter a number in Value")

    @staticmethod
    def remove_data_from_list(term):
        """ Removes bikes and values entered by the user

        :term: (string) this is the item the user wants to remove
        :return: (string) Bike and its corresponding value
        """
        try:
            term: input("Confirm the bike you want to delete or type 'exit' to return to Menu of Options: ")
        except ValueError:
            print('Invalid input')


# Main Body of the Script -------------------------------------------------------------------------------------------- #
# Step 4 - When the program starts, load data from ToDoFile.txt


lstTable = Processor.read_data_from_text_file(strFileName)

# Step 4 - Display a menu of choices to the user
while True:
    try:

# Step 5 Calling the function to display menu of options
        IO.print_menu_of_Options()
        strChoice = IO.input_menu_choice()

# Step 6 Calling the function to display current inventory
        if strChoice == 1:
            IO.print_current_inventory_in_list(lstTable)
            IO.input_press_to_continue()
            continue

# Step 7 Calling the function to enter new data to list
        elif strChoice == 2:
            tplData = IO.input_new_inventory_and_value()
            Processor.add_data_to_list(lstTable, tplData[0], tplData[1])
            IO.print_current_inventory_in_list(lstTable)
            IO.input_press_to_continue()
            continue

# Step 8 Calling the function to remove data from list
        elif strChoice == 3:
            Processor.remove_data_from_list(lstTable)
            IO.input_press_to_continue()
            continue

# Step 9 Calling the function to save data from list to .txt and "pickling" data to .dat file
        elif strChoice == 4:
            print('\n Would you like to save your data?')
            strSaveToFileInput = input("Enter 'y' or 'n': ")
            if strSaveToFileInput == 'n':
                print('Data not saved!')
            if strSaveToFileInput == 'y':
                Processor.write_data_from_list_to_text_file(strFileName, lstTable)
                print('\nYour data is saved to', strFileName)
                Processor.write_data_from_list_to_pickle_file(pickleFile, lstTable)
                print('Your data is also saved in', pickleFile)
                IO.print_current_inventory_in_list(lstTable)
                IO.input_press_to_continue()
            continue

# Step 10 Calling the function to reload data from .txt file to list
        elif strChoice == 5:
            print("This action will overwrite all unsaved inventory!")
            strAcceptOrDecline = input("Update data without saving? type 'y' or 'n' ")
            if strAcceptOrDecline.lower() == 'y':
                lstTable.clear()
                lstTable = Processor.read_data_from_text_file(strFileName)
                IO.print_current_inventory_in_list(lstTable)
            else:
                input("File no updated. Press Enter to go back to Menu of Options")
                IO.print_menu_of_Options()
            continue

# Step 11 Calling the function to "unpickle" data from .dat file to list
        elif strChoice == 6:
            print("This action will overwrite all unsaved inventory!")
            strAcceptOrDecline = input("Update data without saving? type 'y' or 'n' ")
            if strAcceptOrDecline.lower() == 'y':
                lstTable.clear()
                lstTable = Processor.read_data_from_pickle_file(pickleFile)

            else:
                input("File no updated. Press Enter to go back to Menu of Options")
                IO.print_menu_of_Options()
            continue

# Step 12 Ending the program and exit
        elif strChoice == 7:
            print("Goodbye!")
            EndProgram = input('\n(Press Enter to End Program)')
            break
        else:
            print('\nInvalid entry. Please enter a number from 1 to 7')
    except ValueError:
        print('\nInvalid entry. Please enter a number from 1 to 7')
