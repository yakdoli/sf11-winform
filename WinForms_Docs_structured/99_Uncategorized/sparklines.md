---
title: sparklines.md
original_path: WinForms_Docs/99_Uncategorized/sparklines.md
created_at: 2025-08-05
---






#### Sparklines {#sparklines style="tab-stops: 0pt"}

[] 

Sparklines Creation Using MS Excel 2010:

In MS Excel 2010, the Sparklines can be inserted by selecting any of the sparklines type from the Insert menu.

 

In MS Excel 2010, click Insert Menu. Select any of the Sparklines type.

 

{border="0"}

Figure 79: Create Sparklines Dialog Box

 

MS Excel 2010 allows you to select the range of data for the Sparklines creation. It also allows you to to choose where the sparklines can be placed.

 

[{border="0"}]{#Figure2}

Figure 80: Sparklines Tool

The Sparklines appear once you select the data range and the location range. Now you can customize the apperance of Sparklines in terms of color, style etc. A group of Sparkline tools are available on the ribbon to change the high point, low point, color, edit the sparkline data etc.

**Sparkline Creation Using XlsIO:**

XlsIO provides support for creation of Sparklines by using simple APIs.

[] 

[·      ]**ISparklineGroups** interface caches the SparklineGroup that needs to be added to the Spreadsheet.

[·      ]**ISparklineGroup** represents Sparklines in object, and has properties that allows  to customize it.

[·      ]**ISparklines** interface returns the collection of Sparkline present in a Worksheet.

[·      ]**ISparkline** represents a sparkline in the Sparklines. Currently, XlsIO supports all the three types of sparklines- Line, Column, Win/Loss which are supported in Excel 2010.

Following code example illustrates how to create Sparklines by using XlsIO.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                          |
| []                                                                                                                                   |
|                                                                                                                                                                          |
| [ISparklineGroup][ sparklineGroup = sheet.SparklineGroups.Add();]                |
|                                                                                                                                                                          |
| []                                                                                                                                   |
|                                                                                                                                                                          |
| [sparklineGroup.SparklineType = [SparklineType].Line;]                                                       |
|                                                                                                                                                                          |
| []                                                                                                                                   |
|                                                                                                                                                                          |
| [ISparklines][ sparklines = sparklineGroup.Add();]                               |
|                                                                                                                                                                          |
| [           []]                                                                                                |
|                                                                                                                                                                          |
| [IRange][ dataRange = sheet.Range\[[\"D6:G17\"]\];]      |
|                                                                                                                                                                          |
| [IRange][ referenceRange = sheet.Range\[[\"H6:H17\"]\];] |
|                                                                                                                                                                          |
| [            []]                                                                                               |
|                                                                                                                                                                          |
| [sparklines.Add(dataRange,referenceRange); ]                                                                                         |
|                                                                                                                                                                          |
| []                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                 |
|                                                                                                                                                                                                  |
| [Dim][ sparklineGroup [As] ISparklineGroup = sheet.SparklineGroups.Add()]              |
|                                                                                                                                                                                                  |
| [sparklineGroup.SparklineType = SparklineType.Line]                                                                                                          |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [Dim][ sparklines [As] ISparklines = sparklineGroup.Add()]                             |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [Dim][ dataRange [As] IRange = sheet.Range([\"D6:G17\"])]      |
|                                                                                                                                                                                                  |
| [Dim][ referenceRange [As] IRange = sheet.Range([\"H6:H17\"])] |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [sparklines.Add(dataRange,referenceRange)]                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Sparklines Options by XlsIO:

MS Excel 2010 provides various options through Sparklines tool ribbon in order to customize the appearance of Sparklines.See [[figure 2]{.UGHyperlink}](#Figure2)

Type:

In MS Excel 2010, click Design and then Type in order to customize the Sparkline type for the current Sparklines. XlsIO provides an equivalent API to perform this with simple properties as follows.

[] 

+-----------------------------------------------------------------------------------------+
| **[\[C#\]]**                                        |
|                                                                                         |
| [sparklineGroup.SparklineType = SparklineType.Line] |
|                                                                                         |
| []                                                  |
+-----------------------------------------------------------------------------------------+

**[]** 

Show:

In MS Excel 2010, click Design and then Show in order to customize the view of the Sparklines with high point, low point, first point, last point, negative point, markers. XlsIO provides an equivalent API to perform this with simple properties as follows.

*Known Limitations: The Markers can be applied only for the line sparkline type.*

+-------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                      |
|                                                                                                       |
| [sparklineGroup.ShowFirstPoint = [true];]    |
|                                                                                                       |
| [sparklineGroup.ShowLastPoint = [true];]     |
|                                                                                                       |
| [sparklineGroup.ShowHighPoint = [true];]     |
|                                                                                                       |
| [sparklineGroup.ShowLowPoint = [true];]      |
|                                                                                                       |
| [sparklineGroup.ShowMarkers = [true];]       |
|                                                                                                       |
| [sparklineGroup.ShowNegativePoint = [true];] |
|                                                                                                       |
| []                                                                |
+-------------------------------------------------------------------------------------------------------+

**[]** 

Sparkline Color:

**[]** 

The appearance of the Sparklines can be customized by applying colors.  Click Design and then select Style. Choose the Sparkline color option in order to customize the Sparklines. XlsIO provides an equivalent API to perform this with simple property as follows.

+-------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                            |
|                                                                                                             |
| [sparklineGroup.SparklineColor = [Color].Blue;] |
+-------------------------------------------------------------------------------------------------------------+

[] 

Marker Color:

**[]** 

The apperance of points in the sparklines can be customized by applying colors to it. Click Design and then select Style. Choose the Marker Color option to customize the appearance of points in the Sparklines. XlsIO provides an equivalent API to perform this with simple properties as follows.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [sparklineGroup.FirstPointColor = [Color].Green;            sparklineGroup.LastPointColor = [Color].DarkOrange;            sparklineGroup.HighPointColor = [Color].DarkBlue;            sparklineGroup.LowPointColor = [Color].DarkViolet;            sparklineGroup.MarkersColor = [Color].Black;            []] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Edit Group Data and Location:

**[]** 

MS Excel provides an option to edit the location and group data of an exsisting Sparklines, by which you can assign a new location or group data for an exsisting sparklines. XlsIO provides an equivalent API to perform this funtionality.

 

+--------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                           |
|                                                                                            |
| [sparklines.RefreshRanges(dataRange, referenceRange);] |
+--------------------------------------------------------------------------------------------+

**[]** 

Line Weight:

MS Excel 2010 provides an exclusive option to customize  the Line Weight of the Line Sparkline type. XlsIO provides an API to perform this functionality.

 

+------------------------------------------------------------------------+
| [\[C#\]]                           |
|                                                                        |
| [sparklineGroup.LineWeight = 1.0;] |
+------------------------------------------------------------------------+

*[]* 

Known Limitations: The Line weight can be applied only for the line sparkline type.

**[]** 

Hidden and Empty Cell Settings:

 

Normally,  in a sparkline group data there is a possibility of an empty cell or an hidden cell. MS Excel 2010 provides a dialog box to

{border="0"}

Figure 81: Hidden and Empty cells Settings

 

XlsIO provides a simple API to implement the above functionality.This is illustrated in the following code.

 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                               |
|                                                                                                                                |
| [sparklineGroup.DisplayEmptyCellsAs = [SparklineEmptyCells].Gaps;] |
|                                                                                                                                |
| [sparklineGroup.DisplayHiddenRC = [true];]                            |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

Display Axis:

**[]** 

MS Excel 2010 provides an option to display the axis for the sparklines types.This is illustrated in the following code.

 

+-------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                |
|                                                                                                 |
| [sparklineGroup.DisplayAxis = [true];] |
+-------------------------------------------------------------------------------------------------+

**[]** 

Plot Right to Left:

**[]** 

The plotting of Sparklines is done from left to right by default. There is an option available in the Sparkline tools to customize the plotting nature from right to left. XlsIO provides a simple API to perform this functionality.

 

+-----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                    |
|                                                                                                     |
| [sparklineGroup.PlotRightToLeft = [true];] |
+-----------------------------------------------------------------------------------------------------+

**[]** 

Clear:

XlsIO provides an API to clear the selected Sparklines within the sparkline groups and also the selected sparklinegroup within the excel spreadsheet.This is illustrated in the following code.

 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                       |
|                                                                                                                                        |
| [//Clears the sparkline group from the sheet.][] |
|                                                                                                                                        |
| [sheet.SparklineGroups.Remove(sparklineGroup);]                                                    |
|                                                                                                                                        |
| [//Clears the Sparkline from the sparklines.][]  |
|                                                                                                                                        |
| [sparklines.Remove(sparkline);]                                                                    |
|                                                                                                                                        |
| []                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

