from collections import deque, Counter
from typing import Union, List, Deque, Iterable, Any, Optional
import random

class DequeGenerator:

    @staticmethod
    def create_bounded_deque(maxlen: Optional[int] = None) -> Deque:
        """
        Create a bounded deque with an optional limit on the number of elements.

        Args:
            maxlen (Optional[int]): The maximum number of elements the deque can hold.
                                    If set to None (default), the deque will be unbounded.

        Returns:
            deque: A new deque with the specified limit on elements or an unbounded deque.
        """
        return deque(maxlen=maxlen) if maxlen is not None else deque()

    @staticmethod
    def create_deque_with_integer_elements(element_count: int = 10, limit_elements: bool = False) -> Deque[int]:
        """
        Create a deque with n integer elements.

        Args:
            element_count (int): The number of integer elements to insert into the deque (default is 10).
            limit_elements (bool): If True, the deque will have a fixed size with 'element_count' elements.
                                   If False (default), the deque will be unbounded and can grow indefinitely.

        Returns:
            Deque[int]: A new deque containing the specified number of integer elements.
        """
        deque_instance = DequeGenerator.create_bounded_deque(maxlen=element_count) if limit_elements else deque()
        list_values = [random.randint(0, element_count // 2) for _ in range(element_count)]
        deque_instance.extend(list_values)
        return deque_instance