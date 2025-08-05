---
title: bindingthelabelsource1.md
original_path: WinForms_Docs/03_Data_Binding/bindingthelabelsource1.md
created_at: 2025-08-05
---








  









### Binding the Label Source {#binding-the-label-source style="tab-stops: 0pt"}

To bind the label source with the map, create a class with the following properties:

 


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


 


Note: Properties marked with \* are mandatory.


Create another class with the previous class collection. For example List, ObservableCollection.

Create an object for the Collection Class.

Bind the object to the *LabelSource*.

To create a collection class

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                          |
| [namespace][ SilverlightSampleBrowser]                                                                                                              |
|                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [    [using] System;]                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| [    [using] System.Net;]                                                                                                                                                       |
|                                                                                                                                                                                                                                          |
| [    [using] System.Windows;]                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [    [using] System.Windows.Controls;]                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [    [using] System.Windows.Documents;]                                                                                                                                         |
|                                                                                                                                                                                                                                          |
| [    [using] System.Windows.Ink;]                                                                                                                                               |
|                                                                                                                                                                                                                                          |
| [    [using] System.Windows.Input;]                                                                                                                                             |
|                                                                                                                                                                                                                                          |
| [    [using] System.Windows.Media;]                                                                                                                                             |
|                                                                                                                                                                                                                                          |
| [    [using] System.Windows.Media.Animation;]                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [    [using] System.Windows.Shapes;]                                                                                                                                            |
|                                                                                                                                                                                                                                          |
| [    [using] System.Collections.ObjectModel;]                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [    [public] [class] [LabelCollection] : [ObservableCollection]\<[MapsLabel]\>]   |
|                                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                          |
| [        [public] LabelCollection()]                                                                                                                                            |
|                                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [            [this].Add([new] [MapsLabel] { Latitude = 48, Longitude = -121, Text = [\"Washington\"] });]  |
|                                                                                                                                                                                                                                          |
| [            [this].Add([new] [MapsLabel] { Latitude = 27, Longitude = -115, Text = [\"Alaska\"] });]      |
|                                                                                                                                                                                                                                          |
| [            [this].Add([new] [MapsLabel] { Latitude = 31, Longitude = -100, Text = [\"Texas\"] });]       |
|                                                                                                                                                                                                                                          |
| [            [this].Add([new] [MapsLabel] { Latitude = 41, Longitude = -80, Text = [\"Pennsylvania\"] });] |
|                                                                                                                                                                                                                                          |
| [            [this].Add([new] [MapsLabel] { Latitude = 39, Longitude = -101, Text = [\"Kansas\"] });]      |
|                                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                          |
| [    }]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                          |
| [    [public] [class] [MapsLabel]]                                                                                                 |
|                                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                          |
| [        [public] [double] Latitude { [get]; [set]; }]                                                           |
|                                                                                                                                                                                                                                          |
| [        [public] [double] Longitude { [get]; [set]; }]                                                          |
|                                                                                                                                                                                                                                          |
| [        [public] [string] Text { [get]; [set]; }]                                                               |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [    }]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Add the Following code in Resource Dictionary

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Xaml\]]                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<!\-- Local Refers the Namespace of the Project :- xmlns:local=\"clr-namespace:SilverlightSampleBrowser\"  \--\>]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][local][:][LabelCollection][ x][:][Key][=\"lc\"/\>][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Xaml\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<!\--syncfusion refers : xmlns:syncfusion=\"clr-namespace:Syncfusion.Windows.Controls.Map;assembly=Syncfusion.Maps.Silverlight\" \--\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<syncfusion][:][MapControl][ ShapeFill][=\"#8f7c5c\"][ Name][=\"Map\"][ LayeredContent][=\"{][Binding][ ElementName][=shapeLayer}\" \>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][MapControl.Layers][\>][                                        ][\<][syncfusion][:][Layers\>][]                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][ShapeFileLayer][ LabelSource][{][Binding][ Source][={][StaticResource][ lc][}}]                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\"][ Uri][=\"Maps.ShapeFiles.states.shp\"][ x][:][Name][=\"shapeLayer\"/\>][]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][syncfusion][:][Layers][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][syncfusion][:][MapControl.Layers][\>][]                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][syncfusion][:][MapControl][\>][]                                                                                                                                                                                                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                              |
|                                                                                                                                                                           |
| [  [// Create a Instance for LabelCollection class]]                                                            |
|                                                                                                                                                                           |
| [  [LabelCollection] lblCollection = [new] [LabelCollection]();] |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [  [// Assign the object as Label Source of the Shape File Layer]]                                              |
|                                                                                                                                                                           |
| [  [this].shapeLayer.LabelSource = lblCollection;]                                                               |
|                                                                                                                                                                           |
| []                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

[]{#related-topics}

