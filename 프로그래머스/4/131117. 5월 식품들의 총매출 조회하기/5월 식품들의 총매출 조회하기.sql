# 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회하는 SQL문을 작성

# 총매출을 기준으로 내림차순 정렬해주시고 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬

select A.PRODUCT_ID, A.PRODUCT_NAME, sum(A.PRICE * B.AMOUNT) as TOTAL_SALES
from FOOD_PRODUCT as A
join FOOD_ORDER as B
on A.PRODUCT_ID = B.PRODUCT_ID
where MONTH(B.PRODUCE_DATE) = 5
group by PRODUCT_ID
order by TOTAL_SALES desc, A.PRODUCT_ID asc