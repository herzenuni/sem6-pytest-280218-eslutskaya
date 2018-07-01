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
    
  #asserts
def test_assert():
    keys = ['123', '45']
    values = ['начало', 'конец']
    expected = { '123': 'начало', '45': 'конец' }

    assert dictn(keys, values) == expected

def test_assert2():
    keys = ['Ключ', 'клюЧ']
    values = ['значение']
    expected = { 'Ключ': 'значение', 'клюЧ': None }

    assert dictn(keys, values) == expected
