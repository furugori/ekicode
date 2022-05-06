import sqlite3
import pandas as pd

# csvテーブルのインポート
df = pd.read_csv('ekicode.csv')
# ダンプ
with sqlite3.connect('ekicode.sqlite3', isolation_level=None) as conn:
    df.to_sql(name='駅コード', con=conn)