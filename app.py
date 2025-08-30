from src import main
from flask import Flask , render_template , url_for ,request , send_file ,redirect
import io
import os
key=""
app=Flask(__name__,template_folder="templates")


@app.route("/")
def display_get_key():
    return render_template('key.html')


@app.route("/index")
def display_index():
    return render_template("index.html", special_message=request.args.get('special_message'))

@app.route("/display_encrypt")
def display_encrypt_page():
    encrypted_message=""
    return render_template("encrypt.html",encrypted_message=encrypted_message)

@app.route("/encrypt",methods=["post"])
def encrypt():
    file=request.files.get('message')
    if not file or file.filename=="":
        return "No file uploaded", 400
    message = file.read().decode()
   
    if not message:
        return "The file is empty", 400
    else:
        encrypted_message=main.encrypt(message)
        file_data=io.BytesIO(encrypted_message.encode("utf-8"))
        file_data.seek(0)
        return send_file(
            file_data,
            as_attachment=True,
            download_name=f"encrypted_{os.path.splitext(file.filename)[0]}",
            mimetype="text/plain"
        )

@app.route("/display_decrypt")
def display_decrypt_page():
    original_message=""
    return render_template("decrypt.html",original_message=original_message)


@app.route("/decrypt",methods=["Post"])
def decrypt():
    file=request.files.get('encrypted_message')
    if not file or file.filename=="":
        return "No file uploaded", 400
    encrypted_message=file.read().decode()
    if not encrypted_message:
        return "The file is empty", 400
    else:
        message=main.decrypt(encrypted_message)
        file_data=io.BytesIO(message.encode("utf-8"))
        file_data.seek(0)
        return send_file(
            file_data,
            as_attachment=True,
            download_name=f"message_{os.path.splitext(file.filename)[0]}",
            mimetype="text/plain"
        )
    
    
@app.route("/get_key",methods=["POST"])
def get_key():
    file=request.files.get('key')
    if not file or file.filename=="":
        return 'No file is uploaded' , 400
    
    _key=file.read().decode()
    if main.valid_key(_key):
        global key
        key=_key
        main.save_key(key)
        return redirect(url_for('display_index',special_message=""))
    else:
        return "Invalid key please go back to create an new one" , 401
    
    
@app.route("/new_key",methods=["GET","POST"])
def generate_key(): 
    _key=main.generate_key()
    global key
    key=_key
    main.save_key(key)
    return redirect(url_for('display_index',special_message="New key generated"))


@app.route("/validate_user_key",methods=['POST'])
def validate_user_key():
    key=request.form.get('user_key')
    if main.valid_key(key):
        main.save_key(key)
        return redirect(url_for('display_index',special_message="Key updated sucessfully"))
    else:
        message = "The key you entered is invalid. Please re-enter it, or go back to generate a new one."

        return render_template("key_generation.html", message=message,action='enter')

@app.route("/download_key",methods=["POST"])
def download_key():
    global key
    key_data=io.BytesIO(key.encode("utf-8"))
    key_data.seek(0)
    return send_file(
        key_data,
        download_name='key.txt',
        as_attachment=True,
        mimetype="text/plain"
    )


if(__name__=="__main__"):
    app.run(debug=True)