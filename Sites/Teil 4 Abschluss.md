# Teil 4 Abschluss
Der letzte Teil der Arbeit. Hier wird die ganze Auswertung des Projektes beschrieben. Eine Selbstreflexion und die ganzen Anhänge und Quellen sind hier dokumentiert.

- [Teil 4 Abschluss](#teil-4-abschluss)
- [Auswerten](#auswerten)
  - [Zusammenfassung](#zusammenfassung)
  - [Analyse der Effizienssteigerung](#analyse-der-effizienssteigerung)
  - [Reflexion](#reflexion)
    - [Persönlich Reflexion](#persönlich-reflexion)
    - [Reflexion der Technischen Umsetzung](#reflexion-der-technischen-umsetzung)
      - [Analysen und Planung](#analysen-und-planung)
      - [Entscheidung](#entscheidung)
      - [Umsetzung des Projektes](#umsetzung-des-projektes)
      - [Datenmigration](#datenmigration)
      - [Optimierung](#optimierung)
    - [Fazit](#fazit)
      - [Kosteneffizienz](#kosteneffizienz)
      - [Skalierbarkeit und Flexibilität](#skalierbarkeit-und-flexibilität)
      - [Sicherheit und Zugänglichkeit](#sicherheit-und-zugänglichkeit)
    - [Lernerfahrungen](#lernerfahrungen)
    - [Mögliche Weiterentwicklung](#mögliche-weiterentwicklung)
      - [Erweiterte Datenanalyse](#erweiterte-datenanalyse)
      - [Verbesserte Sicherheitsmaßnahmen](#verbesserte-sicherheitsmaßnahmen)
  - [Quellen](#quellen)


# Auswerten
Im Kapitel Auswerten wird der Abschluss des Projektes beschrieben. Es wird Zusammengefasst, Reflektiert und Analysiert. Auch alle Quellen die verwendet wurden werden angehängt.

## Zusammenfassung

In diesem Projekt habe ich eine Projektmanagement Methode angewendet und umgesetzt. Dies wurde nach der IPERKA Methode durchgeführt. Alle Schritte wurden genau dokumentiert. Die Planung und Entscheidung des Projektes sind mit Grafiken evaluiert worden, sodass alles bestmöglich ersichtlich ist. Die Realisierung wurde dann über ein Python Skriot und dem Camunda ausgeführt. Alle Probleme wurden gelöst und die Tests wurden durchgeführt und notiert. Das Projekt wurde mit Notion geführt und so konnte die Struktur und Organisation gut und übersichtlich gehandhabt werden. Alle Quellen wurden aufgeführt und korrekt verlinkt. Die Gespräche wurde notiert und die Gesprächsthemen dokumentiert.

## Analyse der Effizienssteigerung
## Reflexion
### Persönlich Reflexion

Meiner Meinung nach ist das Projekt gut gelaufen. Alle meine Ziele konnte ich erreichen und die Dokumentation ist mir gelungen. Der Aufbau ist für mich klar ersichtlich und strukturiert. Es war spannend, neue Tools kennenzulernen wie Gant und Notion. Zusätzlich konnte ich meine erlernten Skills gut anwenden und mein Skript-Wissen weiterentwickeln. Das Zertifikat war eine Herausforderung für mich und ich war sehr nervös vor der Prüfung. Die Vorbereitung hatte ich jedoch gut geplant und sehr viel gelernt. Die Zeitplanung könnte ich noch etwas genauer Planen, da mir manchmal noch etwas aufgefallen ist, was ich noch zusätzlich dokumentieren sollte. Ich habe genug Zeit für Überraschungen eingeplant, jedoch verursacht es trotzdem einen gewissen Stress.

### Reflexion der Technischen Umsetzung
#### Analysen und Planung

Ich begann mit einer detaillierten Analyse, um die Bedürfnisse der Kunden zu verstehen. Dort wurde veranschaulicht, was für Anforderungen an Datenvolumen, Zugriffszeiten und Sicherheit der Daten steht. Dann wurde noch kurz die Theorie zum Thema Big Data beschrieben. Dies half mir später, die richtige Entscheidung für die Storage-Lösung zu treffen.

Die Planungsphase war wichtig, da sie die Grundlage für eine erfolgreiche Implementierung legte. Es wurde ein Zeitplan entworfen und ein Lernplan. Zusätzlich wurde das Tool Notion verwendet, um eine genaue Struktur zu schaffen.

#### Entscheidung

Bei der Entscheidung wurden viele Aspekte beachtet. Es wurde ein Produktvergleich zwischen zwei gewählten Storage-Lösungen gemacht. Die Vor -und Nachteile wurden auch aufgezeigt. Es gab noch eine Kostenanalyse und zum Schluss eine Entscheidungsmatrix.

Nun stand fest, dass man den Azure Blob Storage evaluieren wird.

#### Umsetzung des Projektes

Als nächster Schritt wurde ein CLI-Skript geschrieben. In diesem werden alle Ressourcen direkt installiert, sodass man von Hand nichts mehr selbst machen musste. Da ich keine erfahrene skripterin bin, war dies eine Herausforderung. Mit Hilfe des Internet und Troubleshooting meines Dozenten, hat dies aber super funktioniert. Die Probleme konnten schnell überwunden werden und das Skript funktionierte.

Damit ich nicht jedes Mal von Hand die Ressourcen löschen musste, habe ich ein kurzes Löschungs-skript geschrieben, welches dies für mich übernommen hatte. Die Nutzung von Azure-Tools wie dem Azure Storage Explorer und der Azure CLI vereinfachte diese Prozesse erheblich.

#### Datenmigration

Mit az Storage Upload konnte ich alle Daten direkt hochladen. Dies habe ich im Skript integriert, sodass alles mit dem Ausführen des Skriptes direkt erledigt ist.

#### Optimierung

Nach der Implementierung führte ich Tests durch, um potenzielle Probleme frühzeitig zu erkennen. Die Tests sind gut verlaufen und wurden dokumentiert.

### Fazit
#### Kosteneffizienz

Die Nutzung von Azure Blob Storage führte zu erheblichen Kosteneinsparungen im Vergleich zu herkömmlichen On-Premise-Speicherlösungen. Dies lag vor allem an der bedarfsgerechten Skalierbarkeit und den flexiblen Preismodellen von Azure.

#### Skalierbarkeit und Flexibilität

Die Speicherlösung ist jetzt hoch skalierbar und flexibel, was ermöglicht, problemlos auf wachsende Datenmengen zu reagieren. Dies ist besonders wichtig für zukünftiges Wachstum und datenintensive Anwendungen.

#### Sicherheit und Zugänglichkeit

Durch die Implementierung der Sicherheitsmassnahmen konnte die Datensicherheit verbessert werden. Gleichzeitig sind die Daten nun von überall und jederzeit zugänglich, was die Effizienz der Arbeitsprozesse erhöht.

### Lernerfahrungen

Ich haben gelernt, dass eine gründliche Planung und Automatisierung entscheidend für den Erfolg solcher Projekte sind. Analysen und korrekte Informationsbeschaffungen sind ebenfalls notwendig, um ein Projekt erfolgreich umzusetzen.

### Mögliche Weiterentwicklung

Für die zukünftige Weiterentwicklung der Azure Blob Storage-Implementierung haben ich noch einige Ideen:

#### Erweiterte Datenanalyse

Durch die Integration von Azure Data Lake und Azure Databricks kann man erweiterte Analysen und Big-Data-Verarbeitung durchführen, um wertvolle Erkenntnisse aus den Daten zu gewinnen.

#### Verbesserte Sicherheitsmaßnahmen

Kontinuierliche Überprüfung und Verbesserung der Sicherheitsmaßnahmen, einschließlich der Implementierung von Azure Security Center, um Bedrohungen frühzeitig zu erkennen und zu verhindern. Durch die Implementierung von RBAC könnte man die Datensicherheit erheblich verbessern.

## Quellen
Kapitel IPERKA, Site Einleitung
Bexio. (2020): Mit der IPERKA-Methode bessere Entscheidungen für Ihre KMU treffen. Aufgerufen am: 30.10.2024. Online unter: https://www.bexio.com/de-CH/blog/view/iperka-methode

Kapitel Analyse des aktuellen Onboarding Prozess, Site Vorbereitung
Chat GPT. (2024): kannst du mir einen text schreiben über die aktuelle situation eines onboardings. Aufgerufen am: 01.11.2024. Online unter: https://chatgpt.com/share/6724ab57-b13c-800e-bfc9-da621fae374f

Kapitel Anforderungen erheben, Site Vorbereitung
Chat GPT. (2024): Was wären die Anforderungen um dies umzusetzten mit Python und camunda. Aufgerufen am: 01.11.2024. Online unter: https://chatgpt.com/share/6724ab57-b13c-800e-bfc9-da621fae374f

Kapitel Was kann automatisieren werden?, Site Vorbereitung
Chat GPT. (2024): Identifizieren was man automatisieren kann. Aufgerufen am: 01.11.2024. Online unter: https://chatgpt.com/share/6724ab57-b13c-800e-bfc9-da621fae374f

Kapitel Produkte vergleichen, Site Vorbereitung
Chat GPT. (2024): kannst du mir kurzgefasst vor- und nachteile von power automate zeigen. Aufgerufen am: 13.11.2024. Online unter:
https://chatgpt.com/share/67345da2-6254-800e-be15-93c889e0d68f

Kapitel Entscheidungsmatrix, Site Vorbereitung
Chat GPT. (2024): machst du mir daraus eine entscheidungsmatrix und camunda muss gewinnen. Aufgerufen am: 13.11.2024. Online unter:
https://chatgpt.com/share/67345da2-6254-800e-be15-93c889e0d68f

> Back [Page](https://github.com/lauradubach/Semesterarbeit2/blob/main/Sites/Teil%203%20Realisierung.md)
>
> Back [Start](https://github.com/lauradubach/Semesterarbeit2?tab=readme-ov-file)