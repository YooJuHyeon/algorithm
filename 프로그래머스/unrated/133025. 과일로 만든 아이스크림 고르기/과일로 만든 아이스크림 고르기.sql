-- 상반기 아이스크림 총 주문량이 3000보다 높다 (TOTAL_ORDER > 3000)
-- 아이스크림의 주 성분이 과일 (INGREDITENT_TYPE = 'fruit_based')
-- 출력은 아이스크림 맛만, 주문량 순으로 DESC

SELECT
    T1.FLAVOR
FROM
    ICECREAM_INFO AS T1
INNER JOIN FIRST_HALF AS T2
    ON T1.FLAVOR = T2.FLAVOR
WHERE
    INGREDIENT_TYPE = 'fruit_based' 
    AND TOTAL_ORDER > 3000
ORDER BY
    TOTAL_ORDER DESC;