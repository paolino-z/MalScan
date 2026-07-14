### La classe Base: Check

Questa è la classe astratta, la "madre" di tutti i controlli.
Utilizza il modulo abc (Abstract Base Classes) di Python. Definisce un unico metodo che definisce il "contratto" che tutte le sottoclassi devono rispettare. Ogni volta che si crea un nuovo controllo, bisogna implementare analyze. Questo metodo deve sempre accettare il percorso del file e restituire un dizionario con una struttura fissa: name, score e details.


### Le Sottoclassi

Ecco come i controlli attuali verranno implementati, ognuno specializzato in un compito:
* HashCheck: Apre il file in modalità binaria a blocchi (per non saturare la RAM se il file è enorme) e calcola i checksum MD5 e SHA256. Non genera punteggio di rischio (score = 0), serve solo come info di telemetria.

* ExtensionCheck: Fa un controllo rapidissimo sull'estensione. Ha una blacklist interna (.exe, .bat, .ps1, ecc.). Se c'è un match, assegna un rischio iniziale di 40.

* EntropyCheck: Questo è un po' più matematico. Calcola l'entropia di Shannon del file (la casualità dei byte). Se l'entropia è molto alta (> 7.2), significa che il file è probabilmente compresso, criptato o offuscato (tecnica tipica dei malware/packer). In tal caso, spara un bonus di rischio di 35.

* RegexCheck: Scansiona il binario alla ricerca di stringhe testuali sospette. Ogni match aumenta il rischio in modo cumulativo (fino a un tetto massimo di 60).

### Il Motore

Il motore è un semplice orchestratore. Ha una lista interna chiamata self.checks.
Quando chiami engine.run(file_path), lui fa un ciclo for su tutti i controlli registrati. Riceve il dizionario, somma i punteggi (facendo un cap massimo a 100) e mappa il livello di rischio finale.

### Come estendere MalScan

Vuoi aggiungere un controllo? Ti basta seguire questi due passi:

Passo 1: Crea la tua sottoclasse
Scrivi la tua classe derivata da Check in un nuovo file:

```python
from malscan.engine import Check
class esempio(Check):
    def analyze(self, file_path: str) -> dict:
        pass
```

Passo 2: Registra il controllo nel main()
Vai nella funzione main() dove viene configurato l'engine e aggiungi la tua riga:

```python
from checks.esempio import esempio

engine = MalScanEngine()
engine.add_check(HashCheck())
engine.add_check(ExtensionCheck())
engine.add_check(EntropyCheck())
engine.add_check(RegexCheck())
engine.add_check(esempio())
```