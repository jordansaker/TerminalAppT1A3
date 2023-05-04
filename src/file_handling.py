# File handling module
'''
    The module will be a function that receives an argument that is a file name, an argument that contains
    text the will be added to the file, and a flag to specify whether to read or write.
    The file will be opened and to be read or written based on the flag.
'''
def file_handler(filename, file_type, input_text, read_or_write):
    try:
        with open(filename, read_or_write) as f:
            # for line in f:
            #     print(f'Item: {line.strip()}')
            match file_type:
                case '.md':
                    # call md_file_search module
                    pass
                case '.txt':
                    # write input_text to file if TRUE
                    if input_text:
                        f.write(input_text)
                    # Else read from file
                    else:
                        pass
    except OSError as error:
        print('File name not found: %s' % filename)
        print(type(error))
        return type(error)