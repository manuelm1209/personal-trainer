
# Personal Trainer AI Assistant

This project leverages the OpenAI API to create an AI assistant specialized in personal training and nutrition. The assistant is designed to provide tailored advice on fitness and nutrition, with expertise in building lean muscle and strength training.

## Features

- **Customizable Assistant**: Configure the assistant with specific expertise and training goals.
- **Thread Management**: Start and maintain conversation threads with the AI assistant.
- **Real-Time Responses**: Receive advice and instructions on exercises, nutrition, and fitness routines.
- **Logging and Debugging**: Track execution steps and log interactions for analysis.
- **Asynchronous Interaction**: Wait for AI run completions and fetch responses efficiently.

## Requirements

- Python 3.7+
- OpenAI Python library
- `python-dotenv` for environment variable management
- Basic libraries: `time`, `datetime`, `logging`

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/personal-trainer
   cd personal-trainer
   ```

2. **Install Dependencies**:
   Install the required Python libraries using pip:
   ```bash
   pip install openai python-dotenv
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Run the Script**:
   Execute the script to interact with the assistant:
   ```bash
   python main.py
   ```

## Usage

- Create a new assistant with personalized instructions.
- Start a new thread for a fitness query, or use an existing thread for ongoing interaction.
- Send messages to the assistant and fetch responses.
- Monitor the assistant's execution steps and performance.

## Project Structure

- `main.py`: The main script containing assistant configuration, thread creation, and interaction handling.

## Logs and Error Handling

- Logs are generated for all major activities and errors, helping you debug and monitor interactions.

## Author

Developed by Manuel Montoya.

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.
