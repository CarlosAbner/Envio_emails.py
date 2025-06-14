_create by: Abner Carlos_

# ABOUT PROJECT


This project there objective of create archive body.html in archive.pdf and send from e-mail the archive


## Project Structure

The Project start in make download of packages in the computer of user. Is necessary make download of these two archives:
- pdfkit
- jinja2

For jinja2 is necessary configure environment variables


## About send E-mail
The method that I use is Gmail for send, for this is necessary configurations in account Gmail, makeing auth 2FA, and create password of Gmail. And import this password that google generates in your gmail for send e-mail



## Method of Use
The code Python is in the version <b>Python 3.9.9</b> make the pip install of libs <b>(pdfkit and jinja2)</b> and import in your code.

The code starts with the function that starts the html creation parameters for generating the pdf. The function receive the somes parameters (optional) for fill in some spaces in code.html. After filling in the spaces, generate the PDF and save the file in root project

After generate of archive.pdf the function send_email, receiver thres paramenters:
- email of who is sending;
- email of who is receiver and
- password that google generated

Send_email function has the scope ready for this scenario of Gmail, take archive.pdf + subject + body for send addressee. When it is sent, the code will send the archive.pdf as an attachment.



## Structure of archives
```
│── PDF_EMAIL/  
│   ├── template/  
│        ── body.html/  
│   ├── main.py/  
│   ├── envio_email.py/  
│── gitignores  
│── config.py  
│── output.py
│── README.md  
│── variaveis_ambiente.py
```