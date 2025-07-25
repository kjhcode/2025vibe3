import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
df = pd.read_csv("202506_202506_연령별인구현황_월간_합계.csv", encoding="cp949")
seoul_row = df.iloc[0]

# 연령별 인구 데이터 추출
age_columns = [col for col in df.columns if '2025년06월_계_' in col and '총인구수' not in col and '연령구간인구수' not in col]
ages = [col.replace('2025년06월_계_', '') for col in age_columns]
population = [int(str(seoul_row[col]).replace(',', '')) if isinstance(seoul_row[col], str) else int(seoul_row[col])
              for col in age_columns]

# 데이터프레임 생성
age_df = pd.DataFrame({'연령': ages, '인구수': population})

# 시각화
st.title("🧓 서울특별시 연령별 인구 분포 (2025년 6월)")
fig = px.bar(age_df, x='연령', y='인구수', labels={'연령': '연령대', '인구수': '인구 수'})
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)
