---
title: customizingchartlegenditem.md
original_path: WinForms_Docs/04_Controls/Chart/customizingchartlegenditem.md
created_at: 2025-08-05
---








  









### Customizing ChartLegendItem {#customizing-chartlegenditem style="tab-stops: 0pt"}

There are several options to customize the image rendered in the legend. The following table lists the properties that allow you to customize the image rendered in the legend:

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ChartLegend Property              | Description                                                                                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ShowSymbol                        | If true, the exact symbol rendered in the series data points will also be used to render the icon in the legend. This overrides most of the other settings. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RepresentationType                | Specifies how each legend item should be represented, as the name implies:                                                                                  |
|                                   |                                                                                                                                                             |
|                                   | [·      ]None (default setting)                                                                                                |
|                                   |                                                                                                                                                             |
|                                   | [·      ]SeriesType - An icon representing the series type.                                                                    |
|                                   |                                                                                                                                                             |
|                                   | [·      ]SeriesImage - Will use the ImageList associated with the Series style.                                                |
|                                   |                                                                                                                                                             |
|                                   | [·      ]Rectangle                                                                                                             |
|                                   |                                                                                                                                                             |
|                                   | [·      ]Line                                                                                                                  |
|                                   |                                                                                                                                                             |
|                                   | [·      ]StraightLine                                                                                                          |
|                                   |                                                                                                                                                             |
|                                   | [·      ]Circle                                                                                                                |
|                                   |                                                                                                                                                             |
|                                   | [·      ]Diamond                                                                                                               |
|                                   |                                                                                                                                                             |
|                                   | [·      ]Hexagon                                                                                                               |
|                                   |                                                                                                                                                             |
|                                   | [·      ]Pentagon                                                                                                              |
|                                   |                                                                                                                                                             |
|                                   | [·      ]Triangle                                                                                                              |
|                                   |                                                                                                                                                             |
|                                   | [·      ]InvertedTriangle                                                                                                      |
|                                   |                                                                                                                                                             |
|                                   | [·      ]Cross                                                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

The following table lists the ChartLegendItem properties, which can be accessed by using the Legend.Items list that typically override the above settings set in the legend:

 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ChartLegendItem Property          | Description                                                                                                                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DrawSeriesIcon                    | Specifies if an icon representing the series type should be rendered for this legend item.                                                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ImageList                         | Contains a collection of images and will be referred to, by using the ImageList property.                                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ImageIndex                        | Specifies the index in the ImageList array, which contains the image for this item.                                                                                                   |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Interior                          | Specifies the BrushInfo used to render the interior of a Chart Symbol.                                                                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RepresentationSize                | Specifies the size of the rectangle inside which the associated image or symbol will get rendered.                                                                                    |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ShowSymbol                        | If true, the exact symbol rendered in the corresponding series data points will also be used to render the icon in this legend. This overrides most of the other settings.            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Symbol                            | Symbols rendered in the legend item can be customized by using this property.                                                                                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Type                              | When ShowSymbol is set to false, you can customize the type of icon that gets rendered in the legend item. The default value will reflect the ChartLegend.RepresentationType setting. |
|                                   |                                                                                                                                                                                       |
|                                   | The possible values are the following:                                                                                                                                                |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]Area                                                                                                                                            |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]Circle                                                                                                                                          |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]Cross                                                                                                                                           |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]Diamond                                                                                                                                         |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]Hexagon                                                                                                                                         |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]Image                                                                                                                                           |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]InvertedTriangle                                                                                                                                |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]Line                                                                                                                                            |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]None                                                                                                                                            |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]Pentagon                                                                                                                                        |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]PieSlice                                                                                                                                        |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]Rectangle                                                                                                                                       |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]Spline                                                                                                                                          |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]SplineArea                                                                                                                                      |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]StraightLine                                                                                                                                    |
|                                   |                                                                                                                                                                                       |
|                                   | [·      ]Rectangle[]                                                                                        |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ShowIcon                          | If set to false, no icons will be rendered. This overrides most of the other settings including ShowSymbol.                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

Series Type Icon

An icon representing the series type can be rendered in the legend.

{border="0"}

Figure 286: Legend item with the Series type icon

Series Symbol

You can also choose to show the exact same symbol that is shown in the data points in a series.

The code displayed below shows how all the legend items can be rendered with the same symbol.


\[C#\]

[//Set a symbol for first series][]

[chartModel.Series\[0\].Style.Symbol.Shape = [ChartSymbolShape].Diamond;][]

[chartModel.Series\[0\].Style.Symbol.Color = [Color].Red ;][]

[chartModel.Series\[0\].Style.Symbol.Size = [new] [Size](7, 7);][]

[] 

[//This will cause the legend to render with the same symbol defined above.][]

[chartModel.Legend.ShowSymbol = [true];][]

[] 

[//Setting RepresentationType to None to hide other representations][]

[chartModel.Legend.RepresentationType = [ChartLegendRepresentationType.]None;][]


[] 

[] 

{border="0"}

Figure 287: Legend items rendered with the same symbol

[] 

Custom Representation Icon

You can also choose to use one of the built-in representation icons in the legend items.

The code displayed below shows how to  use one of the built-in representation icons for all the legend items.

[] 

this.chartControl1.Legend.RepresentationType = ChartLegendRepresentationType.Diamond;

[] 


[// To specify a custom color for the interior of the icon][]

[chartModel.Legend.Items\[0\].Interior = [new] [BrushInfo]([Color].Violet);]


[] 

{border="0"}

Figure 288: Legend item with a Custom Representation icon

 

To use one of the built-in representation icons only on specific legend items, use the ChartLegendItem.Type property.

 

More Symbol Shapes

ChartLegendItem has the Symbol property, by using which you can customize the symbols for particular legend items. This setting overrides the Series\[0\].Style.Symbol settings.

 

{border="0"}

Figure 289: Legend item customized with \"Triangle\" symbol in \"Yellow\" color

 

Custom Images

You can also choose to show custom images in the legend items as follows:

 

{border="0"}

Figure 290: Chart legend items with custom images

 

The following screenshots illustrate the various representation types of a legend:

{border="0"}

Figure 291: LegendPosition = \"Top\"; RepresentationType = \"Cross\"

[] 

{border="0"}

Figure 292: LegendPosition = \"Top\"; RepresentationType = \"Line\"

[] 

{border="0"}

Figure 293: LegendPosition = \"Top\"; RepresentationType = \"Pentagon\"

[] 

{border="0"}

Figure 294: LegendPosition = \"Top\"; RepresentationType = \"InvertedTriangle\"

[] 

{border="0"}

Figure 295: LegendPosition = \"Top\"; RepresentationType = \"StraightLine\"

[] 

{border="0"}

Figure 296: LegendPosition = \"Top\"; RepresentationType = \"Triangle\"

[]{#related-topics}

