# MalScan

**MalScan** è un semplice scanner statico per l'analisi preliminare di file potenzialmente malevoli. Il progetto utilizza una serie di controlli modulari per assegnare un punteggio di rischio e generare un report leggibile sia in formato testuale che JSON.

> **Nota:** MalScan non sostituisce un antivirus professionale. È uno strumento didattico e di analisi preliminare.

---

## Requisiti

- Python 3.9+

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
