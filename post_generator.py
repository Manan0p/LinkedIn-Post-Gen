from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    elif length == "Medium":
        return "6 to 10 lines"
    else:
        return "more than 10 lines"

def generate_post(length, language, topic):
    length_str = get_length_str(length)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {topic}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''

    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    post = generate_post("Short", "English", "Job Search")
    print(post)