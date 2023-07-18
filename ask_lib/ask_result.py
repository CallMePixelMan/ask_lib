from __future__ import annotations

from enum import Enum


class AskResult(Enum):
    """Each member represent the choice of the user, either yes or no."""

    YES = "yes"
    NO = "no"

    @classmethod
    def from_bool(cls, b: bool) -> AskResult:
        """
        Converts a boolean into an AskResult member.

        Args:
            b (bool): The boolean that needs to be converted.

        Returns:
            AskResult: AskResult.YES if True, else AskResult.NO.
        """
        return cls.YES if b else cls.NO

    def __bool__(self):
        return self is AskResult.YES
