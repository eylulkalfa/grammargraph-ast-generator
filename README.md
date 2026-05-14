# GrammarGraph: Dynamic AST Generator

BNF benzeri gramer dosyalarını okuyup cümleleri ayrıştıran, geçerli cümleler için parse ağacı üreten ve PNG olarak görselleştiren küçük bir Python projesi. İki farklı gramer (`grammar1.txt`, `grammar2.txt`) ve örnek cümle listeleri (`sentences1.txt`, `sentences2.txt`) içerir. LaTeX raporu `document/document.tex` altında yer alır.

## Gereksinimler

- Python 3.8+ (önerilir)
- [Graphviz](https://graphviz.org/) (PNG üretimi için; `pydot` bunu kullanır)

**macOS (Homebrew) Kurulumu:**
`brew install graphviz`

*(Not: Windows kullanıcıları Graphviz'i resmi sitesinden indirip kurulum sırasında 'Add to PATH' seçeneğini işaretlemelidir.)*

## Kurulum

```bash
cd "programminglanguages_FINAL"
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
