### 181. [Employees Earning More Than Their Managers](https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/)

解法一：我们可以生成两个实例对象进行内交通过ManagerId和Id，然后限制条件是一个Salary大于另一个。

```sql
SELECT e1.Name AS Employee FROM Employee e1
LEFT JOIN Employee e2 ON e1.ManagerId = e2.Id
WHERE e1.Salary > e2.Salary
```
解法二：自连接

```sql
SELECT e1.Name AS Employee 
FROM Employee e1, Employee e2
WHERE e1.ManagerId = e2.Id and e1.Salary > e2.Salary
```

### 182. [Duplicate Emails](https://leetcode-cn.com/problems/duplicate-emails/)

解法一：自连接

```sql
SELECT DISTINCT p1.Email 
FROM Person p1, Person p2
WHERE p1.Email = p2.Email and p1.Id != p2.Id
```

解法二：分组查询(group by, having)

```sql
SELECT Email FROM Person
GROUP BY Email
HAVING COUNT(*) > 1
```

### 183. [Customers Who Never Order](https://leetcode-cn.com/problems/customers-who-never-order/)

解法一：使用NOT IN

```sql
SELECT Name AS Customers
FROM Customers c 
WHERE c.Id NOT IN (select CustomerId from Orders o)
```

解法二：使用NOT EXISTS

```sql
SELECT c.Name AS Customers
FROM Customers c
WHERE NOT EXISTS (SELECT o.CustomerId FROM Orders o WHERE c.Id = o.CustomerId)
```

### 184. [Department Highest Salary](https://leetcode-cn.com/problems/department-highest-salary/)

```sql
SELECT d.Name AS Department, e.Name AS Employee, t.Salary FROM employee e
INNER JOIN 
(
    SELECT DepartmentId, MAX(Salary) AS Salary
    FROM Employee
    GROUP BY DepartmentId) t
USING(DepartmentId, Salary)
INNER JOIN Department d ON e.DepartmentId = d.Id
```

### 185. [Department Top Three Salary](https://leetcode-cn.com/problems/department-top-three-salaries/)

```sql
SELECT d.Name AS Department, e.Name AS Employee, e.Salary FROM Employee e, Department d
WHERE ( SELECT COUNT(DISTINCT(Salary)) 
    FROM Employee 
    WHERE DepartmentId = e.DepartmentId and Salary > e.Salary) < 3
and e.DepartmentId = d.Id
ORDER BY e.DepartmentId, e.Salary DESC
```
