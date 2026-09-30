# CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서
# 자동차 종류가 '트럭'인 자동차의 대여 기록에 대해서 대여 기록 별로 대여 금액(컬럼명: FEE)을 구하여 대여 기록 ID와 대여 금액 리스트를 출력하는 SQL문을 작성해주세요. 
# 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 대여 기록 ID를 기준으로 내림차순 정렬해주세요.
 
with RENTAL as (
    select
        H.HISTORY_ID,
        H.CAR_ID,
        datediff(H.END_DATE, H.START_DATE) + 1 as DURATION
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY H
)

select
    R.HISTORY_ID,
    C.DAILY_FEE
        * R.DURATION
        * (100 - coalesce(P.DISCOUNT_RATE, 0)) / 100 as FEE
from RENTAL R
join CAR_RENTAL_COMPANY_CAR C
    on R.CAR_ID = C.CAR_ID
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
    on C.CAR_TYPE = P.CAR_TYPE
    and P.DURATION_TYPE =
        case
            when R.DURATION >= 90 then '90일 이상'
            when R.DURATION >= 30 then '30일 이상'
            when R.DURATION >= 7 then '7일 이상'
        end
where C.CAR_TYPE = '트럭'
order by FEE desc, R.HISTORY_ID desc;