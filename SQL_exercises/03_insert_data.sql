-- Insert users
INSERT INTO users (name, email) VALUES
('Alba',  'alba@hbtn.com'),
('Enea',  'enea@hbtn.com'),
('Evis',  'evis@hbtn.com'),
('Renis', 'renis@hbtn.com'),
('Sokol', 'sokol@hbtn.com');

-- Insert 20 tasks
INSERT INTO tasks (user_id, description, status, due_date) VALUES
(1, 'Finish MySQL exercises', 'pending', '2025-10-30'),
(1, 'Update project documentation', 'completed', '2025-10-22'),
(2, 'Review pull requests', 'pending', '2025-10-25'),
(2, 'Refactor the login module', 'completed', '2025-10-20'),
(2, 'Fix bug in authentication', 'pending', '2025-10-28'),
(3, 'Write unit tests for book API', 'completed', '2025-10-19'),
(3, 'Plan sprint backlog', 'pending', '2025-10-27'),
(3, 'Update UI design draft', 'pending', '2025-11-01'),
(4, 'Prepare client report', 'completed', '2025-10-21'),
(4, 'Research new framework', 'pending', '2025-11-03'),
(4, 'Organize team meeting', 'completed', '2025-10-23'),
(4, 'Fix CSS alignment issue', 'pending', '2025-10-29'),
(5, 'Optimize SQL queries', 'pending', '2025-10-26'),
(5, 'Test database migrations', 'completed', '2025-10-20'),
(5, 'Write deployment guide', 'pending', '2025-11-02'),
(1, 'Create presentation slides', 'pending', '2025-11-04'),
(2, 'Set up CI/CD pipeline', 'completed', '2025-10-18'),
(3, 'Analyze app performance', 'pending', '2025-10-31'),
(4, 'Clean up unused branches', 'pending', '2025-11-05'),
(5, 'Add comments to code', 'completed', '2025-10-22');
