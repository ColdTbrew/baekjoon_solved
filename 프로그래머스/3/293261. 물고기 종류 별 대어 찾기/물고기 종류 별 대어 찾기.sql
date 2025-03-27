SELECT i.id AS ID, n.fish_name AS FISH_NAME, i.length AS LENGTH
FROM fish_info i
JOIN fish_name_info n
ON i.FISH_TYPE = n.FISH_TYPE
WHERE i.length = (
    SELECT MAX(length)
    FROM fish_info i2
    WHERE i2.FISH_TYPE = i.FISH_TYPE
)
ORDER BY i.id ASC;