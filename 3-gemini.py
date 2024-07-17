import os
from dotenv import load_dotenv
import google.generativeai as genai

# ==== 1. Few shot ====
def send_gemini_request_fs(examples, task):
    # Load API key from .env file
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    # Configure the Gemini API client
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # Prepare the prompt with examples and task
    context = "You are a helpfull asistant. Bellow are some examples all of which " + \
    "start with 'Example #:'. Then you will be presented with a task, that you " + \
    "must solve, based on the examples provided.\n"

    prompt_parts = []

    prompt_parts.append(context)
    for i, example in enumerate(examples):
        prompt_parts.append(f"Example {i}: {example}")

    prompt_parts.append(f"Task: {task}")

    # Send the request to the Gemini API
    response = model.generate_content(prompt_parts)

    # Return the generated response
    return response.text, prompt_parts

# ==== 2. CoT ====
def send_gemini_request_cot(task):
    # Load API key from .env file
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    # Configure the Gemini API client
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # Prepare the CoT prompt
    cot_prompt = f"For the following task, think step-by-step and explain your reasoning:\n\nTask: {task}\n\nThought Process:"

    # Send the request to the Gemini API with CoT prompt
    response = model.generate_content(cot_prompt)

    # Return the generated response
    return response.text, cot_prompt

# ==== 3. Generative Knowledge Prompting ====
def send_gemini_request_gk(topic, task):
    # Load API key from .env file
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    # Configure the Gemini API client
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # Generate context about the topic
    context_prompt = f"Generate relevant context about the topic: {topic}"
    context_response = model.generate_content(context_prompt)
    generated_context = context_response.text

    # Prepare the prompt with the generated context and task
    prompt = f"Context: {generated_context}\n\nTask: {task}\nResponse:"

    # Send the request to the Gemini API with the prompt
    response = model.generate_content(prompt)

    # Return the generated response
    return response.text, promt


# Example usage

# ==== 1. Few Shot ====
examples = [
    "Input: 2+2=\nOutput: 4",
    "Input 5+5=\nOutput: 10"
]
task = "10+10="
result, prompt_parts = send_gemini_request_fs(examples, task)
print("#" * 30, "1. Few Shot", "#" * 30)
print(prompt_parts)
print(result)

# ==== 2. CoT ====
task = "Explain the process of photosynthesis in plants."
result, promt = send_gemini_request_cot(task)
print("#" * 30, "2. CoT", "#" * 30)
print(promt)
print(result)

# ==== 3. Generative Knowledge Prompting ====
topic = "Photosynthesis"
task = "Explain the process of photosynthesis in plants, including the role of chloroplasts and the light and dark reactions."
result, promt = send_gemini_request_gk(topic, task)
print("#" * 30, "3. GKP", "#" * 30)
print(promt)
print(result)