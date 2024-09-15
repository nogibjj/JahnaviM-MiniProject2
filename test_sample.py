from sample import return_str

def test_return_str():
    assert 'hey' == return_str('hey')
    assert '123' == return_str('123')
    print('Both test cases passed! Returning True')
    return True

test_return_str()