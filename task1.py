def dictn(keys, values):
    try:
        if type(keys) is not list or type(values) is not list:
            raise TypeError('Input argument is not a list')
    except TypeError:
        print('Argument is not a list.')
    else:
        result = dict.fromkeys(keys, None)
        result.update(zip(keys, values))
        return result


def test_dictn():
    assert dictn([3,5,7],['t','p','s'])=={3: 't', 5: 'p', 7: 's'}
    assert dictn([1,2,3], 0)==None
    assert dictn(8,['a','b','c'])==None
    assert dictn([],['k','a','t', 'e'])=={}
