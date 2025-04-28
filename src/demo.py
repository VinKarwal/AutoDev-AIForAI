from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="codellama")
response = llm.invoke("What is a job aggregator application?")
print(response)
