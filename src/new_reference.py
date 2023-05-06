from reference_type import common_reference_details_inputs, website_reference_details_inputs, website_reference_builder, book_reference_details_inputs, book_reference_builder, journal_reference_details_inputs, journal_reference_builder, video_reference_details_inputs, video_reference_builder

def new_reference(temporary_reference_list):
    # ask for reference type
    reference_type = input(
        "\nType of refereence: (Website, Book, Journal, Video)\n Or type 'add' to add references to reference list.\n>> ").lower()
    
    if reference_type in 'add':
        return reference_type, temporary_reference_list
     
    # first call common details function
    author_name, title, date_published, date_accessed, URL = common_reference_details_inputs()
    
    # then call reference type function
    match reference_type:
        case 'website':
            website_name = website_reference_details_inputs()
            # call reference building function for reference type
            reference = website_reference_builder(author_name, title, date_published, date_accessed, website_name, URL)
        case 'book':
            chapter_title, edition, volume_number, publisher, publisher_place, page_range = book_reference_details_inputs()

            reference = book_reference_builder(author_name, title, date_published, date_accessed, URL, chapter_title, edition, volume_number, publisher, publisher_place, page_range)
        case 'journal':
            journal_name, volume_number, issue_number, page_range, database_name, DOI = journal_reference_details_inputs()

            reference = journal_reference_builder(author_name, title, date_published, date_accessed, URL, journal_name, volume_number, issue_number, page_range, database_name, DOI)
        case 'video':
            publisher, video_format = video_reference_details_inputs()

            reference = video_reference_builder(author_name, title, date_published, date_accessed, URL, publisher, video_format)

    # insert new reference to temp list, once user types 'add', add to references.txt
    temporary_reference_list.append(reference)

    return reference_type, temporary_reference_list
   