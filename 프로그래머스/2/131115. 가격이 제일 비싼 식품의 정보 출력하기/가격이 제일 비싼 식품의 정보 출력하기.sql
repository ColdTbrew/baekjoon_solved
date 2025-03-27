-- 코드를 입력하세요
with maxprice as(
    select max(price) as maxprice
    from food_product
)
SELECT a.PRODUCT_ID,a.PRODUCT_NAME,a.PRODUCT_CD,a.CATEGORY,a.PRICE
from food_product a, maxprice
where a.price = maxprice