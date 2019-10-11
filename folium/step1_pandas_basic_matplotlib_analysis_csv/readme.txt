[[데이터 분석 수업 후 실습 방식]]
1. 수업에서 진행하는 데이터를 기준으로 이에 준하는 데이터를 수집하여
   같은 방식으로 다시 분석을 진행한다.
2. 서울시 CCTV 현황과 서울 자치구별 인구에 대한 영향 분석
   => 부산시 CCTV현황과 부산 자치구별 인구에 대한 영향 분석

==========================================================================

1. 서울시의 구별 cctv 현황 분석 (제동되는 데이터기준으로 몇년치)
2. 구별 인구 현황/비율 분석
3. 인구 대비 CCTV 설치 비율
4. 구별로 CCTV 설치 시각화
5. pandas, matplotlib에 대한 사용법 익히는데 주안점을 둔다.

1. 문제제기 :
   인구 대비 CCTV의 설치 수가 적적한가?
2. 가설 :
   (시각화 후 다시 정립)
   인구 대비 cctv가 적은 지역은 범죄율이 높을 것이다
3. 데이터 수집 : (데이터 성격이 통계청, 서울시 공공데이터를 통해서 이미 가공된 데이터를 받아서 사용)
- step1 : 서울시 구별 CCTV 현황 자료
  > 서울 열린 데이터 광장 (http://data.seoul.go.kr/)
    접속이 안될경유 구글검색해서 -> (http://115.84.165.39/dataList/datasetView.do?infId=OA-2734&srvType=C&serviceKind=1&currentPageNo=1&searchValue=&searchKey=)
  > sheet 선택
  > csv 다운로드
  > 현 프로젝트 data폴더로 파일 이동
  > 실습
  > 용도별 CCTV설치현황
  > 부산광역시 주민등록인구통계
  접속이 안될경유 구글검색해서 -> https://opendata.busan.go.kr/detail/viewFileDataDetail.do?docId=3076607&dnCnt=616&page=1&brmNCd=OC0003&updtDt=2018-09-27&nextUpdt=2019-09-21
- step2 : 서울시 구별 인구 현황 자료
  > 구글
  > 서울 열린 데이터 광장
  > 부산 공동 데이터
  https://data.busan.go.kr/main/cmm/CMPubrHome/viewCMPubrHome.do