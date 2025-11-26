import React, { useState } from 'react';
import { Send, Bot, User, Loader2 } from 'lucide-react';
import { cn } from '../lib/utils';

export default function ChatInterface() {
    const [messages, setMessages] = useState([
        { role: 'assistant', content: 'Hello! I am GrokChatX. How can I help you today?' }
    ]);
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!input.trim()) return;

        const userMessage = { role: 'user', content: input };
        setMessages(prev => [...prev, userMessage]);
        setInput('');
        setIsLoading(true);

        try {
            // Placeholder for API call
            // const response = await fetch('http://localhost:3001/api/chat', ...);

            // Simulate response
            setTimeout(() => {
                setMessages(prev => [...prev, { role: 'assistant', content: 'This is a simulated response from GrokChatX.' }]);
                setIsLoading(false);
            }, 1000);
        } catch (error) {
            console.error(error);
            setIsLoading(false);
        }
    };

    return (
        <div className="flex flex-col h-screen bg-background text-foreground">
            <header className="p-4 border-b flex items-center gap-2">
                <Bot className="w-6 h-6" />
                <h1 className="font-bold text-xl">GrokChatX</h1>
            </header>

            <div className="flex-1 overflow-y-auto p-4 space-y-4">
                {messages.map((msg, idx) => (
                    <div key={idx} className={cn("flex gap-3", msg.role === 'user' ? "justify-end" : "justify-start")}>
                        {msg.role === 'assistant' && (
                            <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-primary-foreground">
                                <Bot size={16} />
                            </div>
                        )}
                        <div className={cn(
                            "max-w-[80%] p-3 rounded-lg",
                            msg.role === 'user' ? "bg-primary text-primary-foreground" : "bg-muted"
                        )}>
                            {msg.content}
                        </div>
                        {msg.role === 'user' && (
                            <div className="w-8 h-8 rounded-full bg-secondary flex items-center justify-center">
                                <User size={16} />
                            </div>
                        )}
                    </div>
                ))}
                {isLoading && (
                    <div className="flex gap-3">
                        <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-primary-foreground">
                            <Bot size={16} />
                        </div>
                        <div className="bg-muted p-3 rounded-lg flex items-center">
                            <Loader2 className="animate-spin w-4 h-4" />
                        </div>
                    </div>
                )}
            </div>

            <form onSubmit={handleSubmit} className="p-4 border-t flex gap-2">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Type a message..."
                    className="flex-1 p-2 rounded-md border bg-background focus:outline-none focus:ring-2 focus:ring-primary"
                />
                <button
                    type="submit"
                    disabled={isLoading}
                    className="p-2 bg-primary text-primary-foreground rounded-md hover:opacity-90 disabled:opacity-50"
                >
                    <Send size={20} />
                </button>
            </form>
        </div>
    );
}
