import requests
from dateutil.parser import parse

__all__ = ["TAG", "RELEASE_DATE"]

QTILE_METADATA = "https://api.github.com/repos/qtile/qtile/releases/latest"


# Retrieve details of latest Qtile release from github
response = requests.get(QTILE_METADATA)

try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    raise ValueError(f"Unable to retrieve release data from GitHub: {e}")

try:
    latest = response.json()
    TAG = latest["tag_name"]
    RELEASE_DATE = parse(latest["published_at"])
except (requests.exceptions.JSONDecodeError, KeyError) as e:
    raise ValueError(f"Cannot parse release data from GitHub: {e}")
