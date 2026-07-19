from dataclasses import dataclass, field
from typing import List


@dataclass
class JobPost:
    role: str
    job_type: str
    location: str
    emails: List[str]
    country: str = "Unknown"
    spam: bool = False

@dataclass
class JobPost:
    role: str
    job_type: str
    location: str
    emails: List[str]
    country: str = "Unknown"
    spam: bool = False
    skills: List[str] = field(default_factory=list)