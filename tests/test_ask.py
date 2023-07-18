import io

import pytest

from ask_lib import ask, AskFlag, AskResult


def test_ask_default(monkeypatch):
    out = io.StringIO()
    monkeypatch.setattr("sys.stdout", out)

    # AskResult.YES
    monkeypatch.setattr("sys.stdin", io.StringIO("y\n"))
    assert ask("Test", AskResult.YES)
    assert out.getvalue() == "Test [Y/n] "
    out.truncate(0)
    out.seek(0)

    monkeypatch.setattr("sys.stdin", io.StringIO("n\n"))
    assert not ask("Test", AskResult.YES)
    assert out.getvalue() == "Test [Y/n] "
    out.truncate(0)
    out.seek(0)

    monkeypatch.setattr("sys.stdin", io.StringIO("unknown\n"))
    assert ask("Test", AskResult.YES)
    assert out.getvalue() == "Test [Y/n] "
    out.truncate(0)
    out.seek(0)

    # AskResult.NO
    monkeypatch.setattr("sys.stdin", io.StringIO("y\n"))
    assert ask("Test", AskResult.NO)
    assert out.getvalue() == "Test [y/N] "
    out.truncate(0)
    out.seek(0)

    monkeypatch.setattr("sys.stdin", io.StringIO("n\n"))
    assert not ask("Test", AskResult.NO)
    assert out.getvalue() == "Test [y/N] "
    out.truncate(0)
    out.seek(0)

    monkeypatch.setattr("sys.stdin", io.StringIO("unknown\n"))
    assert not ask("Test", AskResult.NO)
    assert out.getvalue() == "Test [y/N] "
    out.truncate(0)
    out.seek(0)


def test_ask_flag(monkeypatch):
    out = io.StringIO()
    monkeypatch.setattr("sys.stdout", out)

    assert ask("Test", AskResult.YES, AskFlag.YES_TO_ALL)
    assert ask("Test", AskResult.NO, AskFlag.YES_TO_ALL)

    assert not ask("Test", AskResult.YES, AskFlag.NO_TO_ALL)
    assert not ask("Test", AskResult.NO, AskFlag.NO_TO_ALL)

    assert ask("Test", AskResult.YES, AskFlag.DEFAULT_TO_ALL)
    assert not ask("Test", AskResult.NO, AskFlag.DEFAULT_TO_ALL)

    # No message displayed
    assert out.getvalue() == ""


def test_invalid_result():
    with pytest.raises(ValueError):
        ask("Test", "invalid_result")  # type: ignore


def test_invalid_flag():
    with pytest.raises(ValueError):
        ask("Test", AskResult.YES, "invalid_flag")  # type: ignore
