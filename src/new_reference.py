from reference_type import (common_reference_details_inputs, 
                                website_reference_details_inputs, website_reference_builder, 
                                    book_reference_details_inputs, book_reference_builder, 
                                        journal_reference_details_inputs, journal_reference_builder, 
                                            video_reference_details_inputs, video_reference_builder)

def new_reference(temporary_reference_list, temporary_citation_list):
    # ask for reference type
    reference_type = input(
        "\nType of refereence: (Website, Book, Journal, Video)\n Or type 'add' to add references to reference list. Type '\quit' to return to main (This won't save any references you've added)\n>> ").lower()
    
    if reference_type == 'add':
        return (reference_type, temporary_reference_list,
                 temporary_citation_list)
    elif reference_type == '\quit':
        reference_type = 'add'
        return reference_type, [], []
     
    reference, citation = inputs_function(reference_type)

    # insert new reference to temp list, once user types 'add', add to references.txt
    temporary_reference_list.append(reference)
    # insert citations to temporary citation list
    temporary_citation_list.append(citation)

    return (reference_type, temporary_reference_list,
             temporary_citation_list)
   

def edit_reference(reference_citation_list, 
                   reference_number, reference_or_citation, new_citation):
    # ask for reference type
    if reference_or_citation in 'reference':
        reference_type = input(
        "\nType of refereence: (Website, Book, Journal, Video)\n Or type 'add' to add references to reference list. Type '\quit' to return to main (This won't save any references you've added)\n>> ").lower()
    
        reference, citation = inputs_function(reference_type)

    if reference_or_citation in 'reference':
        reference_citation_list[reference_number] = reference
        return reference_citation_list, citation
    else:
        reference_citation_list[reference_number + 1] = new_citation
        return reference_citation_list
    

def inputs_function(reference_type):
    # first call common details function
    author_name, title, date_published, date_accessed, URL, author_name_citation = common_reference_details_inputs()
    
    # then call reference type function
    match reference_type:
        case 'website':
            website_name = website_reference_details_inputs()
            # call reference building function for reference type
            reference, citation = website_reference_builder(author_name,
                                                             title, date_published, date_accessed, 
                                                                website_name, URL, author_name_citation)
        case 'book':
            chapter_title, edition, volume_number, publisher, publisher_place, page_range = book_reference_details_inputs()

            reference, citation = book_reference_builder(author_name, title, date_published,
                                                          date_accessed, URL, chapter_title, edition,
                                                            volume_number, publisher, publisher_place, page_range,
                                                              author_name_citation)
        case 'journal':
            journal_name, volume_number, issue_number, page_range = journal_reference_details_inputs()

            reference, citation = journal_reference_builder(author_name,
                                                             title, date_published, date_accessed, URL,
                                                               journal_name, volume_number, issue_number,
                                                                 page_range, author_name_citation)
        case 'video':
            publisher, video_format = video_reference_details_inputs()

            reference, citation = video_reference_builder(author_name, title,
                                                           date_published, date_accessed, URL,
                                                             publisher, video_format, author_name_citation)

    return reference, citation