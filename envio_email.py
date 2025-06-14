import smtplib
from email.message import EmailMessage
import logging


def send_email(email_address, receiver, password):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 465

        subject = 'Conteudo do Seu E-mail'

        # Configuração do e-mail
        msg = EmailMessage()
        msg['From'] = email_address
        msg['To'] = receiver
        msg['Subject'] = subject

        # Aqui adicionamos o texto do corpo do email
        msg.set_content('Olá,\n\nSegue em anexo o arquivo solicitado.\n\nQualquer dúvida estou à disposição.\n\nAtenciosamente,\n[Seu Nome]')


        # Anexar o arquivo
        file_path = 'output.pdf'  # caminho para seu arquivo
        with open(file_path, 'rb') as f:
            file_data = f.read()
            file_name = f.name  # nome do arquivo

        msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

        # Envio do email
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
            smtp.login(email_address, password)
            smtp.send_message(msg)

        print('E-mail enviado com sucesso')
    except Exception as e:
        logging.error('Erro ao enviar e-mail: ' + str(e))