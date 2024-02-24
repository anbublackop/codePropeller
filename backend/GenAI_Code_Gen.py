from vertexai.language_models import CodeGenerationModel
import vertexai
def generate_code(prompt_str):
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 2048,
        "temperature": 0.9
    }
    vertexai.init(project='poc-analytics-ai', location='us-central1')

    model = CodeGenerationModel.from_pretrained("code-bison")
    response = model.predict(
        prefix = prompt_str,
        **parameters
    )
    #print(f"Response from Model: {response.text}")
    resp_text=response.text.replace("```python","")
    resp_text=resp_text.replace("```","")
    output_file='sample_code.py'
    with open(output_file, 'w') as json_file:
        json_file.write(resp_text)

    # with open(res_dic['file_path'], 'w') as json_file:
    #     json_file.write(responses.text)

    return (output_file,resp_text)

prompt_str="""Write a python code which does following task.
                    1. Read the sample_test_data.csv file 
                    2. Iterate over all the lines and convert it into the JSON format.
                    3. First row signifies the column header.
                    4. Do not assume any column names by your own.
                    5. Save the output in separate file with same name but extension as .json.
                    6. Write a well formatted code fulfilling the above the requirement.
    """

# print(generate_code(prompt_str))