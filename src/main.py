from file_handling import file_handler
from new_reference import new_reference
import os.path



# select which modules to run
'''
    The following condition statements will select which 
    modules to run based on what the user inputs.
'''
# ask user whether they want to handle a file or not
print('\n')
print('***** Harvard Referencing for Markdown *****')


# main loop
# Check is references.txt exists. If yes, ask user what they want to do
if os.path.isfile('references.txt'):
    print("\nWhat would you like to do? \n\nOptions: 'Insert references', 'Insert citations', 'New Reference'. \nType '\help' to print help document. Type '\quit' to exit. Type '\delete' to delete references list and citations")
    module_to_run = input('\n>> ').lower()

    # make sure user understands delete
    if module_to_run in '\delete':
        print("\nThis will delete all the current references. Are you sure?")
        # ask user to type Y to confirm N to cancel 
        user_confirm = input('\nY/N:\n>>')
        if user_confirm in 'Y':
            os.remove("references.txt")
            # os.remove("citations.txt")
            print("\nReferences deleted successfully")
            print("\nEnter a reference to get started\n")
            module_to_run = 'new reference'
# if not get user to enter new reference
else:
    print("\nEnter a reference to get started\n")
    module_to_run = 'new reference'


match module_to_run:
# if handle file, ask user for file name
    case 'insert references':
        # get the references in references.txt file and place in a list

        # get the markdown file name
        file_name = input('What is the Markdown file name? \n>> ')
        file_handler(file_name, '.md', '', 'a+') if '.md' in file_name else file_handler(file_name + '.md', '.md', '', 'a+')
    case 'insert citations':
        # get the citations in citations.txt file

        # get the markdown file name
        pass
# if not, run the reference module
    case 'new reference':
        temporary_reference_list = []
        end_listing = 0
        # run new reference function until user types add
        while end_listing != 'add':
            end_listing, temporary_reference_list = new_reference(temporary_reference_list)
        # add the references to the reference.txt file
        # call the file handler function and write to file
        file_handler('references.txt', '.txt', ''.join(temporary_reference_list), 'a+')
    case '\help':
        # print the help documentation by calling the module function
        pass