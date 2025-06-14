import sys
import os
import jinja2
import pdfkit
import pandas as pd


# Adiciona a pasta raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from envio_email import send_email
import config

def main(nome_empresa, cnpj_empresa,valor_nota):
    context = {'primeira_palavra': nome_empresa,
            'cnpj_empresa': cnpj_empresa,
            'valor_nota': valor_nota}

    # Configuração do Jinja2
    template_loader = jinja2.FileSystemLoader('./template')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("body.html")
    output_text = template.render(context)

    # Configuração do PDFKit
    try:
        # Caminhos alternativos comuns no Windows
        possible_paths = [
            r'C:\Program Files\wkhtmltox\bin\wkhtmltopdf.exe',
            r'C:\Program Files\wkhtmltox\bin\wkhtmltopdf.exe',
            r'C:\Program Files\wkhtmltox\bin\wkhtmltopdf.exe'
        ]

        config = None
        for path in possible_paths:
            if os.path.exists(path):
                config = pdfkit.configuration(wkhtmltopdf=path)
                break

        if config is None:
            # Tenta usar do PATH
            config = pdfkit.configuration()

        # Opções para evitar erros comuns
        options = {
            'enable-local-file-access': None,
            'quiet': ''
        }

        # Gera o PDF
        pdfkit.from_string(
            output_text,
            'output.pdf',
            configuration=config,
            options=options
        )

        print("PDF gerado com sucesso!")
        x=0

    except Exception as e:
        print(f"Erro ao gerar PDF: {str(e)}")
        print("\nSoluções possíveis:")
        print("1. Verifique se wkhtmltopdf está instalado corretamente")
        print("2. Especifique o caminho exato no código")
        print("3. Como alternativa, use WeasyPrint:")
        print("4. pip install weasyprint")
        print("5. from weasyprint import HTML")
        print("6. HTML(string=output_text).write_pdf('output.pdf')")


if __name__ == '__main__':
    main(nome_empresa='Nome Empresa', cnpj_empresa='00.000.000/0000-00',valor_nota='789.49')

    # envia o .pdf por gmail
    send_email(config.EMAIL, config.DESTINATARIOS, config.PASSWORD)