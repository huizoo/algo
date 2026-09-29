# 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.
# 이때 결과는 시간대 순으로 정렬해야 합니다.

with recursive HOURS as (
    select 0 as HOUR
    
    union all
    
    select HOUR + 1
    from HOURS
    where HOUR < 23
)

select H.HOUR, count(A.DATETIME) as COUNT
from HOURS H
left join ANIMAL_OUTS A
    on H.HOUR = HOUR(A.DATETIME)
group by H.HOUR
order by H.HOUR