import pandas as pd
import os
from datetime import datetime


class LoadData:
    def __init__(self) -> None:
        self.__path = os.path.dirname(os.path.realpath(__file__))

    def load(self, transform_html_data):
        data_frame = pd.DataFrame(transform_html_data)

        print(data_frame)

        date = str(datetime.today().timestamp())

        dir_to = self.__path + '/../../../tmp/exported-' + date + '.csv'
        data_frame.to_csv(dir_to)