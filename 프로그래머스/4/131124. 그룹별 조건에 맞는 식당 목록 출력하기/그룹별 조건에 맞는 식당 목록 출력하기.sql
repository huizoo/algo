# MEMBER_PROFILE와 REST_REVIEW 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL문을 작성
# 회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력되도록 작성

# 결과는 리뷰 작성일을 기준으로 오름차순, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬

select A.MEMBER_NAME, B.REVIEW_TEXT, B.REVIEW_DATE
from MEMBER_PROFILE as A
join REST_REVIEW as B
on A.MEMBER_ID = B.MEMBER_ID
where A.MEMBER_ID = (
    select MEMBER_ID
    from REST_REVIEW
    group by MEMBER_ID
    order by count(*) desc limit 1
)
order by B.REVIEW_DATE asc, REVIEW_TEXT asc