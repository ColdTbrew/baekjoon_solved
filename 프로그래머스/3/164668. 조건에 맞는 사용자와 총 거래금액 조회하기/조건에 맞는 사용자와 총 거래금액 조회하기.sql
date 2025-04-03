SELECT u.USER_ID, u.nickname, sum(b.PRICE) as TOTAL_SALES
from USED_GOODS_USER u
join USED_GOODS_BOARD b
on b.WRITER_ID=u.USER_ID	
where b.STATUS = 'DONE'
group by u.USER_ID, u.nickname
having sum(b.PRICE) >= 700000
order by TOTAL_SALES