select 
    U.USER_ID,
    U.NICKNAME,
    CONCAT(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) as 전체주소,
    CONCAT(SUBSTRING(U.TLNO, 1, 3), '-',  SUBSTRING(U.TLNO, 4, 4), '-', SUBSTRING(U.TLNO, 8, 4)) as 전화번호
from USED_GOODS_USER as U
where U.USER_ID in (
    select B.WRITER_ID
    from USED_GOODS_BOARD as B
    group by B.WRITER_ID
    having count(B.BOARD_ID) >= 3
)
order by U.USER_ID desc

