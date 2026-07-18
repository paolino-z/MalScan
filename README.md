# MalScan

**MalScan** è un semplice scanner statico per l'analisi preliminare di file potenzialmente malevoli. Il progetto utilizza una serie di controlli modulari per assegnare un punteggio di rischio e generare un report leggibile sia in formato testuale che JSON.

> **Nota:** MalScan non sostituisce un antivirus professionale. È uno strumento didattico e di analisi preliminare.

---

## Caratteristiche

- Analisi dell'estensione del file
- Calcolo degli hash MD5 e SHA-256
- Analisi dell'entropia per individuare file compressi o cifrati
- Ricerca di pattern sospetti tramite espressioni regolari
- Report in formato testo o JSON
- Architettura modulare facilmente estendibile

---

## Struttura del progetto

```text
malscan/
│
├── __main__.py
├── __init__.py
├── cli.py                 # Interfaccia a riga di comando
├── engine.py              # Motore di scansione
│
└── checks/
    ├── base.py            # Classe astratta per i controlli
    ├── entropy.py         # Analisi dell'entropia
    ├── extension.py       # Controllo estensioni sospette
    ├── hash.py            # Calcolo hash
    └──regex.py           # Ricerca pattern sospetti
```

---

## Installazione

Clonare il repository:

```bash
git clone https://github.com/<username>/malscan.git
cd malscan
```

Installare le dipendenze:

```bash
pip install requests
```

In alternativa:

```bash
pip install -r requirements.txt
```

---

## Utilizzo

Analisi di un file:

```bash
python -m malscan percorso/del/file
```

Oppure:

```bash
python -m malscan sample.exe
```

Per ottenere un report JSON:

```bash
python -m malscan sample.exe --json
```

---

## Controlli eseguiti

### Extension Check

Verifica se il file possiede un'estensione comunemente associata a software eseguibile o script potenzialmente pericolosi.

Esempi:

- `.exe`
- `.dll`
- `.bat`
- `.cmd`
- `.ps1`
- `.vbs`
- `.jar`

---

### Hash Analysis

Calcola:

- MD5
- SHA-256

Gli hash possono essere utilizzati per:

- identificare un file
- confrontarlo con database malware
- verificare l'integrità

---

### Entropy Analysis

Calcola l'entropia di Shannon del file.

Un'entropia elevata può indicare:

- file cifrati
- file compressi
- malware packato

---

### Regex Analysis

Ricerca firme e pattern sospetti, ad esempio:

- PowerShell
- cmd.exe
- WScript
- URL HTTP/HTTPS
- chiamate `eval()`
- chiamate `exec()`
- `system()`
- firma del file di test EICAR

---

## Output

Esempio:

```text
============================================================
 MALSCAN REPORT
============================================================

Punteggio di rischio: 45/100

Livello di rischio: Medio

[+] Extension Security Check
    extension: .exe
    is_suspicious: True

[+] Hash Analysis
    md5: ...
    sha256: ...

[+] Entropy Analysis
    entropy: 7.53
    packed_or_encrypted: True

[+] Regex Analysis
    PowerShell Execution Reference
    Network Activity Indicator
```

---

## Architettura

Ogni controllo eredita dalla classe astratta `Check`:

```python
class Check:
    def analyze(self, file_path):
        ...
```

Il motore (`MalScanEngine`) esegue tutti i controlli registrati e produce un report finale contenente:

- risultati dei singoli controlli
- punteggio complessivo
- livello di rischio

Questo rende semplice aggiungere nuovi moduli di analisi.

---

## Dipendenze

- Python 3.9+

---

## Disclaimer

Questo software è stato sviluppato per scopi didattici e di analisi. Gli autori non sono responsabili per eventuali usi impropri o danni derivanti dall'utilizzo del software.
