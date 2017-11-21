# Portfolio
Kevin van Veen | KB74 Applied Data Science |  30 augustus 2017

# Inhoud
1. [Inleiding](#inleiding)
2. [Scrum](#scrum)
3. [Producten](#producten) <br>
3.1 [Issues](#issues) <br>
3.2 [Overige](#overige) <br>
4. [Notulen & Presentaties](#notulen_en_Presentaties)
5. [Cursussen & Workshops](#cursussen_en_workshops) <br>
5.1 [Datacamp](#datacamp) <br>
5.2 [Coursera](#coursera) <br>
5.3 [Calling Bullshit](#calling_bullshit) <br>
5.4 [Notebooks](#notebooks) <br>
5.5 [Spark](#spark) <br>

# 1. Inleiding<a name="inleiding"></a> 
URBINN is het LearningLab rondom autonoom rijdend vervoer binnen stedelijke gebieden (last mile). Binnen URBINN wordt een autonoom rijdend voertuig ontwikkeld dat als basis zal dienen om steeds verder te ontwikkelen en waar allerlei onderzoek op en mee gedaan zal gaan worden. Ik ben werkzaam geweest binnen de minor applied data science waarbij de focus lag bij het semantisch mappen en object detection. Voor meer informatie over deze minor of overige minoren binnen het Urbinn project zie de website van [Urbinn](http://urbinn.nl/studenten/#1503314382730-7ee1aad3-63d9) 

# 2. Scrum<a name="scrum"></a> 
Binnen de deze minor is gekozen om te werken met de ontwikkelmethode Scrum. Als eerst is er een introductie workshop van Scrum gegeven om algemene kennis van Scrum te krijgen. 

# 3. Producten<a name="producten"></a> 

## 3.1 Issues<a name="issues"></a> 
Aangezien we met de Scrum methode werken waarbij elke sprint 2 weken duurt, plannen we elke maandag een moment in om de taken, oftewel issues, voor de aankomende sprint te bepalen. Dit doen we aan de hand van de online plannings board [Waffle](https://waffle.io/urbinn/urbinn)
De issues die in Waffle opgenomen worden zijn direct verbonden aan Git. Hierdoor worden de issues ook zichtbaar bijgehouden in [Git](https://github.com/urbinn/urbinn) 

In het onderstaande overzicht is een korte beschrijving gemaakt per issue waaraan ik heb gewerkt:

Issue | Omschrijving | Data
------------ | -------------| -------------
[#1 Literatuur scan: gebruikte technologieën](https://github.com/urbinn/urbinn/issues/1) |Dit was de allereerste issue die wij hebben ingevoerd in het Waffle Board. Aangezien we nog geen goed overzicht hadden van de scope en bestaande technologieën voor het creëren van een semantische map heb ik als eerste gezocht en bestudeerd naar documenten/rapporten die gericht waren op semantische mappen aan de hand van de camera beelden | [Existing Technologies.pdf](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Issues/Issue%201%20-%20Existing%20Technologies/Issue%201%20-%20Existing%20Technologies.pdf)
[#19 Serie foto's als test case](https://github.com/urbinn/urbinn/issues/19) | Ik heb een camera meegenomen met een viertal Rubiks Kubussen om een aantal foto’s te nemen die we als eerste testcase kunnen gebruiken SLAM-algoritme uitproberen. | 
[#21 Zoeken naar tutorials/videos voor LSD SLAM](https://github.com/urbinn/urbinn/issues/21) | Er is een issue aangemaakt voor het zoeken naar bestaande tutorial van LSD-SLAM op het gebied van installatie, toepassingen en evaluatie. Echter bleek dat er geen (nuttige) tutorials beschikbaar waren | 
[#28 ORB SLAM 2 paper bestuderen](https://github.com/urbinn/urbinn/issues/28) | Dit betreft een issue die door ieder groepslid is uitgevoerd. Het paper van ORB-SLAM2 is gelezen en bestudeerd voor de eerste close-reading sessie waarbij het paper nader besproken werd. | [mur 2017 ORB-SLAM2.pdf](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Overige%20Producten/Close%20Reading/mur%202017%20ORB-SLAM2.pdf)
[#32 Planning](https://github.com/urbinn/urbinn/issues/32) | Ik heb een planning opgesteld waarbij ik een viertal milestones heb opgenomen zodat het doel van het project goed inzicht blijft. Middels deze milestones en de planning is er een duidelijk overzicht gecreëerd voor het gehele team. Hiermee heeft iedereen binnen het team een goed idee wat er voor de desbetreffende sprint uitgevoerd moet worden om de milestone te kunnen behalen. Tevens zorgt dit ervoor dat de realisatie van het doel van het project behaald kan worden middels een strakke planning. | [Urbinn planning](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Overige%20Producten/Planning/Urbinn%20-%20Planning%20v1.0.xlsx) ps. dit bestand is in .xlsx formaat aangezien de planning in .pdf niet overzichtelijk is.
[#33 Planning notulist](https://github.com/urbinn/urbinn/issues/33) | Voor dit issue heb ik een planning opgesteld voor wie de notulisten rol uitvoert gedurende een bepaalde sprint. Naast het notuleren van bijvoorbeeld vergaderingen en retrospectives is de notulist ook verantwoordelijk om per week (sprint heeft 2 weken) het [blog van Urbinn](https://kb74.github.io/) te updaten en de prestaties te verzorgen. | [Urbinn planning](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Overige%20Producten/Planning/Urbinn%20-%20Planning%20v1.0.xlsx) ps. dit bestand is in .xlsx formaat aangezien de planning in .pdf niet overzichtelijk is.
[#39 Dataset Slinger dataset/evaluatie](https://github.com/urbinn/urbinn/issues/39) | In verband met het ontbreken van een stereo camera zijn er opnames gemaakt met behulp van twee monologen webcams die synchroon mogelijk geïnstalleerd zijn. Nadat de opnames gemaakt waren zijn de opnames geconverteerd naar losstaande frames.  | [Evaluating Egomotion and Structure-from-Motion Approaches Using the TUM RGB-D Benchmark](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Issues/Issue%2039%20-%20Dataset%20Slinger%20datasetevaluatie/sturm12iros_ws.pdf)
[#49 Paper Object Detection Selecteren](https://github.com/urbinn/urbinn/issues/49) | Naast het maken van een semantisch map voor het project moeten ook object gedetecteerd kunnen worden zoals voetgangers, verkeersborden, auto’s etc. Middels reseach in bestaande technologieen heb ik gekeken welke frameworks het meest aansluiten bij ons doel. Uit dit onderzoek is een het paper/framework YOLO (You Only Look Once Unified, Real-Time Object Detection ) geselecteerd.  | [Object detection papers](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/tree/master/Data/Issues/Issue%2049%20-%20Real%20Time%20Object%20detection)
[#55 Object detection papers lezen](https://github.com/urbinn/urbinn/issues/55) | Voor de tweede close reading sessie hebben we gekozen om YOLO (You Only Look Once Unified, Real-Time Object Detection ) paper te gebruiken voor de reading. Dit issue betrof het lezen van de paper om een zo goed mogelijk indruk te krijgen van het YOLO-framework. | [You Only Look Once Unified, Real-Time Object Detection.pdf](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Overige%20Producten/Close%20Reading/You%20Only%20Look%20Once%20Unified%2C%20Real-Time%20Object%20Detection.pdf)
[#57 Beschrijven data structuur KeyFrame in ORB2](https://github.com/urbinn/urbinn/issues/57) | Het ORB-SLAM2 Framework is geschreven in de C++ programmeertaal. Deze complexe code bevatte helaas geen commentaar. Hierdoor waren er methodes en attributen die onduidelijk waren in de werking. Om meer duidelijkheid te scheppen van de klassen die gebruikt worden binnen ORB-SLAM2 is per klas code commentaar toegevoegd. Dit issues betrof het omschrijven van de klasse “KeyFrame”. | [KeyFrame](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Issues/Issue%2057%20-%20Beschrijven%20data%20structuur%20KeyFrame%20in%20ORB2/KeyFrame.cc)
[#63 Evaluatie: aanpak pointcloud vs pointcloud](https://github.com/urbinn/urbinn/issues/63) | Voor issue 63 heb ik gekeken naar hoe evaluatie van pointcloud vs pointcloud gerealiseerd kan worden. De basisstappen voor de evaluatie en de bevindingen zijn opgenomen in het evaluatieplan point_cloud.pdf | [Evaluatieplan point cloud](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Issues/Issue%2063%20-%20Pointcloud%20vs%20Pointcloud/Issue%2063%20-%20Evaluatieplan%20point%20cloud.pdf)
[#70 KITTI point cloud resultaten](https://github.com/urbinn/urbinn/issues/70) | Ik heb gewerkt aan het genereren van een pointcloud aan de hand van de datatset Kitti. De bedoeling is dat op de server runs worden gedaan op delen van de KITII dataset en de pointclouds in .csv formaat worden bewaard op de server.| 
[#73 Yolo run uitvoeren op Kitti sequence 00](https://github.com/urbinn/urbinn/issues/73) | Er moest een run uitgevoerd worden binnen YOLO aan de hand van de Kitti dataset sequence 00. Er is een phyton script gemaakt die deze run geautomatiseerd kan uitvoeren. | 
[#74 Yolo run KITTI evalueren tegen ground truth object 2D task](https://github.com/urbinn/urbinn/issues/74) | Ik heb gewerkt aan het evalueren van YOLO aan de hand van de Kitti dataset. De Kitti dataset beschikt over 2D objecten met groundtruth. Dit gedeelte van de Kitti dataset heb ik geëvalueerd aan de hand van een script. De uitkomsten van deze evaluatie bleken goed te zijn.  | [Evaluatie resultaten](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Issues/Issue%2074%20-%20Yolo%20run%20KITTI%20evalueren%20tegen%20ground%20truth%20object%202D%20task/Yolo_evaluatie.md)
[#82 Yolo training data verzamelen](https://github.com/urbinn/urbinn/issues/82) | Ik heb gewerkt aan het verzamelen van verschillende soorten dataset. Het idee hierachter is dat we aan de hand van verschillende soorten datasets onze eigendataset kunnen creeëren. Er zijn een aantal websites die datasets ter beschikking hebben gesteld. Alle bruikbare data is op onze server gezet | [Deeplearning](http://deeplearning.net/datasets/)
[#83 Vaststellen klassen voor trainen Yolo](https://github.com/urbinn/urbinn/issues/83) | Ik heb alle klassen die wij in eerste instantie willen gebruiken bij object detectie in kaart gebracht. | [Klassen voor trainen eigen dataset](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Issues/Issue%2083%20-%20Vaststellen%20klassen%20voor%20trainen%20Yolo/Issue%2083%20-%20Klassen%20voor%20trainen%20eigen%20dataset.pdf)
[#88 Opzoeken labeling tool](https://github.com/urbinn/urbinn/issues/88) | Om het YOLO detectie framework te kunnen trainen met eigendata moest gekeken worden naar mogelijkheden om snel en effectief afbeeldingen te kunnen labelen. Daarnaast moest deze tool in staat zijn om direct een correct output te kunnen genereren zodat deze output direct in YOLO ingevoerd kon worden. Ik heb de labeltool Bbox aangeraden vanwege de gebruikersvriendelijkge interface en voornamelijk vanwege het de correct output dit Bbox genereerd  | [Bbox label tool](https://github.com/puzzledqs/BBox-Label-Tool)
[#86 Ground truth nieuwe trainingsdata labelen](https://github.com/urbinn/urbinn/issues/86) | Aan de hand van de KITTI dataset hebben wij alle afbeeldingen geherlabeld. Er is een uitbreiding van het aantal klassen die op dit moment uit 132 verschillende soorten klassen bestaat. Deze herlabelling is nodig om onze eigen dataset te kunnen creeeren  | [klassen voor training eigen dataset]
[#93 trainen tiny YOLO maandag nacht](https://github.com/urbinn/urbinn/issues/93) | Voor dit issue heb ik meerder werkzaamheden uitgevoerd ik ben begonnen meth het runnen van Yolo op op de Tritanium (server Leiden). Helaas waren de GPU's niet beschikbaar (waarschijnlijk werkzaamheden). Vervolgens bleek een error in YOLO te zitten die veroorzaakt werd door een NVIDEA update. Ik ben verder gaan onderzoeken welke alternatieve mogelijkheden er nog waren. Darkflow was hierin een zeer geschikte kandidaat aanzien Darkflow een implementatie van YOLO is in  Tensorflow. Darkflow verwachte echter ander soort iput formaat voor de afbeeldingen, labels en annotaties waardoor we eerst een aantal scripts moesten maken die voor deze convert zorgde. Echter bleek de CUDA error in Darknet (YOLO) verholpen te zijn. Hierdoor zijn we verder gegaan met het trainen van YOLO in Darknet i.p.v. Darkflow. Na een nacht trainen in YOLO waren de resultaten dat er 70000 weights waren weggeschreven (na ca. 18M images), en gekopieerd naar darknet/kitti/tiny-yolo-kitti_final. De avg. recall (gelabelde objecten dat herkend wordt) ca. 50%. Dit is een redelijk resulataat aanzien YOLO na 1 weken trainen op +/- 60% avg. recall zit.


## 3.2 Overige <a name="overige"></a> 
Overige producten waaraan ik heb gewerkt zijn:<br>

**Locatie foto’s:**<br>
We zijn in het begin van het project naar de locatie Delft gegaan om een indruk te krijgen van de locatie. Ik heb direct foto's gemaakt die wellicht nuttig kunnen zijn tijdens het project. Daarnaast had ik het idee op deze foto's ook te gebruiken in onze eigen dataset 
[foto's](foto’s.zip)<br>

**Close Reading session**<br>
Gedurende het project hebben we een aantal close reading sessies gehouden. Dit is gedaan om eventuele misverstanden binnen het team van de geselecteerde papers weg te nemen.

**Sessie 1 – Woensdag 20 september 2017**<br>
-[mur 2017 ORB-SLAM2.pdf](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Overige%20Producten/Close%20Reading/mur%202017%20ORB-SLAM2.pdf)

**Sessie 2 – Woensdag 27 september 2017**<br>
-[You Only Look Once Unified, Real-Time Object Detection.pdf](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Overige%20Producten/Close%20Reading/You%20Only%20Look%20Once%20Unified%2C%20Real-Time%20Object%20Detection.pdf)<br>
-[mustafah 2012 Stereo vision images processing for real-time object distance and size measurements.pdf](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Overige%20Producten/Close%20Reading/mustafah%202012%20Stereo%20vision%20images%20processing%20for%20real-time%20object%20distance%20and%20size%20measurements.pdf)


# 4. Notulen & Presentaties<a name="notulen_en_Presentaties"></a>
In de [planning](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Overige%20Producten/Planning/Urbinn%20-%20Planning%20v1.0.xlsx) staat aangegeven per sprint wie verantwoordelijk is voor het updaten van het [Urbinn blog](https://kb74.github.io/urbinn/) en het geven van de wekelijkse prestenaties. Ik heb een notule [template](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/tree/master/Data/Notulen%20%26%20Presentaties/Notulen) opgesteld zodat elke notulist deze eenvoudige kan gebruiken bij het notuleren. Daarnaast heb ik een aantal [prestanties](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/tree/master/Data/Notulen%20%26%20Presentaties/Presentaties) gemaakt en gehouden.

# 5. Cursussen & workshops<a name="cursussen_en_workshops"></a> 
Gedurende deze minor heb ik meerdere cursussen en workshops gevolgd. 

## 5.1 Datacamp<a name="datacamp"></a> 
DataCamp biedt trainingen aan voor het leren en toepassen van de programmeertaal Python in combinatie met een aantal van Machine Learning technieken. Deze cursus was een verplicht onderdeel gedurende de minor. Ik heb alle verplichte onderdelen behaald in deze cursus.<br>
![Datacamp verplichte onderdelen](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Images/DataCamp%20Afbeeldingen/DataCamp%20Courses%20Completed.jpg)

## 5.2 Coursera<a name="coursera"></a> 
Coursera biedt een specifieke cursus aan op het gebied van Machine Learning. Deze cursus richt zich voornamelijk op het gebied van lineaire regressie (algebra) en hoe je dit kan toepassen in Machine Learning. Ik heb alle verplicht onderdelen behaald in deze cursus.
![Coursera verplichte onderdelen 1 t/m 3](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Images/Coursera%20Afbeeldingen/Machine%20Learning%20Stanford%20University%20-%20Completed%20-%201-2-3.jpg)
<br>
<br>
![Coursera verplicht onderdeel 6](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/blob/master/Data/Images/Coursera%20Afbeeldingen/Machine%20Learning%20Stanford%20University%20-%20Completed%20-%206.jpg)<br>

## 5.3 Calling Bullshit<a name="calling_bullshit"></a> 
Aan de hand van een drietal workshop genaamd "Calling bullshit in the age of big data" hebben wij de opdracht gekregen om een aantal verschillende soorten informatie kanalen te doorzoeken waarbij de informatie onjuist bleek te zijn. (link nog toevoegen)

## 5.4 Notebooks<a name="notebooks"></a> 
Gedurende het project waren er een aantal opdrachten die wij in de Phyton programeertaal moesten uitvoeren. Alle notebooks kunnen [hier](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/tree/master/Data/Notebooks/Python%20Notebooks) gevonden worden.

## 5.5 Spark<a name="spark"></a>
Gedurende het project waren er aantal opdrachten die wij moesten uitvoeren, betreffende Spark. Alle notebooks kunnen [hier](https://github.com/M4dmuffin/KB74-Urbinn-Portfolio/tree/master/Data/Notebooks/Spark%20Notebooks) gevonden worden.








