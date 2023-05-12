import pytest
import file_handling
import md_file_search
import reference_type

# check pytest
def test_basic():
    assert 'hello' == 'hello'

# test function for no input arguments
def test_No_Arguments():
    with pytest.raises(Exception):
        file_handling.insert_references_citations()


# check builder functions still run if some inputs are left blank

def test_video_reference_builder():
    assert reference_type.video_reference_builder('author_name', 'title', '', 'date_accessed', '', 'publisher', 'video_format', 'author_name_citation')


def test_website_reference_builder():
    assert reference_type.website_reference_builder('author_name', 'title', 'date_published', '', 'website_name', 'URL', 'author_name_citation')


# test add_new_reference function writes to a file
def test_add_new_references(tmpdir):
    file = tmpdir.join('output.txt')
    file_handling.add_new_reference(file.strpath, 'Ref1\n', 'a+') 
    assert file.read() == 'Ref1\n'


# test md_search_for_references_flag
# a temp file is created and the [\References] flag is added to it
# the md_search_for_reference_list_flag function is called, it's result saved in test
# test is then written to teh temp file and an assertion is made
def test_md_search_references_flag(tmpdir):
    file = tmpdir.join('test.md')
    file_handling.add_new_reference(file.strpath, '[\References]', 'a+')
    test = md_file_search.search_md_for_reference_list_flag(file.strpath, 'Insert refs')
    file_handling.add_new_reference(file.strpath, test, 'w')
    assert file.read() == 'Insert refs\n'

# test search_md_for_citation_flags function
def test_md_search_citation_flags(tmpdir):
    file = tmpdir.join('test.md')
    file_handling.add_new_reference(file.strpath, '[1]', 'a+')
    test = md_file_search.search_md_for_citation_flags(file.strpath, '1')
    file_handling.add_new_reference(file.strpath, test, 'w')
    assert file.read() == '1\n'