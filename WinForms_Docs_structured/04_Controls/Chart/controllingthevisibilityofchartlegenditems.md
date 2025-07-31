---
title: controllingthevisibilityofchartlegenditems.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\controllingthevisibilityofchartlegenditems.md
created_at: 2025-07-03
---






##### Controlling the Visibility of Chart Legend Items {#controlling-the-visibility-of-chart-legend-items style="tab-stops: 0pt"}

Essential Chart WPF now provides support to toggle the visibility of the Chart Legend Items. This is achieved by using the **VisibilityOnLegend** property.

[] 

Table 19: Property Table


+-----------------------------------+------------------------------------------------------------------------------------------+
| Property                          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| VisibilityOnLegend                | Sets the visibility of Legend Items. It includes the following options.                  |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   |                                                                                          |
|                                   | [·      ]*Visible*-Items in the Legend will be Visible.     |
|                                   |                                                                                          |
|                                   | [·      ]*Hidden*-Items in the Legend will be Hidden.       |
|                                   |                                                                                          |
|                                   | [·      ]*Collapsed*-Items in the Legend will be Collapsed. |
+-----------------------------------+------------------------------------------------------------------------------------------+


[] 

The following code example illustrates how to set this property.

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][ChartSeries][ Name][=\"SeriesB\"][ Type][=\"Bar\"][ VisibilityOnLegend][=\"Hidden\"][ BindingPathX][=\"FruitName\"] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [BindingPathsY][=\"FruitID,NumberOfFruits,Price,Year\"][ Label][=\"Series B\"][ Stroke][=\"#FF000000\"][ StrokeThickness][=\"0.5\" \>]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][syncfusion][:][ChartSeries][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                      |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [Chart1.Areas\[0\].Series\[0\].VisibilityOnLegend = [Visibility].Hidden;] |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 107: VisibilityOnLegend property set to \"Hidden\" for Series A

[] 

Methods

[] 

The **LegendItemSource** method associated with this feature can also be used to control the visibility of the Legend Items. The following code example illustrates how to use this method.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                             |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [public][ [void] LegendItemSource([ChartSeries] chartSeries)]              |
|                                                                                                                                                                                                              |
| [{]                                                                                                                                                                      |
|                                                                                                                                                                                                              |
| [    [ChartSeriesCollection] collection = [new] [ChartSeriesCollection]();]                         |
|                                                                                                                                                                                                              |
| [    [foreach] ([ChartSeries] item [in] chartSeries.Area.Series)]                                      |
|                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                  |
|                                                                                                                                                                                                              |
| [        [if] (item.IsVisibleOnLegend == [true] && item.VisibilityOnLegend != [Visibility].Collapsed)] |
|                                                                                                                                                                                                              |
| [        {]                                                                                                                                                              |
|                                                                                                                                                                                                              |
| [            collection.Add(item);]                                                                                                                                      |
|                                                                                                                                                                                                              |
| [        }]                                                                                                                                                              |
|                                                                                                                                                                                                              |
| [    }]                                                                                                                                                                  |
|                                                                                                                                                                                                              |
| [    Legend.ItemsSource = collection;]                                                                                                                                   |
|                                                                                                                                                                                                              |
| [}]                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Events

[] 

The **OnVisibilityOnLegend** event is triggered when the value of the VisibilityOnLegend property is changed. The following code example illustrates how to handle this event.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [public][ [static] [readonly] [DependencyProperty] VisibilityOnLegendProperty =]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [DependencyProperty][.Register([\"VisibilityOnLegend\"], [typeof]([Visibility]), [typeof]([ChartSeries]), [new] [PropertyMetadata]([Visibility].Visible, [new] [PropertyChangedCallback](OnVisibilityOnLegend)));] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [public][ [Visibility] VisibilityOnLegend]                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [    [get] { [return] ([Visibility])GetValue(VisibilityOnLegendProperty); }]                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [    [set] { SetValue(VisibilityOnLegendProperty, [value]); }]                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [private][ [static] [void] OnVisibilityOnLegend([DependencyObject] d, [DependencyPropertyChangedEventArgs] args)]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [    [ChartSeries] type = ([ChartSeries])d;]                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [    type.Area.LegendItemSource(type);]                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p67} 

 

[]{#related-topics}

