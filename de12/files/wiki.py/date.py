import pandas as pd  # データ分析に用いるライブラリ
import matplotlib.pyplot as plt  # グラフ表示に用いるライブラリ
pd.set_option('display.unicode.east_asian_width', True)  # 表示のずれを少し緩和
plt.rcParams['font.family'] = 'IPAexGothic'  # グラフ表示におけるフォントの指定
data_path = "../de12"
df_data = pd.read_csv(data_path,  encoding="utf-8-sig")
print(df_data.sample(10))