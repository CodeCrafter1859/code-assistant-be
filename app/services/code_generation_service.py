# from openai import OpenAI
from dotenv import load_dotenv
import google.generativeai as genai
import os
load_dotenv()


# OPEN_AI_API = os.getenv("OPEN_AI_API")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")
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