---
title: howtogettheselectedrowsinthegrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtogettheselectedrowsinthegrid.md
created_at: 2025-07-03
---








  









## How to get the selected rows in the Grid {#how-to-get-the-selected-rows-in-the-grid style="tab-stops: 0pt"}

[] 

You can use the **Table.SelectedRecords** collection of the GridGroupingControl to get the selected rows in the Grid.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [SelectedRecord rec = [default](SelectedRecord);]                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [foreach][ ([var] rec [in] [this].gridGroupingControl1.Table.SelectedRecords)] |
|                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [Console][.WriteLine(rec.Record.ToString());]                                                                                              |
|                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                              |
| [Dim][ rec [As] SelectedRecord]                                                                                    |
|                                                                                                                                                                                                                              |
| [For][ [Each] rec [In] [Me].gridGroupingControl1.Table.SelectedRecords ] |
|                                                                                                                                                                                                                              |
| [Console.WriteLine(rec.Record.ToString()) ]                                                                                                                                              |
|                                                                                                                                                                                                                              |
| [Next][ rec]                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p120} 

[]{#related-topics}

