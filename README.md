# Einsendeaufgabe TST-E1: Testen (MealPlan-Projekt)

Sprache: Python 3.12, Test-Framework: pytest, Mocking: `unittest.mock`.
Domäne: MealPlan (Wochenmenüplaner): Einkaufsliste & Warenkorb.

Tests ausführen:
```
pip install pytest
python3 -m pytest teil1_unittests/tests/ teil2_shoppingcart/tests/ teil3_mocking/tests/ -v
```
Vollständiger Testlauf zum Beleg: `mock_durchlauf.txt`.

A1. Unit tests 
(teil1_unittests/src/shopping_list.py und teil1_unittests/tests/test_shopping_list.py)

einfach nur getestet, wie die Klasse von ShoppingList Zutaten (wie Name, Preis und Menge) sammelt und dabei die Gesamtkosten und Durchschnittspreise berechnet.
Es wird ja dabei geprüft, ob bei ungültiger Menge (negativ oder Menge 0) bzw. negativem Preis (was eine Exception werfen soll) mit ValueError geantwortet wird. Im Normalfall soll es ja nur sein, dass ein Artikel oder mehrere doppelte Artikel zusammengeführt werden, und nicht überschrieben.
Codeblock:
            if item.name == name:
                item.quantity += quantity
                return
Also z.B.: Apfel, 1, gespeichert. Dann Apfel, 2: item.name == name, Apfel == Apfel, führt zu 1 + 2 = 3.
Beim Pflicht-Exception-Test average_item_price() auf leerer Liste (wie oben benannt) soll eine Exception geworfen werden (EmptyShoppingListError), statt ZeroDivisionError. Wir haben die Exception ja selbst definiert, sodass wir beim Testen fachlich erkennen können, wo der Fehler war (statt nur eines technischen Zufallstreffers durch die Division durch 0).


A2. TDD Shopping Cart

Die Codebasis von und den ersten Testdurchführung wurde von der KI generiert, sodass ich mir eine mögliche Lösungsansatz mit Beispielcode und ersten Tests als überblickt zu generieren. Dann lasse ich mich dann von KI das ja erklären, bis ich sie selbst verstehen und nachvollziehen konnte. Danach habe ich die Test nachgemacht, um neue Test methode zu implementieren und habe mir das von KI korrigieren lassen.

Es zeigt mir die TDD Shopping Cart, wie ein Red-Green-Refactor-Prozess aussieht und umgesetzt wird, mithilfe eines bestimmten Testing-Vorgangs: Man sieht zuerst, dass der Test fehlschlägt (ROT), weil die Funktion noch nicht implementiert wurde. Das stellt sicher, dass der Test überhaupt etwas Echtes prüft. Erst danach wird der Code so weit gebaut, dass der Test besteht(GREEN). Der Sinn dahinter ist, den Code zunächst grob und minimal zu entwerfen und ihn danach zu verfeinern, um zukünftige Fehler zu vermeiden (Refactoring). Es ist ja abgesichert dadurch, dass der Test währenddessen weiter bestehen muss.

Anhand unseres Beispiels ist die Prüfung der Funktion add_item wie folgt: zuerst wird ein Test erstellt, der prüft, ob ein Artikel korrekt zum Warenkorb hinzugefügt wurde. Dafür reicht zunächst eine rohe Liste von Tupeln als Datenhaltung. Sobald der Test erfolgreich ist (GREEN), wird refactored, indem die Datenhaltung durch eine CartItem-Dataclass ersetzt wird. Alle Items im Warenkorb sind dann klarer strukturiert und leichter erweiterbar.


A3. Mocking

Die Klasse ShoppingReminder übernimmt ja die Aufgabe, den wöchentlichen Einkaufstag zu verwalten. Sie greift dabei auf das aktuelle Datum des Systems zu. Für unseren Test wurde die Methode date.today() gemockt, sodass sie nicht mehr das tatsächliche Datum, sondern ein fest eingestelltes Datum zurückliefert. Ohne Mocking würden die Testergebnisse von dem Tag abhängen, an dem der Test ausgeführt wird. Zum Beispiel könnte der Fall "heute ist Sonntag" nur an einem einzigen Tag erfolgreich überprüft werden, nämlich an einem Sonntag selbst. Der Test würde dadurch keinen Sinn ergeben und unzuverlässige Ergebnisse liefern.

Mit patch.object(shopping_reminder, "date") wird die im Modul verwendete Klasse date vorübergehend durch ein Mock-Objekt ersetzt. Alle Aufrufe von date.today() innerhalb des with-Blocks verwenden dadurch nicht mehr die echte Datumsfunktion, sondern das Mock-Objekt. Die Anweisung mock_date.today.return_value = date(2026, 6, 21) legt fest, welcher Wert zurückgegeben werden soll, wenn today() aufgerufen wird (hier also der 21.06.2026). Das aktuelle Datum wird dabei nicht abgefragt, sondern stattdessen das festgelegte Datum zurückgegeben. Für den getesteten Code wird die Ausführung so simuliert, als wäre es der 21.06.2026. Dadurch lässt sich gezielt jeder beliebige Wochentag testen, ohne vom tatsächlichen Kalendertag abhängig zu sein.

Der Grund, warum date.today() gemockt werden muss, hängt damit zusammen, dass es von einem ständig sich ändernden Faktor abhängt: der Systemzeit. Da sich die Zeit immer weiter verändert, liefert date.today() je nach Ausführungszeitpunkt ein anderes Ergebnis. Die Methode ist dadurch nicht-deterministisch. Um sie trotzdem zuverlässig testen zu können, muss der Rückgabewert von date.today() im Test gezielt festgelegt werden, statt ihn der echten Systemuhr zu überlassen.

Eingesetztes Werkzeug: Claude (Anthropic), eingesetzt für Code und Methode Testing

Prompt (sinngemäß): A2: Kannst du mir die Aufgabe hier anschauen und code plus test snippet generieren.
Danach: Hier habe ich nach dein Beispiel meine eigene tests ausprobiert zu schreiben, kannst du das korrigieren und verbessern?
A3: Kannst du anhand mein Code (Was bei mir komplett von KI umgeschrieben wurde um dies leserlich und einfacher zu machen) anmerkungen geben und verbessern?

KI-Ausgabe:

Strukturierter und sauberer Code mit Erweiterung der Testing-Methoden.

A4: Mutation-testing habe ich nicht gemacht

A5: Eigene Kritik (übersehene Edge-Cases der KI-Ausgabe):

1. Der ursprüngliche Code von Cart.add_item hat jedes neu hinzugefügte Produkt als eigenen Eintrag im Warenkorb behandelt. Sobald derselbe Artikel mehrmals hinzugefügt wurde, entstanden mehrere separate Einträge statt eines einzigen Eintrags mit entsprechend angepasster, höherer Menge. Das führt zu Datenredundanz und Unübersichtlichkeit. Das Problem wurde durch einen zusätzlichen Test aufgedeckt, der gezielt prüfte, ob die Menge beim wiederholten Hinzufügen wirklich zusammengeführt wird. Dieser Test schlug zunächst fehl(RED), weil der ursprüngliche Code die Mengen stattdessen überschrieben. Zur Behebung wurde Cart.add_item so angepasst, dass zuerst geprüft wird, ob der Artikel schon existiert: Falls ja, wird nur die Menge addiert statt eines neuen Eintrags; falls nein, wird der Artikel neu eingetragen.
2. Wenn man "Apfel" und "apfel" hinzufügt, entstehen zwei unterschiedliche Einträge für denselben Artikel, da der Vergleich der Namen Groß- und Kleinschreibung unterscheidet. Es wird also als zwei verschiedene Artikel eingetragen und gespeichert. Das ist erkannt und ließe sich relativ leicht durch eine automatische Normalisierung lösen, z. B. indem alle Namen einheitlich klein- oder großgeschrieben werden, bevor sie verglichen werden. Das war jedoch nicht Teil der Aufgabenstellung, daher wurde es bewusst nicht umgesetzt.
3. ShoppingReminder nutzt date.today(), was die lokale Systemzeit des Geräts verwendet, auf dem der Code läuft (ohne Berücksichtigung von Zeitzonen). Das kann bei Nutzern, die zwischen Zeitzonen reisen, zu Verwirrung führen: Ist ein Reminder z. B. für 23:00 Uhr UK-Zeit gesetzt und der Nutzer landet kurz danach in Deutschland, ist es dort durch den Zeitzonensprung bereits Mitternacht. Der Reminder kommt je nachdem, welche Zeitzone das System tatsächlich verwendet, zu früh oder zu spät an. Eine konkrete Lösung wäre, die Zeitzone des Nutzers explizit zu berücksichtigen, statt sich auf die Systemzeit des Geräts zu verlassen.

Fazit: Meiner Meinung nach habe ich bemerkt, dass KI Probleme sehr schnell lösen kann, doch letztlich kommt es immer darauf an, dies selbst zu verstehen und anzuwenden. Durch weitere Erklärungen konnte ich mit Hilfe von Claude die einzelnen Konzepte besser nachvollziehen. Insgesamt hat mir die Auseinandersetzung mit den Testing-Prozessen ziemlich viel beigebracht, wie wichtig Code-Testing eigentlich ist.