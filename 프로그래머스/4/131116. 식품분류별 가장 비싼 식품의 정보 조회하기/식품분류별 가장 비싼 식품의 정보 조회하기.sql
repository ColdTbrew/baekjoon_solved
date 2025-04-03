# -- 코드를 입력하세요
# SELECT CATEGORY, max(price), product_name
# from food_product
# join (

# )

select b.CATEGORY, b.price as MAX_PRICE, b.PRODUCT_NAME
from food_product b
join (
    select CATEGORY, max(price) as max_price
    from food_product
    group by CATEGORY
) a
on b.price = a.max_price and a.category = b.category
where b.CATEGORY in ('과자', '국', '김치', '식용유')
group by b.CATEGORY
order by b.price desc