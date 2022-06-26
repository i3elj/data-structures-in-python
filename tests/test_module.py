from colorama import Fore

from algorithms.cards import *
from algorithms.add_two_numbers import ListNode as ln
from algorithms.add_two_numbers import Solution as sl
from tests.test_cases import card_tests


def show_results(result, expected_output, index):
    """show results"""
    if result == expected_output:
        print(f"{Fore.WHITE}{card_tests[index]['description']}")
        print(f"{Fore.WHITE}{card_tests[index]['name']} {index}:", end=" ")
        print(f"{Fore.GREEN}True", end="\n\n")
    else:
        print(f"{Fore.WHITE}{card_tests[index]['description']}")
        print(f"{Fore.WHITE}{card_tests[index]['name']} {index}:", end=" ")
        print(f"{Fore.RED}False", end="\n\n")


def testing():
    """ This function will apply some algorithm and test it
    using a pre-defined dictonary. """
    index = 0
    while index < len(card_tests):
        result = recursive(card_tests[index]['input']['query'],
                        card_tests[index]['input']['cards'])
        output = card_tests[index]['output']
        show_results(result, output, index)
        index += 1

    # n1 = ln(0, ln(0, ln(7, ln(8, ln(7, ln(2, ln(3)))))))
    # l1 = ln(1, ln(1, ln(4)))

    # solution = sl()
    # node = solution.addTwoNumbers(n1, l1)
    # print(node.val, node.next.val, node.next.next.val)
