from __future__ import annotations

import plotly.express as px

import psycopg2
import psycopg2.extensions
from database.queries.query import getConfirmationsByMedName


def generateReport(conn: psycopg2.extensions.connection, medName: str) -> str:
    file_path = ''
    confirm_data_x = []
    confirm_data_y = []

    confirm_tuples = getConfirmationsByMedName(conn, medName)

    if len(confirm_tuples) > 0:

        file_path = f"EXPOFILES/assets/generatedImages/{medName}.png"

        for confirm in confirm_tuples:
            confirm_data_x.append(confirm.createdAt)
            confirm_data_y.append(confirm.taken)
            

        df = px.data.stocks()
        fig = px.line(df, x=confirm_data_x, y=confirm_data_y)
        fig.write_image(file_path)

    return file_path