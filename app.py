from flask import Flask, request, jsonify
app = Flask(__name__)

# utility function: to check for valid files, only images
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload_image', methods= ['POST'])
def upload_image():
    # check if the post request has the file part
    if 'file' not in request.files:
      response = jsonify({'message' : 'No file part in the request'})
      response.status_code = 400
      return response
    
    file = request.files['file']

    # check if file not selected
    if file.filename == '':
      response = jsonify({'message' : 'No file selected for uploading'})
      response.status_code = 400
      return response
    
    # if file is valid
    if file and allowed_file(file.filename):
      response = jsonify({'message' : 'File successfully uploaded',
                          'filename' : str(file)
                        })
      response.status_code = 201
      return response
    
    # Check for other uncaught errors
    else:
      response = jsonify({'message' : 'Allowed file types are images: png, jpg, jpeg, gif'})
      response.status_code = 400
      return response

if __name__ == '__main__':
    app.debug = True
    app.run()

# from flask import Flask

# UPLOAD_FOLDER = '/Users/mujahidfa/Documents/tong-tong/uploads'

# app = Flask(__name__)
# app.secret_key = "secret key"
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# app.py
# from flask import Flask, request, jsonify
# app = Flask(__name__)

# @app.route('/getmsg/', methods=['GET'])
# def respond():
#     # Retrieve the name from url parameter
#     name = request.args.get("name", None)

#     # For debugging
#     print(f"got name {name}")

#     response = {}

#     # Check if user sent a name at all
#     if not name:
#         response["ERROR"] = "no name found, please send a name."
#     # Check if the user entered a number not a name
#     elif str(name).isdigit():
#         response["ERROR"] = "name can't be numeric."
#     # Now the user entered a valid name
#     else:
#         response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

#     # Return the response in json format
#     return jsonify(response)

# @app.route('/post/', methods=['POST'])
# def post_something():
#     param = request.form.get('name')
#     print(param)
#     # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
#     if param:
#         return jsonify({
#             "Message": f"Welcome {name} to our awesome platform!!",
#             # Add this option to distinct the POST request
#             "METHOD" : "POST"
#         })
#     else:
#         return jsonify({
#             "ERROR": "no name found, please send a name."
#         })

# # A welcome message to test our server
# @app.route('/')
# def index():
#     return "<h1>Welcome to our server !!</h1>"

# if __name__ == '__main__':
#     # Threaded option to enable multiple instances for multiple user access support
#     app.run(threaded=True, port=5000)