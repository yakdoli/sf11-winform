---
title: configuringthepropertiesofcellstyle1.md
original_path: WinForms_Docs/02_Concepts/configuringthepropertiesofcellstyle1.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Configuring the properties of Cell Style {#configuring-the-properties-of-cell-style style="tab-stops: 0pt"}

The following properties of Grid cell can be customized, so that the grid appears in a custom style rather than the default one:

+---------------+-------------------------------------------------+-------------+------------------+-----------------+
|               |                                                 |             |                  |                 |
|               |                                                 |             |                  |                 |
| Property Name | Description                                     | Type        | Value it Accepts | Reference Links |
+---------------+-------------------------------------------------+-------------+------------------+-----------------+
| Background    | Gets or sets the Background color of Grid cell. | Brush       | \-               | \-              |
+---------------+-------------------------------------------------+-------------+------------------+-----------------+
| FontFamily    | Gets or sets the Font family of Grid cell.      | FontFamily  | \-               | \-              |
+---------------+-------------------------------------------------+-------------+------------------+-----------------+
| FontSize      | Gets or sets the Font size of Grid cell.        | int         | \-               | \-              |
+---------------+-------------------------------------------------+-------------+------------------+-----------------+
| FontWeight    | Gets or sets the Font weigh of Grid cell.       | FontWeight  | \-               | \-              |
+---------------+-------------------------------------------------+-------------+------------------+-----------------+
| Foreground    | Gets or sets the Foreground color of Grid cell. | Brush       | \-               | \-              |
+---------------+-------------------------------------------------+-------------+------------------+-----------------+

 

The Column, Row, Summary and Value cells of Grid can be formatted independently using the following properties:

[·      ]ColumnHeaderStyle

[·      ]RowHeaderStyle

[·      ]SummaryColumnStyle

[·      ]SummaryRowStyle

[·      ]ValueCellsStyle

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
|                    [// Specifying the Background color for Grid column header]                                                                                                           |
|                                                                                                                                                                                                                |
|             [this].OlapGrid1.ColumnHeaderStyle.Background = [new][SolidColorBrush]([Color].FromRgb(175, 209, 255));  |
|                                                                                                                                                                                                                |
|             [// Specifying the Background color for Grid row header]                                                                                                                     |
|                                                                                                                                                                                                                |
|             [this].OlapGrid1.RowHeaderCellStyle.Background = [new][SolidColorBrush]([Color].FromRgb(175, 209, 255)); |
|                                                                                                                                                                                                                |
|             [// Specifying the Background color for Grid summary cell]                                                                                                                   |
|                                                                                                                                                                                                                |
|             [this].OlapGrid1.SummaryColumnStyle.Background = [new][SolidColorBrush]([Color].FromRgb(206, 225, 248)); |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[VB\]                                                                                                                                                          |
|                                                                                                                                                                 |
|                                                                                                                                                                 |
|                                                                                                                                                                 |
|                    [\' Specifying the Background color for Grid column header]                                                            |
|                                                                                                                                                                 |
|                    [Me].OlapGrid1.ColumnHeaderStyle.Background = [New] SolidColorBrush(Color.FromRgb(175, 209, 255))  |
|                                                                                                                                                                 |
|                    [\' Specifying the Background color for Grid row header]                                                               |
|                                                                                                                                                                 |
|                    [Me].OlapGrid1.RowHeaderCellStyle.Background = [New] SolidColorBrush(Color.FromRgb(175, 209, 255)) |
|                                                                                                                                                                 |
|                    [\' Specifying the Background color for Grid summary cell]                                                             |
|                                                                                                                                                                 |
|                    [Me].OlapGrid1.SummaryColumnStyle.Background = [New] SolidColorBrush(Color.FromRgb(206, 225, 248)) |
|                                                                                                                                                                 |
|                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The **Value cell** text alignment can be changed using the following property of OlapGrid,

+----------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                               |
|                                                                                                                      |
|                                                                                                                      |
|                                                                                                                      |
| [// Specifying the Value Cell TextAlignment as Center]                                         |
|                                                                                                                      |
| [this].OlapGrid1.ValueCellTextAlignment = [HorizontalAlignment].Center; |
|                                                                                                                      |
|                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------+

 

Sample Location

A sample demo is available at the following location:

**..\\Syncfusion\\EssentialStudio\\\<Versionnumber\>\\BI\\WPF\\OlapGrid.WPF\\Samples\\Exporting\\Exporting Grid Demo**

 

[]{#related-topics}

