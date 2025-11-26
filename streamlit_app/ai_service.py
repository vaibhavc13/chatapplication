import os
from llm_factory import get_llm
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

class AIService:
    def __init__(self):
        self.providers = ["grok"]
        self.fallback_order = ["grok"]

    def route_request(self, messages, provider=None, api_keys=None):
        if api_keys is None:
            api_keys = {}

        # Convert dict messages to LangChain messages
        lc_messages = []
        for msg in messages:
            role = msg.get("role")
            content = msg.get("content", "")
            if role == "user":
                lc_messages.append(HumanMessage(content=content))
            elif role == "assistant":
                lc_messages.append(AIMessage(content=content))
            elif role == "system":
                lc_messages.append(SystemMessage(content=content))

        # Try specific provider
        if provider and provider in self.providers:
            try:
                print(f"Attempting specific provider: {provider}")
                llm = get_llm(provider, api_keys=api_keys)
                response = llm.invoke(lc_messages)
                if not response.content:
                    raise ValueError("Model returned empty response")
                return {"provider": provider, "response": response.content}
            except Exception as e:
                print(f"Specific provider {provider} failed: {str(e)}")
                raise e

        # Fallback logic
        last_error = None
        for p in self.fallback_order:
            try:
                print(f"Attempting provider: {p}")
                llm = get_llm(p, api_keys=api_keys)
                response = llm.invoke(lc_messages)
                return {"provider": p, "response": response.content}
            except Exception as e:
                print(f"Provider {p} failed: {str(e)}")
                last_error = e
                continue
        
        raise Exception(f"All AI providers failed. Last error: {str(last_error)}")
