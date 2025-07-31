---
title: howtospecifyanimageforagridcolumnheader.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtospecifyanimageforagridcolumnheader.md
created_at: 2025-07-03
---








  









## How to specify an image for a Grid column header {#how-to-specify-an-image-for-a-grid-column-header style="tab-stops: 0pt"}

[] 

You can specify an image for a column header of a particular column via the Properties settings. Choose the Column via the **TableDescriptor\'s Columns** collection, and set the **ImageUrl** property of the ColumnHeaderCell in the Appearance settings.

 

The below code snippet illustrates this.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                            |
| [this][.GridGroupingControl1.TableDescriptor.Columns\[0\].Appearance.ColumnHeaderCell.ImageUrl = [@\"Images\\Image1.PNG\"]; ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [Me][.GridGroupingControl1.TableDescriptor.Columns(0).Appearance.ColumnHeaderCell.ImageUrl = [\"Images\\Image1.PNG\"]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p127} 

[]{#related-topics}

