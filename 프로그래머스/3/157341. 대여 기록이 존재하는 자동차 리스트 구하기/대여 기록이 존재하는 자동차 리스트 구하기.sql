select A.CAR_ID
from CAR_RENTAL_COMPANY_CAR A
where A.CAR_TYPE = '세단'
    and exists (
        select 1
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY B
        where B.CAR_ID = A.CAR_ID and B.START_DATE between '2022-10-01' and '2022-10-31'
    )
order by A.CAR_ID desc