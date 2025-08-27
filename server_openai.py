# server_openai.py
# Минимальный FastAPI-сервер без torch/transformers.
# Всегда возвращает "привет" для /v1/chat/completions.
from typing import List, Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    role: str
    content: Union[str, List[dict]]

class ChatCompletionsRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: Optional[float] = 0.0
    max_tokens: Optional[int] = 1

@app.get("/")
def root():
    return {"status": "ok", "mode": "stub", "message": "я отвечаю 'привет' без загрузки модели"}

@app.post("/v1/chat/completions")
def chat_completions(req: ChatCompletionsRequest):
    # Мгновенный ответ без какой-либо генерации
    return {
        "id": "cmpl-stub-hello",
        "object": "chat.completion",
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": "привет"},
                "finish_reason": "stop",
            }
        ],
        "model": req.model,
    }
