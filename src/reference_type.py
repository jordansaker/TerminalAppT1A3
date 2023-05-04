def common_reference_details_inputs():
    author_name = input('Author Name: ')
    title = input('Title: ')
    date_published = input('Date Published (yyyy): ')
    date_accessed = input('Date Accessed (dd/mm/yyyy): ')

    return author_name, title, date_published, date_accessed

def website_reference_details_inputs():
    website_name = input('Website Name: ')
    URL = input('URL: ')

    return website_name, URL

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