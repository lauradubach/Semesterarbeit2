# Teil 2 Vorbereitung

- [Teil 2 Vorbereitung](#teil-2-vorbereitung)
- [Informieren](#informieren)
  - [Analyse des aktuellen Onboarding Prozess](#analyse-des-aktuellen-onboarding-prozess)
    - [Manuelle Erstellung des Benutzerkontos](#manuelle-erstellung-des-benutzerkontos)
    - [Manuelle Zuweisung von Lizenzen und Gruppen:](#manuelle-zuweisung-von-lizenzen-und-gruppen)
    - [Potenzielle Herausforderungen und Risiken:](#potenzielle-herausforderungen-und-risiken)
  - [Anforderungen erheben](#anforderungen-erheben)
    - [Integration von Azure und Camunda](#integration-von-azure-und-camunda)
    - [Definieren der Onboarding-Prozessschritte in Camunda](#definieren-der-onboarding-prozessschritte-in-camunda)
    - [Automatisierung mit Python-Skripten](#automatisierung-mit-python-skripten)
    - [Sicherheits- und Compliance-Anforderungen](#sicherheits--und-compliance-anforderungen)
    - [Beispielhafte Architektur:](#beispielhafte-architektur)
    - [Zusammenfassung der Anforderungen](#zusammenfassung-der-anforderungen)
  - [Was kann automatisieren werden?](#was-kann-automatisieren-werden)
    - [Automatische Benutzererstellung in Azure](#automatische-benutzererstellung-in-azure)
    - [Automatische Lizenzzuweisung](#automatische-lizenzzuweisung)
    - [Automatisierte Gruppenzuweisung](#automatisierte-gruppenzuweisung)
    - [Zusammenfassung der Automatisierungsmöglichkeiten](#zusammenfassung-der-automatisierungsmöglichkeiten)
  - [Ist Zustand](#ist-zustand)
  - [Soll Zustand](#soll-zustand)
  - [Seusag](#seusag)
    - [Systemgrenzen](#systemgrenzen)
      - [Technologische Systemgrenzen](#technologische-systemgrenzen)
      - [Organisatorische Systemgrenzen](#organisatorische-systemgrenzen)
      - [Regulatorische Anforderungen](#regulatorische-anforderungen)
- [Planen](#planen)
  - [Zeitplan](#zeitplan)
    - [Meilensteine](#meilensteine)
      - [Einreichungsformular](#einreichungsformular)
      - [Entscheidungsmatrix](#entscheidungsmatrix)
      - [Realisieren](#realisieren)
      - [Testen](#testen)
      - [Präsentation](#präsentation)
      - [Abgabe](#abgabe)
- [Entscheiden](#entscheiden)
  - [Produkte vergleichen](#produkte-vergleichen)
    - [Vor -und Nachteile](#vor--und-nachteile)
  - [Kostenanalyse](#kostenanalyse)
  - [Entscheidungsmatrix](#entscheidungsmatrix-1)

# Informieren
In diesem Kapitel werde ich alle Informationen zusammentragen, um das Prijekt umsetzten zu können.

## Analyse des aktuellen Onboarding Prozess
Das aktuelle Onboarding-Verfahren für neue Benutzer in der Azure-Umgebung ist stark manuell geprägt, was Zeit und Ressourcen beansprucht und potenzielle Fehlerquellen mit sich bringt. Der Ablauf gestaltet sich wie folgt:

### Manuelle Erstellung des Benutzerkontos
Jeder neue Benutzer wird in Azure Active Directory (AAD) von einem Administrator manuell erstellt. Dabei müssen grundlegende Informationen wie Benutzername, E-Mail und andere personenbezogene Daten von Hand eingegeben werden. Dies erfordert eine akkurate und vollständige Eingabe, um spätere Korrekturen oder Unstimmigkeiten zu vermeiden.

### Manuelle Zuweisung von Lizenzen und Gruppen:
Nachdem der Benutzer angelegt wurde, erfolgt die manuelle Zuweisung der erforderlichen Lizenzen, je nach Rolle oder Abteilung des neuen Mitarbeiters. Auch die Mitgliedschaft in verschiedenen Gruppen wird individuell vergeben, um den Zugriff auf die notwendigen Ressourcen und Anwendungen zu ermöglichen. Da dies manuell erfolgt, besteht das Risiko, dass Benutzer fälschlicherweise unzureichende oder zu umfangreiche Zugriffsrechte erhalten.

### Potenzielle Herausforderungen und Risiken:
Das stark manuelle Verfahren erhöht das Risiko für menschliche Fehler, wie Tippfehler, vergessene Zugriffsrechte oder falsche Gruppenzuweisungen. Dadurch können Sicherheits- und Compliance-Risiken entstehen, insbesondere wenn sensible Daten oder Ressourcen betroffen sind. Zudem erhöht sich durch diesen manuellen Ansatz die Einarbeitungszeit neuer Benutzer und das Onboarding verzögert sich.

Dieses manuelle Vorgehen im Onboarding ist zeitaufwändig und fehleranfällig und erschwert eine schnelle Anpassung an Unternehmensanforderungen. 

> (Chat GPT) [Quelle](https://chatgpt.com/share/6724ab57-b13c-800e-bfc9-da621fae374f)

## Anforderungen erheben
Um das Onboarding in Azure effizienter und automatisiert mit Python und Camunda umzusetzen, müssen verschiedene Anforderungen erfüllt werden. 

### Integration von Azure und Camunda
   - API-Zugriff auf Azure Active Directory: Die Azure AD REST API muss in Python verwendet werden, um Benutzerkonten zu erstellen, Lizenzen zuzuweisen und Gruppenmitgliedschaften zu verwalten.
   - Camunda-Integration: Camunda dient als BPMN-Engine (Business Process Model and Notation), die Workflows steuert und automatisierte Prozesse verwaltet. Python und Camunda können über REST-APIs kommunizieren, um den Workflow zu steuern und Zustandsänderungen zu überwachen.

### Definieren der Onboarding-Prozessschritte in Camunda
   - Prozessmodellierung: Der gesamte Onboarding-Prozess wird in Camunda modelliert.

### Automatisierung mit Python-Skripten
   - Benutzeranlage: Ein Python-Skript kann mithilfe der Azure AD API automatisch einen neuen Benutzer erstellen.
   - Lizenzzuweisung: Python kann die Lizenzzuweisungen über die Azure API automatisieren, basierend auf im Prozess festgelegten Variablen.
   - Gruppenmanagement: Gruppenmitgliedschaften lassen sich ebenfalls automatisiert zuweisen. Das Python-Skript ruft die Gruppeninformationen ab und weist Benutzer basierend auf Jobrolle oder Abteilung der entsprechenden Gruppe zu.

### Sicherheits- und Compliance-Anforderungen
   - Authentifizierung und Berechtigungen: Python-Skripte benötigen ein sicheres Authentifizierungsverfahren, um auf Azure-Ressourcen zuzugreifen.

### Beispielhafte Architektur:

- Camunda steuert den gesamten Workflow und sendet für jeden Prozessschritt REST-Anfragen an die Python-Skripte.
- Python-Skripte führen die API-Aufrufe an Azure AD aus und geben die Ergebnisse an Camunda zurück.

### Zusammenfassung der Anforderungen

- API-Kenntnisse: Azure AD API für Python und Camunda REST API.
- Python-Kompetenzen: Fähigkeit zur Entwicklung von Skripten für Benutzerverwaltung, Lizenz- und Gruppenmanagement.
- Prozessmodellierung: BPMN in Camunda für den Aufbau und die Steuerung des Onboardings.
- Fehlerbehandlung und Sicherheitsmaßnahmen in Python und Camunda, um Compliance sicherzustellen.


Mit dieser Architektur lassen sich manuelle Aufgaben reduzieren, Fehler vermeiden und ein konsistenter und dokumentierter Onboarding-Prozess etablieren.

> (Chat GPT) [Quelle](https://chatgpt.com/share/6724ab57-b13c-800e-bfc9-da621fae374f)

## Was kann automatisieren werden?
Um das Onboarding in Azure mit Python und Camunda effizienter zu gestalten, können mehrere Schritte automatisiert werden. Dabei gibt es verschiedene Bereiche, in denen die Automatisierung zu einer erheblichen Zeitersparnis, Fehlervermeidung und Prozessverbesserung führt.

### Automatische Benutzererstellung in Azure
   - Beschreibung: Das manuelle Anlegen eines Benutzers in Azure AD kann durch ein Python-Skript automatisiert werden, das die Azure AD API verwendet. Dies beinhaltet die Erfassung und Validierung der Benutzerdaten, die dann automatisch an Azure übergeben werden.
   - Vorteil: Vermeidet manuelle Eingabefehler und sorgt für einheitliche Benutzerdaten.

### Automatische Lizenzzuweisung
   - Beschreibung: Abhängig von der Rolle oder Abteilung des neuen Benutzers kann ein Python-Skript Lizenzen automatisiert zuweisen. Dazu könnten Bedingungen in Camunda hinterlegt werden, die auf den Benutzerdaten basieren und die entsprechenden Lizenzen automatisch zuteilen.
   - Vorteil: Zeitersparnis und Reduzierung des administrativen Aufwands, da keine manuelle Lizenzzuweisung erforderlich ist.

### Automatisierte Gruppenzuweisung
   - Beschreibung: Basierend auf den Jobrollen und Abteilungsinformationen können Benutzer automatisch den entsprechenden Azure AD-Gruppen zugewiesen werden, um Zugriff auf die benötigten Ressourcen zu erhalten. Camunda könnte den Gruppenzuweisungsprozess steuern, während Python-Skripte die tatsächlichen API-Aufrufe ausführen.
   - Vorteil: Sicherstellung eines einheitlichen und schnellen Zugriffs auf die richtigen Ressourcen.

### Zusammenfassung der Automatisierungsmöglichkeiten

Durch die Automatisierung dieser Schritte wird der gesamte Onboarding-Prozess beschleunigt und zuverlässiger gestaltet. Hier die wichtigsten Automatisierungsbereiche im Überblick:

1. Benutzererstellung in Azure AD
2. Lizenzzuweisung
3. Gruppenzuweisung

Durch diese Automatisierungen wird der manuelle Aufwand deutlich reduziert, und es entsteht ein strukturierter, effizienter Prozess, der weniger fehleranfällig ist und die Compliance-Anforderungen erfüllt.

> (Chat GPT) [Quelle](https://chatgpt.com/share/6724ab57-b13c-800e-bfc9-da621fae374f)

## Ist Zustand
Der aktuelle Onboarding-Prozess ist manuell und weist folgende Probleme auf:
- Zeitaufwendig: Manuelle Abläufe wie Profilanlegung und Zugangserstellung führen zu Verzögerungen.
- Fehleranfälligkeit: Häufige manuelle Eingabefehler können Sicherheitsrisiken erhöhen.
- Mangelnde Skalierbarkeit: Der Aufwand steigt linear mit der Anzahl der Neueinstellungen.

## Soll Zustand
Die automatisierte Lösung soll den Onboarding-Prozess effizienter gestalten:
- Automatisierung: Durch Python-Skripte und Camunda-Workflows wird der Prozess erheblich beschleunigt.
- Standardisierung: Ein BPMN-Workflow gewährleistet einheitliche Abläufe.
- Fehlerreduktion: Automatisierte Eingaben und Prüfungen senken das Fehlerrisiko.
- Zentrale Steuerung: Camunda ermöglicht die Prozessüberwachung und schnellere Fehlerbehebung.
- Skalierbarkeit: Die Lösung ist flexibel und für steigende Mitarbeiterzahlen geeignet.

![IST-und Soll Zustand](<../Pictures/Ist- und Soll Zustand.png>)

## Seusag

![Seusag](../Pictures/Seusag.png)

### Systemgrenzen
#### Technologische Systemgrenzen
- Programmiersprache: Die Geschäftslogik wird ausschließlich in Python umgesetzt; andere Sprachen oder Frameworks sind ausgeschlossen.
- Automatisierungsplattform: Nur Camunda wird für die Prozessautomatisierung und BPMN-Modellierung genutzt, alternative Tools sind nicht vorgesehen.
- Kommunikationsschnittstellen: Die Integration zwischen Python und Camunda erfolgt über definierte APIs, ohne zusätzliche externe Schnittstellentechnologien.
- Datenverarbeitung: Alle Daten werden innerhalb des Camunda-Workflows und des Python-Skripts verarbeitet. Externe Datenbanken oder Speicherlösungen sind nicht eingeplant.
- Testumgebung: Die Lösung ist ein funktionierender Prototyp und daher technologisch auf eine begrenzte Skalierbarkeit ausgelegt.
- Produktive Umgebung: Das System ist nicht für eine vollwertige Produktion vorgesehen, sondern als Testumgebung zur Prüfung der Machbarkeit und zur Ermittlung potenzieller Effizienzsteigerungen. Dies auch, da Firmendaten nicht Preisgegeben werden können.

#### Organisatorische Systemgrenzen
- Anwendungsbereich: Der Prototyp deckt nur den Onboarding-Prozess neuer Mitarbeiter ab andere HR-Prozesse sind ausgeschlossen.
- Projektumfang:  Die Semesterarbeit beschränkt den Projektumfang auf die verfügbaren Ressourcen und schließt eine vollständige Integration in die Unternehmens-IT aus.
- Vergleich: Die Effizienz und die Fehlerreduktion des Prototyps werden nur im Vergleich zu den aktuell manuellen Prozessen des Unternehmens evaluiert.
- Produktivitätsanalyse: Es wird keine langfristige Produktivitätsanalyse durchgeführt, die über den Testzeitraum des Projekts hinausgeht.
- Compliance-Prüfung: Die Lösung berücksichtigt nur allgemeine Datenschutzanforderungen, ohne vollständige Compliance-Prüfungen. Es werden keine besonderen Maßnahmen zur Einhaltung branchenspezifischer Standards implementiert, da dies den Projektumfang überschreiten würde.
- Projektmanagement: Die Methode wird beschrieben und umgesetzt
- Unterstützung: Zur Unterstützung des Projektes werden die Fachdozenten und die Modulunterlagen verwendet

#### Regulatorische Anforderungen
- Abschluss: Das Enddatum dieses Projektes ist verbindlich. Nach dem Abschluss des Projektes wird keine Nachbearbeitung geplant
- Meetings: Es weden Zwischengespräche mit dem Fachdozenten gehalten und diese werden dokumentiert. Meetings werden mit dem Fachdozenten geplant und angepasst
- Hilfsmittel: Alle Hilfsmittel für die Umsetzung des Projektes sind vorhanden

# Planen

## Zeitplan
### Meilensteine
#### Einreichungsformular
#### Entscheidungsmatrix
#### Realisieren
#### Testen
#### Präsentation
#### Abgabe

# Entscheiden

## Produkte vergleichen
### Vor -und Nachteile
## Kostenanalyse
## Entscheidungsmatrix

> Back [Page](https://github.com/lauradubach/Semesterarbeit2/blob/main/Sites/Teil%201%20Einleitung.md)
>
> Next [Page](https://github.com/lauradubach/Semesterarbeit2/blob/main/Sites/Teil%203%20Realisierung.md)