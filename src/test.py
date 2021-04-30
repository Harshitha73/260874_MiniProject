import pytest
import main


def test_show_elements():
    file = open('studentList.txt', 'r')
    assert print("Student List\n\n" + str(file.read())) == main.show_elements()
    file.close()


def test_search():
    file = open('studentList.txt', 'r')
    output = main.search(str(102), file)
    assert print("Record Found\nRoll.No: 102\nName:Sunny") == output
    file.close()


def test_search_element():
    file = open('studentList.txt', 'r')
    output = main.search(str(101), file)
    assert print("Record Found\nRoll.No: 101\nName:Harshitha") == output
    file.close()
