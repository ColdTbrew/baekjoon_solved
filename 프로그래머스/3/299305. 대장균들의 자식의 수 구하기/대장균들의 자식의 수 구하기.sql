select e.id, count(e2.id) as CHILD_COUNT
from ECOLI_DATA e
left join ECOLI_DATA e2
on e.id = e2.parent_id
group by e.id