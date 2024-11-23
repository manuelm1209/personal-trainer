import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime

# === Environment Setup ===
load_dotenv()

# === OpenAI API Client Configuration ===
client = openai.OpenAI()
model = "gpt-4o-mini"

# === Assign Existing IDs ===
assistant_id = "asst_apdzzpUtS9w6lA56dKKC07zt"
thread_id = "thread_IfD0SO3thgXNcVxWwdcDA7Bh"

# === Get User Input from Terminal ===
message = input("Enter your question for the assistant: ")

# === Sending Messages ===
try:
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message
    )
    print("Message sent to the assistant!")
except Exception as e:
    print(f"Error sending message: {e}")
    logging.error(f"Error sending message: {e}")

# === Running the Assistant ===
run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as James Bond"
)

# === Helper Function: Wait for Run Completion ===
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
            print(f"An error occurred while retrieving the run: {e}")
            break
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)

# === Running the Wait Function ===
wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

# === Log Execution Steps ===
try:
    run_steps = client.beta.threads.runs.steps.list(
        thread_id=thread_id,
        run_id=run.id
    )
    print(f"\nSteps---> {run_steps.data}")
except Exception as e:
    logging.error(f"Error retrieving run steps: {e}")
    print(f"Error retrieving run steps: {e}")