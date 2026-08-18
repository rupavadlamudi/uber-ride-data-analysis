-- ============================================
-- UBER DATA ANALYSIS - SQL QUERIES
-- ============================================
create database uber_project;
USE uber_project;
select * from uber_Cleaned;

-- 1. Total bookings
SELECT 
    COUNT(*) AS total_bookings
FROM uber_cleaned;


-- 2. Booking status distribution
SELECT 
    `Booking Status`,
    COUNT(*) AS total_bookings,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM uber_cleaned), 2) AS percentage
FROM uber_cleaned
GROUP BY `Booking Status`
ORDER BY total_bookings DESC;


-- 3. Bookings by vehicle type
SELECT 
    `Vehicle Type`,
    COUNT(*) AS total_bookings
FROM uber_cleaned
GROUP BY `Vehicle Type`
ORDER BY total_bookings DESC;


-- 4. Revenue / Booking Value by vehicle type
SELECT 
    `Vehicle Type`,
    COUNT(*) AS bookings,
    ROUND(SUM(`Booking Value`), 2) AS total_booking_value,
    ROUND(AVG(`Booking Value`), 2) AS average_booking_value
FROM uber_cleaned
WHERE `Booking Value` IS NOT NULL
GROUP BY `Vehicle Type`
ORDER BY total_booking_value DESC;


-- 5. Top 10 pickup locations
SELECT 
    `Pickup Location`,
    COUNT(*) AS total_bookings
FROM uber_cleaned
GROUP BY `Pickup Location`
ORDER BY total_bookings DESC
LIMIT 10;


-- 6. Top 10 drop locations
SELECT 
    `Drop Location`,
    COUNT(*) AS total_bookings
FROM uber_cleaned
GROUP BY `Drop Location`
ORDER BY total_bookings DESC
LIMIT 10;


-- 7. Cancellation analysis
SELECT 
    `Booking Status`,
    COUNT(*) AS cancellations
FROM uber_cleaned
WHERE `Booking Status` IN (
    'Cancelled by Customer',
    'Cancelled by Driver'
)
GROUP BY `Booking Status`
ORDER BY cancellations DESC;


-- 8. Customer cancellation reasons
SELECT 
    `Reason for cancelling by Customer`,
    COUNT(*) AS cancellation_count,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*)
         FROM uber_cleaned
         WHERE `Reason for cancelling by Customer` IS NOT NULL),
        2
    ) AS percentage
FROM uber_cleaned
WHERE `Reason for cancelling by Customer` IS NOT NULL
GROUP BY `Reason for cancelling by Customer`
ORDER BY cancellation_count DESC;


-- 9. Driver cancellation reasons
SELECT 
    `Driver Cancellation Reason`,
    COUNT(*) AS cancellation_count,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*)
         FROM uber_cleaned
         WHERE `Driver Cancellation Reason` IS NOT NULL),
        2
    ) AS percentage
FROM uber_cleaned
WHERE `Driver Cancellation Reason` IS NOT NULL
GROUP BY `Driver Cancellation Reason`
ORDER BY cancellation_count DESC;


-- 10. Average ride distance and booking value by vehicle
SELECT 
    `Vehicle Type`,
    ROUND(AVG(`Ride Distance`), 2) AS avg_ride_distance,
    ROUND(AVG(`Booking Value`), 2) AS avg_booking_value
FROM uber_cleaned
GROUP BY `Vehicle Type`
ORDER BY avg_booking_value DESC;


-- 11. Ratings by vehicle type
SELECT 
    `Vehicle Type`,
    ROUND(AVG(`Driver Ratings`), 2) AS avg_driver_rating,
    ROUND(AVG(`Customer Rating`), 2) AS avg_customer_rating
FROM uber_cleaned
GROUP BY `Vehicle Type`
ORDER BY avg_driver_rating DESC;


-- 12. Booking analysis by hour
SELECT 
    HOUR(`Time`) AS booking_hour,
    COUNT(*) AS total_bookings
FROM uber_cleaned
WHERE `Time` IS NOT NULL
GROUP BY HOUR(`Time`)
ORDER BY total_bookings DESC;


-- 13. Booking analysis by weekday
SELECT 
    DAYNAME(`Date`) AS weekday,
    COUNT(*) AS total_bookings
FROM uber_cleaned
WHERE `Date` IS NOT NULL
GROUP BY DAYOFWEEK(`Date`), DAYNAME(`Date`)
ORDER BY DAYOFWEEK(`Date`);


-- 14. Monthly booking trend
SELECT 
    YEAR(`Date`) AS booking_year,
    MONTH(`Date`) AS booking_month,
    COUNT(*) AS total_bookings,
    ROUND(SUM(`Booking Value`), 2) AS total_booking_value
FROM uber_cleaned
WHERE `Date` IS NOT NULL
GROUP BY YEAR(`Date`), MONTH(`Date`)
ORDER BY booking_year, booking_month;


-- 15. Cancellation rate by vehicle type
SELECT 
    `Vehicle Type`,
    COUNT(*) AS total_bookings,
    SUM(
        CASE 
            WHEN `Booking Status` IN (
                'Cancelled by Customer',
                'Cancelled by Driver'
            )
            THEN 1
            ELSE 0
        END
    ) AS cancelled_bookings,
    ROUND(
        SUM(
            CASE 
                WHEN `Booking Status` IN (
                    'Cancelled by Customer',
                    'Cancelled by Driver'
                )
                THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS cancellation_rate
FROM uber_cleaned
GROUP BY `Vehicle Type`
ORDER BY cancellation_rate DESC;


-- 16. Top pickup locations by cancellation rate
SELECT 
    `Pickup Location`,
    COUNT(*) AS total_bookings,
    SUM(
        CASE 
            WHEN `Booking Status` IN (
                'Cancelled by Customer',
                'Cancelled by Driver'
            )
            THEN 1
            ELSE 0
        END
    ) AS cancelled_bookings,
    ROUND(
        SUM(
            CASE 
                WHEN `Booking Status` IN (
                    'Cancelled by Customer',
                    'Cancelled by Driver'
                )
                THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS cancellation_rate
FROM uber_cleaned
GROUP BY `Pickup Location`
HAVING COUNT(*) >= 100
ORDER BY cancellation_rate DESC
LIMIT 10;


-- 17. Booking status by vehicle type
SELECT 
    `Vehicle Type`,
    `Booking Status`,
    COUNT(*) AS bookings
FROM uber_cleaned
GROUP BY `Vehicle Type`, `Booking Status`
ORDER BY `Vehicle Type`, bookings DESC;


-- 18. Payment method analysis
SELECT 
    `Payment Method`,
    COUNT(*) AS total_bookings,
    ROUND(SUM(`Booking Value`), 2) AS total_booking_value,
    ROUND(AVG(`Booking Value`), 2) AS average_booking_value
FROM uber_cleaned
WHERE `Payment Method` IS NOT NULL
GROUP BY `Payment Method`
ORDER BY total_booking_value DESC;


-- 19. Completed rides performance
SELECT 
    COUNT(*) AS completed_rides,
    ROUND(AVG(`Ride Distance`), 2) AS avg_ride_distance,
    ROUND(AVG(`Booking Value`), 2) AS avg_booking_value,
    ROUND(AVG(`Driver Ratings`), 2) AS avg_driver_rating,
    ROUND(AVG(`Customer Rating`), 2) AS avg_customer_rating
FROM uber_cleaned
WHERE `Booking Status` = 'Success';


-- 20. Top 10 vehicle/location combinations by booking value
SELECT 
    `Vehicle Type`,
    `Pickup Location`,
    COUNT(*) AS total_bookings,
    ROUND(SUM(`Booking Value`), 2) AS total_booking_value
FROM uber_cleaned
WHERE `Booking Value` IS NOT NULL
GROUP BY `Vehicle Type`, `Pickup Location`
ORDER BY total_booking_value DESC
LIMIT 10;