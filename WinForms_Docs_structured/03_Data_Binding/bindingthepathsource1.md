---
title: bindingthepathsource1.md
original_path: WinForms_Docs/03_Data_Binding/bindingthepathsource1.md
created_at: 2025-08-05
---








  









### Binding the Path Source {#binding-the-path-source style="tab-stops: 0pt"}


  ------------------- -------------------------------
  Name                Data Type
  Points\*            ObservableCollection\<Point\>
  Label               String
  Color               Brush
  LabelColor          Brush
  LabelPosition\*\*   PathLabelPosition
  LabelPoint\*\*      Point
  FontFamily          FontFamily
  FontSize            Double
  FontStyle           FontStyle
  ------------------- -------------------------------


 


Note:


[·      ]***Properties marked with \* are mandatory.***

[·      ]***Properties marked with \*\* are mandatory when label is set.***

 

To create a collection class

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                    |
| [namespace][ SilverlightSampleBrowser]                                                                                                        |
|                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [    [using] System;]                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [    [using] System.Net;]                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [    [using] System.Windows;]                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [    [using] System.Windows.Controls;]                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [    [using] System.Windows.Documents;]                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [    [using] System.Windows.Ink;]                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [    [using] System.Windows.Input;]                                                                                                                                       |
|                                                                                                                                                                                                                                    |
| [    [using] System.Windows.Media;]                                                                                                                                       |
|                                                                                                                                                                                                                                    |
| [    [using] System.Windows.Media.Animation;]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [    [using] System.Windows.Shapes;]                                                                                                                                      |
|                                                                                                                                                                                                                                    |
| [    [using] System.Collections.ObjectModel;]                                                                                                                             |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [  [public] [class] [PathCollection] : [ObservableCollection]\<[MapsPath]\>] |
|                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [        [MapsPath] mpath;]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [        [public] PathCollection()]                                                                                                                                       |
|                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                    |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](-119, 47));]                                                                                          |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](-115, 27));]                                                                                          |
|                                                                                                                                                                                                                                    |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                    |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](-119, 47));]                                                                                          |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](-80, 41));]                                                                                           |
|                                                                                                                                                                                                                                    |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                    |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](-115, 27));]                                                                                          |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](-80, 41));]                                                                                           |
|                                                                                                                                                                                                                                    |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                    |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](-101, 39));]                                                                                          |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](-115, 27));]                                                                                          |
|                                                                                                                                                                                                                                    |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                    |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](-119, 47));]                                                                                          |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](-100, 31));]                                                                                          |
|                                                                                                                                                                                                                                    |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                    |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](0, 0));]                                                                                              |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](0, 0));]                                                                                              |
|                                                                                                                                                                                                                                    |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                    |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](0, 0));]                                                                                              |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](0, 0));]                                                                                              |
|                                                                                                                                                                                                                                    |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                    |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](0, 0));]                                                                                              |
|                                                                                                                                                                                                                                    |
| [            mpath.Points.Add([new] [Point](0, 0));]                                                                                              |
|                                                                                                                                                                                                                                    |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [    public][ [class] [MapsPath]]                                                                |
|                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [        [public] [ObservableCollection]\<[Point]\> Points { [get]; [set]; }]   |
|                                                                                                                                                                                                                                    |
| [        [public] [Point] LabelPoint { [get]; [set]; }]                                                 |
|                                                                                                                                                                                                                                    |
| [        [public] [string] Label { [get]; [set]; }]                                                        |
|                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                    |
| [}][]                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Add the Following code in Resource Dictionary

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Xaml\]]                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<!\-- Local Refers the Namespace of the Project :- xmlns:local=\"clr-namespace:SilverlightSampleBrowser\"  \--\>]                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][local][:][PathCollection][ x][:][Key][=\"pc\"/\>][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

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
| [\<][syncfusion][:][ShapeFileLayer][ PathSource="][{][Binding][ Source][={][StaticResource][ pc][}}"]                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [ ][Uri][=\"Maps.ShapeFiles.states.shp\"][ x][:][Name][=\"shapeLayer\"/\>][]                                                                                                                                                                                                                                                                                       |
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
| [  [// Create a Instance for PathCollection class]]                                                             |
|                                                                                                                                                                           |
| [   [PathCollection] pathCollection = [new] [PathCollection]();] |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [  [// Assign the object as Path Source of the Shape File Layer]]                                               |
|                                                                                                                                                                           |
| [  [this].shapeLayer.PathSource = pathCollection;]                                                               |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| []                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

 

[]{#related-topics}

