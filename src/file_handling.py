# File handling module
'''
    The module contains functions based on specific cases matched in the main loop.
'''
from md_file_search import search_md_for_reference_list_flag, search_md_for_citation_flags
from txt_file_search import reference_search
import re


def insert_references_citations(file_type, read_or_search):
    reference_citation_list = []
    try:
        with open(file_type, 'r') as file:
            for index, line in enumerate(file):
                if file_type in 'references.txt':
                    
                    exp_to_search = re.search('[0-9]', line)

                    if exp_to_search:
                        list_line = line.split(' ')
                        del list_line[0]
                        line = ' '.join(list_line)
                    
                    numbered_reference = f'{index + 1}. {line}'
                    reference_citation_list.append(numbered_reference)
                else:
                    reference_citation_list.append(line)
            add_new_reference('references.txt', reference_citation_list, 'w')
            # get the markdown file name
            if read_or_search in 'read':
                file_name = input(
                    "What is the Markdown file name? (Type '\quit' to exit to main menu) \n>> ")
                if file_name in '\quit':
                    return None
            # open the markdown file and store in temp file
            if file_type in 'references.txt' and read_or_search in 'read':
                temp_file = search_md_for_reference_list_flag(
                    file_name, reference_citation_list)
            elif file_type in 'citations.txt' and read_or_search in 'read':
                temp_file = search_md_for_citation_flags(
                    file_name, reference_citation_list)

    except OSError as error:
        print('References List does not exist. Create a list by added a new reference')
        print(type(error))
        return type(error)

    # search for references
    if file_type in 'references.txt' and read_or_search in 'search':
        reference_number = reference_search(reference_citation_list)
        return reference_number, reference_citation_list
    if file_type in 'citations.txt' and read_or_search in 'search':
        return reference_citation_list
    # re-write markdown with temp file
    if read_or_search in 'read':
        with open(file_name, 'w') as file:
            file.writelines(temp_file)
    else:
        pass

def add_new_reference(filename, input_text, read_or_write):
    try:
        with open(filename, read_or_write) as file:
            if input_text:
                # Else display error message
                for line in input_text:
                    file.write(line)
            else:
                print('Reference fields are empty. Try again.')
    except OSError as error:
        print('File name not found: %s' % filename)
        print(type(error))
        return type(error)
