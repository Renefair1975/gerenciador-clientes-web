from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

# Função genérica para criar PDFs
def criar_pdf(nome_arquivo, titulo, conteudo):
    caminho_arquivo = os.path.join(os.getcwd(), nome_arquivo)

    c = canvas.Canvas(caminho_arquivo, pagesize=A4)
    largura, altura = A4

    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, altura - 100, titulo)

    c.setFont("Helvetica", 12)
    texto_y = altura - 140

    for linha in conteudo.split("\n"):
        c.drawString(100, texto_y, linha)
        texto_y -= 20

    c.save()
    return caminho_arquivo

# Gerar Contrato
def gerar_contrato(cliente_id, nome, cpf, telefone, email, endereco):
    conteudo = f"""
    Nome: {nome}
    CPF: {cpf}
    Telefone: {telefone}
    Email: {email}
    Endereço: {endereco}

    Pelo presente contrato, as partes têm entre si justo e contratado o seguinte:
    1. O contratado prestará serviços conforme acordado.
    2. O contratante pagará pelos serviços conforme combinado.
    3. O presente contrato tem validade a partir da data de sua assinatura.

    Assinado digitalmente pelas partes.
    """
    return criar_pdf(f"Contrato_{nome.replace(' ', '_')}.pdf", "CONTRATO DE PRESTAÇÃO DE SERVIÇOS", conteudo)

# Gerar Procuração
def gerar_procuracao(cliente_id, nome, cpf, telefone, email, endereco):
    conteudo = f"""
    Nome: {nome}
    CPF: {cpf}
    Endereço: {endereco}

    Pelo presente instrumento particular, {nome}, concede poderes ao advogado para representá-lo
    em juízo ou fora dele, com poderes para o foro em geral, incluindo o direito de substabelecer.

    Assinado digitalmente pelas partes.
    """
    return criar_pdf(f"Procuracao_{nome.replace(' ', '_')}.pdf", "PROCURAÇÃO", conteudo)

# Gerar Nota Promissória
def gerar_nota_promissoria(cliente_id, nome, cpf, telefone, email, endereco):
    conteudo = f"""
    Nome: {nome}
    CPF: {cpf}
    Endereço: {endereco}

    Pelo presente instrumento, {nome} promete pagar a quantia de R$ _______ ao credor, no prazo estabelecido.

    Assinado digitalmente pelas partes.
    """
    return criar_pdf(f"Nota_Promissoria_{nome.replace(' ', '_')}.pdf", "NOTA PROMISSÓRIA", conteudo)

# Gerar Declaração
def gerar_declaracao(cliente_id, nome, cpf, telefone, email, endereco):
    conteudo = f"""
    Nome: {nome}
    CPF: {cpf}
    Endereço: {endereco}

    Declaro para os devidos fins que {nome} reside no endereço acima e não possui nenhuma pendência legal.

    Assinado digitalmente pelas partes.
    """
    return criar_pdf(f"Declaracao_{nome.replace(' ', '_')}.pdf", "DECLARAÇÃO", conteudo)

# Gerar Recibo de Pagamento
def gerar_recibo(cliente_id, nome, cpf, telefone, email, endereco):
    conteudo = f"""
    Nome: {nome}
    CPF: {cpf}
    Endereço: {endereco}

    Pelo presente, {nome} declara ter recebido a quantia de R$ _______ referente a _______.

    Assinado digitalmente pelas partes.
    """
    return criar_pdf(f"Recibo_{nome.replace(' ', '_')}.pdf", "RECIBO DE PAGAMENTO", conteudo)
