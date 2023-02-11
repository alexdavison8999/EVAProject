

from datetime import datetime
from typing import Union


class Medication:
    """
    Class corresponding to the `medications` table in the EVA database

    Inputs:
        sql_tuple:          SQL tuple returned from a query to initialize data

    Attributes:
        `id`:               ID of the medication. Unique to the medication as the user uploads a
                            medication via the workflow
        `medName`:          Medication name
        `dateFilled`:       Date the medication was filled, from the bottle scan
        `refillsLeft`:      Amount of refills left for the bottle, from the bottle scan
        `timesPerDay`:      # of times per day the user should be notified to take medication
        `timesPerWeek`:     # of times per week the user should be notified to take medication
        `folderPath`:       Folder path to the image generated from the bottle scan (to be deprecated)
        `createdAt`:        Time in which the medication was added to the DB
    """
    def __init__(self, sql_tuple: tuple) -> None:
        print(sql_tuple)
        self.id = sql_tuple[0]
        self.medName = sql_tuple[1]
        self.dateFilled = sql_tuple[2]
        self.refillsLeft = sql_tuple[3]
        self.timesPerDay = sql_tuple[4]
        self.timesPerWeek = sql_tuple[5]
        self.folderPath = sql_tuple[6]
        self.createdAt = sql_tuple[7]

    id: int
    medName: Union[str, None]
    dateFilled: Union[datetime, None]
    refillsLeft: Union[int, None]
    timesPerDay: Union[int, None]
    timesPerWeek: Union[int, None]
    folderPath: Union[str, None]
    createdAt: Union[datetime, None]
