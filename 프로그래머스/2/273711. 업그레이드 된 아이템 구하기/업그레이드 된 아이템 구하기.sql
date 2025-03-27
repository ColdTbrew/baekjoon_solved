SELECT 
    ITEM_INFO.ITEM_ID, 
    ITEM_INFO.ITEM_NAME, 
    ITEM_INFO.RARITY
FROM 
    ITEM_INFO
JOIN
    item_tree 
on
    item_info.item_id = item_tree.item_id
WHERE 
    item_tree.parent_item_id in(
        select item_info.item_id
        from item_info
        where rarity = "RARE"
    )

    
ORDER BY 
    ITEM_ID DESC;