import streamlit as st
from streamlit_folium import st_folium
import folium

# 세션 상태에 장소 저장
if 'locations' not in st.session_state:
    st.session_state.locations = []

st.title("📍 나만의 북마크 지도")

# 입력 폼
with st.form("location_form"):
    name = st.text_input("장소 이름")
    lat = st.number_input("위도 (Latitude)", format="%.6f")
    lon = st.number_input("경도 (Longitude)", format="%.6f")
    submitted = st.form_submit_button("➕ 북마크 추가")
    if submitted and name:
        st.session_state.locations.append({"name": name, "lat": lat, "lon": lon})
        st.success(f"✅ '{name}' 장소가 추가되었습니다!")

# Folium 지도 초기화
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)  # 서울 중심

# 저장된 장소 마커 추가
for loc in st.session_state.locations:
    folium.Marker(
        [loc["lat"], loc["lon"]],
        popup=loc["name"],
        tooltip=loc["name"],
        icon=folium.Icon(color="blue", icon="bookmark")
    ).add_to(m)

# 지도 렌더링
st_data = st_folium(m, width=700, height=500)

# 북마크 목록 출력
if st.session_state.locations:
    st.subheader("📋 저장된 북마크 목록")
    for loc in st.session_state.locations:
        st.markdown(f"- **{loc['name']}** ({loc['lat']}, {loc['lon']})")
