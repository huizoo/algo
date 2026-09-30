# 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요.
# 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.


select T.ANIMAL_ID, T.NAME
from (
    select
        I.ANIMAL_ID,
        I.NAME,
        (O.DATETIME - I.DATETIME) as DURATION,
        rank() over (order by (O.DATETIME - I.DATETIME) desc) as RNK
    from ANIMAL_INS I
    join ANIMAL_OUTS O
        on I.ANIMAL_ID = O.ANIMAL_ID
) as T
order by T.RNK, T.DURATION desc
limit 2
