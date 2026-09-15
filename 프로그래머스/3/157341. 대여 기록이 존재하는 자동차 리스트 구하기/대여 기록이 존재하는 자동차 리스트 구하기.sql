select distinct A.CAR_ID 
from CAR_RENTAL_COMPANY_CAR A
inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY B
on A.CAR_ID = B.CAR_ID
where A.CAR_TYPE = '세단' and (B.START_DATE between '2022-10-01' and '2022-10-31')
order by A.CAR_ID desc
