-- CRUD OPERATIONS

-- Create tasks table
CREATE TABLE tasks(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    priority TEXT,
    completed BOOLEAN DEFAULT FALSE
);

-- Create and insert a new task into tasks table
INSERT INTO tasks(
    title,
    description,
    priority
)
VALUES (
    'Learn PostgreSQL',
    'Understand PostgreSQL',
    'high'
);

-- Get all tasks from tasks table
SELECT * FROM tasks;

-- Update a specific task using id in tasks table
UPDATE tasks
SET priority = 'medium'
WHERE id = 1;

-- delete a specific task using id in tasks table
DELETE FROM tasks
WHERE id = 1;

-- Conversations

CREATE TABLE conversations(
    id UUID PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM conversations;

-- Messages

CREATE TABLE messages(
    id SERIAL PRIMARY KEY,
    conversation_id UUID NOT NULL,
    role TEXT NOT NULL,
    content JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (conversation_id)
    REFERENCES conversations(id)
);

-- Testing
INSERT INTO conversations(id)
VALUES(
    '550e8400-e29b-41d4-a716-446655440000'
);

INSERT INTO messages(
    conversation_id,
    role,
    content
)
VALUES(
    '50000000000000000000000000000000',
    'user',
    '{"text": "Learn about fast api" }'
);

SELECT * FROM messages;