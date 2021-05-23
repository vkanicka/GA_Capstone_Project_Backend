SELECT TAG, SUM(COUNT) AS TOTAL FROM
(
  SELECT tag.tag AS TAG, COUNT(emotion.emotion) AS COUNT
  from emotion
  LEFT JOIN emotiontags ON emotion.id=emotiontags.emotion_id LEFT JOIN tag ON tag.id = emotiontags.tag_id
  WHERE emotion.id IN (4, 5, 2)
  GROUP BY tag.tag

  UNION ALL

  SELECT tag.tag AS TAG, COUNT(thought.thought) AS COUNT
  from thought
  LEFT JOIN thoughttags ON thought.id=thoughttags.thought_id
  LEFT JOIN tag ON tag.id = thoughttags.tag_id
  WHERE thought.id IN (1, 2, 4, 6)
  GROUP BY tag.tag

  UNION ALL

  SELECT tag.tag AS TAG, COUNT(behavior.behavior) AS COUNT
  from behavior
  LEFT JOIN behaviortags ON behavior.id=behaviortags.behavior_id
  LEFT JOIN tag ON tag.id = behaviortags.tag_id
  WHERE behavior.id IN (1)
  GROUP BY tag.tag
)
GROUP BY (TAG)
ORDER BY TOTAL DESC
;
