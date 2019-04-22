### 175. [Combine Two Tables](https://leetcode-cn.com/problems/combine-two-tables/submissions/)

```sql
SELECT Person.FirstName, Person.LastName, Address.City, Address.State 
FROM Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId
```

### 176. [Second Highest Salary](https://leetcode-cn.com/problems/second-highest-salary/)
```sql
SELECT IFNULL((
    SELECT DISTINCT Salary From Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1), null
) as SecondHighestSalary
```

### 177. [Nth Highest Salary](https://leetcode-cn.com/problems/nth-highest-salary/)
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare m int;
SET m = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT IFNULL((
          SELECT DISTINCT Salary FROM Employee
          ORDER BY Salary DESC
          LIMIT 1 OFFSET m), null)
  );
END
```

### 178. [Rank Scores](https://leetcode-cn.com/problems/rank-scores/)
对于每一个分数，找出表中有多少个大于或等于该分数的不同的分数，然后按降序排列即可。
```sql
SELECT Score, (
    SELECT COUNT(DISTINCT(Score)) FROM Scores 
    WHERE Score >= s.Score
) as Rank
FROM Scores s
ORDER BY Score DESC
```

### 180. [Consecutive Numbers](https://leetcode-cn.com/problems/consecutive-numbers/)
我们需要建立三个表的实例，我们可以用l1分别和l2, l3内交，l1和l2的Id下一个位置比，l1和l3的下两个位置比，然后将Num都相同的数字返回即可。
```sql
SELECT DISTINCT L1.Num AS ConsecutiveNums FROM Logs L1
LEFT JOIN Logs L2 ON L1.Id = L2.Id - 1
LEFT JOIN Logs L3 ON L1.Id = L3.Id - 2
WHERE L1.Num = L2.Num and L1.Num = L3.Num
```
