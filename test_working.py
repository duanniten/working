import pytest

from working import convert

def test_check_minutes():
    hora = '9:00 AM to 5:00 PM'
    assert convert(hora) == '09:00 to 17:00' 

def test_check_no_minutes():
    hora = '9 AM to 5 PM'
    assert convert(hora) == '09:00 to 17:00' 

def test_check_first_minutes():
    hora = '9:15 AM to 5 PM'
    assert convert(hora) == '09:15 to 17:00' 

def test_check_last_minutes():
    hora = '9 AM to 5:15 PM'
    assert convert(hora) == '09:00 to 17:15' 

def test_first_pm():
    hora = '9 PM to 5:15 AM'
    assert convert(hora) == '21:00 to 05:15' 

def test_invalid_minutes():
    hora = '9:60 AM to 5:00 PM'
    with pytest.raises(ValueError):
        convert(hora)
    
    hora = '9:00 AM to 5:60 PM'
    with pytest.raises(ValueError):
        convert(hora)

def test_invalid_hour():
    hora = '13:00 AM to 5:00 PM'
    with pytest.raises(ValueError):
        convert(hora)
    
    hora = '9:00 PM to 13:00 AM'
    with pytest.raises(ValueError):
        convert(hora)

def test_invalid_hour():
    hora = '09:00 AM - 5:00 PM'
    with pytest.raises(ValueError):
        convert(hora)

def test_hour_12AM():
    hora = '12:00 AM to 12:00 PM'
    assert convert(hora) == '00:00 to 12:00'
    hora = '12:00 PM to 12:00 AM'
    assert convert(hora) == '12:00 to 00:00'     