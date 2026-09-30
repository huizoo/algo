# 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요.
# 이때 결과는 보호 시작일 순으로 조회해야 합니다.


select I.NAME, I.DATETIME
from ANIMAL_INS I
where I.ANIMAL_ID not in (
    select O.ANIMAL_ID
    from ANIMAL_OUTS O
)
order by I.DATETIME limit 3