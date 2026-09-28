# '경제' 카테고리에 속하는 도서들의 도서 ID(BOOK_ID), 저자명(AUTHOR_NAME), 출판일(PUBLISHED_DATE) 리스트를 출력
# 결과는 출판일을 기준으로 오름차순 정렬해주세요.

select B.BOOK_ID, A.AUTHOR_NAME, B.PUBLISHED_DATE
from BOOK as B
join AUTHOR as A
on B.AUTHOR_ID = A.AUTHOR_ID
where B.CATEGORY = '경제'
order by B.PUBLISHED_DATE asc