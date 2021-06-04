def clearSuggestedExerciseTable():
    import sqlite3
    con = sqlite3.connect('capstone.sqlite')
    cur = con.cursor()
    cur.execute('''DELETE FROM suggestedexercise''')
    con.commit()
    con.close()

def suggestExercise():
    import sqlite3
    con = sqlite3.connect('capstone.sqlite')
    cur = con.cursor()

    # for development:
    cur.execute('''
    DELETE FROM suggestedexercise;''')
    # for production:
    # truncate postgres, drop and create peewee

    # tables: [emotion, thought, behavior, emotiontags, thoughttags, behaviortags, exercisetags, exercise]
    suggested_exercise_query_result = cur.execute('''
    SELECT EXERCISE.ID, EXERCISE.NAME, EXERCISE.DESCRIPTION FROM (
      SELECT ID AS TAG_ID, TAG, SUM(COUNT) AS TOTAL FROM
      (
        SELECT tag.id AS ID, tag.tag AS TAG, COUNT(emotion.emotion) AS COUNT
        from emotion
        LEFT JOIN emotiontags ON emotion.id=emotiontags.emotion_id LEFT JOIN tag ON tag.id = emotiontags.tag_id
        WHERE emotion.status = 1
        GROUP BY tag.tag
        UNION ALL
        SELECT tag.id AS ID,  tag.tag AS TAG, COUNT(thought.thought) AS COUNT
        from thought
        LEFT JOIN thoughttags ON thought.id=thoughttags.thought_id
        LEFT JOIN tag ON tag.id = thoughttags.tag_id
        WHERE thought.status = 1
        GROUP BY tag.tag
        UNION ALL
        SELECT tag.id AS ID,  tag.tag AS TAG, COUNT(behavior.behavior) AS COUNT
        from behavior
        LEFT JOIN behaviortags ON behavior.id=behaviortags.behavior_id
        LEFT JOIN tag ON tag.id = behaviortags.tag_id
        WHERE behavior.status = 1
        GROUP BY tag.tag
      )
      GROUP BY (TAG)
      ORDER BY TOTAL DESC
      LIMIT 1
    ) AS FOUND_TAG
    LEFT JOIN exercisetags ON exercisetags.tag_id = FOUND_TAG.tag_id
    LEFT JOIN exercise ON exercise.id = exercisetags.exercise_id
    ;
    ''').fetchone()

    con.close()
    return suggested_exercise_query_result

print(suggestExercise())
