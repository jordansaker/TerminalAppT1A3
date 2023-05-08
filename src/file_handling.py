# File handling module
'''
    The module contains functions based on specific cases matched in the main loop.
'''
from md_file_search import search_md_for_reference_list_flag, search_md_for_citation_flags



def insert_references():
    reference_list = []
    try:
        with open('references.txt', 'r') as file:
            for line in file:
                reference_list.append(line)

            # get the markdown file name
            file_name = input('What is the Markdown file name? \n>> ')
            # open the markdown file and store in temp file
            
            temp_file = search_md_for_reference_list_flag(file_name, reference_list)
    except OSError as error:
        print('References List does not exist. Create a list by added a new reference')
        print(type(error))
        return type(error)
        

    # re-write markdown with temp file
    with open(file_name, 'w') as file:
        file.writelines(temp_file)

def insert_citations():
    citation_list = []
    try:
        with open('citations.txt', 'r') as file:
            for line in file:
                citation_list.append(line)

            # get the markdown file name
            file_name = input('What is the Markdown file name? \n>> ')
            # open the markdown file and store in temp file
            
            temp_file = search_md_for_citation_flags(file_name, citation_list)
    except OSError as error:
        print('References List does not exist. Create a list by added a new reference')
        print(type(error))
        return type(error)
        

    # re-write markdown with temp file
    with open(file_name, 'w') as file:
        file.writelines(temp_file)

def add_new_reference(filename, input_text, read_or_write):
    try:
        with open(filename, read_or_write) as file:
            if input_text:
                file.write(input_text)
            # Else display error message
            else:
                print('Reference fields are empty. Try again.')
    except OSError as error:
        print('File name not found: %s' % filename)
        print(type(error))
        return type(error)