from typing import Optional

from .ask_result import AskResult
from .ask_flag import AskFlag


def ask(
    message,
    default_option=AskResult.YES,
    flag: Optional[AskFlag] = None,
) -> bool:
    """Ask user's confirmation about an action.

    Args:
        message (str): The question that will be asked to the user.
        default_option (str, optional): Default response if users does not give a valid
            response. Must be AskResult.YES, or AskResult.NO.
        flag (AskFlag | None, optional): If not None; does not ask the question and
            return the flag's truth value.

    Returns:
        bool: True if the user accepted / False if he didn't.
            True if the user's input is unsupported and default_option is AskResult.YES
            False if the user's input is unsupported and default_option is AskResult.NO
            True if flag is AskFlag.YES_TO_ALL
            False if flag is AskFlag.NO_TO_ALL
            default_option if flag is AskFlag.DEFAULT_TO_ALL

    Notes:
        If flag is not None, the question will not be displayed.

    Raises:
        ValueError: If the default option ins't AskResult.YES, or AskResult.NO.
        ValueError: If the flag isn't AskFlag.YES_TO_ALL, AskFlag.NO_TO_ALL,
                    AskFlag.DEFAULT_TO_ALL, or None
    """
    if default_option not in (AskResult.YES, AskResult.NO):
        raise ValueError(f"{default_option=} isn't a supported default option.")
    if flag not in (
        AskFlag.YES_TO_ALL,
        AskFlag.NO_TO_ALL,
        AskFlag.DEFAULT_TO_ALL,
        None,
    ):
        raise ValueError(f"{flag=} isn't a supported AskFlag.")

    # Process flag if it exist
    if flag is not None:
        return flag.truth_value(default_option)

    # Display message
    ending = " [Y/n] " if default_option else " [y/N] "
    response = input(message + ending)

    if response.lower() in ("y", "ye", "yes"):
        return True
    elif response.lower() in ("n", "no"):
        return False
    else:
        return bool(default_option)
