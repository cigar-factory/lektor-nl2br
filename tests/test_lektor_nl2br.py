from lektor_nl2br import _nl2br


def test_no_breaks():
    assert _nl2br("abc") == "abc"


def test_unix():
    assert _nl2br("abc\ndef") == "abc<br>\ndef"


def test_windows():
    assert _nl2br("abc\r\ndef") == "abc<br>\ndef"


def test_multiple():
    assert _nl2br("abc\n\ndef") == "abc<br>\n<br>\ndef"


def test_escaping():
    assert "<script>" not in _nl2br("<script>alert('XSS');</script>")
