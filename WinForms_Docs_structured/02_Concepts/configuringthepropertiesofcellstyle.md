---
title: configuringthepropertiesofcellstyle.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\configuringthepropertiesofcellstyle.md
created_at: 2025-07-03
---








  









### Configuring the properties of Cell Style {#configuring-the-properties-of-cell-style style="tab-stops: 0pt"}

The following properties of the Grid cell can be customized, so that the grid appears in a custom style rather than the default style.

Table 7: Properties of the Grid cell

 


+---------------+-----------------------------------------------------+-------------+------------------+-----------------+
|               |                                                     |             |                  |                 |
|               |                                                     |             |                  |                 |
| Property Name | Description                                         | Type        | Value it Accepts | Reference Links |
+---------------+-----------------------------------------------------+-------------+------------------+-----------------+
| Background    | Gets or sets the Background color of the Grid cell. | Brush       | \-               | \-              |
+---------------+-----------------------------------------------------+-------------+------------------+-----------------+
| FontFamily    | Gets or sets the Font family of the Grid cell.      | FontFamily  | \-               | \-              |
+---------------+-----------------------------------------------------+-------------+------------------+-----------------+
| FontSize      | Gets or sets the Font size of the Grid cell.        | int         | \-               | \-              |
+---------------+-----------------------------------------------------+-------------+------------------+-----------------+
| FontWeight    | Gets or sets the Font weight of the Grid cell.      | FontWeight  | \-               | \-              |
+---------------+-----------------------------------------------------+-------------+------------------+-----------------+
| Foreground    | Gets or sets the Foreground color of the Grid cell. | Brush       | \-               | \-              |
+---------------+-----------------------------------------------------+-------------+------------------+-----------------+


 

The Column, Row, Summary, and Value cells of Grid can be formatted independently by using the following properties:

[·      ]ColumnHeaderStyle

[·      ]RowHeaderStyle

[·      ]SummaryColumnStyle

[·      ]SummaryRowStyle

[·      ]ValueCellsStyle

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [            [// Specifying the Background color for Grid column header]]                                                                                                                    |
|                                                                                                                                                                                                                                                        |
| [            [this].OlapGrid1.ColumnHeaderStyle.Background = [new] [SolidColorBrush]([Color].FromRgb(175, 209, 255));]   |
|                                                                                                                                                                                                                                                        |
| [            [// Specifying the Background color for Grid row header]]                                                                                                                       |
|                                                                                                                                                                                                                                                        |
| [            [this].OlapGrid1.RowHeaderCellStyle.Background = [new] [SolidColorBrush]([Color].FromRgb(175, 209, 255));]  |
|                                                                                                                                                                                                                                                        |
| [            [// Specifying the Background color for Grid summary cell]]                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| [            [this].OlapGrid1.SummaryColumnStyle.Background = [new] [SolidColorBrush]([Color].FromRgb(206, 225, 248)); ] |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                               |
|                                                                                                                                                                                                |
| [            [\' Specifying the Background color for Grid column header]]                                                            |
|                                                                                                                                                                                                |
| [            [Me].OlapGrid1.ColumnHeaderStyle.Background = [New] SolidColorBrush(Color.FromRgb(175, 209, 255))]  |
|                                                                                                                                                                                                |
| [            [\' Specifying the Background color for Grid row header]]                                                               |
|                                                                                                                                                                                                |
| [            [Me].OlapGrid1.RowHeaderCellStyle.Background = [New] SolidColorBrush(Color.FromRgb(175, 209, 255))] |
|                                                                                                                                                                                                |
| [            [\' Specifying the Background color for Grid summary cell]]                                                             |
|                                                                                                                                                                                                |
| [            [Me].OlapGrid1.SummaryColumnStyle.Background = [New] SolidColorBrush(Color.FromRgb(206, 225, 248))] |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

Sample Location

A sample demo is available at the following location:

..\\Syncfusion\\EssentialStudio\\\<Versionnumber\>\\BI\\Silverlight\\Syncfusion.OlapGrid.Silverlight.Samples\\Syncfusion.OlapGrid.Silverlight.Samples\\Samples\\ExportDemo

 

[]{#related-topics}

