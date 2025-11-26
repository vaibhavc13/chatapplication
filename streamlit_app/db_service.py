import sqlite3
import os
from datetime import datetime

DB_NAME = "chat_history.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # Create conversations table
    c.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create messages table
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id INTEGER,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            provider TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (conversation_id) REFERENCES conversations (id) ON DELETE CASCADE
        )
    ''')
    
    conn.commit()
    conn.close()

def get_conversations():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM conversations ORDER BY created_at DESC')
    conversations = [dict(row) for row in c.fetchall()]
    conn.close()
    return conversations

def create_conversation(title):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO conversations (title) VALUES (?)', (title,))
    conversation_id = c.lastrowid
    conn.commit()
    conn.close()
    return conversation_id

def get_messages(conversation_id):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM messages WHERE conversation_id = ? ORDER BY created_at ASC', (conversation_id,))
    messages = [dict(row) for row in c.fetchall()]
    conn.close()
    return messages

def add_message(conversation_id, role, content, provider=None):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO messages (conversation_id, role, content, provider)
        VALUES (?, ?, ?, ?)
    ''', (conversation_id, role, content, provider))
    conn.commit()
    conn.close()

def delete_conversation(conversation_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM conversations WHERE id = ?', (conversation_id,))
    conn.commit()
    conn.close()
