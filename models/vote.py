from dataclasses import dataclass

@dataclass
class Vote:
    member_id: int
    data_id: int
    status: str