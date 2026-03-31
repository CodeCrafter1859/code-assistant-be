def generate_code(prompt: str, language: str):
    
    if language.lower() == "python":
        return f"# Python code for: {prompt}\nprint('Hello from AI assistant')"

    if language.lower() == "javascript":
        return f"// JavaScript code for: {prompt}\nconsole.log('Hello from AI assistant')"

    return "Language not supported"