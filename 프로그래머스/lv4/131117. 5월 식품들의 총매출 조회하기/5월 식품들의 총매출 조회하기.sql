-- FOOD_PRODUCT와 FOOD_ORDER 테이블에서 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회
-- 결과는 총매출을 기준으로 내림차순 정렬, 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬

SELECT O.PRODUCT_ID, P.PRODUCT_NAME, (P.PRICE*SUM(O.AMOUNT)) AS TOTAL_SALES
FROM FOOD_PRODUCT AS P
INNER JOIN FOOD_ORDER AS O
    ON P.PRODUCT_ID =O.PRODUCT_ID
WHERE O.PRODUCE_DATE LIKE '2022-05%'
GROUP BY O.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, O.PRODUCT_ID;