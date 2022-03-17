from tests.test_cases import card_tests
from algorithms.cards import linear
from colorama import Fore


def show_results(result, expected_output, index):
    if result == expected_output:
        print(f"{Fore.WHITE}{card_tests[index]['description']}")
        print(f"{Fore.WHITE}{card_tests[index]['name']} {index}:", end=" ")
        print(f"{Fore.GREEN}True", end="\n\n")
    else:
        print(f"{Fore.WHITE}{card_tests[index]['description']}")
        print(f"{Fore.WHITE}{card_tests[index]['name']} {index}:", end=" ")
        print(f"{Fore.RED}False", end="\n\n")


def testing():
    index = 0
    while index < len(card_tests):
        result = linear(card_tests[index]['input']['query'],
                        card_tests[index]['input']['cards'])
        output = card_tests[index]['output']
        show_results(result, output, index)
        index += 1
