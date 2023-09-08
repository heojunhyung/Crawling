import requests
from bs4 import BeautifulSoup

# 빌보드 실시간 차트 페이지 URL
url = 'https://www.billboard.com/charts/hot-100/'

# HTTP 요청을 보내고 페이지 내용을 가져옵니다.
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 노래 제목과 아티스트 정보가 있는 HTML 요소를 찾습니다.
song_elements = soup.find_all(class_='o-chart-results-listing')

# 결과를 출력합니다.
for song_element in song_elements:
    title = song_element.find(class_='o-chart-results-track-title').text.strip()
    artist = song_element.find(class_='o-chart-results-artist').text.strip()
    print(f"노래 제목: {title}")
    print(f"아티스트: {artist}")
    print("-" * 30)

