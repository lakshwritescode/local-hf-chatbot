import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# --------------------------------------------------
# 1. Model configuration
# --------------------------------------------------

MODEL_ID = "facebook/blenderbot_small-90M"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

print("Loading BlenderBot Small...")
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID)

# Set the model to inference mode.
model.eval()

print("Model loaded successfully!")


# --------------------------------------------------
# 2. Build the conversation context
# --------------------------------------------------

def build_prompt(message, history):
    """
    Combine recent chat messages with the current input.
    BlenderBot receives the conversation as a text sequence.
    """

    conversation = []

    # Keep only a few recent messages to limit input size.
    for item in history[-6:]:
        role = item.get("role")
        content = item.get("content", "")

        if (
            role in {"user", "assistant"}
            and isinstance(content, str)
            and content.strip()
        ):
            conversation.append(content.strip())

    conversation.append(message.strip())

    # Separate dialogue turns using BlenderBot's special tokens.
    separator = (
        f" {tokenizer.eos_token} "
        f"{tokenizer.bos_token} "
    )

    return separator.join(conversation)


# --------------------------------------------------
# 3. Generate a chatbot response
# --------------------------------------------------

def respond(message, history):
    if not message or not message.strip():
        return "Please enter a message."

    # Prepare the current message and recent conversation.
    prompt = build_prompt(message, history)

    # Convert the conversation to PyTorch tensors.
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=256,
    )

    # Generate text without calculating training gradients.
    with torch.inference_mode():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=64,
            min_new_tokens=3,
            num_beams=1,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            no_repeat_ngram_size=3,
        )

    # Convert generated tokens into a normal text response.
    answer = tokenizer.decode(
        output_ids[0],
        skip_special_tokens=True,
    ).strip()

    return answer or "I couldn't generate a response. Please try again."


# --------------------------------------------------
# 4. Create the Gradio interface
# --------------------------------------------------

demo = gr.ChatInterface(
    fn=respond,
    title="Local AI Chatbot",
    description=(
        "A lightweight conversational chatbot powered by "
        "BlenderBot Small and Hugging Face Transformers. "
        "Model inference runs locally on your computer."
    ),
    examples=[
        "Tell me something interesting about space.",
        "Explain machine learning in simple terms.",
        "Why is learning Python useful?",
    ],
    textbox=gr.Textbox(
        placeholder="Send a message to the chatbot...",
        label="Your message",
    ),
)


# --------------------------------------------------
# 5. Launch locally
# --------------------------------------------------

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        inbrowser=True,
        share=False,
    )