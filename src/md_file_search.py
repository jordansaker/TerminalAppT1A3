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
