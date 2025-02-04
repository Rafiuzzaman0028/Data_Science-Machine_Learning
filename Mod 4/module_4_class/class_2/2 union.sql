-- union
SELECT * FROM AA
UNION 
SELECT * FROM BB

-- union all
SELECT id FROM AA
UNION 
SELECT id FROM BB
ORDER BY id

-- union all
SELECT id FROM AA
UNION ALL
SELECT id FROM BB
ORDER BY id

-- union all
SELECT firstName from patient
union ALL
SELECT firstName from guardian
ORDER BY firstName