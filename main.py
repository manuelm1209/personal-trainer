"""
main.py

This script utilizes the OpenAI API to create and interact with an AI assistant specialized in personal training and nutrition. It demonstrates the creation of an assistant, managing threads, sending messages, and handling assistant responses. The script includes a helper function to wait for run completion and logs messages and execution steps.

Dependencies:
- openai
- python-dotenv (for environment variable management)
- logging (for log generation)
- time (for time formatting and waiting intervals)
- datetime (for handling date and time)

Author: [Your Name]
Date: [Date]

"""

# === Libraries and Environment Setup ===
"""
Imports required libraries, loads environment variables, and initializes configurations.
- `openai`: The OpenAI API library for interaction.
- `dotenv`: To load the OpenAI API key from a `.env` file.
- `time`: For time formatting and waiting intervals.
- `logging`: To set up error and activity logs.
- `datetime`: For working with time data.
"""

import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime

# === Environment Setup ===
"""
Load the `.env` file to retrieve the OpenAI API key.
Other options for adding the API key are commented out for reference.
"""

load_dotenv()

# === OpenAI API Client Configuration ===
"""
Initializes the OpenAI API client and selects the model to use.
- `client`: The OpenAI client object.
- `model`: Specifies the GPT model being used.
"""

client = openai.OpenAI()
model = "gpt-3.5-turbo-16k"

# === Assistant Creation ===
"""
Code block to create a new assistant.
Uncomment the relevant lines to create a new assistant with specific instructions.
- `personal_trainer_assistant`: Represents the newly created assistant.
- `assistant_id`: The unique ID of the created assistant.
"""

# Uncomment to create a new assistant
# personal_trainer_assistant = client.beta.assistants.create(
#     name="Personal Trainer",
#     instructions="""You are the best personal trainer and nutritionist who knows how to get clients to build lean muscles. You've trained high-caliber athletes and movie stars.""",
#     model=model
# )
# assistant_id = personal_trainer_assistant.id
# print(assistant_id)

# === Thread Creation ===
"""
Code block to create a new thread for conversation.
Uncomment the relevant lines to start a new conversation with the assistant.
- `thread`: Represents the newly created thread.
- `thread_id`: The unique ID of the created thread.
"""

# Uncomment to create a new thread
# thread = client.beta.threads.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "How do I get started working out to lose fat and build muscle?"
#         }
#     ]
# )
# thread_id = thread.id
# print(thread_id)

# === Assign Existing IDs ===
"""
Assign existing assistant and thread IDs for continuing interaction.
- `assistant_id`: The unique ID of the assistant.
- `thread_id`: The unique ID of the conversation thread.
"""

assistant_id = "asst_apdzzpUtS9w6lA56dKKC07zt"
thread_id = "thread_IfD0SO3thgXNcVxWwdcDA7Bh"

# === Sending Messages ===
"""
Send a message to the assistant within an existing thread.
- `message`: Contains the user query or command.
- The message is sent using the OpenAI API, and the assistant processes the response.
"""

message = "What are the best exercises for lean muscle and getting strong?"
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=message
)

# === Running the Assistant ===
"""
Create and run an assistant interaction within the specified thread.
- Custom instructions can be passed during the run.
- Logs and outputs the run details and responses.
"""

run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as James Bond"
)

# === Helper Function: Wait for Run Completion ===
"""
Waits for a run to complete, periodically checking its status.
- Retrieves the response once the run is completed.
- Logs elapsed time and any errors during the process.
Parameters:
- `client`: The OpenAI client object.
- `thread_id`: The ID of the thread.
- `run_id`: The ID of the run.
- `sleep_interval`: Time (in seconds) between checks for run completion.
"""

def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    """
    Wait for a run to complete and print the elapsed time.
    Logs messages and errors during the process.
    """
    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime(
                    "%H:%M:%S", time.gmtime(elapsed_time)
                )
                print(f"Run completed in {formatted_elapsed_time}")
                logging.info(f"Run completed in {formatted_elapsed_time}")
                
                # Retrieve and print the assistant's response
                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"Assistant Response: {response}")
                break
        except Exception as e:
            logging.error(f"An error occurred while retrieving the run: {e}")
            break
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)
        
# === Running the Wait Function ===
"""
Waits for the current run to complete and handles responses.
- Uses the `wait_for_run_completion` function to monitor the run status.
"""

wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

# === Log Execution Steps ===
"""
Retrieve and print the steps executed during the assistant's run.
- Outputs the steps as a list for debugging or auditing purposes.
"""

run_steps = client.beta.threads.runs.steps.list(
    thread_id=thread_id,
    run_id=run.id
)
print(f"\nSteps---> {run_steps.data}")