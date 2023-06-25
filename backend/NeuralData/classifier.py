import warnings

import pandas as pd
from catboost import CatBoostRegressor
import numpy as np
from tqdm import tqdm
import pickle
import datetime
warnings.filterwarnings('ignore')


class ModelReg:
    cat_features = ["Кодзадачи", 'obj_subprg', 'Статуспоэкспертизе', 'Экспертиза', 'season', 'Генподрядчик',
                    'Генпроектировщик']

    def __init__(self, df: pd.DataFrame, pretty: bool = True):
        self.start_df = df

        self.drop_x_cols = ['obj_key', 'y']
        self.model = CatBoostRegressor().load_model('NeuralData/files/cat_model')
        if pretty:
            self.start_df['Время на выполнение'] = 0
            self.df: pd.DataFrame = self.pretty(self.start_df.copy())
        else:
            self.start_df['y'] = 0
            self.df: pd.DataFrame = self.start_df.copy()
        self.new_df: pd.DataFrame = pd.DataFrame()

    def predict(self) -> pd.DataFrame:
        ans = self.model.predict(self.new_df.drop(self.drop_x_cols, axis=1))
        return ans

    @staticmethod
    def find_good_idx(vals: np.ndarray, start_index: int = 12) -> tuple[int, bool]:
        good_idx = 0
        for i in range(start_index, len(vals) - 2):
            if not np.isnan(vals[i]):
                good_idx = i
        if good_idx == 0:
            return 0, False
        else:
            return good_idx, True

    @staticmethod
    def pretty(df: pd.DataFrame) -> pd.DataFrame:
        """
        Я даже документацию под это писать не хочу
        :param df:
        :return: pandas dataframe
        :doc-author: zayycev22
        """
        date_reports = df['date_report'].unique()
        columns = ['obj_key', 'obj_subprg', 'Кодзадачи', 'ДатаНачалаЗадачи', 'Статуспоэкспертизе', 'Экспертиза',
                   'season',
                   'Скорость', 'Кол-во рабочих', 'Генподрядчик', 'Генпроектировщик', 'Площадь', *date_reports, 'y']
        df = df.sort_values(['obj_key', 'Кодзадачи', 'ПроцентЗавершенияЗадачи', 'date_report'])
        new_df = pd.DataFrame(columns=columns)
        keys = df['obj_key'].unique()
        keys.sort()
        for key in tqdm(keys):
            codes = df[df['obj_key'] == key]['Кодзадачи'].unique()
            for code in codes:
                objects = df[(df['obj_key'] == key) & (df['Кодзадачи'] == code)]
                start = objects.head(1)
                last = objects.tail(1)
                obj_key = key
                obj_subprg = last['obj_subprg'].values[0]
                obj_code = code
                start_date = start['ДатаНачалаЗадачи'].values[0]
                status_exp = last['Статуспоэкспертизе'].values[0]
                exp = last['Экспертиза'].values[0]
                season = last['season'].values[0]
                speed = last['Скорость'].values[0]
                rab_count = start['Кол-во рабочих'].values[0]
                gen_pod = last['Генподрядчик'].values[0]
                gen_proc = last['Генпроектировщик'].values[0]
                square = last['Площадь'].values[0]
                y_value = last['Время на выполнение'].values[0]
                dates = objects['date_report'].unique()
                d_dates = {key: np.nan for key in date_reports}
                row_data = [obj_key, obj_subprg, obj_code, start_date, status_exp, exp, season, speed, rab_count,
                            gen_pod,
                            gen_proc, square]
                for date in dates:
                    prc = objects[objects['date_report'] == date].head(1)['ПроцентЗавершенияЗадачи'].values[0]
                    d_dates[date] = prc
                row_data.extend(list(d_dates.values()))
                row_data.append(y_value)
                new_df = new_df.append(pd.Series(row_data, index=columns), ignore_index=True)

        for i, row in new_df.iterrows():
            has_nan = row.isna().any()
            if has_nan:
                vals = row.values
                for j in range(12, len(vals)):
                    if np.isnan(vals[j]):
                        good_idx, ans = ModelReg.find_good_idx(vals, j)
                        if ans:
                            vals[j] = vals[good_idx]
                        else:
                            good_idx, ans = ModelReg.find_good_idx(vals, 12)
                            vals[j] = vals[good_idx]
                new_df.loc[i] = vals

        new_df['Генпроектировщик'] = new_df['Генпроектировщик'].astype(int)
        new_df['Генподрядчик'] = new_df['Генподрядчик'].astype(int)
        new_df['Кол-во рабочих'] = new_df['Кол-во рабочих'].astype(int)
        new_df['ДатаНачалаЗадачи'] = pd.to_datetime(new_df['ДатаНачалаЗадачи']).apply(lambda x: x.toordinal())
        new_df['obj_subprg'] = new_df['obj_subprg'].astype(int)
        new_df['Статуспоэкспертизе'] = new_df['Статуспоэкспертизе'].astype(int)
        new_df['Экспертиза'] = new_df['Экспертиза'].astype(int)
        new_df['season'] = new_df['season'].astype(int)
        new_df['y'] = new_df['y'].astype(int)
        for column in date_reports:
            new_df[column] = new_df[column].astype(int)
        return new_df

    @staticmethod
    def tokenize(df: pd.DataFrame) -> pd.DataFrame:
        with open("NeuralData/files/encoder.pkl", "rb") as f:
            encoder = pickle.load(f)
        encoded_features = encoder.transform(df[ModelReg.cat_features])
        encoded_df = pd.DataFrame(encoded_features.toarray()).reset_index(drop=True)
        df_no_cat = df.drop(ModelReg.cat_features, axis=1).reset_index(drop=True)
        new_data = pd.concat([encoded_df, df_no_cat], axis=1)
        df.drop(ModelReg.cat_features, inplace=True, axis=1)
        new_data.columns = [str(col) for col in
                            new_data.columns]  # добавляем префикс к имени каждой колонки, чтобы избежать дубликатов
        new_df2 = new_data.copy()
        return new_df2

    def get_answer(self) -> pd.DataFrame:
        return self.df

    def main(self) -> None:
        self.new_df = ModelReg.tokenize(self.df.copy())
        self.df['yy'] = self.predict()
        self.df['yy'] = self.df['yy'].apply(lambda x: 0 if x < 0 else x)
        self.df['yy'] = self.df['yy'].round().astype(int)
        self.df['ДатаНачалаЗадачи'] = self.df['ДатаНачалаЗадачи'].apply(lambda x: datetime.date.fromordinal(x))
        self.df['ДатаОкончанияЗадачи'] = self.df['ДатаНачалаЗадачи'] + pd.to_timedelta(self.df['yy'], unit='d')


if __name__ == '__main__':
    #pred_final = pd.read_csv('files\\pred_final.csv')
    times = pd.read_csv('files\\times.csv')
    model = ModelReg(times, pretty=False)
    model.main()
    print(model.df.head(5))
