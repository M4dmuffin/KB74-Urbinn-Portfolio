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
#1 Literatuur scan: gebruikte technologieën |Dit was de allereerste issue die wij hebben ingevoerd in het Waffle Board. Aangezien we nog geen goed overzicht hadden van de scope en bestaande technologieën voor het creëren van een semantische map heb ik als eerste gezocht en bestudeerd naar documenten/rapporten die gericht waren op semantische mappen aan de hand van de camera beelden | data
#19 Serie foto's als test case | Ik heb een camera meegenomen met een viertal Rubiks Kubussen om een aantal foto’s te nemen die we als eerste testcase kunnen gebruiken SLAM-algoritme uitproberen. Zie “Issues -> Foto’s -> Rubiks Kubussen - Fotoset & Opname”. | data
#21 Zoeken naar tutorials/videos voor LSD SLAM | Er is een issue aangemaakt voor het zoeken naar bestaande tutorial van LSD-SLAM op het gebied van installatie, toepassingen en evaluatie. Echter bleek dat er geen (nuttige) tutorials beschikbaar waren | data
#28 ORB SLAM 2 paper bestuderen | Dit betreft een issue die door ieder groepslid is uitgevoerd. Het paper van ORB-SLAM2 is gelezen en bestudeerd voor de eerste close-reading sessie waarbij het paper nader besproken werd. | data
#32 Planning | Ik heb een planning opgesteld waarbij ik een viertal milestones heb opgenomen zodat het doel van het project goed inzicht blijft. Middels deze milestones en de planning is er een duidelijk overzicht gecreëerd voor het gehele team. Hiermee heeft iedereen binnen het team een goed idee wat er voor de desbetreffende sprint uitgevoerd moet worden om de milestone te kunnen behalen. Tevens zorgt dit ervoor dat de realisatie van het doel van het project behaald kan worden middels een strakke planning. | data
#33 Planning notulist | Voor dit issue heb ik een planning opgesteld voor wie de notulisten rol uitvoert gedurende een bepaalde sprint. Naast het notuleren van bijvoorbeeld vergaderingen en retrospectives is de notulist ook verantwoordelijk om per week (sprint heeft 2 weken) het [blog van Urbinn](https://kb74.github.io/) te updaten en de prestaties te verzorgen. | data
#39 Dataset Slinger dataset/evaluatie | In verband met het ontbreken van een stereo camera zijn er opnames gemaakt met behulp van twee monologen webcams die synchroon mogelijk geïnstalleerd zijn. Nadat de opnames gemaakt waren zijn de opnames geconverteerd naar losstaande frames.  | data
#49 Paper Object Detection Selecteren | Naast het maken van een semantisch map voor het project moeten ook object gedetecteerd kunnen worden zoals voetgangers, verkeersborden, auto’s etc. Middels reseach in bestaande technologieen heb ik gekeken welke frameworks het meest aansluiten bij ons doel. Uit dit onderzoek is een het paper/framework YOLO (You Only Look Once Unified, Real-Time Object Detection ) geselecteerd.  | data
#55 Object detection papers lezen | Voor de tweede close reading sessie hebben we gekozen om YOLO (You Only Look Once Unified, Real-Time Object Detection ) paper te gebruiken voor de reading. Dit issue betrof het lezen van de paper om een zo goed mogelijk indruk te krijgen van het YOLO-framework. | data
#57 Beschrijven data structuur KeyFrame in ORB2 | Het ORB-SLAM2 Framework is geschreven in de C++ programmeertaal. Deze complexe code bevatte helaas geen commentaar. Hierdoor waren er methodes en attributen die onduidelijk waren in de werking. Om meer duidelijkheid te scheppen van de klassen die gebruikt worden binnen ORB-SLAM2 is per klas code commentaar toegevoegd. Dit issues betrof het omschrijven van de klasse “KeyFrame”. | data
#63 Evaluatie: aanpak pointcloud vs pointcloud | Voor issue 63 is gekeken naar hoe evaluatie van pointcloud vs pointcloud gerealiseerd kan worden. De basisstappen voor de evaluatie en de bevindingen zijn opgenomen in het evaluatieplan point_cloud.doc | data
#70 KITTI point cloud resultaten | Content from cell 2 | data
#73 Yolo run uitvoeren op Kitti sequence 00 | Content from cell 2 | data
#74 Yolo run KITTI evalueren tegen ground truth object 2D task | Content from cell 2 | data
#82 Yolo training data verzamelen | Content from cell 2 | data
#83 Vaststellen klassen voor trainen Yolo | Content from cell 2 | data
#88 Opzoeken labeling tool | Content from cell 2 | data
#86 Ground truth nieuwe trainingsdata labelen | Content from cell 2 | data
#93 trainen tiny YOLO maandag nacht | Content from cell 2 | data

## 3.2 Overige <a name="overige"></a> 
Overige producten waaraan ik heb gewerkt zijn:<br>

**Locatie foto’s:**<br>
We zijn in het begin van het project naar de locatie Delft gegaan om een indruk te krijgen van de locatie. Ik heb direct foto's gemaakt die wellicht nuttig kunnen zijn tijdens het project. Daarnaast had ik het idee op deze foto's ook te gebruiken in onze eigen dataset 
[foto's](foto’s.zip)<br>

**Close Reading session**<br>
Gedurende het project hebben we een aantal close reading sessies gehouden. Dit is gedaan om eventuele misverstanden binnen het team van de geselecteerde papers weg te nemen.

**Sessie 1 – Woensdag 20 september 2017**<br>
- mur 2017 ORB-SLAM2.pdf

**Sessie 2 – Woensdag 27 september 2017**<br>
- You Only Look Once Unified, Real-Time Object Detection.pdf
- mustafah 2012 Stereo vision images processing for real-time object distance and size measurements.pdf


# 4. Notulen & Presentaties<a name="notulen_en_Presentaties"></a> 

# 5. Cursussen & workshops<a name="cursussen_en_workshops"></a> 
Gedurende deze minor heb ik meerdere cursussen en workshops gevolgd. 

## 5.1 Datacamp<a name="datacamp"></a> 
DataCamp biedt trainingen aan voor het leren en toepassen van de programmeertaal Python in combinatie met een aantal van Machine Learning technieken. Deze cursus was een verplicht onderdeel gedurende de minor. 

## 5.2 Coursera<a name="coursera"></a> 
Coursera biedt een specifieke cursus aan op het gebied van Machine Learning. Deze cursus richt zich voornamelijk op het gebied van lineaire regressie (algebra) en hoe je dit kan toepassen in Machine Learning. 


## 5.3 Calling Bullshit<a name="calling_bullshit"></a> 

## 5.4 Notebooks<a name="notebooks"></a> 

## 5.5 Spark<a name="spark"></a> 







