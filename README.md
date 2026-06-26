# MalScan
Repo del progetto finale di Python
# Proposta di progetto

## Titolo

**MalScan – Analizzatore statico di file sospetti**

## Descrizione del progetto

Il progetto consiste nello sviluppo di un programma da riga di comando in Python che analizza un file e ne valuta il livello di rischio attraverso una serie di controlli statici. Lo scanner calcola gli hash del file (SHA256, MD5), verifica la presenza di stringhe sospette tramite espressioni regolari, analizza l'entropia del contenuto per individuare file compressi o offuscati, controlla l'estensione e altre caratteristiche del file e produce un report finale con un punteggio di rischio. Come estensione opzionale, il programma potrà interrogare servizi online come VirusTotal (o altri scanner simili) utilizzando le API pubbliche, confrontando l'hash del file con database di malware già conosciuti.

## Problema che risolve e destinatari

Il programma è pensato come uno strumento didattico per effettuare una prima valutazione di un file sospetto prima della sua esecuzione. Può essere utile a studenti, appassionati di cybersecurity o amministratori di sistema che desiderano ottenere rapidamente informazioni sul potenziale livello di rischio di un file senza eseguirlo. L'obiettivo non è sostituire un antivirus professionale, ma fornire un'analisi statica basata su più controlli indipendenti.

## Competenze del corso utilizzate

* OOP
* Ereditarietà e polimorfismo
* File e JSON
* Hashing
* Regex
* Richieste HTTP tramite API REST (opzionale/terza fase con virutotal o altri scanner)
* Gestione delle eccezioni
* CLI con argparse

## Gerarchia di ereditarietà

Il progetto utilizza una classe `Check`, che rappresenta un generico controllo eseguibile su un file.

Sottoclassi:
* `HashCheck`
* `RegexCheck`
* `EntropyCheck`
* `ExtensionCheck`
* `VirusTotalCheck` (opzionale)
* eventuali altri controlli futuri (es altri scanner)

Tutte le sottoclassi implementano il metodo polimorfico `analyze(file_path)`, che restituisce il risultato del controllo. Lo scanner principale esegue tutti i controlli senza conoscere la loro implementazione specifica, sfruttando il polimorfismo. L'ereditarietà rende inoltre semplice aggiungere nuovi moduli di analisi senza modificare il funzionamento del motore principale.

## Piano di sviluppo

### Fase 1

* Progettazione delle classi.
* Implementazione della struttura del progetto.
* Realizzazione della CLI.
* Implementazione della classe base `Check`.

### Fase 2

* Implementazione dei controlli locali:
  * calcolo hash;
  * ricerca di stringhe sospette tramite regex;
  * analisi dell'entropia;
  * controllo dell'estensione del file.
* Generazione del report finale stampato sul terminale o con esportazione in formato JSON. 

### Fase 3

* Miglioramento della gestione degli errori.
* Implementazione opzionale del controllo tramite API di VirusTotal o altri servizi analoghi.

### Obiettivo a metà percorso

A metà dello sviluppo il programma dovrà essere in grado di analizzare un file tramite i controlli locali, generare un report con il livello di rischio e presentare i risultati in modo leggibile da riga di comando (sostanzialmente fino alla fase 2). L'integrazione con servizi online rappresenterà un'estensione successiva del progetto.
