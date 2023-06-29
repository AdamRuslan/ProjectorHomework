-- 1. Find the user with the most reservations
SELECT Users.user_id, Users.username
FROM Users
JOIN Reservations ON Users.user_id = Reservations.guest_id
GROUP BY Users.user_id, Users.username
ORDER BY COUNT(Reservations.reservation_id) DESC
LIMIT 1;

-- 2. Find the host who earned the most money for the last month
SELECT Users.user_id, Users.username AS hostname, SUM(Payments.amount) AS earnings
FROM Users
JOIN Hosts ON Users.user_id = Hosts.host_id
JOIN Rooms ON Hosts.host_id = Rooms.host_id
JOIN Reservations ON Rooms.room_id = Reservations.room_id
JOIN Payments ON Reservations.reservation_id = Payments.reservation_id
WHERE DATE_TRUNC('month', Payments.payment_date) = DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
GROUP BY Users.user_id, Users.username
ORDER BY earnings DESC
LIMIT 1;

-- 3. Find the host with the best average rating
SELECT Users.user_id, Users.username AS hostname, AVG(Reviews.rating) AS avg_rating
FROM Users
JOIN Hosts ON Users.user_id = Hosts.host_id
JOIN Reviews ON Hosts.host_id = Reviews.host_id
GROUP BY Users.user_id, Users.username
ORDER BY avg_rating DESC
LIMIT 1;
