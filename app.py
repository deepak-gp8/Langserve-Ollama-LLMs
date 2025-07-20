from fastapi import FastAPI
from langchain.llms import Ollama
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn

model = Ollama(model="qwen3:0.6b")


app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="API Server"
)

add_routes(
    app,
    model,
    path="/llm"
)

prompt=ChatPromptTemplate.from_template("Write an essay on {topic}")
prompt1=ChatPromptTemplate.from_template("Tell me a joke about {topic}")

add_routes(
    app,
    prompt|model,
    path="/essay"
)

add_routes(
    app,
    prompt1|model,
    path="/joke"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)