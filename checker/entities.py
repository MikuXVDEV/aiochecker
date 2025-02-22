from dataclasses import dataclass

@dataclass
class User:
    mention: str
    is_channel: bool
    channel_link: str