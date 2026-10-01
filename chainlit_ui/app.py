"""Chainlit-интерфейс для paint_agent: запускает агента локально через Runner."""

import sys
import uuid
from pathlib import Path

# Чтобы импортировался пакет paint_agent из корня проекта.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import chainlit as cl
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from paint_agent.agent import root_agent

# Ключ Gemini лежит в paint_agent/.env.
load_dotenv(Path(__file__).resolve().parent.parent / "paint_agent" / ".env")

APP_NAME = "paint_agent"
USER_ID = "local_user"

session_service = InMemorySessionService()
runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)


@cl.on_chat_start
async def on_chat_start() -> None:
    """Создаёт новую сессию ADK для каждого нового чата."""
    session_id = str(uuid.uuid4())
    await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=session_id
    )
    cl.user_session.set("session_id", session_id)
    await cl.Message(
        content="Привет! Я консультант по краскам Cymbal Shops. Чем помочь?"
    ).send()


@cl.on_message
async def on_message(message: cl.Message) -> None:
    """Отправляет сообщение агенту и показывает финальный ответ."""
    session_id = cl.user_session.get("session_id")
    content = types.Content(role="user", parts=[types.Part(text=message.content)])

    answer = ""
    async for event in runner.run_async(
        user_id=USER_ID, session_id=session_id, new_message=content
    ):
        if event.is_final_response() and event.content and event.content.parts:
            answer = "".join(p.text or "" for p in event.content.parts)

    await cl.Message(content=answer or "(пустой ответ)").send()
