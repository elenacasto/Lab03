import csv
from datetime import datetime
from logging import exception


# METODI GETTER E SETTER, DA VEDERE BENE + COLLEZIONI DI OGGETTI

class Automobili:
    def __init__(self, codice, marca, modello, anno, num_posti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.num_posti = num_posti

    def __str__(self):
        return f"{self.codice} - {self.marca} {self.modello} ({self.anno}), {self.num_posti} posti"


class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.automobili = []
        self.noleggi = {}

    def set_responsabile(self, nuovo_nome):
        self.responsabile = nuovo_nome

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=',')
                for row in reader:
                    if len(row) < 5 or not row[4].isdigit():
                        continue
                    codice, marca, modello, anno, num_posti = row
                    auto = Automobili(codice, marca, modello, int(anno), int(num_posti))
                    self.automobili.append(auto)
        except FileNotFoundError:
            print("File non trovato")


    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        codici_numerici = [int(a.codice[1:]) for a in self.automobili if a.codice.startswith("A") and a.codice[1:].isdigit()]
        if codici_numerici:
            nuovo_numero = max(codici_numerici) + 1
        else:
            nuovo_numero = 1

        nuovo_codice = f"A{nuovo_numero}"
        auto = Automobili(nuovo_codice, marca, modello, anno, num_posti)
        self.automobili.append(auto)
        return auto

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        return sorted(self.automobili, key=lambda a: a.marca ) #corretto

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        if id_automobile not in [a.codice for a in self.automobili]:
            raise Exception("Automobile non trovata")

        if id_automobile in self.noleggi:
            raise Exception("Automobile già noleggiata")

        self.noleggi[id_automobile] = {
            "cliente": cognome_cliente,
            "data": data
        }

        return f"{id_automobile} noleggiata da {cognome_cliente} il {data}"


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        if id_noleggio not in self.noleggi :
            raise Exception("Noleggio non trovato")
        del self.noleggi[id_noleggio]


def main(): # da leggere bene per poter scruvere il programma
    autonoleggio = Autonoleggio("Polito Rent", "Alessandro Visconti")

    while True:
        print("\n--- MENU AUTONOLEGGIO ---")
        print("1. Modifica nome del responsabile dell’autonoleggio")
        print("2. Carica automobili da file")
        print("3. Aggiungi nuova automobile (da tastiera)")
        print("4. Visualizza automobili ordinate per marca")
        print("5. Noleggia automobile")
        print("6. Termina noleggio automobile")
        print("7. Esci")

        scelta =  input("Scegli un'opzione >> ")

        if scelta == "1":
            nuovo_responsabile = input("Inserisci il nuovo responsabile: ")
            autonoleggio.set_responsabile(nuovo_responsabile)
            print("Responsabile aggiornato")

        elif scelta == "2":
            while True:
                try:
                    file_path = input("Inserisci il path del file da caricare: ").strip()
                    autonoleggio.carica_file_automobili(file_path)
                    break
                except Exception as e:
                    print(e)

        elif scelta == "3":
            marca = input("Marca: ")
            modello = input("Modello: ")
            try:
                anno = int(input("Anno di Immatricolazione: ").strip())
                posti = int(input("Numero di posti: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue
            automobile = autonoleggio.aggiungi_automobile(marca, modello, anno, posti)
            print(f"Automobile aggiunta: {automobile}")

        elif scelta == "4":
            automobili_ordinate = autonoleggio.automobili_ordinate_per_marca()
            for a in automobili_ordinate:
                print(f'- {a}')

        elif scelta == "5":
            id_auto = input("ID automobile: ")
            cognome_cliente = input("Cognome cliente: ")
            data = datetime.now().date()
            try:
                noleggio = autonoleggio.nuovo_noleggio(data, id_auto, cognome_cliente)
                print(f"Noleggio andato a buon fine: {noleggio}")
            except Exception as e:
                print(e)

        elif scelta == "6":
            id_noleggio = input("ID noleggio da terminare: ")
            try:
                autonoleggio.termina_noleggio(id_noleggio)
                print(f"Noleggio {id_noleggio} terminato con successo.")
            except Exception as e:
                print(e)

        elif scelta == "7":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida!")

if __name__ == "__main__":
    main()
