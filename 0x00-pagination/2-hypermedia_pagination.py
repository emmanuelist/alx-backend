#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
import math
from typing import Tuple, List, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Parameters:
    page (int): The page number for which to calculate the indices.
    page_size (int): The number of items per page.

    Returns:
    Tuple[int, int]: A tuple containing the start and end indices for the
    given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
        """
        Find the correct indexes to paginate dataset.

        Parameters:
        page (int): The page number to retrieve. Default is 1.
        page_size (int): The number of records per page. Default is 10.

        Returns:
        List[List]: A list of lists representing the records for the
        specified page. If the start index is out of range, an empty
        list is returned.
        """
        assert isinstance(
            page, int) and page > 0, "Page number must be a \
                positive integer."
        assert isinstance(
            page_size, int) and page_size > 0, "Page size must be \
        a positive integer."

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []  # Return an empty list if start index is out of range

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return dataset as a dictionary with hypermedia pagination details.

        Parameters:
        page (int): The page number to retrieve. Default is 1.
        page_size (int): The number of records per page. Default is 10.

        Returns:
        Dict[str, Any]: A dictionary containing pagination details
        and the data for the specified page.
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
