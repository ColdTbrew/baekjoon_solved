select year(e1.DIFFERENTIATION_DATE) as year , max_size - e1.size_of_colony as YEAR_DEV, e1.id
from ecoli_data e1
join (
select year(e2.DIFFERENTIATION_DATE) as year , max(e2.size_of_colony) as max_size
from ecoli_data e2
group by year(e2.DIFFERENTIATION_DATE) 
    ) m
on year(e1.DIFFERENTIATION_DATE) = m.year
order by year(e1.DIFFERENTIATION_DATE), YEAR_DEV
