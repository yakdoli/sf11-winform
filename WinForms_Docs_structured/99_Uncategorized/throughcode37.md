---
title: throughcode37.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode37.md
created_at: 2025-07-03
---






#### Through Code {#through-code style="tab-stops: 0pt"}

[] 

Here is some minimal code that is necessary to create a Grid Record Navigation control**.**

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [this][.recordNavigationControl1 = [new] Syncfusion.Windows.Forms.Grid.[GridRecordNavigationControl]();] |
|                                                                                                                                                                                                                                            |
| [this][.recordNavigationControl1.Location = [new] System.Drawing.[Point](32, 48);]                       |
|                                                                                                                                                                                                                                            |
| [this][.recordNavigationControl1.MaxLabel = [\"of 1000\"];]                                                                   |
|                                                                                                                                                                                                                                            |
| [this][.recordNavigationControl1.MaxRecord = 1000;]                                                                                                   |
|                                                                                                                                                                                                                                            |
| [this][.recordNavigationControl1.NavigationBarWidth = 237;]                                                                                           |
|                                                                                                                                                                                                                                            |
| [this][.recordNavigationControl1.Size = [new] System.Drawing.[Size](520, 256);]                          |
|                                                                                                                                                                                                                                            |
| [this][.recordNavigationControl1.SplitBars = Syncfusion.Windows.Forms.[DynamicSplitBars].Both;]                               |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [this][.gridControl1 = [new] Syncfusion.Windows.Forms.Grid.[GridControl]();]                             |
|                                                                                                                                                                                                                                            |
| [this][.gridControl1.ColCount = 16;]                                                                                                                  |
|                                                                                                                                                                                                                                            |
| [this][.gridControl1.NumberedRowHeaders = [false];]                                                                              |
|                                                                                                                                                                                                                                            |
| [this][.gridControl1.RowCount = 1000;]                                                                                                                |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [// Adds the grid to the Record Navigation control.]                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [this][.recordNavigationControl1.Controls.Add([this].gridControl1);]                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [// Adds the Record Navigation control to the form.]                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [this][.Controls.Add([this].recordNavigationControl1);]                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.recordNavigationControl1 = ][New][ Syncfusion.Windows.Forms.Grid.GridRecordNavigationControl()] |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.recordNavigationControl1.Location = ][New][ System.Drawing.Point(32, 48)]                       |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.recordNavigationControl1.MaxLabel = ][\"of 1000\"]                                                                                             |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.recordNavigationControl1.MaxRecord = 1000]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.recordNavigationControl1.NavigationBarWidth = 237]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.recordNavigationControl1.Size = ][New][ System.Drawing.Size(520, 256)]                          |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.recordNavigationControl1.SplitBars = Syncfusion.Windows.Forms.DynamicSplitBars.Both]                                                                                                               |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.gridControl1 = ][New][ Syncfusion.Windows.Forms.Grid.GridControl()]                             |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.gridControl1.ColCount = 16]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.gridControl1.NumberedRowHeaders = ][False]                                                                                                        |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.gridControl1.RowCount = 1000]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                             |
| [\' Adds the grid to the Record Navigation control.]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.recordNavigationControl1.Controls.Add(][Me][.gridControl1)]                                     |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                             |
| [\' Adds the Record Navigation control to the form.]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                             |
| [Me][.Controls.Add(][Me][.recordNavigationControl1)]                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p528} 

[]{#related-topics}

