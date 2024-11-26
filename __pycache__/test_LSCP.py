import Target08 as s02

'''
make a sufficient number of test functions to assure the completeness of the functions you made.
If you can find some failing cases while your code does its work, you will earn an extra point. 
'''

def test_str2num():
    result = s02.str2num("daeju")
    assert result == 157

def test_str2num():
    result = s02.str2num("hwanmin")
    assert result == 155