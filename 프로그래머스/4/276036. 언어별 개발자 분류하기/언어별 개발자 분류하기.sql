# DEVELOPERS 테이블에서 GRADE별 개발자의 정보를 조회하려 합니다. GRADE는 다음과 같이 정해집니다.

# A : Front End 스킬과 Python 스킬을 함께 가지고 있는 개발자
# B : C# 스킬을 가진 개발자
# C : 그 외의 Front End 개발자
# GRADE가 존재하는 개발자의 GRADE, ID, EMAIL을 조회하는 SQL 문을 작성해 주세요.

# 결과는 GRADE와 ID를 기준으로 오름차순 정렬해 주세요.

with skills as (
    select
        sum(case
            when CATEGORY = 'Front End' then CODE
            else 0
        end) as FRONT_CODE,

        max(case
            when name = 'Python' then CODE
        end) as PYTHON_CODE,

        max(case
            when NAME = 'C#' then CODE
        end) as CSHARP_CODE
    from SKILLCODES
),
GRADED as (
    select
        case
            when (D.SKILL_CODE & S.FRONT_CODE) > 0
                and (D.SKILL_CODE & S.PYTHON_CODE) > 0
                then 'A'

            when (D.SKILL_CODE & S.CSHARP_CODE) > 0
                then 'B'

            when (D.SKILL_CODE & S.FRONT_CODE) > 0
                then 'C'
        end as GRADE,

        D.ID,
        D.EMAIL
    from DEVELOPERS as D
    cross join SKILLS as S
)

select GRADE, ID, EMAIL
from GRADED
where grade is not null
order by GRADE, ID