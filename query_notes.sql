SELECT T.id, T.tag, COUNT(E.emotion) AS count
from emotion e
LEFT JOIN emotiontags ET ON E.id=ET.emotion_id LEFT JOIN tag T ON T.id = ET.tag_id
WHERE E.id IN (4, 5, 2)
GROUP BY T.tag
ORDER BY COUNT DESC;

-- id|tag|count
-- 1|Time Management|2
-- 6|Depression|1
