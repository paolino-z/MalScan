# Architettura Generale

MalScan segue una filosofia molto semplice: **disaccoppiamento totale**.

Il nucleo dell'applicazione non sa (e non gli interessa sapere) come un singolo controllo analizzi il file. Il motore si limita a prendere una lista di controlli, passargli il file e raccogliere i risultati.

Il flusso dei dati è lineare:

* **La CLI (`main`)** intercetta il percorso del file.
* Viene istanziato il motore principale (`MalScanEngine`).
* Vengono registrati i moduli di analisi (i vari `Check`).
* Il motore lancia l'analisi collettiva, calcola il punteggio aggregato e restituisce il report (a schermo o in formato `JSON`).

## La Gerarchia delle Classi (Il cuore del Polimorfismo)

Per l'architettura dei controlli abbiamo sfruttato a fondo la programmazione a oggetti (OOP), in particolare l'ereditarietà e il polimorfismo. Al centro di tutto c'è una classe base astratta.
