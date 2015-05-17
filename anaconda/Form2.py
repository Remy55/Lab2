# coding=utf-8
from spyre import server
import pandas as pd
import numpy as np
import os

class StockExample(server.App):
    title = "Lab2"

    inputs = [{"input_type": 'dropdown',
                'label': "Выбирете область",
                "options": [{"label": "Винницкая", "value": "01"},
                {"label": "Днепропетровская", "value": "02"},
                {"label": "Днепропетровская", "value": "03"},
                {"label": "Донецкая", "value": "04"},
                {"label": "Житомирская", "value": "05"},
                {"label": "Закарпатская", "value": "06"},
                {"label": "Запорожская", "value": "07"},
                {"label": "Івано-Франковская", "value": "08"},
                {"label": "Киевская", "value": "09"},
                {"label": "Кировоградская", "value": "10"},
                {"label": "Луганская", "value": "11"},
                {"label": "Львовськая", "value": "12"},
                {"label": "Николаевская", "value": "13"},
                {"label": "Одесская", "value": "14"},
                {"label": "Полтавская", "value": "15"},
                {"label": "Ровенская", "value": "16"},
                {"label": "Сумская", "value": "17"},
                {"label": "Тернопільскяа", "value": "18"},
                {"label": "Харьковская", "value": "19"},
                {"label": "Херсонская", "value": "20"},
                {"label": "Хмельницкая", "value": "21"},
                {"label": "Черкасская", "value": "22"},
                {"label": "Черновецкая", "value": "23"},
                {"label": "Черниговская", "value": "24"},
                {"label": "Крым", "value": "25"}],
                "variable_name": 'reg',
                "action_id": "update_data"},
                {"input_type": 'dropdown',
                "label": 'Выберите временной ряд',
                "options": [{"label": "VCI", "value": "VCI"},
                {"label": "TCI", "value": "TCI"},
                {"label": "VHI", "value": "VHI"}],
                "variable_name": 'temp',
                "action_id": "update_data"},
                {"input_type": 'text',
                "label": "Выберите год",
                "value": 1982,
                "variable_name": 'year',
                "action_id": 'update_data'},
                {"input_type": "text",
                "variable_name":'from',
                "label": "Выводить данные, начиная с недели",
                "value": 36,
                "action_id": "update_data"},
                {"input_type": "text",
                "variable_name": "to",
                "label": "по",
                "value": 52,
                "action_id": "update_data"}]


    controls = [{"control_type": "hidden",
                "label": "get historical stock prices",
                "control_id": "update_data"}]

    tabs = ["Plot", "Data"]

    outputs = [{"output_type": "plot",
                "output_id": "plot",
                "control_id": "update_data",
                "tab": "Plot",
                "on_page_load": True},
                {"output_type": "table",
                "output_id": "table_id",
                "control_id": "update_data",
                "tab": "Data",
                "on_page_load": True}]

    def getData(self, params):
        df = pd.read_csv('VHI_'+str(params['reg'])+'.csv',index_col=False, header=1)
        df = df.rename(columns={'%Area_VHI_LESS_15': 'extrim', '%Area_VHI_LESS_35': 'temperate'})
        result = df[(df.year == int(params['year']))& (df['week']>=int(params['from']))& (df['week']<=int(params['to']))]
        return result

    def getPlot(self, params):
        df = self.getData(params)
        plt_obj = df.set_index('week').ix[:, params['temp']].plot()
        plt_obj.set_title('Changing'+params['temp'])
        fig = plt_obj.get_figure()
        return fig


app = StockExample()
app.launch(port=9080)