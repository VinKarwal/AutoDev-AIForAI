from langchain_ollama import OllamaLLM

class CrewAIOllamaWrapper(OllamaLLM):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stop = []

    def supports_stop_words(self):
        return False

    def get_stop_words(self):
        return []

    # ✅ Accept additional keyword arguments like `callbacks`
    def call(self, prompt: str, stop: list = None, **kwargs):
        return self.invoke(prompt)
