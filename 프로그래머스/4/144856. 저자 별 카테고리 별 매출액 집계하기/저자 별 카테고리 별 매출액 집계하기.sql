# 2022년 1월의 도서 판매 데이터를 기준으로 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여,
# 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력하는 SQL문을 작성해주세요.

# 결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬해주세요.



select A.AUTHOR_ID, B.AUTHOR_NAME, A.CATEGORY, sum(A.PRICE * C.SALES) as TOTAL_SALES
from BOOK as A
join AUTHOR as B
    on A.AUTHOR_ID = B.AUTHOR_ID
join (
    select BOOK_ID, sum(SALES) as SALES
    from BOOK_SALES
    where SALES_DATE between '2022-01-01' and '2022-01-31'
    group by BOOK_ID
) as C
    on A.BOOK_ID = C.BOOK_ID
group by A.AUTHOR_ID, B.AUTHOR_NAME, A.CATEGORY
order by AUTHOR_ID, CATEGORY desc

