from dataclasses import Field
from typing import Protocol, Dict


class IDataClass(Protocol):
    __dataclass_fields__: Dict[str, Field]
