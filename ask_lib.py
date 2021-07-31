"""
Simple module to ask user's confirmation about an action in terminal.
This module provides the ask() function who acts as a wrapper of the input() function.
"""

class AskResult:
    # Symbolic constants for aks_lib, should not be modified
    YES = "yes"
    NO = "no"

def ask(message, default_option = AskResult.YES) -> bool:
    """Ask user's confirmation about an action.

    Args:
        message (str): The question that will be asked to the user.
        default_option (str,optional): Must be AskResult.YES ("yes"), or AskResult.NO ("no").
            This is the default option if the user doesn't give a response / gives a unsupported response.

    Returns:
        bool: True if the user accepted / False if he didn't.
            Will returns True if the user's input is unsupported, and if default_option == AskResult.YES
            Will returns False if the user's input is unsupported, and if default_option == AskResult.NO

    Raises:
        ValueError: If the default option ins't AskResult.YES ("yes"), or AskResult.NO ("no").
    """
    _check_default_option(default_option)
    ending = _message_ending(default_option)
    response = input(message + ending)

    return _process_response(response, default_option)

def _check_default_option(default_option: str) -> None:
    """Check if default_option is a supported value for the ask() function.
    
    Args:
        default_option (str) 

    Raises:
        ValueError: If the default option ins't AskResult.YES ("yes"), or AskResult.NO ("no").

    Note:
        You should not use this function, this is an implementation detail for the ask() function.
    """
    if default_option not in [AskResult.YES,AskResult.NO]:
        raise ValueError(f"'{default_option}' isn't a supported default option.")

def _message_ending(default_option: str) -> str:
    """Return the correct ending based on the default option given.

    Args:
        default_option (str): Must be "yes" or "no". Gives the function the wanted
            default option if the user doesn't give a response / gives a unsupported response.

    Returns:
        str: Will return " [Y/n] " or " [y/N] ".

    Note:
        You should not use this function, this is an implementation detail for the ask() function.
    """
    if default_option == AskResult.YES:
        return " [Y/n] "
    elif default_option == AskResult.NO:
        return " [y/N] "

def _process_response(response: str, default_option: str) -> bool:
    """Figures out user's input, and assign a boolean representation of it.

    Args:
        response (str): This is the response given by the user.
        default_option (str): Must be "yes" or "no". Gives the function the wanted
            default option if the user doesn't give a response / gives a unsupported response.

    Returns:
        bool: True if the user accepted / False if he didn't.
            Will returns True if the user's input is unsupported, and if default_option == AskResult.YES
            Will returns False if the user's input is unsupported, and if default_option == AskResult.NO

    Note:
        You should not use this function, this is an implementation detail for the ask() function.
    """
    if response.lower() in ["y","o","yes","oui"]:
        return True
    elif response.lower() in ["n","no","non"]:
        return False
    elif default_option == AskResult.YES:
        return True
    elif default_option == AskResult.NO:
        return False