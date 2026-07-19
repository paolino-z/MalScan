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

### 16, 17, 18 e 19 luglio
siamo riusciti a finire il progetto aggiungendo le classi finali per il controllo dell'hash e entropia. ci sono venute in mente anche altre idee per le regex e le abbiamo volute suddividere per renderci più facile la lettura, tutte inserite nel proprio file.
Abbiamo anche aggiunto la classe VirusTotal, in modo da poterlo usare sia in locale che online.

* 16 luglio: Classe HashCheck con contollo hash e md5
* 17 luglio: Classe EntropyCheck con controllo sull'entropia del file e aggiunta espressioni regex
* 18 e 19 luglio: Classe VirusTotal


### Fine progetto: 19 luglio.