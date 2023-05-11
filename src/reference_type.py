from file_handling import add_new_reference
import re
import datetime
import calendar

class IncorrectDateFormat(Exception):
    "Incorrect date format. Correct date format is dd/mm/yyyy"
    pass

def common_reference_details_inputs():
    multi_author = input('Multiple Authors? Y/N ').lower()
    author_list = []
    if multi_author in 'y':
        number_of_authors = ''
        while isinstance(number_of_authors, str):
            try:
                number_of_authors = int(input('Number of Authors: '))
            except ValueError as error:
                print('Please enter a number')

        
        for index in range(number_of_authors):
            author_name = input('Author Name: ')
            author_list.append(author_name)
    else:
        author_name = input('Author Name: ')
        author_list.append(author_name)
    title = input('Title: ')
    date_published = input('Date Published (yyyy): ')

    date_format = None
    # get current year
    today = datetime.date.today()
    current_year = today.year
    # create while loop
    while not date_format:
        try:
            date_accessed = input('Date Accessed (dd/mm/yyyy): ')
            day = date_accessed[:2]
            month = date_accessed[3:5]
            year = date_accessed[6:10]
            
            # check for the correct format dd/mm/yyyy
            if day.isnumeric() and month.isnumeric() and year.isnumeric():
                day = int(day)
                month = int(month)
                year = int(year)
                if 0 < day <= 31 and 0 < month <= 12 and current_year >= year > 0:
                    # get get month name
                    month_name = calendar.month_name[month]
                    new_date_accessed = 'viewed ' + f'{day} {month_name} {year}'
                    date_format = True
                else:
                    print('Day or months exceed the 1-31 range for days and 1-12 \
                          for months. Enter new day or month')
            else:
                raise IncorrectDateFormat

        except IncorrectDateFormat:
            print('Incorrect Date format. Correct date format is dd/mm/yyyy')


    URL = "<" + input('URL: ') + ">"

    # cases where user does not input anything
    if len(date_accessed) == 7:
        date_accessed = ''
    if URL in '<>':
        URL = ''
    # rearrange author's name to list surname first then initail
    author_name = ''
    author_name_citation = ''
    for author in author_list:
        mod_author_name = author.split(' ')
        author_name += f'{mod_author_name[-1]}, {mod_author_name[0][:1]}. '
        author_name_citation += f'{mod_author_name[-1]}, '

    return (author_name, title, date_published, 
            new_date_accessed, URL, author_name_citation)


# Type of Reference Functions ----------------------------------
# function to cycle through inputs
def input_reference_detail_loop(input_string):
    reference_details = []
    for index, reference_detail in enumerate(input_string):
        reference_detail = input(input_string[index])
        reference_details.append(reference_detail)
    
    return reference_details


def website_reference_details_inputs():
    website_name = input('Website Name: ')

    return website_name

def book_reference_details_inputs():
    input_strings = ['Chapter Title: ', 'Edition: ', 'Volume Number: ',
                     'Publisher: ', 'Publisher Place: ', 'Page Range: ']

    reference_details = input_reference_detail_loop(input_strings)

    return (reference_details[0], reference_details[1], reference_details[2], 
                reference_details[3], reference_details[4], reference_details[5])

def journal_reference_details_inputs():
    input_strings = ['Journal Name: ', 'Volume Number: ',
                    'Issue Number: ', 'Page Range: ']

    reference_details = input_reference_detail_loop(input_strings)

    return (reference_details[0], reference_details[1], 
                reference_details[2], reference_details[3])


def video_reference_details_inputs():
    input_strings = ['Publisher: ', 'Format: ']
    reference_details = input_reference_detail_loop(input_strings)

    return reference_details[0], reference_details[1]

# Reference Builder functions   --------------------------------   
def website_reference_builder(author_name, title, date_published, 
                              date_accessed, website_name, URL, author_name_citation):
    
    if author_name:
        author_string = author_name
    elif website_name:
        author_string = f'{website_name}. '
    else:
        author_string = 'anon. '
    
    date_string =  f'{date_published}. ' if date_published else 'n.d ' 
    date_string_citation = f'{date_published}' if date_published else 'n.d' 

    # generate reference citation
    citation = '(' + author_name_citation + date_string_citation + ')\n'

    return (author_string + date_string + 
                f'*{title}*. {website_name} [online] Available at: {URL}, {date_accessed}\n',
                    citation)

def book_reference_builder(author_name, title, date_published, date_accessed,
                            URL, chapter_title, edition, volume_number,
                              publisher, publisher_place, page_range, author_name_citation):
    if chapter_title:
        new_chapter_title = chapter_title + ' in'
    else:
        new_chapter_title = ''
    if volume_number:
        new_volume_number = 'vol. ' + volume_number
    else:
        new_volume_number = ''
    if page_range:
        new_page_range = 'pp. ' + page_range
    else:
        new_page_range = ''

    # generate citation
    citation = '(' + author_name_citation + date_published + ')\n'

    return f"{author_name} {date_published}. {new_chapter_title} \
        *{title}*, {edition}, {new_volume_number}, {publisher}, \
            {publisher_place}, {new_page_range}. {date_accessed} {URL}" + '\n', citation

def journal_reference_builder(author_name, title, date_published,
                                date_accessed, URL, journal_name, volume_number, issue_number,
                                  page_range, author_name_citation):
    
    if volume_number:
        new_volume_number = 'vol. ' + volume_number
    else:
        new_volume_number = ''
    if issue_number:
        new_issue_number = 'vol. ' + issue_number
    else:
        new_issue_number = ''
    if page_range:
        new_page_range = 'pp. ' + page_range
    else:
        new_page_range = ''
    
    # generate citation
    citation = '(' + author_name_citation + date_published + ')\n'

    return f"{author_name} {date_published}. '{title}', \
          *{journal_name}*, {new_volume_number}, {new_issue_number}, {new_page_range}. \
              {date_accessed}, {URL}" + '\n', citation

def video_reference_builder(author_name, title, date_published, date_accessed,
                             URL, publisher, video_format, author_name_citation):
    if URL:
        new_URL = 'Available at: ' + URL
    else:
        new_URL = ''
    
    # generate citation
    citation = '(' + author_name_citation + date_published + ')\n'
    
    return f"{author_name} *{title}* {date_published}. \
          {video_format} {publisher} {new_URL} {date_accessed}" + '\n', citation