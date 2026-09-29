# 물고기 종류 별로 가장 큰 물고기의 ID, 물고기 이름, 길이를 출력하는 SQL 문을 작성해주세요.

# 물고기의 ID 컬럼명은 ID, 이름 컬럼명은 FISH_NAME, 길이 컬럼명은 LENGTH로 해주세요.

# 결과는 물고기의 ID에 대해 오름차순 정렬해주세요.

# 단, 물고기 종류별 가장 큰 물고기는 1마리만 있으며 10cm 이하의 물고기가 가장 큰 경우는 없습니다.

select A.ID, B.FISH_NAME, A.LENGTH
from FISH_INFO A
join FISH_NAME_INFO B
    on A.FISH_TYPE = B.FISH_TYPE
where (A.FISH_TYPE, A.LENGTH) in (
    select FISH_TYPE, MAX(LENGTH) as LENGTH
    from FISH_INFO
    group by FISH_TYPE
    having MAX(LENGTH)
)
order by A.ID