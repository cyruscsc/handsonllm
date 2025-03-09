from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    device_map="auto",
    torch_dtype="auto",
    trust_remote_code=False,
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

# create a pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=False,
    max_new_tokens=500,
    do_sample=False,
)


def main():
    # prompt
    prompt = input("Enter a prompt: ")
    messages = [
        {"role": "user", "content": prompt},
    ]

    # generate output
    output = generator(messages)
    print(output[0]["generated_text"])


if __name__ == "__main__":
    main()
