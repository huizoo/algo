# 2022년 1월의 카테고리 별 도서 판매량을 합산하고, 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력하는 SQL문을 작성

# 결과는 카테고리명을 기준으로 오름차순 정렬해주세요.

select A.CATEGORY, sum(B.SALES) as TOTAL_SALES
from book A
join (
    select BOOK_ID, sum(SALES) as SALES
    from BOOK_SALES
    where SALES_DATE >= '2022-01-01' and SALES_DATE < '2022-02-01'
    group by BOOK_ID
) as B
    on A.BOOK_ID = B.BOOK_ID
group by A.CATEGORY
order by A.CATEGORY