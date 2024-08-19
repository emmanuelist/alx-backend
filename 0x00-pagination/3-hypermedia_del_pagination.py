#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a dictionary with key-value pairs (index, next_index,
        page_size, data).

        Parameters:
        index (int): The starting index of the page.
        page_size (int): The number of records per page.

        Returns:
        Dict[str, Any]: A dictionary containing pagination details and
        the data for the specified page.
        """
        assert isinstance(index, int), "Index must be an integer."
        assert isinstance(page_size, int), "Page size must be an integer."
        assert index >= 0, "Index must be a non-negative integer."

        csv = self.indexed_dataset()
        csv_size = len(csv)
        assert index < csv_size, "Index out of range."

        data = []
        next_index = index

        for _ in range(page_size):
            while next_index < csv_size and next_index not in csv:
                next_index += 1
            if next_index >= csv_size:
                break
            data.append(csv[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
