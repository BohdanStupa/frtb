from frtb._frtb_bucket import FrtbBucket
from typing import Tuple, List


class ValueFrtbBucket(FrtbBucket):

    def __init__(self, file_name: str):
        super().__init__(file_name)
        self.__data = {}
        for line in self.read_file():
            key, value = self.__get_data_from_line(line)
            self.__data[key] = value

    def get_bucket(self, value: str) -> int:
        try:
            return self.__data[value]
        except KeyError:
            return -1

    def __get_data_from_line(self, line: List[str]) -> Tuple[str, int]:
        if len(line) != 2 or not line[0].isdigit():
            raise ValueError("Invalid value in line")

        return line[1], int(line[0])
