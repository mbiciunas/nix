import pytest

from cli_config.script_tag import script_tag
from utility.nix_error import NixError


def test_script_tag_add_no_script(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        script_tag.script_tag("nixconfig", ["add"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: script, tags" in _err, "StdErr doesn't contain expected string"


def test_script_tag_add_no_tag(capsys):
    with pytest.raises(SystemExit) as _excinfo:
        script_tag.script_tag("nixconfig", ["add", "script1"])

    _out, _err = capsys.readouterr()

    assert "2" in str(_excinfo.value), "Exception doesn't contain expected string"
    assert len(_out) == 0, "StdOut should be empty, contains: {}".format(_out)
    assert "the following arguments are required: tags" in _err, "StdErr doesn't contain expected string"


def test_script_tag_add_bad_script(capsys):
    with pytest.raises(NixError) as _excinfo:
        script_tag.script_tag("nixconfig", ["add", "badscript", "tag1"])

    _out, _err = capsys.readouterr()

    assert "Unable to find script: badscript" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)


def test_script_tag_add_bad_tag(capsys):
    with pytest.raises(NixError) as _excinfo:
        script_tag.script_tag("nixconfig", ["add", "script1", "badtag"])

    _out, _err = capsys.readouterr()

    assert "Unknown tags: badtag" in str(_excinfo.value)
    assert len(_out) is 0, "StdOut should be empty, contains: {}".format(_out)
    assert len(_err) is 0, "StdErr should be empty, contains: {}".format(_err)
