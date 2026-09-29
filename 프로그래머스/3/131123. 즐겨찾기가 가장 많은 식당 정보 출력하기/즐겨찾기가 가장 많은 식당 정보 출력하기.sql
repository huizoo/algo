# REST_INFO 테이블에서 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회하는 SQL문을 작성해주세요.
# 이때 결과는 음식 종류를 기준으로 내림차순 정렬해주세요.

select
    A.FOOD_TYPE,
    A.REST_ID,
    A.REST_NAME,
    A.FAVORITES
from REST_INFO A
join (
    select FOOD_TYPE, MAX(FAVORITES) as MAX_FAVORITES
    from REST_INFO
    group by FOOD_TYPE
) as B
    on A.FOOD_TYPE = B.FOOD_TYPE
    and A.FAVORITES = B.MAX_FAVORITES
order by FOOD_TYPE desc
