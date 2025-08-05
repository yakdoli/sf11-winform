---
title: excellikeui.md
original_path: WinForms_Docs/99_Uncategorized/excellikeui.md
created_at: 2025-08-05
---






#### Excel-like UI {#excel-like-ui style="tab-stops: 0pt"}

[] 

Grids can be adopted in many real time applications where the database is of crucial importance. As such applications are widely spread; the grids are indispensably used world-wide. This section elaborates on some of the real time applications which can use Essential Grid.

[] 

Real-time Applications

[] 

Some real time applications which can use Essential Grid are listed below:

[] 

[·      ]Applications with high frequency updates

[·      ]Excel like UI applications

[] 

1.   Applications with High Frequency Updates

[] 

Grid can be used in applications with frequent updates, for example stock values in share market. When grid is switched over to virtual mode, it reforms itself as a light weight control that consumes a very little memory and processing power, and provides a very small latency under heavy load. Such virtual grids are typically useful when there is a need to display enormous data very quickly. 

[] 

Sample

**[]** 

A sample which demonstrates such an application is available in the following sample installation location:

 

***\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\Silverlight\\Grid.Silverlight\\Samples\\Performance\\TraderGridTestDemo***

[] 

Excel-like UI Applications

**[]** 

Another important application is Excel like UI that simulates MS Excel 2007 and gives an appearance that resembles excel. This application exhibits the following excel characteristics:

[] 

[·      ]Excel like Current Cell

[·      ]Excel like Selection Frame

[] 

a.   Excel-like Current Cell

[] 

You can select a current cell in the Grid, similar to the current cell behavior in MS Excel. This feature can be enabled, by setting **GridModelOptions.ExcelLikeCurrentCell** property to ***true***, as follows: 

[] 

+--------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                               |
|                                                                                                              |
| []                                                          |
|                                                                                                              |
| [grid.Model.Options.ExcelLikeCurrentCell = [true];] |
+--------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 89: Grid Showing Excel like Current Cell Selection

***[]*** 


{border="0"}Note:  If you have selected a current cell within a specified range, and when you move the current cell selection out of this range, the range will be cleared.


[] 

b.   Excel-like Selection Frame

**[]** 

The active selection can be outlined with a selection frame by setting the **GridModelOptions.ExcelLikeSelectionFrame** property to true, as follows:

[] 

+-----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                  |
|                                                                                                                 |
| []                                                             |
|                                                                                                                 |
| [grid.Model.Options.ExcelLikeSelectionFrame = [true];] |
+-----------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 90: Grid Displaying Excel like Selection Frame

 

[]{#related-topics}

