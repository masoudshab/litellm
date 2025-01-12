import os
import sys, os
import traceback
from dotenv import load_dotenv

load_dotenv()
import os, io

sys.path.insert(
    0, os.path.abspath("../..")
)  # Adds the parent directory to the system path
import pytest
import litellm
from litellm import embedding, completion, text_completion, completion_cost

from langchain.chat_models import ChatLiteLLM
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage

def test_chat_gpt():
    try:
        chat = ChatLiteLLM(model="gpt-3.5-turbo", max_tokens=10)
        messages = [
            HumanMessage(
                content="what model are you"
            )
        ]
        resp = chat(messages)

        print(resp)
    except Exception as e:
        pytest.fail(f"Error occurred: {e}")

test_chat_gpt()


def test_claude():
    try:
        chat = ChatLiteLLM(model="claude-2", max_tokens=10)
        messages = [
            HumanMessage(
                content="what model are you"
            )
        ]
        resp = chat(messages)

        print(resp)
    except Exception as e:
        pytest.fail(f"Error occurred: {e}")

test_claude()

def test_palm():
    try:
        chat = ChatLiteLLM(model="palm/chat-bison", max_tokens=10)
        messages = [
            HumanMessage(
                content="what model are you"
            )
        ]
        resp = chat(messages)

        print(resp)
    except Exception as e:
        pytest.fail(f"Error occurred: {e}")

test_palm()

