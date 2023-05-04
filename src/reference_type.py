def common_reference_details_inputs():
    author_name = input('Author Name: ')
    title = input('Title: ')
    date_published = input('Date Published (yyyy): ')
    date_accessed = input('Date Accessed (dd/mm/yyyy): ')
    URL = input('URL: ')

    return author_name, title, date_published, date_accessed, URL


# Type of Reference Functions ----------------------------------
def website_reference_details_inputs():
    website_name = input('Website Name: ')

    return website_name

def book_reference_details_inputs():
    date_originally_published = input('Date Originally Published: ')
    edition = input('Edition: ')
    volume_number = input('Volume Number: ')
    publisher = input('Publisher: ')
    publisher_place = input('Publisher Place: ')
    page_range = input('Page Range: ')
    ISBN = input('ISBN: ')

    return date_originally_published, edition, volume_number, publisher, publisher_place, page_range, ISBN

def journal_reference_details_inputs():
    name_of_journal = input('Journal Name: ')
    volume_number = input('Volume Number: ')
    issue_number = input('Issue Number: ')
    page_range = input('Page Range: ')
    database_name = input('Database Name: ')
    DOI = input('DOI: ')
    
    return name_of_journal, volume_number, issue_number, page_range, database_name, DOI

def video_reference_details_inputs():
    publisher = input('Publisher: ')
    video_format = input('Format: ')

    return publisher, video_format

# Reference Builder functions   --------------------------------   
def website_reference_builder(author_name, title, date_published, date_accessed, website_name, URL):
    
    if author_name:
        author_string = f'{author_name}. '
    elif website_name:
        author_string = f'{website_name}. '
    else:
        author_string = 'anon. '
    
    date_string =  f'{date_published}. ' if date_published else 'n.d ' 

    # generate reference citation


    return author_string + date_string + f'{title}. [online] Available at: {URL} {date_accessed}\n'