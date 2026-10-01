# PRODUCT 테이블과 OFFLINE_SALE 테이블에서 상품코드 별 매출액(판매가 * 판매량) 합계를 출력하는 SQL문을 작성해주세요.
# 결과는 매출액을 기준으로 내림차순 정렬해주시고 매출액이 같다면 상품코드를 기준으로 오름차순 정렬해주세요.

select
    A.PRODUCT_CODE,
    A.PRICE * sum(SALES_AMOUNT) as SALES
from PRODUCT as A
join OFFLINE_SALE as B
    on A.PRODUCT_ID = B.PRODUCT_ID
group by A.PRODUCT_CODE
order by SALES desc, PRODUCT_CODE