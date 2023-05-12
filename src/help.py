from colorist import Color

def help_document():
    print( f'''

        Markdown Harvard Reference Generator - HELP
        
        To choose which option you want, type in the option name. The options across the app are all case-insensitive.

        i.e. For a new reference, type in 'New Reference' or 'new reference'


        {Color.WHITE}New Reference{Color.OFF}

        In the New Reference interface, select the type of reference that you want to add.

        {Color.BLUE}i.e. For a website reference, type in 'website'{Color.OFF}

        Then enter the information of the reference. You can enter as many references as you want each time
        you return to the New Reference interface.

        To add all the references that you've added to a reference list, type in 'add' in the New Reference interface

        {Color.WHITE}Search{Color.OFF}

        In the Search Interface, the reference list is printed. The user can search for a reference using the author's
        last name or the reference number. A search result is returned and printed. The user then can select one of the returned results
        using the reference number.

        The user is then asked what they want to do with the referenece.

        The reference can be rewritten by typing in {Color.YELLOW}'edit'{Color.OFF} OR it can be deleted 
        permenantly by typing in {Color.RED}'\delete'{Color.OFF}

        {Color.WHITE}Inserting Reference List and Citations{Color.OFF}

        This option is only available when there's items on the reference list.
        In the main interface, typing either "Insert References" or "Insert citations" will result in a prompt
        for the markdown file.

        The input for the filename should have the file type extension.

        {Color.BLUE}i.e. If the user wants to insert citations into a markdown file called "References" 
        the input should be {Color.OFF}{Color.WHITE} "References.md"{Color.OFF}

    ''')