#!/usr/bin/env python3
""" Simple pagination
"""

import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                self.__dataset = dataset[1:]  # Skip the header
            except FileNotFoundError:
                raise ValueError("The file does not exist.")
            except Exception as e:
                raise ValueError(
                    "An error occurred while reading the file: " + str(e)
                )

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset.

        Parameters:
        page (int): The page number to retrieve. Default is 1.
        page_size (int): The number of records per page. Default is 10.

        Returns:
        List[List]: A list of lists representing the records for the
        specified page.
                    If the start index is out of range, an empty list is returned.
        """
        assert isinstance(page, int) and page > 0, \
            "Page number must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer."

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []  # Return an empty list if start index is out of range

        return dataset[start_index:end_index]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing a start and end index.

    Parameters:
    page (int): The page number.
    page_size (int): The number of records per page.

    Returns:
    Tuple[int, int]: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
