-- left join
SELECT AA.ID, AA.Sales, BB.Region
FROM AA
left join BB
on AA.ID = BB.ID 
-- WHERE AA.ID = 'B'


-- right join
SELECT BB.ID, AA.Sales, BB.Region
FROM AA
right join BB
on AA.ID = BB.ID 
-- WHERE AA.ID = 'B'


-- or
-- right join
SELECT BB.ID, AA.Sales, BB.Region
FROM BB
LEFT join AA
on AA.ID = BB.ID 


-- inner join
SELECT BB.ID, AA.Sales, BB.Region
FROM AA
INNER join BB
on AA.ID = BB.ID 


-- full join
SELECT BB.ID, AA.Sales, BB.Region
FROM AA
FULL join BB
on AA.ID = BB.ID 


-- full join
SELECT AA.ID, BB.ID, AA.Sales, BB.Region
FROM AA
FULL join BB
on AA.ID = BB.ID 


-- full join
SELECT ISNULL(AA.ID, BB.ID) as ID, AA.Sales, BB.Region
FROM BB
FULL join AA on AA.ID = BB.ID 


-- full join
SELECT COALESCE(AA.ID, BB.ID) as ID, AA.Sales, BB.Region
FROM BB
FULL join AA on AA.ID = BB.ID 
