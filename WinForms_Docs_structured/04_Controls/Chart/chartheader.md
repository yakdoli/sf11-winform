---
title: chartheader.md
original_path: WinForms_Docs/04_Controls/Chart/chartheader.md
created_at: 2025-08-05
---






##### Chart Header {#chart-header style="tab-stops: 0pt"}

Essential Chart for WPF enables users to set the title for a chart.

[] 

Table 8: Property Table


+------------------+------------------------------+----------------------+------------------------+---------------------------------------------------------------+------------------------------------------------------+
| Name of Property | Description                  | Type of Property     | Value It Accepts       | Property Syntax                                               | Sub Properties                                       |
|                  |                              |                      |                        |                                                               |                                                      |
|                  |                              |                      |                        |                                                               |                                                      |
+------------------+------------------------------+----------------------+------------------------+---------------------------------------------------------------+------------------------------------------------------+
| Header           | Sets the title of the chart. | Dependency  Property | Object/ "Chart Header" |  \<syncfusion:Chart Name=\"chart1\" Header=\"Chart Header\"\> | Sub Property Name : HeaderAlignment                  |
|                  |                              |                      |                        |                                                               |                                                      |
|                  |                              |                      |                        |                                                               | Type: HorizontalAlignment / HorizontalAlignment.Left |
+------------------+------------------------------+----------------------+------------------------+---------------------------------------------------------------+------------------------------------------------------+


 

###### 4.1.1.2.4.1 Setting the Title for a Chart {#setting-the-title-for-a-chart style="tab-stops: 0pt"}

Set the title for a chart by using the following code.

 

+----------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                     |
|                                                                                                    |
| []                                                             |
|                                                                                                    |
| [\<sfchart:Chart Name=\"Chart1\" Header=\"Sales and Month\"\>] |
|                                                                                                    |
| [\</sfchart:Chart\>]                                           |
|                                                                                                    |
| []                                                             |
+----------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                         |
| **[]**                                                                                                              |
|                                                                                                                                                         |
| [chart1.Header = \"][ ][Sales and Month \"] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 63: Chart with Title

 

###### 4.1.1.2.4.2 Customizing Chart Title {#customizing-chart-title style="tab-stops: 0pt"}

Users can customize the chart header using a text block, text box, rectangle, or border control.

Customize the chart header by using the following code.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                              |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [\<sfchart:Chart Name=\"Chart1\" \>]                                                                                                        |
|                                                                                                                                                                                 |
| [   \<sfchart:Chart.Header\>]                                                                                                               |
|                                                                                                                                                                                 |
| [     \<TextBlock Text=\"Sales and Month\" FontSize=\"16\" Foreground=\"Blue\" FontStyle=\"Italic\" FontWeight=\"Bold\" Margin=\"-5\"  /\>] |
|                                                                                                                                                                                 |
| [   \</sfchart:Chart.Header\>]                                                                                                              |
|                                                                                                                                                                                 |
| [\</sfchart:Chart\>]                                                                                                                        |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 64: Customized Chart Header

 

[]{#related-topics}

