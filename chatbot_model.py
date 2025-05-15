import re
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load Chatbot Model (DialoGPT)
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# ✅ Assign pad token
tokenizer.pad_token = tokenizer.eos_token  

def generate_response(prompt):
    inputs = tokenizer(prompt + tokenizer.eos_token, return_tensors="pt", padding=True, truncation=True, max_length=50)

    output = model.generate(
        input_ids=inputs["input_ids"],  
        attention_mask=inputs["attention_mask"],  
        max_length=50,  # ✅ Increased max length for better responses
        temperature=0.8,  # ✅ More creative responses
        top_p=0.9,  # ✅ Improved response variety
        repetition_penalty=1.8,  # ✅ Reduces repetitive answers
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id  
    )

    # Decode Response
    response = tokenizer.decode(output[0], skip_special_tokens=True).strip()

    # ✅ Remove input echo
    response = re.sub(rf"^{re.escape(prompt)}", "", response, flags=re.IGNORECASE).strip()

    # ✅ Stop at first full sentence
    response = re.split(r"[.!?]", response)[0].strip()

    # ✅ Remove unwanted symbols
    response = re.sub(r"[:;<>3D]", "", response)  
    response = response.replace("...", "").strip()  

    return response

# Test
if __name__ == "__main__":
    response = generate_response("Who is Virat Kohli?")
    print("Chatbot Response:", response)