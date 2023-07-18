from __future__ import annotations

from enum import Enum


from .ask_result import AskResult


class AskFlag(Enum):
    """
    Each member represent a flag that could be given by the user when
    the CLI was started.

    Example::

        import sys
        import ask_lib

        flag = ask_lib.AskFlag.YES_TO_ALL if "-Y" in sys.argv else None

        if ask_lib.ask("Delete file ?", flag=flag):
            print("Test")
    """

    YES_TO_ALL = "yes_to_all"
    NO_TO_ALL = "no_to_all"
    DEFAULT_TO_ALL = "default_to_all"

    def truth_value(self, default_option: AskResult) -> bool:
        """
        Returns the boolean representation of the flag based on the default_option.

        Args:
            default_option (AskResult): The default option.

        Returns:
            bool:
                True if YES_TO_ALL, False if NO_TO_ALL, default_option
                if DEFAULT_TO_ALL.
        """
        return {
            AskFlag.YES_TO_ALL: True,
            AskFlag.NO_TO_ALL: False,
            AskFlag.DEFAULT_TO_ALL: default_option,
        }[self]
