select *
from cinema
where not description = "boring"
and not id%2 = 0
order by rating desc