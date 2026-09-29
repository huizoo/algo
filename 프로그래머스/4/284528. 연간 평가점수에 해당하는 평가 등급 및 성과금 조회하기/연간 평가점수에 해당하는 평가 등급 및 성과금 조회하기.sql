# HR_DEPARTMENT, HR_EMPLOYEES, HR_GRADE 테이블을 이용해 사원별 성과금 정보를 조회하려합니다.
# 평가 점수별 등급과 등급에 따른 성과금 정보가 아래와 같을 때,
# 사번, 성명, 평가 등급, 성과금을 조회하는 SQL문을 작성해주세요.

# 평가등급의 컬럼명은 GRADE로, 성과금의 컬럼명은 BONUS로 해주세요.
# 결과는 사번 기준으로 오름차순 정렬해주세요.

select
    A.EMP_NO,
    A.EMP_NAME,
    B.GRADE,
    A.SAL * (case
                when B.GRADE = 'S' then 0.2
                when B.GRADE = 'A' then 0.15
                when B.GRADE = 'B' then 0.1
                else 0
            end
        ) as BONUS
from HR_EMPLOYEES as A
join (
    select
        EMP_NO,
        case
            when avg(SCORE) >= 96 then 'S'
            when avg(SCORE) >= 90 then 'A'
            when avg(SCORE) >= 80 then 'B'
            else 'C'
        end as GRADE
    from HR_GRADE
    group by EMP_NO
) as B
    on A.EMP_NO = B.EMP_NO
order by A.EMP_NO