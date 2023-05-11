import re

def search_md_for_reference_list_flag(md_file, reference_list):
    line_index = 0
    temp_file = []
    with open(md_file, 'r') as file:
        for index, line in enumerate(file):
            temp_file.append(line)
            if line.lower().strip() in '[\\references]':
                line_index = index
        
    temp_file[line_index] = ''.join(reference_list) + '\n'

    return temp_file

def search_md_for_citation_flags(md_file, citation_list):
    line_index = 0
    temp_file = []

    with open(md_file, 'r') as file:
        # get the length of the citation list to get the potential number of citations in the mark down document
        line_index = 0
        temp_file = []

        for index, line in enumerate(file):
            temp_file.append(line)
            for citation_index, citation in enumerate(citation_list):
                
                if line in "\n":
                    pass
                elif f'[{citation_index}]' in line.lower().strip() or \
                        f'[{citation_index}' in line.lower().strip():

                    line_list = line.strip().split(']')
                    line_list = ''.join(line_list)
                    line_list = line_list.strip().split(' ')
                     
                    for char_index, str in enumerate(line_list):

                        exp_to_search = re.search(f'\[{citation_index}', str)
                        exp_to_search_multiple_brackets = re.search(f'\[{citation_index}\[[0-9]', str)
                        exp_to_search_space = re.search(f'\[{citation_index} ', str)
                        exp_to_search_comma= re.search(f'\[{citation_index},', str)
                        exp_to_search_any_character= re.search(f'\[{citation_index}.', str)
                        exp_to_search_newline = re.search(f'\[{citation_index}.\n', str)

                        if exp_to_search_comma:
                            line_list[char_index] = citation.strip() + ','
                        elif exp_to_search_newline:
                            line_list[char_index] = citation.strip() + '.\n'
                        elif exp_to_search_space:
                            line_list[char_index] = citation.strip() + ' '
                        elif exp_to_search_multiple_brackets:
                            new_str_list = line_list[char_index].split('[')
                            
                            spaces_between = []
                            
                            for list_item in new_str_list:
                                if list_item != '':
                                    list_item = '[' + list_item
                                    if list_item in f'\[{citation_index}':
                                        list_item = citation.strip()
                                spaces_between.append(list_item)

                            str_spaces_between = ' '.join(spaces_between)
                            line_list[char_index] = str_spaces_between
                        elif exp_to_search_any_character:
                            line_list[char_index] = citation.strip() + '.'
                        elif exp_to_search:
                            line_list[char_index] = citation.strip()

                        inserted_citation_line = ' '.join(line_list)
                        line = inserted_citation_line
                    line_index = index
        
                    temp_file[line_index] = inserted_citation_line + '\n'

        return temp_file

