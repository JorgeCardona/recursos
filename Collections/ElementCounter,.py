from collections import deque, Counter
from typing import Union, List, Tuple, Deque, Iterable, Any, Optional
from collections import deque
import random
import inspect

class ElementCounter:
    @staticmethod
    def count_element_in_iterable(iterable: Iterable, element: Any) -> int:
        """
        Counts the number of occurrences of an element in an iterable.

        Args:
            iterable (Iterable): The iterable to search in.
            element (Any): The element to count occurrences of.

        Returns:
            int: The number of occurrences of the element in the iterable.

        Raises:
            TypeError: If the object is not an iterable (list, tuple, deque, generator, or str).
        """
        if isinstance(iterable, (list, tuple, deque, str)):
            return iterable.count(element)
        elif inspect.isgenerator(iterable):
            # Convert the generator to a list and then count occurrences
            return list(iterable).count(element)

        raise TypeError("The iterable object must be of type list, tuple, deque, generator, or str.")

    @staticmethod
    def count_elements_occurrences(iterable: Iterable) -> Counter:
        """
        Count the occurrences of each element in an iterable.

        Args:
            iterable (Iterable): The iterable to count elements in.

        Returns:
            collections.Counter: A Counter object containing the counts of each unique element in the iterable.

        Raises:
            TypeError: If the argument 'iterable' is not a valid iterable (e.g., not of type list, tuple, or str).
        """
        if not isinstance(iterable, (list, tuple, str)):
            raise TypeError("The argument 'iterable' must be a valid iterable (e.g., list, tuple, or str).")

        return Counter(iterable)

    @staticmethod
    def get_element_counts_as_dictionary(iterable: Iterable) -> dict:
        """
        Count the occurrences of elements in an iterable and return the counts as a dictionary.

        Args:
            iterable (Iterable): The iterable to count elements in.

        Returns:
            dict: A dictionary with elements as keys and their respective counts as values.
        """
        elements_counted_as_counter = ElementCounter.count_elements_occurrences(iterable)
        return dict(elements_counted_as_counter)

    @staticmethod
    def rotate_iterable_by_index(iterable: Union[List, Tuple, Deque], rotate_value: int) -> Union[List, Tuple, Deque]:
        """
        Rotate the elements of the iterable by a given index value.

        Args:
            iterable (Union[List, Tuple, Deque]): The iterable to rotate elements in.
            rotate_value (int): The number of positions to rotate the elements. A positive value rotates to the right,
                                and a negative value rotates to the left.

        Returns:
            Union[List, Tuple, Deque]: The iterable with its elements rotated by the given index value.

        Raises:
            TypeError: If the object is not a valid iterable (list, tuple, or deque).
        """
        if isinstance(iterable, (list, tuple)):
            rotate_value = rotate_value % len(iterable)  # Ensure that rotate_value is within the range of the iterable
            return iterable[-rotate_value:] + iterable[:-rotate_value]
        elif isinstance(iterable, deque):
            iterable.rotate(rotate_value)
            return iterable
        else:
            raise TypeError("The iterable object must be of type list, tuple, or deque.")
        
    @staticmethod
    def reverse_elements_from_iterable(iterable: Union[List, Tuple, str, Deque]) -> Union[List, Tuple, str, Deque]:
        """
        Reverse the elements of an iterable while preserving the original type.

        This function takes an iterable (e.g., list, tuple, str, or deque) and reverses its elements.
        The function returns a new iterable with the elements reversed while maintaining the original type.

        Args:
            iterable (Union[List, Tuple, str, Deque]): The iterable to reverse.

        Returns:
            Union[List, Tuple, str, Deque]: The reversed iterable with the same type as the original.

        Raises:
            ValueError: If the type of the iterable is not supported (i.e., not list, tuple, str, or deque).

        Examples:
            >>> reverse_elements_from_iterable([1, 2, 3, 4, 5])
            [5, 4, 3, 2, 1]

            >>> reverse_elements_from_iterable((10, 20, 30, 40, 50))
            (50, 40, 30, 20, 10)

            >>> reverse_elements_from_iterable("hello")
            "olleh"

            >>> from collections import deque
            >>> my_deque = deque([1, 2, 3, 4, 5])
            >>> reverse_elements_from_iterable(my_deque)
            deque([5, 4, 3, 2, 1])
        """
        if isinstance(iterable, list):
            return list(reversed(iterable))
        elif isinstance(iterable, tuple):
            return tuple(reversed(iterable))
        elif isinstance(iterable, str):
            return iterable[::-1]
        elif isinstance(iterable, deque):
            reversed_deque = iterable.copy()
            reversed_deque.reverse()
            return reversed_deque
        else:
            raise ValueError("Unsupported iterable type. Supported types are list, tuple, str, and deque.")
    The function reverse_elements_from_iterable now has the updated name while maintaining the same functionality as before.


    @staticmethod
    def pop_element_from_iterable(iterable: Union[List, Deque], side: str = 'right') -> Any:
        """
        Pop an element from an iterable (list or deque) based on the specified side.

        This function pops an element from the given iterable (list or deque) depending on the specified side.
        If the side is 'right', the last element will be popped from the iterable.
        If the side is 'left', the first element will be popped from the iterable.

        Args:
            iterable (Union[List, Deque]): The iterable (list or deque) to pop an element from.
            side (str, optional): The side from which to pop the element. Default is 'right'.
                                Possible values: 'right' (pop the last element),
                                                'left' (pop the first element).

        Returns:
            Any: The popped element from the iterable.

        Raises:
            TypeError: If the iterable is not a valid type (list or deque).
            IndexError: If the iterable is an empty list or deque and 'side' is set to 'left'.

        Examples:
            >>> pop_element_from_iterable([1, 2, 3, 4], side='right')
            4

            >>> pop_element_from_iterable(deque([1, 2, 3, 4]), side='left')
            1

        Note:
            - For a list, popping an element from the 'left' side has linear time complexity O(n),
            where n is the number of elements in the list. Popping from the 'right' side has constant time complexity O(1).
            - For a deque, popping from either side has constant time complexity O(1).
        """
        if isinstance(iterable, list) or isinstance(iterable, deque):
            if side == 'right':
                return iterable.pop()
            elif side == 'left':
                if isinstance(iterable, list):
                    if not iterable:
                        raise IndexError("Cannot pop from an empty list.")
                    return iterable.pop(0)
                else:  # It must be a deque
                    return iterable.popleft()
        else:
            raise TypeError("Iterable must be a list or a deque.")


    @staticmethod
    def generate_integer_list(num_elements: int = 10, with_repetition: bool = True) -> List[int]:
        """
        Generates a list of random integer elements.

        Args:
            num_elements (int): The number of elements in the list (default: 10).
            with_repetition (bool): If True, allows repetition of elements (default: True).

        Returns:
            list: The generated list of integer elements.
        """
        if num_elements <= 0:
            raise ValueError("Number of elements must be greater than zero.")

        if with_repetition:
            # Generate a list with random integers in the range [0, num_elements // 2]
            integer_list = [random.randint(0, num_elements // 2) for _ in range(num_elements)]
        else:
            if num_elements <= num_elements // 2:
                # Use random.sample to generate a list without repetition
                integer_list = random.sample(range(num_elements), num_elements)
            else:
                # If num_elements is greater than num_elements // 2,
                # use a larger range to avoid ValueError in random.sample
                integer_list = random.sample(range(num_elements * 2), num_elements)

        return integer_list
    
    @staticmethod
    def insert_list_into_iterable_at_index(iterable: Union[List, str, Deque], values_list: List, index: int = 0) -> Union[List, str, Deque]:
        """
        Insert a list of elements into an iterable at a specific index.

        This function takes an iterable (e.g., list, string, or deque) and a list of elements,
        and inserts the list into the iterable at the specified index. The elements are inserted
        in reverse order, i.e., from the last element of the list to the first.

        Args:
            iterable (Union[List, str, Deque]): The iterable to which the list will be inserted.
            values_list (List): The list of elements to insert into the iterable.
            index (int, optional): The index at which to insert the list. Default is 0.

        Returns:
            Union[List, str, Deque]: The iterable with the list inserted at the specified index.

        Raises:
            TypeError: If the provided iterable is not a list, a string, or a deque.

        Examples:
            >>> insert_list_into_iterable_at_index([1, 2, 3], [4, 5], index=1)
            [1, 4, 5, 2, 3]

            >>> insert_list_into_iterable_at_index("hello", [0, 1, 2], index=1)
            'h021ello'

            >>> from collections import deque
            >>> my_deque = deque([1, 2, 3])
            >>> insert_list_into_iterable_at_index(my_deque, [4, 5], index=1)
            deque([1, 4, 5, 2, 3])

        Note:
            - For iterables that do not support insertion at a specific index, such as strings and deques,
            the function creates a new iterable with the elements of the list inserted at the specified index.
        """
        if not isinstance(iterable, (list, str, deque)):
            raise TypeError("The iterable must be a list, string, or deque.")

        # For strings and deques, create a new iterable with the elements inserted at the specified index
        if isinstance(iterable, (str, deque)):
            if isinstance(iterable, str):
                return iterable[:index] + ''.join(map(str, values_list)) + iterable[index:]
            else:
                new_deque = deque(iterable)
                for value in reversed(values_list):
                    new_deque.insert(index, value)
                return new_deque

        # For lists, insert the elements at the specified index in-place and return the modified list
        for value in reversed(values_list):
            iterable.insert(index, value)

        return iterable
    
    @staticmethod
    def insert_list_into_iterable(iterable: Union[list, str, deque], elements: Iterable, position: str = 'start') -> Union[list, str, deque]:
        """
        Insert elements from a list into an iterable (list, str, or deque) at the specified position.

        Args:
            iterable (Union[list, str, deque]): The iterable (list, str, or deque) to which the elements will be inserted.
            elements (Iterable): The iterable containing the elements to insert into the target iterable.
            position (str, optional): The position at which to insert the elements. Default is 'start'.
                                      Possible values: 'start' (insert at the beginning),
                                                      'start_reversed' (insert at the beginning with the elements in reversed order),
                                                      'end_reversed' (insert at the end with the elements in reversed order).

        Returns:
            Union[list, str, deque]: The iterable (list, str, or deque) with the elements inserted.

        Raises:
            ValueError: If the 'position' argument is not one of the allowed values.
            TypeError: If the 'iterable' argument is not a valid iterable (list, str, or deque).

        Examples:
            >>> my_list = [1, 2, 3]
            >>> ElementCounter.insert_list_into_iterable(my_list, [4, 5], position='start')
            [4, 5, 1, 2, 3]

            >>> my_string = "hello"
            >>> ElementCounter.insert_list_into_iterable(my_string, [1, 2, 3], position='end_reversed')
            'hello321'

            >>> my_deque = deque([10, 20, 30])
            >>> ElementCounter.insert_list_into_iterable(my_deque, [40, 50], position='start_reversed')
            deque([50, 40, 10, 20, 30])
        """
        if position.lower() == 'start':
            return ElementCounter.insert_list_into_iterable_at_index(iterable, elements, index=0)
        elif position.lower() == 'start_reversed':
            elements_reversed = list(reversed(list(elements)))
            return ElementCounter._insert_elements_into_iterable(iterable, elements_reversed, 'left')
        elif position.lower() == 'end_reversed':
            elements_reversed = list(reversed(list(elements)))
            return ElementCounter._insert_elements_into_iterable(iterable, elements_reversed, 'right')
        else:
            raise ValueError("Invalid value for 'position'. Allowed values: 'start', 'start_reversed', 'end_reversed'.")

    @staticmethod
    def _insert_elements_into_iterable(iterable: Union[list, str, deque], elements: Iterable, side: str) -> Union[list, str, deque]:
        if isinstance(iterable, list):
            if side == 'left':
                return list(elements) + iterable
            elif side == 'right':
                return iterable + list(elements)
        elif isinstance(iterable, str):
            if side == 'left':
                return ''.join(elements) + iterable
            elif side == 'right':
                return iterable + ''.join(elements)
        elif isinstance(iterable, deque):
            if side == 'left':
                iterable.extendleft(elements)
            elif side == 'right':
                iterable.extend(elements)
            return iterable
        else:
            raise TypeError("The 'iterable' argument must be a valid iterable (list, str, or deque).")
        

    def insert_element_into_iterable(element: Any, iterable: Union[list, deque], position: str = 'end', index: int = 0) -> Union[list, deque]:
        """
        Insert an element into an iterable at the specified position.

        Args:
            element (Any): The element to insert into the iterable.
            iterable (Union[list, deque]): The iterable to which the element will be inserted.
            position (str, optional): The position at which to insert the element. Default is 'end'.
                                    Possible values: 'start' (insert at the beginning), 'end' (insert at the end), 'index' (insert at a specific index).
            index (int, optional): The index at which to insert the element. Default is 0.

        Returns:
            Union[list, deque]: The iterable with the element inserted.

        Raises:
            TypeError: If the input iterable is not of type list or deque.
            ValueError: If the position is not 'start', 'end', or 'index'.

        Examples:
            >>> insert_element_into_iterable(0, [1, 2, 3, 4], position='start')
            [0, 1, 2, 3, 4]

            >>> from collections import deque
            >>> insert_element_into_iterable(0, deque([1, 2, 3, 4]), position='end')
            deque([1, 2, 3, 4, 0])

            >>> insert_element_into_iterable(0, [1, 2, 3, 4], position='index', index=2)
            [1, 2, 0, 3, 4]
        """
        if position.lower() not in ('start', 'end', 'index'):
            raise ValueError("The position must be 'start', 'end', or 'index'.")

        if not isinstance(iterable, (list, deque)):
            raise TypeError("The input iterable must be of type list or deque.")

        if position.lower() == 'start':
            if isinstance(iterable, deque):
                iterable.appendleft(element)
            else:
                iterable.insert(0, element)
        elif position.lower() == 'end':
            iterable.append(element)
        elif position.lower() == 'index':
            iterable.insert(index, element)

        return iterable
