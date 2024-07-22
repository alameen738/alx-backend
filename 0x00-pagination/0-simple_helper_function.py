#!/usr/bin/env python3
"""
Helper function to calculate the index range for pagination.
"""

def index_range(page, page_size):
    """
    Returns a tuple of (start_index, end_index) corresponding to the range of
    indexes to return in a list for the given pagination parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple of (start_index, end_index) for the requested page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, min(end_index, start_index + page_size))
