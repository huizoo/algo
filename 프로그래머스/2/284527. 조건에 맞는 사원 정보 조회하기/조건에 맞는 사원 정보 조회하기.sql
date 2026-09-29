# HR_DEPARTMENT, HR_EMPLOYEES, HR_GRADE 테이블에서 2022년도 한해 평가 점수가 가장 높은 사원 정보를 조회하려 합니다.
# 2022년도 평가 점수가 가장 높은 사원들의 점수, 사번, 성명, 직책, 이메일을 조회하는 SQL문을 작성해주세요.

# 2022년도의 평가 점수는 상,하반기 점수의 합을 의미하고, 평가 점수를 나타내는 컬럼의 이름은 SCORE로 해주세요.

select C.SUM_SCORE as SCORE, B.EMP_NO, B.EMP_NAME, B.POSITION, B.EMAIL
from HR_DEPARTMENT A
join HR_EMPLOYEES B
    on A.DEPT_ID = B.DEPT_ID
join (
    select EMP_NO, sum(SCORE) as SUM_SCORE
    from HR_GRADE
    group by EMP_NO
) C
    on B.EMP_NO = C.EMP_NO
order by C.SUM_SCORE desc limit 1
