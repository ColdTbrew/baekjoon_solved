-- 코드를 입력하세요
with review_counts as (
    select member_id, count(*) as review_count
    from rest_review
    group by member_id
)
SELECT m.MEMBER_NAME, r.REVIEW_TEXT, DATE_FORMAT(r.review_date, '%Y-%m-%d') as REVIEW_DATE
from member_profile m
join rest_review r on m.member_id = r.member_id
where m.member_id in (
    select member_id
    from review_counts
    where review_count = (
        select max(review_count)
        from review_counts
    )
 )
order by REVIEW_DATE asc, REVIEW_TEXT asc

