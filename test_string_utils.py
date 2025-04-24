import pytest
from string_utils import StringUtils


string_utils = StringUtils()

def test_capitalize():

    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("hello world") == "Hello world"
    
  
    assert string_utils.capitalize("") == ""
    assert string_utils.capitalize("123abc") == "123abc"  # Не меняет цифры

def test_trim():
  
    assert string_utils.trim("   skypro   ") == "skypro"
    assert string_utils.trim("   hello   ") == "hello"
    
   
    assert string_utils.trim("") == ""
    assert string_utils.trim("no_spaces") == "no_spaces"  # Без пробелов

def test_contains():
   
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "y") is True
    
 
    assert string_utils.contains("SkyPro", "U") is False
    assert string_utils.contains("", "a") is False  # Пустая строка

def test_delete_symbol():
   
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    

    assert string_utils.delete_symbol("SkyPro", "") == "SkyPro"  # Удаление пустой строки не меняет исходную строку
    assert string_utils.delete_symbol("", "a") == ""  # Удаление из пустой строки возвращает пустую строку