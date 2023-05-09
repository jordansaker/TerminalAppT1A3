from new_reference import new_reference, edit_reference
from md_file_search import search_md_for_reference_list_flag
import os.path
import file_handling


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
    print("\nWhat would you like to do? \n\nOptions: 'Insert references', 'Insert citations', 'New Reference', 'Search'. \nType '\help' to print help document. Type '\quit' to exit. Type '\delete' to delete references list and citations")
    module_to_run = input('\n>> ').lower()

    # make sure user understands delete
    if module_to_run in '\delete':
        print("\nThis will delete all the current references. Are you sure?")
        # ask user to type Y to confirm N to cancel 
        user_confirm = input('\nY/N:\n>> ').lower()
        if user_confirm in 'y':
            os.remove("references.txt")
            os.remove("citations.txt")
            print("\nReferences deleted successfully")
            print("\nEnter a reference to get started\n")
            module_to_run = 'new reference'
# if not get user to enter new reference
else:
    print("\nEnter a reference to get started\n")
    module_to_run = 'new reference'

# main loop which can be exited if user types in quit

while module_to_run != '\quit':
    match module_to_run:
    # if handle file, ask user for file name
        case 'insert references':
            # call the file handling function for inserting references
            file_handling.insert_references_citations('references.txt', 'read')
        case 'insert citations':
            # call the file handling function for inserting citations
            file_handling.insert_references_citations('citations.txt', 'read')
    # if not, run the reference module
        case 'new reference':
            temporary_reference_list = []
            temporary_citation_list = ['']
            end_listing = 0
            # run new reference function until user types add
            while end_listing != 'add':
                end_listing, temporary_reference_list, temporary_citation_list = new_reference(temporary_reference_list, temporary_citation_list)
            # add the references to the references.txt and citations.txt files
                # call the file handler function and write to file
            file_handling.add_new_reference('references.txt', ''.join(temporary_reference_list), 'a+')
            file_handling.add_new_reference('citations.txt', ''.join(temporary_citation_list), 'a+')
        case '\help':
            # print the help documentation by calling the module function
            pass
        case 'search':
            reference_number, reference_list = file_handling.insert_references_citations('references.txt', 'search')
            citation_list = file_handling.insert_references_citations('citations.txt', 'search')

            updated_reference_list, new_generated_citation = edit_reference(reference_list, reference_number, 'reference','')
            updated_citation_list = edit_reference(citation_list, reference_number, 'citation', new_generated_citation)

            file_handling.add_new_reference('references.txt', updated_reference_list, 'w')
            file_handling.add_new_reference('citations.txt', updated_citation_list, 'w')

    print("\nWhat would you like to do? \n\nOptions: 'Insert references', 'Insert citations', 'New Reference', 'Search'. \nType '\help' to print help document. Type '\quit' to exit. Type '\delete' to delete references list and citations")
    module_to_run = input('\n>> ').lower()