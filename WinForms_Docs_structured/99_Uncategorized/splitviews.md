---
title: splitviews.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\splitviews.md
created_at: 2025-07-03
---






#### Split Views {#split-views style="tab-stops: 0pt"}

 

Edit Control provides in-built support for horizontal and vertical splitters, which facilitates the splitting of a single document in the Edit Control into several split views so that you can work with multiple different areas of a document at the same time. A maximum of four split views are supported. However, you can also limit the user to perform either a horizontal or vertical split, only if you wish to support two views instead of four.

 

The vertical and horizontal splitters are always visible, by default. They can be disabled by setting the below given properties to **False**.

 


  ---------------------------------------- ----------------------------------------------------------------------------
           Edit Control Property           Description
  ShowHorizontalSplitters                  Gets / sets value that indicates whether horizontal splitters are visible.
  ShowVerticalSplitters                    Gets / sets value that indicates whether vertical splitters are visible.
  ---------------------------------------- ----------------------------------------------------------------------------


 

The following methods can be used to split the Edit Control into two equal horizontal or vertical halves.

 


  --------------------- -----------------------------------------------------------
  Edit Control Method   Description
  SplitHorizontally     Splits the Edit Control into two equal horizontal halves.
  SplitVertically       Splits the Edit Control into two equal vertical halves.
  --------------------- -----------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [this][.editControl1.ShowHorizontalSplitters = [true];] |
|                                                                                                                                                                   |
| [this][.editControl1.ShowVerticalSplitters = [true];]   |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [this][.editControl1.SplitHorizontally();]                                   |
|                                                                                                                                                                   |
| [this][.editControl1.SplitVertically();]                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                             |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [Me][.editControl1.ShowHorizontalSplitters = [True]] |
|                                                                                                                                                                |
| [Me][.editControl1.ShowVerticalSplitters = [True]]   |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [Me][.editControl1.SplitHorizontally()]                                   |
|                                                                                                                                                                |
| [Me][.editControl1.SplitVertically()]                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Positioning**

[] 

The following properties can be used to position the horizontal and vertical splitters in the Edit Control.

 


  -------------------------------- -------------------------------------------------------
  Edit Control Property            Description
  HorizontalSplitterPosition       Gets / sets position of the horizontal splitter.
  TopVerticalSplitterPosition      Gets / sets position of the top vertical splitter.
  BottomVerticalSplitterPosition   Gets / sets position of the bottom vertical splitter.
  -------------------------------- -------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                                  |
| []                                                                                             |
|                                                                                                                                                  |
| [this][.editControl1.HorizontalSplitterPosition = 220;]     |
|                                                                                                                                                  |
| [this][.editControl1.TopVerticalSplitterPosition = 260;]    |
|                                                                                                                                                  |
| [this][.editControl1.BottomVerticalSplitterPosition = 260;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                            |
|                                                                                                                                               |
| []                                                                                          |
|                                                                                                                                               |
| [Me][.editControl1.HorizontalSplitterPosition = 220]     |
|                                                                                                                                               |
| [Me][.editControl1.TopVerticalSplitterPosition = 260]    |
|                                                                                                                                               |
| [Me][.editControl1.BottomVerticalSplitterPosition = 260] |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

SplitFourQuadrants Method

[] 

The **SplitFourQuadrants** method is used to split the Edit Control into four equal parts.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [this][.editControl1.SplitFourQuadrants();] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                            |
|                                                                                                                               |
| []                                                                          |
|                                                                                                                               |
| [Me][.editControl1.SplitFourQuadrants()] |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 63: Edit Control Split into Four Quadrants

 

A sample which demonstrates Split Views is available in the below sample installation path.

 

..\\My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Edit.Windows\\Samples\\2.0\\Appearance\\SplitViewsDemo

 

See Also

[] 

[Scrolling Support]{.UGHyperlink}[]{.UGHyperlink}

[]{#p95} 

 

[]{#related-topics}

