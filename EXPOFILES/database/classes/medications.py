

from datetime import datetime
from typing import Union


class Medication:
    """
    Class corresponding to the `medications` table in the EVA database
    Attributes:
        :attr:`id`:         ID of the medication. Unique to the medication as the user uploads a
                    medication via the workflow
        :attr:`medName`:    
    """
    def __init__(self) -> None:
        pass

    id: int
    medName: Union[str, None]
    dateFilled: Union[datetime, None]
    refillsLeft: Union[int, None]
    timesPerDay: Union[int, None]
    folderPath: Union[str, None]
