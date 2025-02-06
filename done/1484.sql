select sell_date, 
    count(sell_date) as num_sold, 
    group_concat(distinct product order by product separator ",") as products
from(
    select distinct sell_date, product from Activities
) as disctinct_products
group by sell_date
order by sell_date