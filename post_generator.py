from llm_helper import llm

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    elif length == "Medium":
        return "6 to 10 lines"
    else:
        return "more than 10 lines"

def generate_post(length, language, topic):
    prompt = ''''''
    response = llm.invoke(prompt)
    return response.content