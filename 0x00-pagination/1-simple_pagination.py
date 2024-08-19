import math
import csv
from typing import List

# Assuming index_range is already defined above


@staticmethod
def index_range(page: int, page_size: int) -> tuple:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                if len(dataset) < 2:
                    raise ValueError(
                        "The file is empyt or only contains a header row.")
                self.__dataset = dataset[1:]  # Skip the header
            except FileNotFoundError:
                raise ValueError("The file does not exist.")
            except Exception as e:
                raise ValueError(
                    "An error occurredwhile reading the file: " + str(e))

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset."""
        assert isinstance(
            page, int) and page > 0, "Page number must be a positive integer."
        assert isinstance(
            page_size, int) and page_size > 0, "Page sixe must be a positive integer."

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []  # Return an empty list if start index is out of range

        return dataset[start_index:end_index]
