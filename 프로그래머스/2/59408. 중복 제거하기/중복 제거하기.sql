select count(*)
from (
    select distinct NAME
    from ANIMAL_INS
    where NAME is not null
) as t