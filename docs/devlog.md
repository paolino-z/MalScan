### 4 Luglio
Ho modificato la struttura del progetto inserendo i vari file sotto la cartella /docs richiesti 👀

### 8 luglio
ho aggiornato la struttura del progetto (/src/progetto) con i requisiti e i file principali

### 13 luglio
abbiamo iniziato a scrivere la prima funzione (il motore), decidendo di fare una classe per file. inoltre abbiamo implementato il manuale tecnico (richiede modifiche)

### 14 luglio
aggiunto il controllo dell'estensione, inizio controllo regex

### 15 luglio
fine della classe regex, ho aggiunto anche una stringa conosciuta dagli antivirus: la stringa eicar. Questa stringa viene flaggata come malevola da tutti gli antivirus quindi ho pensato che fosse opportuno aggiungerla.
modifica alla struttura: dato che con il comando 'python3 -m malscan -h' restituiva errore, ho dovuto cambiare totalmente la struttura, aggiungendo 2 nuovi file: uno per la classe Check e uno per il print del report / funzione main (che ho rimosso dal file engine.py) e cambiando come facevo gli import. Ora avviando con il comando precedente il progetto funziona (spero 😿)