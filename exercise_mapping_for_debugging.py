import sqlite3
con = sqlite3.connect('capstone.sqlite')
cur = con.cursor()

exercise_mapping_query = cur.execute('''
SELECT EXERCISE.NAME, EXERCISE.DESCRIPTION, TAG FROM (

  SELECT ID AS TAG_ID, TAG, SUM(COUNT) AS TOTAL FROM
  (
    SELECT tag.id AS ID, tag.tag AS TAG, COUNT(emotion.emotion) AS COUNT
    from emotion
    LEFT JOIN emotiontags ON emotion.id=emotiontags.emotion_id LEFT JOIN tag ON tag.id = emotiontags.tag_id
    GROUP BY tag.tag

    UNION ALL

    SELECT tag.id AS ID,  tag.tag AS TAG, COUNT(thought.thought) AS COUNT
    from thought
    LEFT JOIN thoughttags ON thought.id=thoughttags.thought_id
    LEFT JOIN tag ON tag.id = thoughttags.tag_id
    GROUP BY tag.tag

    UNION ALL

    SELECT tag.id AS ID,  tag.tag AS TAG, COUNT(behavior.behavior) AS COUNT
    from behavior
    LEFT JOIN behaviortags ON behavior.id=behaviortags.behavior_id
    LEFT JOIN tag ON tag.id = behaviortags.tag_id
    GROUP BY tag.tag
  )

  GROUP BY (TAG)

) AS FOUND_TAG
LEFT JOIN exercisetags ON exercisetags.tag_id = FOUND_TAG.tag_id
LEFT JOIN exercise ON exercise.id = exercisetags.exercise_id
;
''').fetchall()

print(exercise_mapping_query)

con.close()
