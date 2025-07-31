---
title: bindingthepathsource.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\bindingthepathsource.md
created_at: 2025-07-03
---








  









### Binding the Path Source {#binding-the-path-source style="tab-stops: 0pt"}

 

The following are steps to bind path source with the map:

1.   Create a class with the following properties:

 


  ------------------- -------------------------------
  **Name**            **Data Type**
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



***[·    ]***Properties marked with \* are mandatory.

***[·    ]***Properties marked with \*\* are mandatory when label is set.



 


2.   Create another class with the collection of the previous class. Type of this class should be collection. For example List and ObservableCollection.

3.   Create an object for the Collection Class.

4.   Bind the object to the *LabelSource*.

 

The following code examples illustrate this:

**     **

Create a collection class as given in the following code example:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [namespace][ SampleBrowser]                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [    [using] System;]                                                                                                                                                     |
|                                                                                                                                                                                                                                                 |
| [    [using] System.Net;]                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [    [using] System.Windows;]                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [    [using] System.Windows.Controls;]                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [    [using] System.Windows.Documents;]                                                                                                                                   |
|                                                                                                                                                                                                                                                 |
| [    [using] System.Windows.Ink;]                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [    [using] System.Windows.Input;]                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [    [using] System.Windows.Media;]                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [    [using] System.Windows.Media.Animation;]                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [    [using] System.Windows.Shapes;]                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [    [using] System.Collections.ObjectModel;]                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [  [public] [class] [PathCollection] : [ObservableCollection]\<[MapsPath]\>] |
|                                                                                                                                                                                                                                                 |
| [    {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [        [MapsPath] mpath;]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [        [public] PathCollection()]                                                                                                                                       |
|                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [           // Adding a New MapsPath in the PathCollection class][]                                                             |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](-119, 47));]                                                                                          |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](-115, 27));]                                                                                          |
|                                                                                                                                                                                                                                                 |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](-119, 47));]                                                                                          |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](-80, 41));]                                                                                           |
|                                                                                                                                                                                                                                                 |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](-115, 27));]                                                                                          |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](-80, 41));]                                                                                           |
|                                                                                                                                                                                                                                                 |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](-101, 39));]                                                                                          |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](-115, 27));]                                                                                          |
|                                                                                                                                                                                                                                                 |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](-119, 47));]                                                                                          |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](-100, 31));]                                                                                          |
|                                                                                                                                                                                                                                                 |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](0, 0));]                                                                                              |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](0, 0));]                                                                                              |
|                                                                                                                                                                                                                                                 |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](0, 0));]                                                                                              |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](0, 0));]                                                                                              |
|                                                                                                                                                                                                                                                 |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [            mpath = [new] [MapsPath]();]                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points = [new] [ObservableCollection]\<[Point]\>();]                                                   |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](0, 0));]                                                                                              |
|                                                                                                                                                                                                                                                 |
| [            mpath.Points.Add([new] [Point](0, 0));]                                                                                              |
|                                                                                                                                                                                                                                                 |
| [            mpath.LabelPoint = mpath.Points\[0\];]                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [            mpath.Label = [string].Empty;]                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [            [this].Add(mpath);]                                                                                                                                          |
|                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [    // Creating a MapPath class][]                                                                                             |
|                                                                                                                                                                                                                                                 |
| [    public][ [class] [MapsPath]]                                                   |
|                                                                                                                                                                                                                                                 |
| [    {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [        [public] [ObservableCollection]\<[Point]\> Points { [get]; [set]; }]   |
|                                                                                                                                                                                                                                                 |
| [        [public] [Point] LabelPoint { [get]; [set]; }]                                                 |
|                                                                                                                                                                                                                                                 |
| [        [public] [string] Label { [get]; [set]; }]                                                        |
|                                                                                                                                                                                                                                                 |
| [    }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Add the following code in Resource Dictionary

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Xaml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<!\-- Local Refers the Namespace of the Project.  \"xmlns:local=\"clr-namespace:Syncfusion.Phone.Map;assembly=Syncfusion.Maps.Phone\"  \--\>]                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][local][:][PathCollection][ x][:][Key][=\"pc\"/\>] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Xaml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<!\--syncfusion refers : xmlns:syncfusion=\"http://schemas.syncfusion.com/wpf\" \--\>][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<syncfusion][:][MapControl][ ShapeFill][=\"#8f7c5c\"][ Name][=\"Map\"][ LayeredContent][=\"{][Binding][ ElementName][=shapeLayer}\" \>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][MapControl.Layers][\>][                                        ][\<][syncfusion][:][Layers\>][]                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][ShapeFileLayer][ PathSource="][{][Binding][ Source][={][StaticResource][ pc][}}"]                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [ ][Uri][=\"Maps.ShapeFiles.states.shp\"][ x][:][Name][=\"shapeLayer\"/\>][]                                                                                                                                                                                                                                                                                                                                           |
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
| **[]**                                                                                                                                |
|                                                                                                                                                                                        |
| [  [// Create an Instance for PathCollection class]]                                                            |
|                                                                                                                                                                                        |
| [   [PathCollection] pathCollection = [new] [PathCollection]();] |
|                                                                                                                                                                                        |
| []                                                                                                                                    |
|                                                                                                                                                                                        |
| [  [// Assign the object as Path Source of the Shape File Layer]]                                               |
|                                                                                                                                                                                        |
| [  [this].shapeLayer.PathSource = pathCollection;]                                                               |
|                                                                                                                                                                                        |
| []                                                                                                                                    |
|                                                                                                                                                                                        |
|                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 26: Data Binding

**[]** 

[]{#related-topics}

