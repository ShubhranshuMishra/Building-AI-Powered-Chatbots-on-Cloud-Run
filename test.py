from google.cloud import aiplatform

PROJECT_ID = "hive-project-427410"
LOCATION = "us-central1"

# Initialize the SDK
aiplatform.init(project=PROJECT_ID, location=LOCATION)

def create_session():
    chat_model = aiplatform.ChatModel.from_pretrained("chat-bison")
    return chat_model

def response(chat, message):
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    result = chat.send_message(message, **parameters)
    return result.text

def run_chat():
    chat_model = create_session()
    print("Chat Session created")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        content = response(chat_model, user_input)
        print(f"AI: {content}")

if __name__ == '__main__':
    run_chat()
