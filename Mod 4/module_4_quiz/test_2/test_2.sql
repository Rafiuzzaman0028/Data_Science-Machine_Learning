-- left join 
SELECT google_laptop.LaptopId, google_laptop.Empid, google_laptop.Brand, google_laptop.Price, 
google_salaries.first_name, google_salaries.last_name
FROM google_laptop
LEFT JOIN google_salaries
on google_laptop.Empid = google_salaries.Empid

-- join 
SELECT 
    google_laptop.LaptopId,
    google_laptop.Empid,
    google_laptop.Brand,
    google_laptop.Price,
    google_salaries.first_name,
    google_salaries.last_name
    
FROM google_laptop
JOIN google_salaries
ON google_laptop.Empid = google_salaries.Empid;
