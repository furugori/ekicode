import sqlite3
import pandas as pd

# csvテーブルのインポート
df = pd.read_csv('ekicode.csv')
# 路線コードと駅順コードのゼロパディング
zf2 = lambda s: s.zfill(2)
df['路線コード'] = df['路線コード'].map(zf2)
df['路線コード'] = df['路線コード'].map(zf2)
df['駅順コード'] = df['駅順コード'].map(zf2)
df['駅順コード'] = df['駅順コード'].map(zf2)
# ダンプ
with sqlite3.connect('ekicode.sqlite3', isolation_level=None) as conn:
    df.to_sql(name='駅コード', con=conn)