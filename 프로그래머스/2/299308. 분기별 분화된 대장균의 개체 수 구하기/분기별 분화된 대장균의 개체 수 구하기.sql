# 각 분기(QUARTER)별 분화된 대장균의 개체의 총 수(ECOLI_COUNT)를 출력하는 SQL 문을 작성해주세요.
# 이때 각 분기에는 'Q' 를 붙이고 분기에 대해 오름차순으로 정렬해주세요. 대장균 개체가 분화되지 않은 분기는 없습니다.


select 
    concat(quarter(DIFFERENTIATION_DATE), 'Q') as QUARTER,
    count(*) as ECOLI_COUNT
from ECOLI_DATA
group by quarter(DIFFERENTIATION_DATE)
order by quarter(DIFFERENTIATION_DATE) 