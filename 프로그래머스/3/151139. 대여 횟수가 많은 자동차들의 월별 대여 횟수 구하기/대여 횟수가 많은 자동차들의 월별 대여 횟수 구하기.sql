-- 코드를 입력하세요
SELECT month(START_DATE), CAR_ID, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where 
    START_DATE between '2022-08-01' and '2022-10-31'
    and car_id in (
        select car_id
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where START_DATE between '2022-08-01' and '2022-10-31'
        group by car_id
        having count(*) >= 5
    )
group by month(START_DATE), CAR_ID
order by month(START_DATE) asc, car_id desc