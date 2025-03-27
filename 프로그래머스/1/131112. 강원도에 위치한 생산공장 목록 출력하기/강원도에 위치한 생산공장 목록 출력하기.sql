-- 코드를 입력하세요
SELECT FACTORY_ID,	FACTORY_NAME,	ADDRESS
from food_factory
where ADDRESS like '%강원도%'
order by factory_id