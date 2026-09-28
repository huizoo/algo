# 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중
# 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고
# 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차

# 에 대해서 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성

select
    A.CAR_ID,
    A.CAR_TYPE,
    floor(A.DAILY_FEE * 30 * (100 - B.DISCOUNT_RATE) / 100) as FEE
from CAR_RENTAL_COMPANY_CAR as A
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as B
    on A.CAR_TYPE = B.CAR_TYPE
    and DURATION_TYPE = '30일 이상'
where A.CAR_TYPE in ('SUV', '세단')
    and A.CAR_ID not in (
        select C.CAR_ID
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY as C
        where C.END_DATE >= DATE('2022-11-01')
            and C.START_DATE <= DATE('2022-11-30')
    )
having FEE >= 500000 and FEE < 2000000
order by FEE desc, A.CAR_TYPE asc, A.CAR_ID desc