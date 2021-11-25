INSERT INTO users(username, password, name) VALUES
    ('dev', 'password123', 'devan'),
    ('bob27', 'password7', 'Bob')
;

INSERT INTO direct_messages(sender_id, receiver_id, message_text) VALUES
    (1, 2, 'This is my first message'),
    (2, 1, 'Oh hey, whats up?'),
    (1, 2, 'Nothing much'),
    (1, 2, 'Just testing out this app'),
    (1, 2, 'hbu?'),
    (2, 1, 'ya same')
;