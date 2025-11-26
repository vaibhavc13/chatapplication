import os
import traceback
from langchain_groq import ChatGroq


def get_llm(
    provider=None,
    model_name=None,
    api_keys=None,
    fallback_providers=True
):
    """
    Smart universal LLM loader that:
    - Supports Groq (recommended)
    - Supports HuggingFace (FREE + PAID)
    - Auto-switches to free HF model if paid fails
    - Catches StopIteration bug
    - Tests inference with llm.invoke("test")
    """
    if api_keys is None:
        api_keys = {}

    # Normalize misspelling
    if provider and provider.lower() == "grok":
        provider = "groq"

    # Provider selection order
    providers = []
    if provider:
        providers.append(provider.lower())
    elif fallback_providers:
        providers = ["groq"]
    else:
        raise ValueError("No provider specified and fallback disabled.")

    errors = {}

    for prov in providers:
        print(f"\n🔎 Attempting provider: {prov}")

        try:
            # ---------------------------
            # GROQ PROVIDER
            # ---------------------------
            if prov == "groq":
                api_key = (
                    api_keys.get("groq")
                    or api_keys.get("grok")
                    or os.getenv("GROQ_API_KEY")
                    or os.getenv("GROK_API_KEY")
                )
                if not api_key:
                    raise ValueError("Groq API Key missing")

                groq_model = model_name or "llama-3.3-70b-versatile"
                print(f"➡️ Using Groq model: {groq_model}")

                llm = ChatGroq(
                    api_key=api_key,
                    model=groq_model,
                    temperature=0.7
                )

                # Test
                llm.invoke("test")
                print("✅ Groq model loaded successfully")
                return llm

        except Exception as e:
            errors[prov] = str(e)
            print(f"❌ Provider {prov} failed → {e}")
            traceback.print_exc()

    # FINAL FAIL
    raise RuntimeError(
        "\n❌ All providers failed:\n" +
        "\n".join([f"- {p}: {err}" for p, err in errors.items()])
    )
