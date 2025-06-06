SELECT DISTINCT d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
FROM DEVELOPERS d
JOIN SKILLCODES s
ON (d.SKILL_CODE & s.CODE) > 0
WHERE s.NAME IN ('Python', 'C#')
ORDER BY d.ID ASC;