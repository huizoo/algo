# DEVELOPERS 테이블에서 GRADE별 개발자의 정보를 조회하려 합니다. GRADE는 다음과 같이 정해집니다.

# A : Front End 스킬과 Python 스킬을 함께 가지고 있는 개발자
# B : C# 스킬을 가진 개발자
# C : 그 외의 Front End 개발자
# GRADE가 존재하는 개발자의 GRADE, ID, EMAIL을 조회하는 SQL 문을 작성해 주세요.

# 결과는 GRADE와 ID를 기준으로 오름차순 정렬해 주세요.

select
    case
        when max(case when S.CATEGORY = 'Front End' then 1 else 0 end) = 1
            and max(case when S.NAME = 'Python' then 1 else 0 end) = 1
            then 'A'
        
        when max(case when S.NAME = 'C#' then 1 else 0 end) = 1
            then 'B'
        
        when max(case when S.CATEGORY = 'Front End' then 1 else 0 end) = 1
            then 'C'
        
    end as GRADE,
    D.ID,
    D.EMAIL
           
from DEVELOPERS as D
join SKILLCODES as S
    on (D.SKILL_CODE & S.CODE) = S.CODE

group by D.ID, D.EMAIL
having 
    max(case when S.CATEGORY = 'Front End' then 1 else 0 end) = 1
    or max(case when S.NAME = 'C#' then 1 else 0 end) = 1

order by GRADE, D.ID