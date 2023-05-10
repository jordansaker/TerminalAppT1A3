import re

def reference_search(references_list):
    query_value = ''
    while query_value != '\quit':
        print('\n***** SEARCH *****')
        print('''\n This option allows you to select a reference and edit the entire reference ''')
        print('\nReferences: \n')
        
        for reference in references_list:
            print(f'{reference}')
        
        print('\nSelect a reference above by author\'s last name or by reference number')
        query_value = input("Author's Last Name Or Reference Number (Type '\quit' to exit search):\n>> ")

        if query_value in '\quit':
            return query_value
        elif query_value.isnumeric():
            reference_number = int(query_value)
            print(f'{references_list[reference_number]}')
        else:
            counter = 0
            for reference in references_list:
                split_reference = reference.split(' ')
                exp_to_search = query_value.lower() + ','
                
                for string in split_reference:
                    # end for loop once title block is reached
                    if re.findall("[*]", string):
                        break
                    elif string.lower() in exp_to_search:
                        print(f'\n{reference}')
                        counter += 1
                        break
            if not counter:
                print("\nReference doesn't exist")
        
        print("\nTo edit a reference, select the reference by it's reference number")
        query_value = input("Enter a reference number (Type '\quit' to exit):\n>> ")

        if query_value.isnumeric():
            return int(query_value)
        elif query_value in '\quit':
            return query_value

