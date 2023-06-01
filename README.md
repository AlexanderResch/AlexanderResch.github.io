# AlexanderResch.github.io
Im Zuge meiner Bachelorarbeit wurden 2 Visualisierungen mittels A-Frame zur Abbildung des ökologischen Fußabdrucks der Länder entwickelt. Die verwendeten Daten sollten dabei Open Data sein.

<h1>Files</h1>
<h2>assets</h2>
In den assets befinden sich die verwendeten Bilder und Ressourcen, die zur Darstellung der Visualisierungen benötigt werden. Ebenfalls ist eine Geo-JSON Datei enthalten, welche für die Visualisierung der Ländergrenzen verwendet wird.

<h2>createVS.py</h2>
Python-Programm um die 2. Visualisierung zu erzeugen. Es wurde ein Python-Skript geschrieben, dass die HTML-Datei der 2. Visualisierung erzeugt, um den Aufwand der erzeugung der Balken der Darstellung zu verringern.

<h2>Visualisierung1.html</h2>
Die Fußabdrücke der einbezogenen Länder werden in dieser Visualisierung durch Balken auf einem Globus dargestellt. Bei der Umsetzung wurde der von <a href="https://github.com/vasturiano/aframe-globe-component/tree/master">Vasco Asturiano</a> veröffentlichte Globe-Component verwendet. Die veröffentlichten Daten unterliegen der <a href="https://de.wikipedia.org/wiki/MIT-Lizenz">MIT License</a> und aus diesem Grund muss der Urheber erwähnt werden. 
Copyright (c) 2019 Vasco Asturiano

Die Visualisierung kann <a href="https://alexanderresch.github.io/Visualisierung1.html">hier</a> als Website aufgerufen werden.

<h2>Visualisierung2.html</h2>
In dieser Visualisierung wird der ökologische Fußabdruck der berücksichtigten Länder im Layout einer Landkarte auf dem Boden mit Balken in der höhe des Fußabdrucks abgebildet. Dem Benutzer ist es möglich durch den Blick auf die Balken, in die genaue höhe des Fußabdrucks einzusehen. Diese Datei wurde durch ein Python-Programm erzeugt, welches sich in der Datei "createVS.py" befindet.

Die Visualisierung kann <a href="https://alexanderresch.github.io/Visualisierung2.html">hier</a> als Website aufgerufen werden.


<h2>Fussabdruck_konvertiert.csv</h2>
Dies ist der Datensatz, der in den Visualisierungen verwendet wird um die Balken zu erzeugen. Bei der Beschaffung der Daten wurde darauf geachtet, dass es sich um Open Data handelt. Insgesamt wurden im Datensatz 182 Länder berücksichtigt.

<h3>Spalten und Lizenzen</h3>
<h4>Land:</h4>
Die Länderbezeichnungen wurden gemeinsam mit dem ökologischen Fußabdruck vom <a href="https://data.footprintnetwork.org/#/">Global Footprint Network</a> zur Verfügung gestellt und übernommen, und unterliegen der <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a> Lizenz.

<h4>Breitengrade:</h4>
Die Breitengrade der relevanten Länder wurden aus dem <a href="https://github.com/google/dspl/blob/master/samples/google/canonical/countries.csv">Git-Repository von Google</a> übernommen und unterliegen der <a href="https://choosealicense.com/licenses/bsd-3-clause/">BSD 3-Clause "New" or "Revised" Lizenz</a>.
Copyright 2018, Google Inc.
All rights reserved.

<h4>Laengengrade:</h4>
Die Längengrade der relevanten Länder wurden aus dem <a href="https://github.com/google/dspl/blob/master/samples/google/canonical/countries.csv">Git-Repository von Google</a> übernommen und unterliegen der <a href="https://choosealicense.com/licenses/bsd-3-clause/">BSD 3-Clause "New" or "Revised" Lizenz</a>.
Copyright 2018, Google Inc.
All rights reserved.

<h4>Oekologischer_Fussabdruck:</h4>
Die ökologischen Fußabdrücke wurden gemeinsam mit den Länderbezeichnungen vom <a href="https://data.footprintnetwork.org/#/">Global Footprint Network</a> zur Verfügung gestellt und übernommen, und unterliegen der <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a> Lizenz.

