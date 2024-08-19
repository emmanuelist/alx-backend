#!/usr/bin/env python3

"""
Calculate the start and end index for a given page and page size.
    """


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indices for a given page and page size.

    Parameters:
    page (int): The page number for which to calculate the indices.
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start and end indices for the
    given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
