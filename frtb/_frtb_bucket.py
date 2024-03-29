from abc import ABCMeta, abstractmethod
from utils.read_files import read_csv_file
from typing import Tuple, List


class FrtbBucket:
    __metaclass__ = ABCMeta
    __slots__ = ["__data", "__file_name"]

    def __init__(self, file_name: str):
        self.__data = None
        self.__file_name = file_name

    def read_file(self):
        return read_csv_file(self.__file_name)

    @abstractmethod
    def get_bucket(self, value: int) -> int:
        pass

    @abstractmethod
    def __get_data_from_line(self, line: List) -> Tuple:
        pass
