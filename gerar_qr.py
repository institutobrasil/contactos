# Gerador de QR codes para os cartoes do Instituto Brasil
#
# COMO USAR:
# 1. Confirma o link base do teu site (ver README).
# 2. Se for diferente do que esta abaixo, edita a variavel BASE.
# 3. Corre:  python3 gerar_qr.py
#    (precisa de:  pip install qrcode pillow)
#
# Os ficheiros nilzete_qr.png e marcella_qr.png sao criados/atualizados.

import qrcode
from qrcode.constants import ERROR_CORRECT_H

# ============================================================
# EDITAR AQUI se o teu link for diferente.
# Tem de terminar com barra "/"
# ============================================================
BASE = "https://institutobrasil.github.io/contactos/"
# ============================================================

PESSOAS = {
    "nilzete":  "nilzete.html",
    "marcella": "marcella.html",
}

AZUL = (31, 95, 166)  # azul institucional IBR

for nome, pagina in PESSOAS.items():
    url = BASE + pagina
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=14, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=AZUL, back_color="white").convert("RGB")
    ficheiro = nome + "_qr.png"
    img.save(ficheiro)
    print("Gerado:", ficheiro, "->", url)

print("\nPronto. Agora abre crachas_imprimir.html e imprime em A4.")
