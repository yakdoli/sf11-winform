---
title: howtoaddasorticonupdownarrowinagridcontrolscolumnheader.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtoaddasorticonupdownarrowinagridcontrolscolumnheader.md
created_at: 2025-07-03
---








  









### How to Add a Sort Icon (Up / Down Arrow) in a GridControl\'s Column Header {#how-to-add-a-sort-icon-up-down-arrow-in-a-gridcontrols-column-header style="tab-stops: 0pt"}

 

**Introduction**

 

Add the **GridSortColumnHeaderCellModel** to the GridControl\'s **CellModels** collection to include the **SortColumn** HeaderCell. Then assign this as the [CellType] and set the **tag** property to either ListSortDirection.Ascending or ListSortDirection.Descending to show the up / down arrow mark.

[] 

Example

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [// Registering the GridSortColumnHeaderCellModel to the GridModel. ]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [this][.gridControl1.CellModels.Add(\"SortHeader\", ][new][ GridSortColumnHeaderCellModel(][this][.gridControl1.Model));] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [// Setting the new celltype to a column header cell.]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [this][.gridControl1\[0,1\].CellType = \"SortHeader\";]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [// Specifying the sort direction in the Tag property of the column header.]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [this][.gridControl1\[0,1\].Tag = ListSortDirection.Ascending;]                                                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\' Registering the GridSortColumnHeaderCellModel to the GridModel. ]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.GridControl1.CellModels.Add(\"SortHeader\", ][New][ GridSortColumnHeaderCellModel(][Me][.GridControl1.Model))] |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\' Setting the new celltype to a column header cell.]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.GridControl1(0, 1).CellType = \"SortHeader\"]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\' Specifying the sort direction in the Tag property of the column header.]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.GridControl1(0, 1).Tag = ListSortDirection.Ascending]                                                                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: This will only display the sort indicator; it does not actually do any sorting.


 

[]{#p545} 

[]{#related-topics}

