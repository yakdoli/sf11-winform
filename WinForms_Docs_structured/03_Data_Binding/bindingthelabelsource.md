---
title: bindingthelabelsource.md
original_path: WinForms_Docs/03_Data_Binding/bindingthelabelsource.md
created_at: 2025-08-05
---








  









### Binding the Label Source {#binding-the-label-source style="tab-stops: 0pt"}

The following are steps to bind label source with the map:

1.   Create a class with the following properties:

 


  ------------- ------------
  Name          Data Type
  Latitude\*    Double
  Longitude\*   Double
  Text\*        String
  Foreground    Brush
  Background    Brush
  FontStyle     FontStyle
  FontFamily    FontFamily
  FontSize      Double
  LabelWidth    Double
  ------------- ------------


 

***[Note: Properties marked with \* are mandatory. ]***

***[]*** 

2.   Create another class with the collection of the previous class. Type of this class should be collection. For example List and ObservableCollection.

3.   Create an object for the Collection Class.

4.   Bind the object to the *LabelSource*.

 

The following code examples illustrate this:

 

Create a collection class as given in the following code example:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [namespace][ SampleBrowser]                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [    [using] System;]                                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [    [using] System.Net;]                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [    [using] System.Windows;]                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [    [using] System.Windows.Controls;]                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [    [using] System.Windows.Documents;]                                                                                                                                         |
|                                                                                                                                                                                                                                                       |
| [    [using] System.Windows.Ink;]                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [    [using] System.Windows.Input;]                                                                                                                                             |
|                                                                                                                                                                                                                                                       |
| [    [using] System.Windows.Media;]                                                                                                                                             |
|                                                                                                                                                                                                                                                       |
| [    [using] System.Windows.Media.Animation;]                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [    [using] System.Windows.Shapes;]                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [    [using] System.Collections.ObjectModel;]                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [    [public] [class] [LabelCollection] : [ObservableCollection]\<[MapsLabel]\>]   |
|                                                                                                                                                                                                                                                       |
| [    {]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [        [public] LabelCollection()]                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [            [// Adding new labels in the LabelsCollection class]]                                                                                                             |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [            [this].Add([new] [MapsLabel] { Latitude = 48, Longitude = -121, Text = [\"Washington\"] });]  |
|                                                                                                                                                                                                                                                       |
| [            [this].Add([new] [MapsLabel] { Latitude = 27, Longitude = -115, Text = [\"Alaska\"] });]      |
|                                                                                                                                                                                                                                                       |
| [            [this].Add([new] [MapsLabel] { Latitude = 31, Longitude = -100, Text = [\"Texas\"] });]       |
|                                                                                                                                                                                                                                                       |
| [            [this].Add([new] [MapsLabel] { Latitude = 41, Longitude = -80, Text = [\"Pennsylvania\"] });] |
|                                                                                                                                                                                                                                                       |
| [            [this].Add([new] [MapsLabel] { Latitude = 39, Longitude = -101, Text = [\"Kansas\"] });]      |
|                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [    }]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [   // Creating a MapLabel class][]                                                                                                   |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [    [public] [class] [MapsLabel]]                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [    {]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [        [public] [double] Latitude { [get]; [set]; }]                                                           |
|                                                                                                                                                                                                                                                       |
| [        [public] [double] Longitude { [get]; [set]; }]                                                          |
|                                                                                                                                                                                                                                                       |
| [        [public] [string] Text { [get]; [set]; }]                                                               |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [    }]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Add the following code in Resource Dictionary

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Xaml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<!\-- Local Refers the Namespace of the Project :-  xmlns:local=\"clr-namespace:SampleBrowser\"  \--\>]                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][local][:][LabelCollection][ x][:][Key][=\"lc\"/\>] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Xaml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<!\--syncfusion refers :- xmlns:syncfusion=\"] [clr-namespace:Syncfusion.Phone.Map;assembly=Syncfusion.Maps.Phone\" \--\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<syncfusion][:][MapControl][ ShapeFill][=\"#8f7c5c\"][ Name][=\"Map\"][ LayeredContent][=\"{][Binding][ ElementName][=shapeLayer}\" \>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][MapControl.Layers][\>][                                        ][\<][syncfusion][:][Layers\>][]                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][ShapeFileLayer][ LabelSource][{][Binding][ Source][={][StaticResource][ lc][}}]                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\"][ Uri][=\"Maps.ShapeFiles.states.shp\"][ x][:][Name][=\"shapeLayer\"/\>][]                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][syncfusion][:][Layers][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][syncfusion][:][MapControl.Layers][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][syncfusion][:][MapControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                        |
| [  [// Create an Instance for LabelCollection class]]                                                           |
|                                                                                                                                                                                        |
| [  [LabelCollection] lblCollection = [new] [LabelCollection]();] |
|                                                                                                                                                                                        |
| []                                                                                                                                    |
|                                                                                                                                                                                        |
| [  [// Assign the object as Label Source of the Shape File Layer]]                                              |
|                                                                                                                                                                                        |
| [  [this].shapeLayer.LabelSource = lblCollection;]                                                               |
|                                                                                                                                                                                        |
|                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

