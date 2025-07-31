---
title: axistitle.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\axistitle.md
created_at: 2025-07-03
---








  









### Axis Title {#axis-title style="tab-stops: 0pt"}

[] 

Essential Chart provides properties to set custom titles for the axes. Set the title text for an axis using **Title** property. Customize this text using **TitleColor** and **TitleFont** properties.

[] 


  ----------------------- ------------------------------------------------
  Chart Axis Properties   Description
  TitleColor              Sets the color for the title text of the axis.
  TitleFont               Sets the font style for the title text.
  ----------------------- ------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                   |
| [//Sets custom title for x- axis. ]                                                                                                                             |
|                                                                                                                                                                                                                   |
| [this][.ChartWebControl1.PrimaryXaxis.Title = [\"x-axis\"];]                                         |
|                                                                                                                                                                                                                   |
| [this][.ChartWebControl1.PrimaryXaxis.TitleColor = Color.Red;]                                                               |
|                                                                                                                                                                                                                   |
| [this][.ChartWebControl1.PrimaryXaxis.TitleFont = [new] Font([\"Arial\"], 10);] |
|                                                                                                                                                                                                                   |
| [//Set custom title for y-axis in the similar method.]                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [\'Sets custom title for x- axis. ]                                                                                                                          |
|                                                                                                                                                                                                                |
| [Me][.ChartWebControl1.PrimaryXaxis.Title = [\"x-axis\"]]                                         |
|                                                                                                                                                                                                                |
| [Me][.ChartWebControl1.PrimaryXaxis.TitleColor = Color.Red]                                                               |
|                                                                                                                                                                                                                |
| [Me][.ChartWebControl1.PrimaryXaxis.TitleFont = [New] Font([\"Arial\"], 10)] |
|                                                                                                                                                                                                                |
| [\'Set custom title for y-axis in the similar method.]                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Drawing Mode of Title Text

[] 

You can now display partial axis title with an ellipsis at the end of text, whose text length exceeds the axis length. There is also an option to wrap the title text. The **Axes.TitleDrawMode** property is used to control this behavior.

[] 


  --------------------- -------------------------------------------------------------------------------------------------------------
  Chart Axis Property   Description
  TitleDrawMode         Sets the drawing mode of the axis title. It can be Ellipse, Wrap or None. By default it is set to **None**.
  --------------------- -------------------------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [//Setting drawing mode of y-axis title]                                                                                                   |
|                                                                                                                                                                                              |
| [this][.chartControl1.PrimaryXAxis.TitleDrawMode = [ChartTitleDrawMode].Ellipsis;] |
|                                                                                                                                                                                              |
| [//Setting drawing mode of secondary y-axis title]                                                                                         |
|                                                                                                                                                                                              |
| [this][.secYAxis.TitleDrawMode = [ChartTitleDrawMode].Wrap;]                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [\'Setting drawing mode of y-axis title]                                                                                                |
|                                                                                                                                                                                           |
| [Me][.chartControl1.PrimaryXAxis.TitleDrawMode = [ChartTitleDrawMode].Ellipsis] |
|                                                                                                                                                                                           |
| [\'Setting drawing mode of secondary y-axis title]                                                                                      |
|                                                                                                                                                                                           |
| [Me][.secYAxis.TitleDrawMode = [ChartTitleDrawMode].Wrap]                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

Figure 258: Y-Axis TitleDrawMode=\'Ellipsis; SecYAxis TitleDrawMode =\'Wrap\'

[]{#p188} 

[]{#related-topics}

