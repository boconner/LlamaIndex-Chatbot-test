# -*- coding: utf-8 -*-
"""PoliChat

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vE6WgBTovDh4xMfev5uAhxCsJNtR_tP0
"""

pip install llama-index

pip install openai

from llama_index import SimpleDirectoryReader

from llama_index import GPTVectorStoreIndex

from llama_index import StorageContext

from llama_index import Document

pip install docx2txt

documents = SimpleDirectoryReader('sample_data').load_data()

import openai
openai.api_key = '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'

index = GPTVectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

response = query_engine.query("Tell me about Jeff Irwin?")

print(response)

response = query_engine.query("thanks for the info")

print(response)

response = query_engine.query("tell me where Jeff Irwin stands on the issues")
print(response)

response = query_engine.query("what about seniors")
print(response)

import logging
import sys

index.storage_context.persist()

from llama_index import StorageContext, load_index_from_storage

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./storage")
# load index
index = load_index_from_storage(storage_context)

response = query_engine.query("Where does Jeff stand on taxes?")

response = query_engine.query("What is the indian tuition waiver?")

print(response)

response = query_engine.query("How do i volunteer?")
print(response)