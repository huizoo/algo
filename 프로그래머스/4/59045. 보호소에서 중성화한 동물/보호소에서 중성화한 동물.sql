# 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다.
# 보호소에 들어올 당시에는 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의
# 아이디와 생물 종, 이름을 조회
# 아이디 순으로 조회하는 SQL 문을 작성해주세요.

select I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
from ANIMAL_INS I
join ANIMAL_OUTS O
    on I.ANIMAL_ID = O.ANIMAL_ID
where I.SEX_UPON_INTAKE regexp 'Intact'
    and O.SEX_UPON_OUTCOME regexp 'Spayed|Neutered'
order by I.ANIMAL_ID