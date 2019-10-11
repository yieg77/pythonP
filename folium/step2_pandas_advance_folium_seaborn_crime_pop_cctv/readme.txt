[[가설 : 인구 대비 CCTV가 적은 지역은 범죄율이 높을 것이다]]


1. 데이터 수집
- 범죄 통계 데이터 수집
- 서울시 관서별 5대 범죄 현황
> https://www.data.go.kr/dataset/3075835/fileData.do
> zip 파일 다운로드
> 해당 파일 풀어서, 2016.csv를 data 폴더에 이동
- 데이터 확인
> 구분 => 310 = 10세트 * 31 (관할서)
  자치구는 총 25개 -> 자치구에 관할서가 반드시 하나는 아니다.
  -> 구분값 -> 경찰서 풀 네임 생성 -> 주소획득 (지오코더 : 구글,카카오API활용)
  -> 자치구가 주소안에 표시 될 것이다.
  -> 관할서의 자치구 값 획득 -> step1의 key인 자치구와 머지가 가능해짐
> 죄종 -> 5대 범죄가 2번씨 세트로 나온다 : 5 * 2 = 10
> 발생검거 -> 2개 반복(발생/검거) -> 발생에 대한 5대범죄 통계, 검거에 대힌 5대 범죄 통계 필요
  -> 관할서 별로 집계 -> 자치구별로 집계 해야 함.
> 건수 -> 정수값
> 데이터를 가공, 정제해서 원하는 통계 분석을 위한 형태로 가기 위해서 필요한 기술
  => 데이터 병합 : concat(), merge()
  => 피벗데이블 : pivot_table()
  
2. 추가 설치 및 업데이트
지도 시각화 라이브러리 설치
pip install folium
머신러닝 라이브러리 업그레이드
pip install scikit-learn --upgrade
고성능 수학 라이브러리 업그레이드
pip install scipy --upgrade

3. 지역명으로 위치 검색 처리
- dev.kakao.com에 가입
- 애플리케이션 생성
- restful 키 획득
- API는 지도관련 사항에서 가서 키워드로 장소검색
- 요청방법 
GET /v2/local/search/keyword.{format} HTTP/1.1
Host: dapi.kakao.com
Authorization: KakaoAK {app_key}
- 응답데이터 (documents의 0번 데이터에서 address_name, y, x, place_name를 취한다)
단, place_name이 온전히 검색어와 일치 할 경우만 해당된다.(이거 통상 0번 데이타)
{
    "documents": [
        {
            "address_name": "서울 중구 저동2가 62-1",
            "category_group_code": "PO3",
            "category_group_name": "공공기관",
            "category_name": "사회,공공기관 > 행정기관 > 경찰서",
            "distance": "",
            "id": "11151738",
            "phone": "182",
            "place_name": "서울중부경찰서",
            "place_url": "http://place.map.daum.net/11151738",
            "road_address_name": "서울 중구 수표로 27",
            "x": "126.98959193048435",
            "y": "37.563620722687844"
        },
        ...
