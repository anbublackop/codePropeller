from vertexai.language_models import CodeChatModel
import vertexai
def doc_gen(file_path, prompt_str):
    chat_model = CodeChatModel.from_pretrained("codechat-bison")
    vertexai.init(project='poc-analytics-ai', location='us-central1')
    if file_path == 'Unknown':
        file_data = ""
    else:
        with open(file_path) as f:
            file_data = f.read()
        file_data = """. Below is the input sample CSV data: """ + file_data
    parameters = {
        # "candidate_count": 1,
        "max_output_tokens": 2048,
        "temperature": 0.9
    }
    chat = chat_model.start_chat()

    # with open(file_path) as f:
    #     file_data = f.read()

    #print("file data: ", file_data)

    prompt= """generate code documentation which contains:
        1. Brief 2 lines about the code functionality.
        2. Name of function
        3. Description or summary of what functions, variables, modules does
        4. Parameters/Arguments
        5. Return value
        6. Raises and exceptions
        7. Dependencies/Requirements
        8. Version History. 
        Show output of all the above points on each separate line.
        Do not include any examples section. """ + prompt_str \
            + ". Generate it for following code: " + file_data


    response = chat.send_message(prompt, **parameters)

    #print(f"Response from Model: {response.text}")

    # res_dic = {}
    # res_dic['file_path'] = "documentation_result.txt"
    # res_dic['response'] = response.text

    # Write the response to a text file
    # with open(res_dic['file_path'], "w") as file:
    #     file.write(response.text)

    resp_text = response.text
    output_file = "documentation_result.txt"
    with open(output_file, 'w') as file:
        file.write(resp_text)


    return (output_file, resp_text)

# if __name__ == "__main__":
#     file_path = "C:\semicolons\sample_code.py"
#     prompt_str=""
#     print(model_response(file_path,prompt_str))