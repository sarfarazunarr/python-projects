from g4f.client import Client
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
client = Client()

def get_chat_completion(prompt):
    messages = [{"role": "user", "content": f"Provide only Full form else say I am not sure: {prompt}"}]
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    )
    return completion.choices[0].message.content



print("\n\nHi FullForm GPT is here to help you!\n\n")
continue_threads = True

while continue_threads:
    prompt = input("Type Short form: ")
    if prompt == "exit":
        continue_threads = False
        print("Goodbye!")
        break

    response = get_chat_completion(prompt)
    print(response)

print("Thanks for using FullForm GPT By Sarfaraz Unar!")



# This is free gpt by g4f.ai
# This program only give you full form of given word else i am not sure.
# Thanks For Watching
