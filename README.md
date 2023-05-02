# Hardvard Referencing for Markdown

### Github repository

URL: https://github.com/jordansaker/TerminalAppT1A3

### Code Styling Conventions

### Features of the Application

- file handling
- structures the inputted strings into a Harvard-style referencing format depending on refernece type
- inserts reference list from **references.txt**, and in-text citations from **citations.txt** into a **.md** file
- allows user to search for numbered references from **.txt** files
- allows user to edit references in **.txt** files and rewrite over the existing file


### Implementation Plan

#### File handling

The file handling feature will be implemented by creating a file_handling module which will be a function that contains a try/except/finally block within this function.

The function will be able to handle a **.txt** and a **.md** file.

The file name will be passed to the function as an argument, the file name coming from a user input. For the **.txt** file, the file can then be changed by adding text to it or if the user is ready to insert the text in the file into a **.md** file, the text is copied and placed into a varible ready to be used to write into the **.md** file.

#### Harvard-style referencing

The application will take inputs from the user, mainly information about a specific source of information that they would like to be referenced too. So the inputs will ask for details such as author's name, date published, date accessed, title, URL, etc. There will be four types of reference sources that can be formatted to the Harvard style. They are websites, books, journals, and videos. For each reference source, a class will be created along with a method for each class to construct the reference using the inputted details. There will also be a method to construct the in-text citation.

#### Inserting reference list and in-text citation into .md file

Copying the reference list and in-text citation from the text files, the application will insert the text into a **.md** file. When the application handles the reference list, it will look for a flag [\reference], and insert the entire reference list below the flag.

For the in-text citation, because the references will be numbered, the flags in the **.md** will correspond to a reference number i.e. [\1] will correspond to reference 1 in the list. The in-text citation for reference 1 will then be inserted and replace the flag.

The following feature will use a search function to find the flags in the **.md** file. In the case of citations, a loop will be used in combination with the serach function to comb the file for flags and input the citations.

#### Search and edit existing references in .txt file

The user will be able to search and edit existing references. Since each reference will be numbered, the user can use the reference number to call up and update the reference.

Another method of editing can be by searching the **.txt** file for the author's name. The search will return and print to the terminal a list of references with matches, including the reference number. The user can then call a reference up using the number.

This feature will use the basic structure of the search function to search through the document.