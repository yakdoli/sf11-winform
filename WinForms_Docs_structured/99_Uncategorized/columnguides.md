---
title: columnguides.md
original_path: WinForms_Docs/99_Uncategorized/columnguides.md
created_at: 2025-08-05
---








  









### Column Guides {#column-guides style="tab-stops: 0pt"}

 

Column Guides are used to highlight columns with special meaning. Essential Edit supports unlimited number of column guides.

 

Each column guide can be provided with a custom color and location. This can be done by setting the **ShowColumnGuides** property of the Edit Control to **True**, and then specifying the color and the location of the Column Guides using **ColumnGuideItem Collection Editor**. The font used to calculate the column location is customized by using             **ColumnGuidesMeasuringFont** property.

 


  --------------------------- ----------------------------------------------------------------------------------
  Edit Control Property       Description
  ShowColumnGuides            Gets / sets value that indicates whether column guides should be drawn.
  ColumnGuideItems            Gets / sets array of ColumnGuideItem objects.
  ColumnGuidesMeasuringFont   Gets / sets font that is used while measuring the position of the column guides.
  --------------------------- ----------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [// Enable Column Guides.]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [this][.editControl1.ShowColumnGuides = [true];]                                                                                            |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [// Specify the color and the location of the Column Guides.]                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [ColumnGuideItem\[\] columnGuideItem = [new] ColumnGuideItem\[2\];]                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [columnGuideItem\[0\] = [new] ColumnGuideItem(20, [Color].Yellow);]                                                                                                     |
|                                                                                                                                                                                                                                                       |
| [columnGuideItem\[1\] = [new] ColumnGuideItem(40, [Color].IndianRed);]                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [this][.editControl1.ColumnGuideItems = columnGuideItem;]                                                                                                        |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [// Font used to calculate the column location.]                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [this][.editControl1.ColumnGuidesMeasuringFont = [new] [Font]([\"Microsoft Sans Serif\"], 12);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                            |
| [\' Enable Column Guides.]                                                                                                                                               |
|                                                                                                                                                                                                                            |
| [Me][.editControl1.ShowColumnGuides = [True]]                                                                    |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                            |
| [\' Specify the color and the location of the Column Guides.]                                                                                                            |
|                                                                                                                                                                                                                            |
| [Dim][ columnGuideItem() [As] ColumnGuideItem = [New] ColumnGuideItem(2)]                   |
|                                                                                                                                                                                                                            |
| [columnGuideItem(0) = [New] ColumnGuideItem(20, Color.Yellow)]                                                                                                    |
|                                                                                                                                                                                                                            |
| [columnGuideItem(1) = [New] ColumnGuideItem(40, Color.IndianRed) ]                                                                                                |
|                                                                                                                                                                                                                            |
| [Me][.editControl1.ColumnGuideItems = columnGuideItem]                                                                                |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [\' Font used to calculate the column location.]                                                                                                                         |
|                                                                                                                                                                                                                            |
| [Me][.editControl1.ColumnGuidesMeasuringFont = [New] Font([\"Microsoft Sans Serif\"],12)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 16: Customized Column Guide Items positioned at Equal Intervals

 

A sample which illustrates the above feature is available in the following sample installation path.

 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Advanced Editor Functions\\ColumnGuidesDemo***

[]{#p35} 

[]{#related-topics}

