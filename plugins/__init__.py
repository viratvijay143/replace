import os
from os import environ

# Your Auto Forward Channel ID's
FROM_CHANNELS = set(int(x)
                    for x in os.environ.get("FROM_CHANNELS", "").split())
TO_CHATS = set(int(x) for x in os.environ.get("TO_CHATS", "").split())

# required to Movies information
OMDB_KEY = environ.get("OMDB_KEY", "")

RE1TXT = os.environ.get("RE1TXT", "@vijaysahu_2")
RE2TXT = os.environ.get("RE2TXT", "@vijaysahu_2")
RE3TXT = os.environ.get("RE3TXT", "⚠️ Uploaded By @vijaysahu_2")
RE4TXT = os.environ.get("RE4TXT", "@vijaysahu_2")
RE5TXT = os.environ.get("RE5TXT", "@vijaysahu_2")
RE6TXT = os.environ.get("RE6TXT", "@vijaysahu_2")

# text you want to replace with text above.
REPLACED = os.environ.get("REPLACED", "@AestheticsOfStubborn")

# MEDIA_FORWARD_ID = int(os.environ.get("MEDIA_FORWARD_ID"))
