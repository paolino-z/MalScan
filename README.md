# MalScan

**MalScan** è un semplice scanner statico per l'analisi preliminare di file potenzialmente malevoli. Il progetto utilizza una serie di controlli modulari per assegnare un punteggio di rischio e generare un report leggibile sia in formato testuale che JSON.

> **Nota:** MalScan non sostituisce un antivirus professionale. È uno strumento didattico e di analisi preliminare.

---

## Caratteristiche

- Analisi dell'estensione del file
- Calcolo degli hash MD5 e SHA-256
- Analisi dell'entropia per individuare file compressi o cifrati
- Ricerca di pattern sospetti tramite espressioni regolari
- Verifica opzionale tramite VirusTotal API
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
    ├── virustotal.py      # Verifica opzionale tramite VirusTotal API
    └── regex.py           # Ricerca pattern sospetti
```

---

## Installazione

Clonare il repository:

```bash
git clone https://github.com/paolino-z/MalScan.git
cd MalScan
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
python __main__.py file
```

Oppure più semplice:

```bash
python -m malscan file
```

Per ottenere un report JSON:

```bash
python -m malscan --json-out report.json file
```

VirusTotal viene usato solo se passi la chiave API:

```bash
python -m malscan --virustotal-api-key LA_TUA_API_KEY file
```

Se non specifichi `--virustotal-api-key`, l'analisi **NON** userà VirusTotal

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

### VirusTotal API Check

Effettua una verifica online opzionale del file tramite VirusTotal quando viene fornita una chiave API.

Il controllo:

- calcola lo SHA-256 del file
- tenta di recuperare il report già presente su VirusTotal
- carica il file solo se il report non è disponibile e l'utente conferma l'upload

Se non specifichi `--virustotal-api-key`, il controllo viene saltato e l'analisi resta locale.

---

## Output

Esempio:

```text
============================================================
 MALSCAN REPORT
============================================================

Punteggio di rischio: 67/100

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

[+] VirusTotal API Check
    Punteggio parziale: 22
    Status: ...
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
- requests, usata per le chiamate a VirusTotal

Se non usi VirusTotal, le analisi locali restano comunque disponibili.

---

## Disclaimer

Questo software è stato sviluppato per scopi didattici e di analisi. Gli autori non sono responsabili per eventuali usi impropri o danni derivanti dall'utilizzo del software.
