# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, Response, request
from flask_cors import CORS

from create_csv_data import create_augmentated_data
from GenAI_Code_Gen import generate_code, prompt_str
from code_review_model_first import model_response
from document_generation import doc_gen
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
CORS(app)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/generate-code', methods=["POST"])
# ‘/’ URL is bound with gen_code() function.
def gen_code():
    try:
        prompt_str = request.json.get('prompt_str')
        logger.info(f"Getting params as {prompt_str}")
        res = generate_code(prompt_str)
        logger.info(res)
        return Response(
            response = res,
            status = 200            
        )
    except Exception as e:
        logger.info(f"Getting exception as: {e}")
        return Response(
            response = "Internal server error",
            status = 500            
        )

@app.route('/augment-data', methods=["POST"])
# ‘/’ URL is bound with augment_data() function.
def augment_data():
    try:
        prompt_str = request.json.get('prompt_str')
        file_path = request.json.get('file_path')
        res = create_augmentated_data(file_path, prompt_str)
        logger.info(res)
        return Response(
            response = res,
            status = 200            
        )
    except Exception as e:
        logger.info(f"Getting exception as: {e}")
        return Response(
            response = "Internal server error",
            status = 500            
        )

@app.route('/code-review',methods=["POST"])
# ‘/’ URL is bound with code_review() function.
def code_review():
    try:
        prompt_str = request.json.get('prompt_str')
        file_path = request.json.get('file_path')
        logger.info(f"Getting params as {prompt_str}")
        res = model_response(file_path, prompt_str)
        logger.info(res)
        return Response(
            response = res,
            status = 200            
        )
        # res = model_response()
        # return Response(
        #     response = str(res),
        #     status = 200            
        # )
    except Exception as e:
        logger.info(f"Getting exception as: {e}")
        return Response(
            response = "Internal server error",
            status = 500            
        )


@app.route('/doc-generation', methods=["POST"])
# ‘/’ URL is bound with gen_code() function.
def doc_generation():
    try:
        prompt_str = request.json.get('prompt_str')
        file_path = request.json.get('file_path')
        logger.info(f"Getting params as {prompt_str}")
        res = doc_gen(file_path,prompt_str)
        logger.info(res)
        return Response(
            response = res,
            status = 200            
        )
    except Exception as e:
        logger.info(f"Getting exception as: {e}")
        return Response(
            response = "Internal server error",
            status = 500            
        )

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()