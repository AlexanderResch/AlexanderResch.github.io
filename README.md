# AlexanderResch.github.io
<p>Im Zuge meiner Bachelorarbeit wurden 2 Visualisierungen mittels A-Frame zur Abbildung des ökologischen Fußabdrucks der Länder entwickelt. Die verwendeten Daten sollten dabei Open Data sein.</p>

<h1>Files</h1>
<h2>assets</h2>
<p>In den assets befinden sich die verwendeten Bilder und Ressourcen, die zur Darstellung der Visualisierungen benötigt werden. Ebenfalls ist eine Geo-JSON Datei enthalten, welche für die Visualisierung der Ländergrenzen verwendet wird.</p>

<h2>createVS.py</h2>
<p>Python-Programm um die 2. Visualisierung zu erzeugen. Es wurde ein Python-Skript geschrieben, dass die HTML-Datei der 2. Visualisierung erzeugt, um den Aufwand der erzeugung der Balken der Darstellung zu verringern.</p>

<h2>Visualisierung1.html</h2>
<p>Die \n \nFußabdrücke der einbezogenen Länder werden in dieser Visualisierung durch Balken auf einem Globus dargestellt. Bei der Umsetzung wurde der von <a href="https://github.com/vasturiano/aframe-globe-component/tree/master">Vasco Asturiano</a> veröffentlichte Globe-Component verwendet. Die veröffentlichten Daten unterliegen der <a href="https://de.wikipedia.org/wiki/MIT-Lizenz">MIT-License</a> und aus diesem Grund muss der Urheber erwähnt werden. Copyright (c) 2019 Vasco Asturiano <p>
<p>Bei der Umsetzung wurden ebenfalls die Move-Controls verwendet, welche Inhalt des A-Frame-Extras-Komponenten sind. Diese sind ebenfalls mit der <a href="https://de.wikipedia.org/wiki/MIT-Lizenz">MIT-License</a> lizenziert. Aus diesem Grund muss der Urheber erwähnt werden. Copyright (c) 2016 Don McCurdy</p>
<p>Die Visualisierung kann <a href="https://alexanderresch.github.io/Visualisierung1.html">hier</a> als Website aufgerufen werden.</p>


<h2>Visualisierung2.html</h2>
<p>In dieser Visualisierung wird der ökologische Fußabdruck der berücksichtigten Länder im Layout einer Landkarte auf dem Boden mit Balken in der höhe des Fußabdrucks abgebildet. Dem Benutzer ist es möglich durch den Blick auf die Balken, in die genaue höhe des Fußabdrucks einzusehen. Diese Datei wurde durch ein Python-Programm erzeugt, welches sich in der Datei "createVS.py" befindet.</p>
<p>Bei der Umsetzung wurden die Move-Controls verwendet, welche Inhalt des A-Frame-Extras-Komponenten sind. Diese sind mit der <a href="https://de.wikipedia.org/wiki/MIT-Lizenz">MIT-License</a> lizenziert. Aus diesem Grund muss der Urheber erwähnt werden. Copyright (c) 2016 Don McCurdy</p>
<p>Die Visualisierung kann <a href="https://alexanderresch.github.io/Visualisierung2.html">hier</a> als Website aufgerufen werden.</p>


<h2>Fussabdruck.csv</h2>
<p>Dies ist der Datensatz, der in den Visualisierungen verwendet wird um die Balken zu erzeugen. Bei der Beschaffung der Daten wurde darauf geachtet, dass es sich um Open Data handelt. Insgesamt wurden im Datensatz 182 Länder berücksichtigt.</p>

<h3>Spalten und Lizenzen</h3>
<h4>Land:</h4>
<p>Die Länderbezeichnungen wurden gemeinsam mit dem ökologischen Fußabdruck vom <a href="https://data.footprintnetwork.org/#/">Global Footprint Network</a> zur Verfügung gestellt und übernommen, und unterliegen der <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a> Lizenz.</p>

<h4>Breitengrade:</h4>
<p>Die Breitengrade der relevanten Länder wurden aus dem <a href="https://github.com/google/dspl/blob/master/samples/google/canonical/countries.csv">Git-Repository von Google</a> übernommen und unterliegen der <a href="https://choosealicense.com/licenses/bsd-3-clause/">BSD 3-Clause "New" or "Revised" Lizenz</a>.</p>
<p>Copyright 2018, Google Inc. All rights reserved.</p>

<h4>Laengengrade:</h4>
<p>Die Längengrade der relevanten Länder wurden aus dem <a href="https://github.com/google/dspl/blob/master/samples/google/canonical/countries.csv">Git-Repository von Google</a> übernommen und unterliegen der <a href="https://choosealicense.com/licenses/bsd-3-clause/">BSD 3-Clause "New" or "Revised" Lizenz</a>.</p>
<p> Copyright 2018, Google Inc. All rights reserved.</p>

<h4>Oekologischer_Fussabdruck:</h4>
<p>Die ökologischen Fußabdrücke wurden gemeinsam mit den Länderbezeichnungen vom <a href="https://data.footprintnetwork.org/#/">Global Footprint Network</a> zur Verfügung gestellt und übernommen, und unterliegen der <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a> Lizenz.</p>


<h2>Lizenztexte:</h2>
<h3>MIT-License</h3>
<p>Permission is hereby granted, free of charge, to any person obtaining a copy</p>
<p>of this software and associated documentation files (the "Software"), to deal</p>
<p>in the Software without restriction, including without limitation the rights</p>
<p>to use, copy, modify, merge, publish, distribute, sublicense, and/or sell</p>
<p>copies of the Software, and to permit persons to whom the Software is</p>
<p>furnished to do so, subject to the following conditions:</p>
<p>\n</p>
<p>The above copyright notice and this permission notice shall be included in all</p>
<p>copies or substantial portions of the Software.</p>
<p>\n</p>
<p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR</p>
<p>IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,</p>
<p>FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE</p>
<p>AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER</p>
<p>LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,</p>
<p>OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE</p>
<p>SOFTWARE.</p>
<h3>BSD 3-Clause "New" or "Revised" License</h3>
<p>Redistribution and use in source and binary forms, with or without</p>
<p>modification, are permitted provided that the following conditions are</p>
<p>met:</p>
<p></br></p>
<p>   1. Redistributions of source code must retain the above copyright</p>
<p>      notice, this list of conditions and the following disclaimer.</p>
<p>\n</p>
<p>   2. Redistributions in binary form must reproduce the above</p>
<p>      copyright notice, this list of conditions and the following</p>
<p>      disclaimer in the documentation and/or other materials provided</p>
<p>      with the distribution.</p>
<p>\n</p>
<p>   3. Neither the name of Google Inc. nor the names of its</p>
<p>      contributors may be used to endorse or promote products derived</p>
<p>      from this software without specific prior written permission.</p>
<p>\n</p>
<p>THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS</p>
<p>"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT</p>
<p>LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR</p>
<p>A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT</p>
<p>OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,</p>
<p>SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT</p>
<p>LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,</p>
<p>DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY</p>
<p>THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT</p>
<p>(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE</p>
<p>OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>


