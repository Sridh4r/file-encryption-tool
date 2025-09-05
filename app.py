from src import main
from flask import Flask , render_template , url_for ,request , send_file ,redirect , session
import io
import os , secrets , base64

app=Flask(__name__,template_folder="templates")
app.secret_key = os.environ.get("SECRET_KEY", secrets.token_hex(16))


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

@app.route("/display_decrypt")
def display_decrypt_page():
    original_message=""
    return render_template("decrypt.html",original_message=original_message)


@app.route("/encrypt",methods=["POST","GET"])
def encrypt():
    file=request.files.get('message')
    if not file or file.filename=="":
        return "No file uploaded", 400
    message = file.read()
    if not message:
        return "The file is empty", 400
    else:
        message=base64.b64encode(message).decode("utf-8")
        encrypted_message=main.encrypt(message)
        file_data=io.BytesIO(encrypted_message.encode("utf-8"))
        file_data.seek(0)
        return send_file(
            file_data,
            as_attachment=True,
            download_name=f"encrypted_{file.filename}.enc",
            
        )

@app.route("/decrypt",methods=["POST","GET"])
def decrypt():
    file=request.files.get('encrypted_message')
    if not file or file.filename=="":
        return "No file uploaded", 400
    encrypted_message=file.read()
    if not encrypted_message:
        return "The file is empty", 400
    else:
        encrypted_message=encrypted_message.decode("utf-8")
        b64_message=main.decrypt(encrypted_message)
        message=base64.b64decode(b64_message)
        file_data=io.BytesIO(message)
        file_data.seek(0)
        return send_file(
            file_data,
            as_attachment=True,
            download_name=f"message_{file.filename[:-4]}",
            
        )
    
    
@app.route("/get_key",methods=["POST","GET"])
def get_key():
    file=request.files.get('key')
    if not file or file.filename=="":
        return 'No file is uploaded' , 400
    
    key=file.read().decode()
    if main.valid_key(key):
        session['key']=key
        main.save_key(session['key'])
        return redirect(url_for('display_index',special_message=""))
    else:
        return "Invalid key please go back to create an new one" , 401
    
    
@app.route("/new_key",methods=["GET","POST"])
def generate_key(): 
    session['key']=main.generate_key()
    main.save_key(session['key'])
    return redirect(url_for('display_index',special_message="New key generated"))


@app.route("/validate_user_key",methods=['POST','GET'])
def validate_user_key():
    key=request.form.get('user_key')
    if main.valid_key(key):
        session['key']=key
        main.save_key(session['key'])
        return redirect(url_for('display_index',special_message="Key updated sucessfully"))
    else:
        message = "The key you entered is invalid. Please re-enter it, or go back to generate a new one."

        return render_template("key_generation.html", message=message,action='enter')

@app.route("/download_key",methods=["POST","GET"])
def download_key():
    key_value=session.get('key')
    if not key_value:
        return "No key found in session. Please generate or upload a key first.", 400
    key_data=io.BytesIO(key_value.encode("utf-8"))
    key_data.seek(0)
    return send_file(
        key_data,
        download_name='key.key',
        as_attachment=True
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # use PORT from Render or default to 5000 locally
    app.run(host="0.0.0.0", port=port)
