### Il problema: Regex
*Cosa ho chiesto:* Ho riscontrato dei SyntaxWarning (relativi a sequenze di escape non valide come \. o \() durante l'esecuzione dei test sulla classe RegexCheck e ho chiesto come risolverli. Ho anche chiesto come gestire meglio l'output in caso di nessun match trovato.

*Cosa mi ha risposto:* L'IA mi ha spiegato che nelle versioni recenti di Python l'uso dei backslash nelle stringhe di byte standard (b"...") genera avvertimenti di sintassi. Per risolvere il problema, abbiamo convertito le definizioni dei pattern in raw byte string utilizzando il prefisso rb"...", che dice a Python di trattare i backslash come caratteri letterali.

Inoltre abbiamo approfondito l'uso del modulo nativo import re (la libreria standard di Python per le espressioni regolari), in particolare la funzione re.findall() utilizzata per cercare corrispondenze all'interno del flusso di byte del file analizzato.