import csv

class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile

        automobili = Autonoleggio()
        automobili.nome = self.nome
        automobili.responsabile = self.responsabile


    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=',')
                for row in reader:
                    self.codice = row[0]
                    self.marca = row[1]
                    self.modello = row[2]
                    self.anno = int(row[3])
                    self.num_posti = int(row[4])


        except FileNotFoundError:
            print("File non trovato")


    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""

        nuova_auto = [self.marca, self.modello, self.anno, self.num_posti]

        for self.codice in Autonoleggio.__dict__.keys():
            if nuova_auto not in Autonoleggio.__dict__[self.codice]:
                Autonoleggio.__repr__(nuova_auto)
            else:
                print("Automobile non può essere aggiunta")


    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""

        return sorted(self.automobili, key=lambda a: a.marca )

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        self._id_automobile = id_automobile
        self._cognome_cliente = cognome_cliente



    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""

