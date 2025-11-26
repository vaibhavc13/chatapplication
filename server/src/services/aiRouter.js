const axios = require('axios');

class AIRouter {
    constructor() {
        this.providers = {
            grok: this.callGrok,
            openai: this.callOpenAI,
            gemini: this.callGemini,
            huggingface: this.callHuggingFace,
            local: this.callLocal,
        };
        this.fallbackOrder = ['grok', 'openai', 'gemini', 'huggingface', 'local'];
    }

    async routeRequest(messages, model) {
        let lastError = null;

        for (const provider of this.fallbackOrder) {
            try {
                console.log(`Attempting provider: ${provider}`);
                const response = await this.providers[provider](messages);
                return { provider, response };
            } catch (error) {
                console.error(`Provider ${provider} failed:`, error.message);
                lastError = error;
                continue;
            }
        }

        throw new Error('All AI providers failed. Last error: ' + lastError.message);
    }

    async callGrok(messages) {
        // Placeholder for Grok implementation
        if (!process.env.GROK_API_KEY) throw new Error('Grok API Key missing');
        // Implementation here
        return "Grok response";
    }

    async callOpenAI(messages) {
        // Placeholder for OpenAI implementation
        if (!process.env.OPENAI_API_KEY) throw new Error('OpenAI API Key missing');
        return "OpenAI response";
    }

    async callGemini(messages) {
        // Placeholder for Gemini implementation
        if (!process.env.GEMINI_API_KEY) throw new Error('Gemini API Key missing');
        return "Gemini response";
    }

    async callHuggingFace(messages) {
        // Placeholder for HF implementation
        if (!process.env.HF_API_KEY) throw new Error('HF API Key missing');
        return "HF response";
    }

    async callLocal(messages) {
        // Placeholder for Local implementation
        return "Local LLM response";
    }
}

module.exports = new AIRouter();
