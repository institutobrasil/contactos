# Cartões digitais — Instituto Brasil

Cartões de contacto digitais para a Nilzete Pacheco e a Marcella Bisetto, com QR code, foto, logo e botão para guardar o contacto (vCard) e WhatsApp.

São permanentes: servem para qualquer evento.

---

## O que está nesta pasta

- `index.html` — página de entrada com as duas pessoas (menu)
- `nilzete.html` — cartão da Nilzete Pacheco
- `marcella.html` — cartão da Marcella Bisetto
- `crachas_imprimir.html` — folha A4 com os dois QR codes para imprimir e recortar
- `nilzete_qr.png` / `marcella_qr.png` — os QR codes (usados pela folha acima)
- `gerar_qr.py` — script para regenerar os QR se o link mudar

As fotos e o logo estão embutidos dentro dos HTML. Não há ficheiros de imagem soltos a gerir.

---

## Como funciona

O QR code aponta para a página do cartão. A pessoa escaneia, abre no telemóvel, e carrega em "Guardar contacto". O telemóvel descarrega um ficheiro `.vcf` e importa-o nativamente — funciona em iPhone, Android, Outlook e Google. Não é preciso servidor.

---

## Pôr online no GitHub Pages (via Code / git)

Os exemplos abaixo usam utilizador `institutobrasil` e repositório `contactos`. Troca pelos teus nomes reais (o nome do repositório fica visível no link, por isso escolhe algo simples como `contactos` ou `cartoes`).

```bash
# dentro desta pasta
git init
git add .
git commit -m "Cartões digitais Instituto Brasil"
git branch -M main
git remote add origin https://github.com/institutobrasil/contactos.git
git push -u origin main
```

Depois, no GitHub:
1. Abre o repositório → Settings → Pages
2. Em Branch escolhe `main` e pasta `/ (root)` → Save
3. Espera 1 a 2 minutos

Os links ficam:
- Menu: `https://institutobrasil.github.io/contactos/`
- Nilzete: `https://institutobrasil.github.io/contactos/nilzete.html`
- Marcella: `https://institutobrasil.github.io/contactos/marcella.html`

### Alternativa sem git (pelo site)
Repositório → Add file → Upload files → arrasta tudo → Commit. Depois faz o passo do Pages acima.

---

## Se o teu link for diferente

Os QR já estão feitos para o link acima. Se usares outro utilizador ou repositório (ou um domínio próprio como `institutobrasil.pt`), faz isto:

1. Abre `gerar_qr.py` e edita a linha `BASE` com o teu link (tem de acabar em `/`).
2. Corre:
   ```bash
   pip install qrcode pillow
   python3 gerar_qr.py
   ```
3. Os QR são atualizados.

---

## Imprimir os crachás

Abre `crachas_imprimir.html` no navegador e imprime em A4 (Ctrl+P). Saem os dois crachás prontos a recortar para um porta-crachás ou botão.

---

## Atualizar dados no futuro

Cada cartão tem um bloco no fim do ficheiro (dentro de `<script>`) com nome, cargo, email, telefone e WhatsApp. Edita aí, grava, e faz novo `git push`. Para trocar a foto é preciso voltar a gerar o HTML (pede ajuda se precisares).

---

## Verificação antes de usar

Testa o fluxo completo num telemóvel: escaneia o QR, abre o cartão, carrega em "Guardar contacto" e confirma que o contacto entra mesmo. Faz com iPhone e Android se possível.
