def isadult(age: int) -> bool:
    return age >= 18

def test_is_adult():
    #given
    age = 18

    #when
    result = isadult(age)

    #then
    assert result
    assert isadult(20)

def test_is_not_adult():
    assert not isadult(17)
