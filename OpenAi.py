import os
import openai

openai.api_key = "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"

userinput = "Who are you?"
message = f"Write a rhyming response for{userinput}:，try to sound philosophical and funny and like a gangster"
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "user",
      "content": message
    }
  ],
  temperature=0,
  max_tokens=1024
)

real_res = response['choices'][0]['message']['content']
print( real_res )