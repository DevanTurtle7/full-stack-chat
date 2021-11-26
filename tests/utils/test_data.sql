INSERT INTO users(username, password, name) VALUES
    ('dev', 'password123', 'devan'),
    ('bob27', 'password7', 'Bob'),
    ('james2285', 'thismypass', 'james'),
    ('user123', 'anotherpass', 'dev')
;

INSERT INTO direct_messages(sender_id, receiver_id, message_text, time_sent) VALUES
    (1, 2, 'This is my first message', (TO_TIMESTAMP('1922-10-03 00:00:01', 'YYYY-MM-DD HH24:MI:SS'))),
    (2, 1, 'Oh hey, whats up?', (TO_TIMESTAMP('1922-10-03 00:00:03', 'YYYY-MM-DD HH24:MI:SS'))),
    (1, 2, 'Nothing much', (TO_TIMESTAMP('1922-10-04 00:00:01', 'YYYY-MM-DD HH24:MI:SS'))),
    (1, 2, 'Just testing out this app', (TO_TIMESTAMP('1923-09-03 00:00:01', 'YYYY-MM-DD HH24:MI:SS'))),
    (1, 3, 'yoyoyoy', (TO_TIMESTAMP('1923-10-03 00:00:01', 'YYYY-MM-DD HH24:MI:SS'))),
    (2, 1, 'ya same', (TO_TIMESTAMP('1923-10-04 00:00:01', 'YYYY-MM-DD HH24:MI:SS'))),
    (3, 1, 'hello', (TO_TIMESTAMP('1921-10-03 00:00:01', 'YYYY-MM-DD HH24:MI:SS'))),
    (2, 3, 'whats up?', (TO_TIMESTAMP('1920-10-03 00:00:01', 'YYYY-MM-DD HH24:MI:SS'))),
    (3, 2, 'dont talk to me', (TO_TIMESTAMP('1920-10-04 00:00:01', 'YYYY-MM-DD HH24:MI:SS')))
;

INSERT INTO group_chats(name) VALUES
    ('OUR CHAT'),
    ('ANOTHER CHAT')
;

INSERT INTO group_memberships(group_chat_id, user_id) VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4)
;

INSERT INTO group_messages(sender_id, group_chat_id, message_text, time_sent) VALUES
    (1, 1, 'hey whats up, welcome to the chat', (TO_TIMESTAMP('1919-10-03 00:00:01', 'YYYY-MM-DD HH24:MI:SS'))),
    (1, 1, 'hows it going?', (TO_TIMESTAMP('1922-10-03 00:00:01', 'YYYY-MM-DD HH24:MI:SS'))),
    (2, 1, 'pretty good pretty good', (TO_TIMESTAMP('1923-10-03 00:00:01', 'YYYY-MM-DD HH24:MI:SS'))),
    (3, 1, 'yo whats up', (TO_TIMESTAMP('1921-10-03 00:00:01', 'YYYY-MM-DD HH24:MI:SS'))),
    (2, 2, 'helloooo', (TO_TIMESTAMP('2020-10-03 00:00:01', 'YYYY-MM-DD HH24:MI:SS')))
;