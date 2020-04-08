from datetime import datetime, timedelta
from typing import Tuple, Iterator, Dict, List
import os
from prettytable import PrettyTable


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ Code segment demonstrating some date_arithmetic operations to perform operations given in the question. """
    date1: str = "27 Feb 2020"
    date2: str = "27 Feb 2019"
    date3: str = "01 Feb 2019"
    date4: str = "30 Sep 2019"
    dt3: datetime = datetime.strptime(date3, "%d %b %Y")
    dt4: datetime = datetime.strptime(date4, "%d %b %Y")
    three_days_after_02272020: datetime = datetime.strptime(date1, "%d %b %Y") + timedelta(days=3)
    three_days_after_02272019: datetime = datetime.strptime(date2, "%d %b %Y") + timedelta(days=3)
    days_passed_01012017_10312017: int = (dt4 - dt3).days
    return three_days_after_02272020, three_days_after_02272019, days_passed_01012017_10312017

def file_reader(path:str, fields, sep=',', header=False) -> Iterator[Tuple[str]]:
    """ The file_reader generator function reads field-separated text files and
    yield a tuple with all of the values from a single line in the file on each call to next()"""
    try:
        fp = open(path, "r")
    except FileNotFoundError:
        print("File not found")
    else:
        with fp:
            line_num: int = 0
            if header == True:
                line_num = 1
                next(fp)
            for line in fp:
                item = tuple(line.strip('\n').split(sep))
                line_num += 1
                try:
                    if len(item) != fields:
                        raise ValueError
                except ValueError:
                    print(f"Value error: {path} has {len(item)} fields on line {line_num} but expected {fields}")
                else:
                    yield item

class FileAnalyzer:
    """ This function searches that directory for Python files (i.e. files ending with .py). For each .py file in the directory, opens each file and calculates a summary of the file including:
    the file name
    the total number of lines in the file
    the total number of characters in the file
    the number of Python functions (lines that begin with ‘def ’, including methods inside class definitions)
    the number of Python classes (lines that begin with ‘class ’)
    """

    def __init__(self, directory: str) -> None:
        """ Your docstring should go here for the description of the method."""
        self.directory: str = directory  # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()
        self.pretty_print()

    def analyze_files(self) -> None:
        """ A method that populate the summarized data into self.files_summary."""
        num_lines: int = 0
        num_class: int = 0
        num_def: int = 0
        num_char: int = 0
        filename: str = ""
        file_list = os.listdir(self.directory)
        for i in range(len(file_list)):
            if file_list[i].endswith(".py"):
                filename = f"{file_list[i]}"
                os.chdir(self.directory)
                fop = open(file_list[i], 'r')
                lines = fop.readlines()
                for item in lines:
                    for char in item:
                        num_char += 1
                    item = item.strip()
                    num_lines += 1
                    if item.startswith("class "):
                        num_class += 1
                    if item.startswith("def "):
                        num_def += 1

                self.files_summary[filename] = {
                    'classes': num_class,  # number of classes in the file
                    'functions': num_def,  # number of functions in the file
                    'lines': num_lines,  # number of lines in the file
                    'characters': num_char
                }
            num_lines = 0
            num_def = 0
            num_class = 0
            num_char = 0
        return self.files_summary

    def pretty_print(self) -> None:
        """ A method that print out the pretty table from the data stored in the """
        pt: PrettyTable = PrettyTable(field_names=['Filename', 'Classes', 'Functions', 'Lines', 'Characters'])
        l: List = []
        for key, value in self.files_summary.items():
            for k, v in value.items():
                l.append(v)
            pt.add_row([key, l[0], l[1], l[2], l[3]])
            l = []
        print(pt)


if __name__ == '__main__':
    print(list(file_reader("test.text", 3, '|', False)))