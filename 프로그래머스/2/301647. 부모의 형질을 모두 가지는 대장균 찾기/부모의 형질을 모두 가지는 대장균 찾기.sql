# ID, PARENT_ID, SIZED_OF_COLONY, DIFFERENTIATION_DATE, GENOTYPE
# id,  부모id,       개체 크기,         분화되어 나온 날짜,     개체의 형질


select 자식.ID, 자식.GENOTYPE, 부모.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA 자식
join ECOLI_DATA 부모 ON 자식.PARENT_ID = 부모.id
where (부모.GENOTYPE & 자식.GENOTYPE) = 부모.GENOTYPE
order by ID
