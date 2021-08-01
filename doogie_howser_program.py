# -*- coding: utf-8 -*-
"""
Doogie Howser Program
This program takes the place of physical journal I am filling out to track
difference aspects of my physical, mental, and spiritual health. The program
will allow me to track data and easily analyze it. It will also save journal
entries

"""
import datetime
import os
import getpass
import csv
from likert_class import *
from my_functions import *



if __name__ == "__main__":

    # Returns a list with formatted dates and times.
    time_list = format_time()

    # Used for a program greeting. Returns the proper salutation based
    # on the current time. 
    greeting_time = return_salutation(time_list[4])
    print(f"\nGood {greeting_time}! Welcome to the Doogie Howser Program.")

    journal_file_path = os.path.join('Doogie Howser Program', 'Journal', \
                                     time_list[2], time_list[3])
    data_file_path = os.path.join('Doogie Howser Program', 'Data')

    # Make_directory creates the directotries if they do not exist already.
    make_directory(journal_file_path)
    make_directory(data_file_path)

    # This is a menu for the program that allows users to navigate
    # to the part of the program they want to use.
    switch_dict = {'journal_switch': False, 'data_gate': False, \
                   'search_gate': False, 'run_program': True}
    while switch_dict['run_program'] == True:
        switch_dict = main_menu()

        # ========================= CSV CODE =============================

        # Creates a CSV and saves it in the current year's directory, or adds 
        # to the existing CSV. First the variables from the CSV need to be 
        # created. This is a good candidate for a function.

        while switch_dict['data_gate'] == True:
            # switch_dict = {'journal_switch': False, 'data_gate': False, \
            #        'search_gate': False, 'run_program': True}
            print(">\n>\n>\n>\n>\n\n<<<DATA ENTRY>>>\n")

            daily_data_csv = os.path.join('{}_daily_data'.\
                                          format(getpass.getuser()))
            data_file_name = os.path.join(data_file_path, '{}'.\
                                          format(daily_data_csv))

            # Returns a list with formatted dates and times.
            time_list = format_time()

            # Makes a list with a nested dictionary to use 
            # in exporting to CSV
            daily_data_set = {'todays_date': None, \
                              'time': None, \
                              'weight_kg': None, \
                              'weight_lbs': None, \
                              'bedtime': None, \
                              'wakeup': None, \
                              'hours_of_sleep': None, \
                              'rested_likert_scale': None, \
                              'yesterday_excercise': None, \
                              'today_excercise': None, \
                              'excercise_type': None, \
                              'excercise_duration': None, \
                              'mental_health_yesterday': None, \
                              'mental_health_today': None, \
                              'physical_health_yesterday': None, \
                              'physical_health_today': None, \
                              'sickness_yesterday': None, \
                              'sickness_today': None, \
                              'meditation_yesterday': None, \
                              'meditation_today': None
                              }

            # Asks user if they want to enter data.
            try:
                entry_gate = ''
                while entry_gate != 'Y' and entry_gate != 'N':
                    entry_gate = input(f"Good {greeting_time}! Would you like to " \
                                       "enter data for today? Enter Y or N: ")
                    entry_gate = entry_gate.capitalize()
            except IOError:
                print("IOError: Please enter Y or N")

            assert entry_gate in {'Y', 'N'}, "entry_gate incorrectly formatted"

            # Creates a dictionary to use as a gate for each data point that
            # needs to be collected.

            if entry_gate == 'N':
                print("Okay. Have a great day!")

                # exit data entry loop
                print("\nReturning to the main menu.\n")
                data_gate = False
                break

            # if entry_gate == 'Y':

            gate_dict = {'weight_gate': False, 'weight_unit_gate': False, \
                         'bedtime_gate': False, \
                         'wakeup_gate': False, 'sleep_gate': False, \
                         'gate_yest_ex': False, 'gate_ex_type': False, \
                         'men_health_gate': False, \
                         'men_health_gate1': False, \
                         'today_ex_gate': False, \
                         'gate_ex_hours': False, \
                         'yes_phy_health': False, \
                         'yesterday_sick': False, \
                         'today_phy_health': False, \
                         'today_sick': False, \
                         'yes_med': False, \
                         'today_med': False \
                         }

            # Returns a list with formatted dates and times.
            time_list = format_time()

            daily_data_set['time'] = time_list[0]
            daily_data_set['todays_date'] = datetime.date.today()

            while gate_dict['weight_gate'] == False:

                try:
                    local_weight = float(input('\nEnter your weight: '))
                    gate_dict['weight_gate'] = True

                except ValueError:
                    print("\nEnter weight as a float or integer")

            while gate_dict['weight_unit_gate'] == False:

                try:
                    weight_unit = input("\nDid you enter pounds (lbs) or " \
                                        "kilograms (kgs)? ")
                    weight_unit = weight_unit.upper()

                except ValueError:
                    print(("Enter LBS or KG"))

                # Converts units to metric or imperial. Saves both.     
                if weight_unit in {'POUNDS', 'LBS', 'LB'}:
                    daily_data_set['weight_lbs'] = local_weight

                    # Converts pounds to kilograms.
                    daily_data_set['weight_kg'] = \
                        pounds_to_kilograms(local_weight)
                    # round(local_weight * .453592, 1)
                    gate_dict['weight_unit_gate'] = True

                if weight_unit in {'KILOGRAMS', 'KGS', 'KG'}:
                    daily_data_set['weight_kg'] = local_weight
                    daily_data_set['weight_lbs'] = \
                        kilograms_to_pounds(local_weight)
                    # round(local_weight / .453592, 1)
                    gate_dict['weight_unit_gate'] = True

                if weight_unit not in {'KILOGRAMS', 'KGS', 'KG', \
                                       'POUNDS', 'LBS', 'LB'}:
                    print("input not valid. Enter a float for weight, and " \
                          "KG or LBS for weight unit.")

            # Pounds do not need decimals, removes the decimal.
            daily_data_set['weight_lbs'] = \
                round(daily_data_set['weight_lbs'])

            while gate_dict['bedtime_gate'] == False:

                try:
                    local_time = input("\nWhat time did you go to bed last " \
                                       "night? \nEnter as HH:MM ")

                    # Returns a list with hour in the 0 index and minutes 
                    # in the 1 index or with False in the 0 index and
                    # an error message in the 1 index.
                    bed_time = validate_time(local_time)

                except ValueError:
                    print(f"{bed_time[1]}")

                # Checks return value of validate_time function
                if bed_time[0] != False:
                    daily_data_set['bedtime'] = local_time
                    # Passes the validated time into the dict variable
                    gate_dict['bedtime_gate'] = True
                else:
                    print(bed_time[1])

            while gate_dict['wakeup_gate'] == False:
                try:
                    local_time = input(\
                        "\nWhat time did you wakeup this morning?" \
                        " \nEnter in 24 hour time HH:MM ")

                    # Function returns a list with hour in the 0 index and 
                    # minutes in the 1 index or with False and an error
                    # message.
                    wake_time = validate_time(local_time)
                except ValueError:
                    print(f"{wake_time[1]}")

                if wake_time[0] != False:
                    daily_data_set['wakeup'] = local_time
                    # Passes the validated time into the CSV ready dict 
                    # variable
                    gate_dict['wakeup_gate'] = True

                # Prints an error.
                else:
                    print(wake_time[1])

            while gate_dict['sleep_gate'] == False:
                # this function returns the hours of sleep with a float 
                # rounded to 3 decimals

                daily_data_set['hours_of_sleep'] = \
                    calculate_sleep(bed_time, wake_time)

                try:
                    temp_likert = int(input("\nHow rested do you feel? " \
                                            "\nEnter a integer between " \
                                            "1 and 7: "))
                    # Use of custom class "Likert"
                    temp_likert = Likert(temp_likert, 7)
                    gate_dict['sleep_gate'] = True

                except NotIntegerError:
                    print("Value and maximum need to be integers.")

                except InvalidRangeError:
                    print("Values outside of range.")

                except ValueError:
                    print("Please input an integer")

                if type(temp_likert) == Likert:
                    daily_data_set['rested_likert_scale'] = \
                        temp_likert
                    gate_dict['sleep_gate'] = True
                else:
                    print('Please only enter integers in range 1 - 7')

            while gate_dict['gate_yest_ex'] == False:

                try:
                    temp_string = str(input("\nDid you excercise yesterday? " \
                                            "\n Enter Y or N: "))
                    temp_string = temp_string.upper()


                except ValueError:
                    print("\nPlease input Y or N")

                if temp_string == 'Y':
                    daily_data_set['yesterday_excercise'] = True
                    gate_dict['gate_yest_ex'] = True

                elif temp_string == 'N':
                    daily_data_set['yesterday_excercise'] = False
                    gate_dict['gate_yest_ex'] = True

                else:
                    print("Invalid Entry. Please only enter 'Y' or 'N'")

            while gate_dict['gate_ex_type'] == False:
                if daily_data_set['yesterday_excercise'] == True:
                    try:
                        daily_data_set['excercise_type'] = \
                            input("\nWhat type of excercise? ")
                        gate_dict['gate_ex_type'] = True

                    except Exception:
                        print('Input Error. PLease enter the excercise type.')

                else:
                    gate_dict['gate_ex_type'] = True

            while gate_dict['gate_ex_hours'] == False:

                if daily_data_set['yesterday_excercise'] == True:

                    try:
                        daily_data_set['excercise_duration'] = \
                            float(input(\
                                "\nHow many hours did you excercise for? "))
                        gate_dict['gate_ex_hours'] = True

                    except ValueError:
                        print('Please enter a number.')

                else:
                    gate_dict['gate_ex_hours'] = True

            while gate_dict['today_ex_gate'] == False:

                try:

                    local_alpha = \
                        input("\nWill you excercise today? \nEnter Y or N: ")
                    local_alpha = local_alpha.upper()

                    if local_alpha == 'Y':
                        daily_data_set['today_excercise'] = True
                        gate_dict['today_ex_gate'] = True

                    if local_alpha == 'N':
                        daily_data_set['today_excercise'] = False
                        gate_dict['today_ex_gate'] = True
                    else:
                        print('Please enter Y or N.')

                except Exception:
                    print("There is a problem with the value you entered.")

            while gate_dict['men_health_gate'] == False:

                try:
                    temp_likert = \
                        int(input("\nHow was your mental health yesterday? " \
                                  "\nEnter a integer between 1 and 7: "))
                    temp_likert = Likert(temp_likert, 7)
                    daily_data_set['mental_health_yesterday'] = temp_likert
                    gate_dict['men_health_gate'] = True
                except NotIntegerError:
                    print("Value and maximum need to be integers.")

                except InvalidRangeError:
                    print("Values outside of range.")

                except ValueError:
                    print("Please input an integer")

                # if no errors switch to True

            while gate_dict['men_health_gate1'] == False:

                try:
                    temp_likert = int(input(\
                        "\nHow is your mental health today? " \
                        "\nEnter a integer between 1 and 7: "))
                    temp_likert = Likert(temp_likert, 7)
                    daily_data_set['mental_health_today'] = temp_likert
                    gate_dict['men_health_gate1'] = True

                except NotIntegerError:
                    print("Value and maximum need to be integers.")

                except InvalidRangeError:
                    print("Values outside of range.")

                except ValueError:
                    print("Please input an integer")

            while gate_dict['yes_phy_health'] == False:

                try:
                    temp_likert = \
                        int(input(\
                            "\nHow was your physical health yesterday? " \
                            "\nEnter a integer between 1 and 7: "))
                    temp_likert = Likert(temp_likert, 7)
                    daily_data_set['physical_health_yesterday'] = temp_likert
                    gate_dict['yes_phy_health'] = True

                except NotIntegerError:
                    print("Value and maximum need to be integers.")

                except InvalidRangeError:
                    print("Values outside of range.")

                except ValueError:
                    print("Please input an integer")

            while gate_dict['yesterday_sick'] == False:
                if daily_data_set['physical_health_yesterday'] <= 2:

                    try:
                        temp_string = \
                            input(\
                                "\nWere you sick yesterday? \nEnter Y or N: ")
                        temp_string = temp_string.upper()


                    except ValueError:
                        print("Please input Y or N")

                    if temp_string == 'Y':
                        daily_data_set['sickness_yesterday'] = True
                        gate_dict['yesterday_sick'] = True

                    if temp_string == 'N':
                        daily_data_set['sickness_yesterday'] = False
                        gate_dict['yesterday_sick'] = True

                    else:
                        print("Please enter Y or N")


                else:
                    daily_data_set['sickness_yesterday'] = False
                    gate_dict['yesterday_sick'] = True

            while gate_dict['today_phy_health'] == False:

                try:
                    temp_likert = \
                        int(input("\nHow was your physical health today? " \
                                  "\nEnter a integer between 1 and 7: "))
                    temp_likert = Likert(temp_likert)
                    daily_data_set['physical_health_today'] = temp_likert
                    gate_dict['today_phy_health'] = True

                except NotIntegerError:
                    print("Value and maximum need to be integers.")

                except InvalidRangeError:
                    print("Values outside of range.")

                except ValueError:
                    print("Please input an integer")

            while gate_dict['today_sick'] == False:
                if daily_data_set['physical_health_today'] <= 2:

                    try:
                        temp_string = \
                            input("\nAre you sick today? \nEnter Y or N: ")
                        temp_string = temp_string.upper()

                    except ValueError:
                        print("Please input Y or N")

                    if temp_string == 'Y':
                        daily_data_set['sickness_today'] = True
                        gate_dict['today_sick'] = True

                    if temp_string == 'N':
                        daily_data_set['sickness_today'] = False
                        gate_dict['today_sick'] = True

                    else:
                        print("Please enter Y or N")

                else:
                    daily_data_set['sickness_today'] = False
                    gate_dict['today_sick'] = True

            while gate_dict['yes_med'] == False:

                try:
                    temp_string = \
                        input("\nDid you meditate yesterday?")
                    temp_string = temp_string.upper()
                    # If Y then TRUE, else False.
                except ValueError:
                    print("Please input Y or N")

                if temp_string == 'Y':
                    daily_data_set['meditation_yesterday'] = True
                    gate_dict['yes_med'] = True

                if temp_string == 'N':
                    daily_data_set['meditation_yesterday'] = False
                    gate_dict['yes_med'] = True
                else:
                    print("Please enter Y or N")

            while gate_dict['today_med'] == False:

                try:
                    temp_string = \
                        input("\nAre you going to meditate today?")
                    temp_string = temp_string.upper()
                    # If Y then TRUE, else False.
                except ValueError:
                    print("Please input Y or N")

                if temp_string == 'Y':
                    daily_data_set['meditation_today'] = True
                    gate_dict['today_med'] = True

                if temp_string == 'N':
                    daily_data_set['meditation_today'] = False
                    gate_dict['today_med'] = True

                else:
                    print("Please enter Y or N")
            
            
            # This loop allows the user to use the public defined method from
            # 
            view_likert_gate = False
            while view_likert_gate == False:
                try:
                    view_likert = input("\nEnter 'Y' to view the likert "\
                                        "scale for your mental health rating"\
                                            "\ntoday or "\
                                            "enter 'N' to finish your entry: ")
                    view_likert = view_likert.upper()
                
                except ValueError:
                    print("Please input Y or N")
                
                if view_likert == 'Y':
                    print\
                    ("\n{}".format\
                        (Likert.print_scale\
                             (daily_data_set['mental_health_today'])))

                    view_likert_gate = True
                
                if view_likert == 'N':
                    view_likert_gate = True
                    
                    
                if view_likert == 'N' and view_likert == 'Y':
                    print("\nPlease enter Y or N")

            print('\nThanks for entering your data today!')

            # Saves dictionary keys as a list to be saved
            # in the CSV file.
            dds_csv_columns = return_keys(daily_data_set)

            try:
                data_file_exists = os.path.isfile(data_file_name)
                # Checks if the file already exists
                with open(data_file_name, 'a+', newline='\n') as csvfile:
                    w = csv.writer(csvfile)
                    if not data_file_exists:
                        print("Data file does not exist")
                        w.writerow(daily_data_set.keys())
                        w.writerow(daily_data_set.values())
                    if data_file_exists == True:
                        w.writerow(daily_data_set.values())
                        # writer.writerow(daily_data_set)
                        # for data in daily_data_set:
                        #     writer.writerow(data)
                        print("...Saving Data")
            except IOError:
                print("I/O error")
            # Run csv creation and writing function

            # exit data entry loop
            print("\nReturning to the main menu.\n")
            switch_dict['data_gate'] = False

        # =================== End of CSV creation ========================

        # ========================= Journal Code ==========================
        # Creates a journal entry and saves it to a .txt file in a custom
        # created directory

        while switch_dict['journal_switch'] == True:

            print(">\n>\n>\n>\n>\n>\n>\n\n<<<JOURNAL>>>")

            journal_file_name = os.path.join\
                (journal_file_path, '{} {} journal.txt' \
                 .format(getpass.getuser(), time_list[3]))

            journal_gate = False
            while journal_gate == False:
                journal_binary = str(input(\
                    "Would you like to make a journal entry " \
                    "today? \nEnter Y or N: "))

                journal_binary = journal_binary.capitalize()
                if journal_binary not in {'Y', 'N'}:
                    print("Please only enter Y or N")

                if journal_binary == 'Y':
                    my_journal = journal_entry()
                    journal_gate = True

                if journal_binary == 'N':
                    print("Shutting journal.")
                    journal_gate = True

            # Creates a file using username and current directory
            if journal_binary == 'Y':
                with open(journal_file_name, "a+") as journal_file:
                    current_time = datetime.datetime.now()
                    journal_file.write(my_journal)
                    print('\nSaving Journal')

            # end journal program loop.
            print("\nReturning to the main menu.\n")
            switch_dict['journal_switch'] = False

        # ===================Search Code=================================
        # Allows user to view data from previous journal entries and

        while switch_dict['search_gate'] == True:

            data_file_path = os.path.join('Doogie Howser Program', 'Data')
            daily_data_csv = os.path.join('{}_daily_data'.\
                                          format(getpass.getuser()))
            data_file_name = os.path.join(data_file_path, '{}'.\
                                          format(daily_data_csv))

            # print("The search function hasn't been written yet.")

            go_to_gate = str(input(">\n>\n>\n>\n>\n>\n>\n\n<<<SEARCH MENU>>>" \
                                   "\nWhat would you like to do? \nEnter: "\
                    "\n'J' to  see the most common words in your Journal "\
                    "\n'S' to see the last day you were sick \n'C' to count"\
                    " how many days you have been sick\n'M' to return to "\
                    "the main menu \n_"))

            go_to_gate = go_to_gate.capitalize()

            # searches for sick days not including the header.
            if go_to_gate == 'S' or go_to_gate == 'C':

                try:
                    data_file_exists = os.path.isfile(data_file_name)
                    # Checks if the file already exists

                    with open(data_file_name, "r") as data_csv:
                        workbook_reader = csv.reader(data_csv)
                        search_data = []
                        if not data_file_exists:
                            print("Data file does not exist")
                        for row in workbook_reader:
                            search_data.append(row)

                except IOError:
                    print("I/O error")

                # Returns the dates ser indicated they were sick.
                days_sick = sick_dates(search_data)

                days_sick = list(days_sick)

                # Counts the number of dates in the days_sick set.
                sick_count = counter(days_sick)

                if go_to_gate == 'C':
                    print(f"\n\nYou have been sick {sick_count} days.")

                    hit_enter_menu_return()

                if go_to_gate == 'S':
                    print(f"\n\nYou were most recently sick on "\
                            f"{max(days_sick)}")

                    hit_enter_menu_return()

            if go_to_gate == 'J':

                journal_search_dir = os.path.join('Doogie Howser Program',\
                                                  'Journal')

                entries = os.scandir(journal_search_dir)
                for entry in entries:
                    if os.path.isfile(os.path.join(journal_search_dir, entry)):
                        print(entry)
                        pass

                # Make a list of all journal entries. each index in the list
                # is a separate .txt file.
                file_name_list = find_journal_entries(journal_search_dir)

                for i in file_name_list:
                    assert os.path.isfile(i), "File does not exist."

                word_list = str()

                # Opens files and writes lines to a list.
                for i in file_name_list:

                    try:
                        with open(i, 'r') as file:
                            for line in file:
                                file_data = file.read()
                                clean_data = tidy_up_string(file_data)

                            word_list = word_list + clean_data


                    except IOError:
                        print("I/O error")

                # Removes '\n' characters and splits the list by word.
                clean_list = strip_and_split(word_list)

                # Creates a dict to use where the key is the word and 
                # the value is how many times it appears.
                count_dict = count_words(clean_list)

                # Sorts count_dict by number of times each word is used.
                sorted_count_list = sort_and_save_dict(count_dict)

                # Prints the ten most used words from the journal.
                most_used_words(sorted_count_list)

                # Pauses the program until the user hits enter.
                hit_enter_menu_return()

            if go_to_gate == 'M':
                print("\nReturning to the main menu.")
                switch_dict['search_gate'] = False

    print(f"\nExiting program. \nHave a good {greeting_time}.")
