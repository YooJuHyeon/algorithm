-- ANIMAL_OUTS 테이블의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID의 외래 키
-- 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회 (보호 시작일이 빠른 순으로 조회)

SELECT A1.ANIMAL_ID, A1.NAME
FROM ANIMAL_INS AS A1
INNER JOIN ANIMAL_OUTS AS A2
    ON A1.ANIMAL_ID = A2.ANIMAL_ID
WHERE A1.DATETIME > A2.DATETIME
ORDER BY A1.DATETIME;