from vertexai.language_models import CodeChatModel
import vertexai

def model_response(file_path,prompt_str):
    if file_path == 'Unknown':
        file_data = ""
    else:
        with open(file_path) as f:
            file_data = f.read()
        file_data = """. Below is the input sample python data: """ + file_data
    # TODO developer - override these parameters as needed:
    vertexai.init(project="poc-analytics-ai", location="us-central1")

    parameters = {
        "candidate_count": 1,
        "temperature": 0.9,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 1024  # Token limit determines the maximum amount of text output.
    }

    code_chat_model = CodeChatModel.from_pretrained("codechat-bison")
    chat = code_chat_model.start_chat()

    # with open(file_path) as f:
    #     file_data = f.read()

    #print("file data: ", file_data)

    # Prompt user for code input
    user_input = """Review the following code and provide suggestions for clarity, efficiency, adherence to best practices, 
                 and potential bugs. suggest optimizations where applicable. Prioritize readability, 
                 maintainability, and performance in your evaluation. 
                 At the end provide the optimized version of the code incorporating 
                 the above suggestions. """ + prompt_str + ". Generate it for above code. " + file_data

    response = chat.send_message(user_input, **parameters)

    #print(f"Response from Model: {response.text}")
    # res_dic = {}
    # res_dic['file_path'] = "review_result.txt"
    # res_dic['response'] = response.text

    # # Write the response to a text file
    # with open(res_dic['file_path'], "w") as file:
    #     file.write(response.text)

    # return res_dic
    resp_text = response.text
    output_file = "review_result.txt"
    with open(output_file, 'w') as file:
        file.write(resp_text)
    return (output_file, resp_text)

# if __name__ == "__main__":
#     file_path = "C:\semicolons\sample_code.py"
#     prompt_str=""
#     print(model_response(file_path,prompt_str))