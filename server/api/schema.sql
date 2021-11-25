DROP TABLE IF EXISTS
    users,
    group_chats,
    group_memberships,
    direct_messages,
    group_messages
 CASCADE;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    name TEXT NOT NULL
);

CREATE TABLE group_chats(
    id SERIAL PRIMARY KEY,
    name TEXT not null
);

CREATE TABLE group_memberships(
    id SERIAL PRIMARY KEY,
    group_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,

    FOREIGN KEY (group_id) REFERENCES group_chats(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE direct_messages(
    id SERIAL PRIMARY KEY,
    sender_id INTEGER NOT NULL,
    reciever_id INTEGER NOT NULL,
    message_text TEXT NOT NULL,
    time_sent TIMESTAMP DEFAULT NOW(),
    read BOOLEAN DEFAULT FALSE,

    FOREIGN KEY (sender_id) REFERENCES users(id),
    FOREIGN KEY (reciever_id) REFERENCES users(id)
);

CREATE TABLE group_messages(
    id SERIAL PRIMARY KEY,
    sender_id INTEGER NOT NULL,
    reciever_id INTEGER NOT NULL,
    message_text TEXT NOT NULL,
    time_sent TIMESTAMP DEFAULT NOW(),
    read BOOLEAN DEFAULT FALSE,

    FOREIGN KEY (sender_id) REFERENCES users(id),
    FOREIGN KEY (reciever_id) REFERENCES users(id)
);

