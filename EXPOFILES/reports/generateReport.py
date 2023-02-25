from __future__ import annotations
import pandas as pd
import datetime as dt

import plotly.express as px

import psycopg2
import psycopg2.extensions
from database.queries.query import getConfirmationsByMedName


def generateReport(conn: psycopg2.extensions.connection, medName: str,) -> str:
    file_path = ''

    confirm_data = {"date": [], "time": [], "taken": []}
    hours = []

    [hours.append(f'{num}:00') for num in range(24)]

    hours = pd.to_datetime(hours).time

    confirm_tuples = getConfirmationsByMedName(conn, medName)

    if len(confirm_tuples) > 0:

        file_path = f"EXPOFILES/assets/generatedImages/{medName}.png"

        for confirm in confirm_tuples:

            created_date = confirm.createdAt.strftime("%B %d")
            created_time = confirm.createdAt.strftime("%H:%M:%S")
            created_time_int = int(confirm.createdAt.strftime("%H%M"))

            print(confirm.createdAt.strftime("%X"))

            confirm_data["date"].append(confirm.createdAt)
            confirm_data["time"].append(created_time_int)
            confirm_data["taken"].append(confirm.taken)


        confirm_data["date"] = pd.to_datetime(confirm_data["date"]).date
        # confirm_data["time"] = pd.to_datetime(confirm_data["time"]).time

        # [print(f'DATE: {d}') for d in confirm_data["date"]]
        # [print(f'TIME: {d}') for d in confirm_data["time"]]
        # [print(f'HOURS: {d}') for d in hours]

        # print([confirm_data["time"].min(), confirm_data["time"].max()])

        # [print(f'TIME: {d}') for d in confirm_data["time"]]
            
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

        fig.update_layout(
            xaxis={
                'type': 'date',
            },
            # yaxis={
            #     'type': 'date',
            #     # 'tickformat': '%H:%M',
            #     # 'nticks': 24,
            #     # 'tick0': hours[0],
            #     # 'dtick': 3600000,
            #     # 'range': [hours[0], hours[len(hours) - 1]],
            #     # 'autorange': False
            # }
            # xaxis_tickformat = '%B %d\n%Y'
            # yaxis_tickformat=f'%X'
        )

        fig.update_traces(marker=dict(size=18,
                                    line=dict(width=2,
                                                color='DarkSlateGrey')),
                        selector=dict(mode='markers'))

        fig.write_image(file_path)

    return file_path