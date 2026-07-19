SPAM_KEYWORDS = [
    "bench",
    "bench sales",
    "marketing",
    "vendor list",
    "consultant available",
]

USA_STATES = {
    "TX", "CA", "NY", "FL", "WA",
    "IL", "NJ", "GA", "PA", "OH"
}


def is_spam(text: str) -> bool:
    text = text.lower()
    return any(keyword in text for keyword in SPAM_KEYWORDS)


def detect_country(location: str) -> str:
    if "," in location:
        state = location.split(",")[-1].strip().upper()
        if state in USA_STATES:
            return "USA"

    return "Unknown"