-- 1. Retrieve all users
--SELECT * FROM users;

-- 2. Display all tasks along with user names
--SELECT t.id, t.description, t.status, t.due_date, u.name AS user_name
--FROM tasks t
--JOIN users u ON t.user_id = u.id;

-- 3. Retrieve all tasks that are still pending
--SELECT * FROM tasks
--WHERE status = 'pending';

-- 4. Find all tasks that are due within the next 7 days
--SELECT *
--FROM tasks
--WHERE due_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 7 DAY);

-- 5. Count the number of tasks assigned to each user
--SELECT u.name AS user_name, COUNT(t.id) AS task_count
--FROM users u
--LEFT JOIN tasks t ON u.id = t.user_id
--GROUP BY u.id, u.name;

-- 6. Update a specific task and mark it as completed
--UPDATE tasks
--SET status = 'completed'
--WHERE id = 1;

-- 7. Delete a user and ensure all their tasks are also removed
--DELETE FROM users
--WHERE id = 1;

-- 8. Display completed tasks along with the user names who completed them
--SELECT t.id, t.description, u.name AS user_name
--FROM tasks t
--JOIN users u ON t.user_id = u.id
--WHERE t.status = 'completed';

-- 9. Find the user with the most assigned tasks
--SELECT u.name AS user_name, COUNT(t.id) AS task_count
--FROM users u
--JOIN tasks t ON u.id = t.user_id
--GROUP BY u.id, u.name
--ORDER BY task_count DESC
--LIMIT 1;

-- 10. Find all users who do not have any assigned tasks
--SELECT u.name AS user_name
--FROM users u
--LEFT JOIN tasks t ON u.id = t.user_id
--WHERE t.id IS NULL;

-- 11. List all tasks assigned after a specific date, along with the user information
--SELECT t.*, u.name AS user_name, u.email
--FROM tasks t
--JOIN users u ON t.user_id = u.id
--WHERE t.due_date > '2025-10-25';

-- 12. Display overdue tasks (past due date) along with the user names assigned to them
SELECT t.id, t.description, t.due_date, u.name AS user_name
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE t.due_date < CURDATE() AND t.status != 'completed';
