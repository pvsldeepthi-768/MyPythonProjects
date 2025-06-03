#step -1:import libraries
import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from huggingface_hub import login

#step- 2: Configure the page
st.set_page_config(page_title="chatbot with you",page_icon=":robot_face:",layout="wide")
st.title("Chatbot with you :robot_face:")
#step-3: Login to Hugging Face
hf_API = "Your Hugging Face API token here"  # Replace with your Hugging Face API token
if hf_API !="":
    login(token=hf_API)
else:
    st.warning("Please provide your Hugging Face API token to access the model.")

#step-4:Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

#step-5: Load the model and tokenizer
@st.cache_resource
def load_model():
    model_name = "ibm-granite/granite-3.3-2b-instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name,
                                                 torch_dtype=torch.bfloat16,
                                                 device_map="auto",
                                                )
    return model, tokenizer
#step-6: Generate response
def generate_response(prompt, model, tokenizer):
    formatted_prompt = f"Human: {prompt}\nAssistant:"
    inputs = tokenizer(formatted_prompt, return_tensors="pt").to(model.device)
    if torch.cuda.is_available():
        inputs = {k: v.to(model.device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=200,  temperature=0.7,
                                 top_p=0.9,do_sample=True)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.split("Assistant:")[-1].strip()


with st.spinner("Loading model..."):
    model, tokenizer = load_model()
st.success("Model loaded successfully!")
#step-7: display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#step-8: User input
if prompt := st.chat_input("You can ask here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            response = generate_response(prompt, model, tokenizer)
    
    # Display the assistant's response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

#step-9: Clear chat history
if st.button("Clear chat history"):
    st.session_state.messages = []
    st.experimental_rerun()  # Refresh the app to clear the chat history