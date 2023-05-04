from reference_type import common_reference_details_inputs, website_reference_details_inputs, website_reference_builder

def new_reference(temporary_reference_list):
    # ask for reference type
    reference_type = input(
        "\nType of refereence: (Website, Book, Journal, Video)\n Or type 'add' to add references to reference list.\n>> ").lower()
    
    if reference_type in 'add':
        return reference_type, temporary_reference_list
     
    # first call common details function
    author_name, title, date_published, date_accessed = common_reference_details_inputs()
    # then call reference type function
    website_name, URL = website_reference_details_inputs()
    # call reference building function for reference type
    reference = website_reference_builder(
        author_name, title, date_published, date_accessed, website_name, URL)
    # insert new reference to temp list, once user types 'add', add to references.txt
    temporary_reference_list.append(reference)

    return reference_type, temporary_reference_list
   