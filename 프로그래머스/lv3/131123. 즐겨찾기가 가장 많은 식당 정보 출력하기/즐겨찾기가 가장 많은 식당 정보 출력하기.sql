-- REST_INFO 테이블에서 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회
-- 결과는 음식 종류를 기준으로 내림차순 정렬
-- 왜 HAVING 말고, WHERE절에 서브쿼리를 써써 해야 하는지를 잘 모르겠음
-- 그룹바이에 조건을 주는게 아니니까...

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE FAVORITES IN (SELECT MAX(FAVORITES) FROM REST_INFO GROUP BY FOOD_TYPE)
GROUP BY FOOD_TYPE
# HAVING MAX(FAVORITES)
ORDER BY FOOD_TYPE DESC;