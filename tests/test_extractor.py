from services.extractor import extract_email


def test_extract_single_email():
    text = "Email: test@example.com"
    assert extract_email(text) == ["test@example.com"]


def test_extract_multiple_emails():
    text = "a@test.com b@test.com"
    assert len(extract_email(text)) == 2


def test_extract_no_email():
    text = "No email here"
    assert extract_email(text) == []