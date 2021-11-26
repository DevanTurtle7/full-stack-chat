INSERT INTO users(username, password, name) VALUES
    ('dev', 'password123', 'devan'),
    ('bob27', 'password7', 'Bob'),
    ('james2285', 'thismypass', 'james')
;

INSERT INTO direct_messages(sender_id, receiver_id, message_text) VALUES
    (1, 2, 'This is my first message'),
    (2, 1, 'Oh hey, whats up?'),
    (1, 2, 'Nothing much'),
    (1, 2, 'Just testing out this app'),
    (1, 2, 'hbu?'),
    (2, 1, 'ya same'),
    (3, 1, 'hello'),
    (2, 3, 'whats up?'),
    (3, 2, 'dont talk to me')
;

INSERT INTO group_chats(name) VALUES ('OUR CHAT');

INSERT INTO group_memberships(group_id, user_id) VALUES
    (1, 1),
    (1, 2),
    (1, 3)
;

INSERT INTO group_messages(sender_id, group_chat_id, message_text) VALUES
    (1, 1, 'hey whats up, welcome to the chat'),
    (1, 1, 'hows it going?'),
    (2, 1, 'pretty good pretty good'),
    (3, 1, 'yo whats up')
;