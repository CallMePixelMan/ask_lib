"""
Simple module to ask user's confirmation about an action in terminal.
This module provides the ask() function who acts as a wrapper of the input() function.
"""

class AskResult:
    # Symbolic constants for aks_lib, should not be modified
    YES = "yes"
    NO = "no"

class AskFlag:
    # Symbolic constants for aks_lib, should not be modified
    YES_TO_ALL = "yes_to_all"
    NO_TO_ALL = "no_to_all"
    DEFAULT_TO_ALL = "default_to_all"

def ask(message, default_option = AskResult.YES, flag=None) -> bool:
    """Ask user's confirmation about an action.

    Args:
        message (str): The question that will be asked to the user.
        default_option (str,optional): Must be AskResult.YES ("yes"), or AskResult.NO ("no").
            This is the default option if the user doesn't give a response / gives a unsupported response.
        flag (Union[str,None],optional): Must be AskFlag.YES_TO_ALL ("yes_to_all"), AskFlag.NO_TO_ALL ("no_to_all"), 
            AskFlag.DEFAULT_TO_ALL("default_to_all") or None.
            This is a flag who can be used in a CLI when the user want to pass the confirmation.
            
            IF THE FLAG IN NOT None, NO QUESTION WILL BE ASKED TO THE USER !


    Returns:
        bool: True if the user accepted / False if he didn't.
            Will returns True if the user's input is unsupported, and if default_option == AskResult.YES
            Will returns False if the user's input is unsupported, and if default_option == AskResult.NO
            Will returns True if flag == AskFlag.YES_TO_ALL
            Will returns False if flag == AskFlag.NO_TO_ALL
            Will returns default_option if flag == AskFlag.DEFAULT_TO_ALL

    Raises:
        ValueError: If the default option ins't AskResult.YES ("yes"), or AskResult.NO ("no").
        ValueError: If the flag isn't AskFlag.YES_TO_ALL ("yes_to_all"), AskFlag.NO_TO_ALL ("no_to_all"), 
                    AskFlag.DEFAULT_TO_ALL("default_to_all") or None.
    """
    _check_default_option(default_option)
    _check_flag(flag)

    if flag is not None:
        return _process_flag(default_option,flag)

    ending = _message_ending(default_option)
    response = input(message + ending)

    return _process_response(response, default_option)

def _askresult_to_bool(askresult):
    """Convert a AskResult constant to a boolean.

    Returns:
        bool: True if askresult == AskResult.YES ("yes"), False if askresult == AskResult.NO ("no").

    Note:
        You should not use this function, this is an implementation detail for the ask_lib module.
    """
    if askresult == AskResult.YES:
        return True
    elif askresult == AskResult.NO:
        return False

def _check_flag(flag: str) -> None:
    """Check if flag is a supported value for the ask() function.

    Args:
        flag (str)

    Raises:
        ValueError: If the flag isn't AskFlag.YES_TO_ALL ("yes_to_all"), AskFlag.NO_TO_ALL ("no_to_all"), 
                    AskFlag.DEFAULT_TO_ALL("default_to_all") or None.

    Note:
        You should not use this function, this is an implementation detail for the ask() function.
    """
    if flag not in [AskFlag.YES_TO_ALL, AskFlag.NO_TO_ALL, AskFlag.DEFAULT_TO_ALL, None]:  
        raise ValueError(f"'{flag}' isn't a supported flag.")

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

def _process_flag(default_option: str, flag: str):
    """Figures out selected flag, and assign a boolean representation of it.

    Args:
        default_option (str): Must be "yes" or "no". Gives the function the wanted default option if flag is not None.
        flag (str): Must be "yes_to_all", "no_to_all" or "default_to_all". Gives the function the wanted flag.

    Note:
        You should not use this function, this is an implementation detail for the ask() function.
    """
    if flag == AskFlag.YES_TO_ALL:
        return True
    elif flag == AskFlag.NO_TO_ALL:
        return False
    elif flag == AskFlag.DEFAULT_TO_ALL:
        return _askresult_to_bool(default_option)

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