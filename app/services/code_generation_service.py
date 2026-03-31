# from openai import OpenAI
import google.generativeai as genai
from app.config import API_KEY, MODEL_NAME



# OPEN_AI_API = os.getenv("OPEN_AI_API")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL_NAME)
# client = OpenAI(api_key=OPEN_AI_API)


# def generate_code(prompt, language):

#     full_prompt = f"""
# You are an expert programmer.
# Generate {language} code for the following request:

# {prompt}

# Return only code.
# """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role":"user","content":full_prompt}
#         ]
#     )

#     return response.choices[0].message.content


def generate_code(prompt, language):

    full_prompt = f"""
        You are an expert programmer.
        Generate {language} code for the following request:
        {prompt}

        Return only code.
        """

    response = model.generate_content(full_prompt)

    return response.text

def explain_code(code):

    full_prompt = f"""
        You are an expert who can explain the code in effective way.
        explain the below code
        {code}
        return step by step explaination.
        """

    response = model.generate_content(full_prompt)
    print(response)

    return response.text