# 분화된 연도(YEAR), 분화된 연도별 대장균 크기의 편차(YEAR_DEV), 대장균 개체의 ID(ID) 를 출력하는 SQL 문을 작성해주세요.

# 분화된 연도별 대장균 크기의 편차는 분화된 연도별 가장 큰 대장균의 크기 - 각 대장균의 크기로 구하며 결과는 연도에 대해 오름차순으로 정렬
# 같은 연도에 대해서는 대장균 크기의 편차에 대해 오름차순으로 정렬해주세요.

select
    YEAR,
    (MAX_SIZE_OF_COLONY - SIZE_OF_COLONY) as YEAR_DEV,
    ID
from (
    select
        year(DIFFERENTIATION_DATE) as YEAR,
        MAX(SIZE_OF_COLONY) over (partition by year(DIFFERENTIATION_DATE)) as MAX_SIZE_OF_COLONY,
        SIZE_OF_COLONY,
        ID
    from ECOLI_DATA
) as t
order by YEAR, YEAR_DEV


