# local-hf-chatbot
A lightweight, locally running AI chatbot built with Hugging Face Transformers, PyTorch, and Gradio using Meta's BlenderBot Small (90M) model.


# Local AI Chatbot — Hugging Face + Gradio

A lightweight conversational AI chatbot that runs locally using Python, Hugging Face Transformers, PyTorch, and Gradio.

This project explores the fundamentals of generative AI inference, tokenization, response generation, and conversation-history handling using Meta's `facebook/blenderbot_small-90M` pretrained model.

## Features

- Local inference using a pretrained conversational model
- Browser-based chat interface powered by Gradio
- Text tokenization and response decoding with Hugging Face Transformers
- Basic multi-turn conversation-history handling
- Configurable text-generation parameters
- No paid hosted-model API required
- Offline execution after the required model files have been downloaded

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| PyTorch | Local neural network inference |
| Hugging Face Transformers | Model loading, tokenization, and text generation |
| Gradio | Interactive browser-based chat interface |
| BlenderBot Small 90M | Pretrained conversational model |

## Model

**Model:** `facebook/blenderbot_small-90M`

**Model source:** https://huggingface.co/facebook/blenderbot_small-90M

BlenderBot Small is a pretrained sequence-to-sequence conversational model designed for open-domain dialogue.

The PyTorch model weights are approximately 350 MB, keeping the model checkpoint within the project's 500 MB target. Additional disk space is required for Python dependencies, tokenizer files, and other application components.

The model is used for experimentation and learning. It can generate generic, repetitive, or contextually inconsistent responses and should not be treated as a reliable source of factual information.

## Project Structure

```text
local-hf-chatbot/
│
├── app.py              # Gradio chatbot application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Files excluded from version control
```

## Getting Started

### Prerequisites

- Python 3.12, or another version supported by your installed dependencies
- Git
- An internet connection for the initial model download
- Sufficient disk space for the model and Python dependencies

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/local-hf-chatbot.git
cd local-hf-chatbot
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Test the model

```bash
python model_test.py
```

On the first run, Hugging Face downloads the required model and tokenizer files. These files are cached locally for subsequent use.

### 5. Launch the chatbot

```bash
python app.py
```

Open the following URL in your browser if it does not open automatically:

http://127.0.0.1:7860

The Gradio server runs on your own machine, and model inference is performed locally.

## How It Works

1. **Input:** Gradio collects the user's message and recent conversation history.
2. **Context preparation:** The application combines recent messages into a model input.
3. **Tokenization:** Hugging Face converts the text into token IDs and attention masks.
4. **Inference:** PyTorch runs the pretrained BlenderBot model to generate a response.
5. **Decoding:** Generated token IDs are converted back into readable text.
6. **Output:** Gradio displays the response in the chat interface.

### Inference Pipeline

```text
User Message
     |
     v
Gradio Chat Interface
     |
     v
Conversation Context
     |
     v
Hugging Face Tokenizer
     |
     v
BlenderBot Small + PyTorch
     |
     v
Generated Token IDs
     |
     v
Decoded Text Response
     |
     v
Gradio Chat Interface
```

## Running Offline

After confirming that all required model files have been downloaded, you can test offline execution.

**Windows PowerShell**

```powershell
$env:HF_HUB_OFFLINE = "1"
python app.py
```

Offline execution requires the model and tokenizer files to be available in the local Hugging Face cache.

## Known Limitations

- Response quality is limited by the size and capabilities of the pretrained model.
- Responses can be repetitive, generic, or contextually inconsistent.
- Conversation history is basic and does not provide persistent long-term memory.
- Model inference speed depends on the computer's hardware.
- The model can generate incorrect information and should not be relied on for high-stakes decisions.

## Potential Improvements

- Add a clear-conversation button and improved error handling.
- Measure response latency and compare generation settings.
- Improve conversation-context management.
- Add automated tests for prompt handling and model responses.
- Explore retrieval-augmented generation (RAG) using personal documents.
- Experiment with other lightweight open-source models.

## Learning Outcomes

This project explores:

- Pretrained language model loading
- Tokenization and numerical text representations
- Sequence-to-sequence text generation
- Local model inference using PyTorch
- Building interactive AI interfaces with Gradio
- Basic conversational context handling

## License and Attribution

The application code in this repository is provided under the MIT License, unless otherwise stated.

The BlenderBot Small model is published under the Apache License 2.0 according to its Hugging Face model card. See the [official model repository](https://huggingface.co/facebook/blenderbot_small-90M) for the model's license and documentation.

Third-party dependencies retain their respective licenses.

---

Built as a hands-on project to understand the fundamentals of local generative AI applications.
