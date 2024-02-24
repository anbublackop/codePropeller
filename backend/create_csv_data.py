from vertexai.preview.language_models import TextGenerationModel
import pandas as pd
import vertexai 
def create_augmentated_data(file_path, prompt_str):

    if file_path == 'Unknown':
        file_data = ""
    else:
        with open(file_path) as f:
            file_data = f.read()
        file_data = """. Below is the input sample CSV data: """ + file_data
    vertexai.init(project="poc-analytics-ai", location="us-central1")

    text_generation_model = TextGenerationModel.from_pretrained("text-bison-32k")
    parameters = {
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1
    }
    #print("file_data:", file_data)

    user_input = f"""
    First row of the given input CSV data specifies column names.
    output should be the 15 different rows in CSV format similar to the given sample data, do not print the coding part. 
    Output should not consist of any Null, NA or None values.
    Output should not copy any data from input data except first row of column names.
    Output rows should consist of first line same as column names specified in the input CSV data.
    """ + prompt_str + file_data

    responses = text_generation_model.predict(prompt=user_input, **parameters)

    print("response:",responses.text)
    res_dic = {}
    res_dic['file_path'] = 'sample_test_data.csv'
    res_dic['response'] = responses.text
    with open(res_dic['file_path'], 'w') as json_file:
        json_file.write(responses.text)
    return responses.text


# file_path = "companies.csv"
# prompt_str=""
# print(create_augmentated_data(file_path, prompt_str))