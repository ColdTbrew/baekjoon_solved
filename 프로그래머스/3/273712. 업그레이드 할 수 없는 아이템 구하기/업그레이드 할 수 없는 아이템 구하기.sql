-- 코드를 작성해주세요
select ITEM_ID,	ITEM_NAME,	RARITY
from ITEM_INFO
where item_id not in (
    select parent_item_id
    from item_tree
    where parent_item_id is not null
)
order by item_id desc

# select parent_item_id
# from ITEM_TREE
# where parent_item_id is not null