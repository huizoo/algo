# USER_INFO 테이블과 ONLINE_SALE 테이블에서 년, 월, 성별 별로 상품을 구매한 회원수를 집계하는 SQL문을 작성해주세요.

# 결과는 년, 월, 성별을 기준으로 오름차순 정렬해주세요. 이때, 성별 정보가 없는 경우 결과에서 제외해주세요.

select
    year(B.SALES_DATE) as YEAR,
    month(B.SALES_DATE) as MONTH,
    A.GENDER,
    count(distinct A.USER_ID) as USERS
from USER_INFO as A
join ONLINE_SALE as B
    on A.USER_ID = B.USER_ID
where A.GENDER is not null
group by YEAR, MONTH, A.GENDER
order by YEAR, MONTH, A.GENDER