from flask import Flask, request, render_template, send_file, redirect, url_for
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_url', methods=['POST'])
def process_url():
    url = request.form['url']

    print("Received URL:", url)

    from yt_dlp import YoutubeDL

    URLS = [url]
    with YoutubeDL(params={
        "paths": {"temp": "files"},
        "noplaylist": True
        }) as ydl:
        ydl.download(URLS)
    
    # return redirect(url_for('download', filename='myfile.pdf'))              

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # Assuming the files are stored in the 'files' directory
    file_path = f'files/{filename}'
    # Send the file to the client
    return send_file(file_path, as_attachment=True)
    

if __name__ == '__main__':
    app.run(debug=True)
