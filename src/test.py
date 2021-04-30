import pytest
import main


def test_show_elements():
    file = open('studentList.txt', 'r')
    assert print("Student List\n\n" + str(file.read())) == main.show_elements()
    file.close()
