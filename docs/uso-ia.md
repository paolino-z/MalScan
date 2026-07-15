### Il problema: Regex
*Cosa ho chiesto:* Ho riscontrato dei SyntaxWarning (relativi a sequenze di escape non valide come \. o \() durante l'esecuzione dei test sulla classe RegexCheck e ho chiesto come risolverli. Ho anche chiesto come gestire meglio l'output in caso di nessun match trovato.

*Cosa mi ha risposto:* L'IA mi ha spiegato che nelle versioni recenti di Python l'uso dei backslash nelle stringhe di byte standard (b"...") genera avvertimenti di sintassi. Per risolvere il problema, abbiamo convertito le definizioni dei pattern in raw byte string utilizzando il prefisso rb"...", che dice a Python di trattare i backslash come caratteri letterali.

Inoltre abbiamo approfondito l'uso del modulo nativo import re (la libreria standard di Python per le espressioni regolari), in particolare la funzione re.findall() utilizzata per cercare corrispondenze all'interno del flusso di byte del file analizzato.

### Errore dei moduli
Provando a runnare il comando python3 -m malscan -h mi usciva un errore ModuleNotFoundError: No module named 'checks'.
*Cosa ho chiesto:* All'IA ho chiesto come mai dopo aver suddiviso i file per classe mi usciva l'errore.
*Cosa mi ha risposto:* Perchè veniva cercato come se fosse un pacchetto di primo livello, cioè qualcosa che Python dovesse trovare direttamente nel path di importazione.
Mi ha suggerito le modifiche e mi ha spiegato 'nel refactor ha messo il punto davanti nei file dentro malscan/ perché lì stiamo facendo import relativi dentro lo stesso package.Mi ha anche dato un esempio: 'in malscan/cli.py scrivere from .checks.hash import HashCheck significa: cerca il modulo hash dentro il package corrente malscan. Questo è il modo giusto quando i file stanno tutti sotto lo stesso package e vuoi evitare dipendenze da come viene lanciato il progetto.'