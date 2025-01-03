-- https://leetcode.com/problems/class-performance/description
-- Table: Scores
-- Column Name	Type
-- student_id	int
-- student_name	varchar
-- assignment1	int
-- assignment2	int
-- assignment3	int
-- student_id is column of unique values for this table.
-- This table contains student_id, student_name, assignment1, assignment2, and assignment3. Write a
-- solution to calculate the difference in the total score (sum of all 3 assignments) between the
-- highest score obtained by students and the lowest score obtained by them. Return the result table 
-- in any order. The result format is in the following example.


SELECT MAX(total_sum) - MIN(total_sum) as difference_in_scores
FROM  
(SELECT student_id, 
        (assignment1 + assignment2 + assignment3) as total_sum
 FROM Scores
 GROUP BY student_id) as subquery;
