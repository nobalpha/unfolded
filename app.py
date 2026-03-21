import speech_recognition as sr
from google import genai
from google.genai import types

# 1. Initialize the Gemini Client
client = genai.Client(api_key="AIzaSyDEE_oQrZX2FXOEH0CJJCWFxMMkpltG1a8")

# 2. Configure the Chatbot
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a warm, engaging interviewer. You will receive a user's answer "
            "along with hidden instructions on which question to ask next. "
            "Acknowledge the user's answer thoughtfully and empathetically, then organically "
            "transition into asking the required next question. Do not reveal that you are reading from a list."
        )
    )
)


def listen_and_transcribe():
    """Captures audio from the mic and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ Listening... (Speak now)")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
            text = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {text}")
            return text
        except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError):
            print("🤖 Could not understand the audio. Please try again.")
            return None

# --- Main Application Loop with Key Questions ---


# Define the exact questions you want to ask, in order.
key_questions = [
    "To start things off, what is your most vivid memory from your childhood?",
    "How did your father, Onno, influence the path you took in life?",
    "Looking back, what is a challenge you faced that ended up teaching you a valuable lesson?",
    "If you could give one piece of advice to the next generation, what would it be?"
]
current_q_index = 0

print("Starting Guided Life-Story Interview... (Say 'quit' to stop)")

# Kick off the conversation with the first question directly
initial_response = chat.send_message(
    f"Warmly greet the user and ask this question: '{key_questions[0]}'")
print(f"\n🤖 Gemini: {initial_response.text}")
current_q_index += 1

while True:
    user_text = listen_and_transcribe()

    if user_text:
        if user_text.lower() in ['quit', 'exit', 'stop', 'done']:
            print("\n🤖 Ending interview. Thank you for sharing your story!")
            break

        print("🤖 Thinking...")

        # Determine what to tell the AI based on where we are in the list
        if current_q_index < len(key_questions):
            next_question = key_questions[current_q_index]
            # The "Director" prompt: telling the AI exactly what to do next
            prompt_to_ai = (
                f"The user just said: '{user_text}'.\n"
                f"Respond to them naturally. Then, transition and ask this exact next question: '{next_question}'"
            )
            current_q_index += 1
        else:
            # We ran out of key questions, so we just let it chat freely!
            prompt_to_ai = (
                f"The user just said: '{user_text}'.\n"
                f"We have finished all the main interview questions. Acknowledge their answer, wrap up the topic, and ask if there is anything else they'd like to add."
            )

        # Send our directed prompt to Gemini
        response = chat.send_message(prompt_to_ai)
        print(f"\n🤖 Gemini: {response.text}")
