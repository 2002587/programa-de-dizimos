DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
);

cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS upload (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            upload_key TEXT UNIQUE
            );
            '''
    )



conn.commit()
## conn.close()
## close only when we have finished everything, otherwise we have to reopen the database each time