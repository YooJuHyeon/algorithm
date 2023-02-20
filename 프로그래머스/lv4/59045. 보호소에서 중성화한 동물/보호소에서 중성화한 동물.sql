-- ANIMAL_OUTS 테이블의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID의 외래 키입니다.
--  보호소에 들어올 당시에는 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회
-- 중성화를 거치지 않은 동물은 성별 및 중성화 여부에 Intact, 중성화를 거친 동물은 Spayed 또는 Neutered라고 표시되어있습니다.

SELECT A1.ANIMAL_ID, A1.ANIMAL_TYPE, A1.NAME
FROM ANIMAL_INS AS A1
INNER JOIN ANIMAL_OUTS AS A2
    ON A1.ANIMAL_ID = A2.ANIMAL_ID
WHERE A1.SEX_UPON_INTAKE LIKE 'Intact%' AND (A2.SEX_UPON_OUTCOME LIKE 'Spayed%' OR A2.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY ANIMAL_ID;