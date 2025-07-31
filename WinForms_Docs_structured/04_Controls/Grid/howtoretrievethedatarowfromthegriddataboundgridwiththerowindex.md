---
title: howtoretrievethedatarowfromthegriddataboundgridwiththerowindex.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtoretrievethedatarowfromthegriddataboundgridwiththerowindex.md
created_at: 2025-07-03
---








  









### How to Retrieve the DataRow from the GridDataBoundGrid with the RowIndex {#how-to-retrieve-the-datarow-from-the-griddataboundgrid-with-the-rowindex style="tab-stops: 0pt"}

[] 

Introduction

[] 

The GridDataBoundGrid has to be bound to the datasource using the **CurrencyManager**. Using the CurrencyManager, the record corresponding to the row index can be retrieved.

[] 

Example

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [CurrencyManager cm=(CurrencyManager)BindingContext\[gridDataBoundGrid1.DataSource, gridDataBoundGrid1.DataMember\]; ]                                                                                                           |
|                                                                                                                                                                                                                                                                                    |
| [DataRow row;]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                    |
| [DataView dv=(DataView)cm.List;]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [// The 2 is the rowindex.]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                    |
| [int][ position = ][this][.gridDataBoundGrid1.Binder.RowIndexToPosition(2);] |
|                                                                                                                                                                                                                                                                                    |
| [row=dv\[position\].Row;]                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ cm ][As][ CurrencyManager= ][CType][(BindingContext(gridDataBoundGrid1.DataSource, gridDataBoundGrid1.DataMember), CurrencyManager)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ row ][As][ DataRow]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ dv ][As][ DataView= ][CType][(cm.List, DataView)]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\' The 2 is the rowindex.]                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ position ][As Integer][ = ][Me][.gridDataBoundGrid1.Binder.RowIndexToPosition(2)]                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [row=dv(position).Row]                                                                                                                                                                                                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p598} 

 

[]{#related-topics}

