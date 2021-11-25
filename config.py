'''
Global arguments
'''
import os

# maximum filesize in megabytes
file_mb_max = 100
# encryption key
app_key = 'any_non_empty_string'
# full path destination for our upload files
upload_dest = os.path.join(os.getcwd(), 'uploads_folder')
# list of allowed allowed extensions
extensions = set(['txt', 'pdf', 'png', 'tiff','gtiff'])


## on page '/upload' load display the upload file
@app.route('/upload')
def upload_form():
    return render_template('upload.html')


#############################
# Additional Code Goes Here #
#############################


if __name__ == "__main__":
    print('to upload files navigate to http://127.0.0.1:4000/upload')
    app.run(host='127.0.0.1', port=4000, debug=True, threaded=True)
