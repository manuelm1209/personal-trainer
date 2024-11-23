import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime

# COMENTS:
#* - HighLighted
#? - Query
#! - Alert
#TODO - TODOS

load_dotenv()
# OTHER WAYS TO ADD THE OPENAI API KEY
# openai.api_key = os.environ.get("OPENAI_API_KEY")
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

client = openai.OpenAI()
model = "gpt-3.5-turbo-16k"

# === Create Assistant ===
#? uncomment to create a new assistant
# personal_trainer_assistant = client.beta.assistants.create(
#     name="Personal Trainer",
#     instructions="""You are the best personal trainer and nutritionist who knows how to get clients to build lean muscles. You've trained high-caliber athletes and movie stars. """,
#     model=model
# )

# assistant_id = personal_trainer_assistant.id
# print(assistant_id)

# Create Thread
#? uncomment to create a new thread
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

#? Assistant ID
assistant_id = "asst_apdzzpUtS9w6lA56dKKC07zt"
thread_id = "thread_IfD0SO3thgXNcVxWwdcDA7Bh"

# === Create a message ===
message = "What are the best exerciese for lean muscle and getting strong?"
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=message
)

# === Run our assistant ===
run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as James Bond"
)

# Helper function waiting for the response
def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    """

    Waits for a run to complete and prints the elapsed time.:param client: The OpenAI client object.
    :param thread_id: The ID of the thread.
    :param run_id: The ID of the run.
    :param sleep_interval: Time in seconds to wait between checks.
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
                # Get messages here once Run is completed!
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
        
# === Run ====
wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

# === Steps --- Logs ===
run_steps =  client.beta.threads.runs.steps.list(
    thread_id=thread_id,
    run_id=run.id
)
print(f"\nSteps---> {run_steps.data}")