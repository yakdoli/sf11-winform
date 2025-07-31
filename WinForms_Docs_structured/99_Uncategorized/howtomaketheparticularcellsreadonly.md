---
title: howtomaketheparticularcellsreadonly.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtomaketheparticularcellsreadonly.md
created_at: 2025-07-03
---








  









### How to Make the Particular Cells ReadOnly {#how-to-make-the-particular-cells-readonly style="tab-stops: 0pt"}

[] 

Introduction

[] 

In general, cell specific style settings (other than CellValue or text) in a GridDataBoundGrid need to be done through an event like **PrepareViewStyleInfo**. Functional properties like **Read-only** that are used to determine the cell\'s functionality need to be set in **Model.QueryCellInfo**. But, visual properties like the **font** and **backcolor** can be set in either the PrepareViewStyleInfo or the Model.QueryCellInfo.

**[]** 

Example

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                      |
| [this][.gridDataBoundGrid1.Model.QueryCellInfo += ][new][ GridQueryCellInfoEventHandler(Model_QueryCellInfo);] |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                      |
| [    private void][ Model_QueryCellInfo(][object][ sender, GridQueryCellInfoEventArgs e)]                      |
|                                                                                                                                                                                                                                                                                                                      |
| [    {]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                      |
| [            // Set ReadOnly property of the Cell(2,2) to true.]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                      |
| [        ][if][(e.ColIndex == 2 && e.RowIndex == 2) ]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                      |
| [        { ]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                      |
| [            e.Style.ReadOnly = ][true][;]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                      |
| [    }]                                                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [AddHandler][ ][Me][.gridDataBoundGrid1.Model.QueryCellInfo, ][AddressOf][ Model_QueryCellInfo]                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [   ][ Private Sub][ Model_QueryCellInfo(sender ][As Object][, e ][As][ GridQueryCellInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [        \' Set ReadOnly property of the Cell(2,2) to true.]                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [        ][If][ e.ColIndex = 2 ][And][ e.RowIndex = 2 ][Then]                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [            e.Style.ReadOnly = ][True]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [       ][ End If]                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    End Sub]                                                                                                                                                                                                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p592} 

 

[]{#related-topics}

