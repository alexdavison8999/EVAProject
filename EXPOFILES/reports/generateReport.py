from __future__ import annotations

import plotly.express as px

import psycopg2
import psycopg2.extensions
from database.queries.query import getConfirmationsByMedName


def generateReport(conn: psycopg2.extensions.connection, medName: str,) -> str:
    file_path = ''

    confirm_data = {"date": [], "time": [], "taken": []}

    confirm_tuples = getConfirmationsByMedName(conn, medName)

    if len(confirm_tuples) > 0:

        file_path = f"EXPOFILES/assets/generatedImages/{medName}.png"

        for confirm in confirm_tuples:

            created_date = confirm.createdAt.strftime("%B %d")
            created_time = confirm.createdAt.strftime("%H:%M:%S")
            created_time_int = int(confirm.createdAt.strftime("%H%M"))

            confirm_data["date"].append(created_date)
            confirm_data["time"].append(created_time_int)
            confirm_data["taken"].append(confirm.taken)
            
        fig = px.scatter(
            confirm_data, 
            x="date", 
            y="time", 
            color="taken",
            opacity=0.5,
            labels={
                "date": "Date",
                "time": "Time of Day (HH:MM)",
                "taken": "Confirm Result"
            },
            color_discrete_sequence=['green', 'red']
        )

        fig.update_yaxes(range=[0,2400])

        # fig.update_layout(
        #     yaxis={
        #         'type': 'date'   
        #     }
        #     # yaxis_tickformat = '%H:%M'
        # )

        fig.update_traces(marker=dict(size=18,
                                    line=dict(width=2,
                                                color='DarkSlateGrey')),
                        selector=dict(mode='markers'))

        fig.write_image(file_path)

    return file_path