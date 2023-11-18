import streamlit as st
import pandas as pd
import plotly.express as px

def read_csv(file_path):
    # CSVファイルをShift-JISで読み込む
    df = pd.read_csv(file_path, encoding='shift_jis')

    # 不要な行を削除
    df = df.drop([0, 1, 2, 4], axis=0)

    # 6列目のデータを削除
    df = df.drop(df.columns[5], axis=1)

    # 4行目をヘッダーとして設定
    df.columns = df.iloc[3]

    # 不要な行を削除
    df = df.drop(3, axis=0)

    return df

def plot_line_chart(df, x_col, y_col, title, y_label):
    # 折れ線グラフ
    fig = px.line(df, x=x_col, y=y_col, title=title,
                  labels={y_col: y_label, x_col: 'Date'})

    # レイアウトの調整
    fig.update_layout(height=400, width=800)

    # プロットの表示
    st.plotly_chart(fig)

def plot_bar_chart(df, x_col, y_col, title, y_label):
    # 棒グラフ
    fig = px.bar(df, x=x_col, y=y_col, title=title,
                 labels={y_col: y_label, x_col: 'Date'})

    # レイアウトの調整
    fig.update_layout(height=400, width=800)

    # プロットの表示
    st.plotly_chart(fig)

def main():
    st.title('Weather Data Visualization')

    # サイドバーにCSVファイルのアップロードウィジェットを追加
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file is not None:
        # アップロードされたCSVファイルを読み込み
        data_frame = read_csv(uploaded_file)

        # データのプロット
        st.subheader('Average Temperature Plot')
        plot_line_chart(data_frame, x_col=data_frame.columns[0], y_col=data_frame.columns[1],
                        title='Average Temperature Over Time', y_label='Average Temperature (℃)')

        st.subheader('Total Precipitation Plot')
        plot_bar_chart(data_frame, x_col=data_frame.columns[0], y_col=data_frame.columns[4],
                       title='Total Precipitation Over Time', y_label='Total Precipitation (mm)')

if __name__ == "__main__":
    # Streamlitアプリを実行
    main()
