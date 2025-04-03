SELECT a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY,sum(b.price*s.sales) as TOTAL_SALES
FROM AUTHOR a
JOIN BOOK b
on a.AUTHOR_ID = b.AUTHOR_ID
join book_sales s
on s.book_id = b.book_id
where year(s.SALES_DATE) = 2022 and month(s.SALES_DATE) = 1
group by a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY
order by a.AUTHOR_ID, b.CATEGORY desc