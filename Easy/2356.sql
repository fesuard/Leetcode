-- https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description/
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | teacher_id  | int  |
-- | subject_id  | int  |
-- | dept_id     | int  |
-- +-------------+------+
-- Write a solution to calculate the number of unique subjects each teacher teaches in the university.
-- Return the result table in any order.


SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
