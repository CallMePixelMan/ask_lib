from ask_lib import AskFlag, AskResult


def test_askresult_bool():
    assert AskResult.YES
    assert not AskResult.NO


def test_arkresult_frombool():
    assert AskResult.from_bool(True) is AskResult.YES
    assert AskResult.from_bool(False) is AskResult.NO


def test_askflag_bool():
    assert AskFlag.YES_TO_ALL.truth_value(AskResult.YES)
    assert AskFlag.YES_TO_ALL.truth_value(AskResult.NO)

    assert not AskFlag.NO_TO_ALL.truth_value(AskResult.YES)
    assert not AskFlag.NO_TO_ALL.truth_value(AskResult.NO)

    assert AskFlag.DEFAULT_TO_ALL.truth_value(AskResult.YES)
    assert not AskFlag.DEFAULT_TO_ALL.truth_value(AskResult.NO)
