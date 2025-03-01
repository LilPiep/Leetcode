select name
from(
    select managerId
    from Employee
    group by managerId
    having count(managerId) >= 5
) as temp
join Employee on Employee.id = temp.managerId