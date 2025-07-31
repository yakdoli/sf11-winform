---
title: throughcode33.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode33.md
created_at: 2025-07-03
---






#### Through Code {#through-code style="tab-stops: 0pt"}

[] 

The following code examples illustrate how to create a Grid control through code.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [// Create the Essential Grid.]                                                                                                                              |
|                                                                                                                                                                                                                |
| [private][ Syncfusion.Windows.Forms.Grid.[GridControl] gridControl1;]                             |
|                                                                                                                                                                                                                |
| [\....]                                                                                                                                                                    |
|                                                                                                                                                                                                                |
| [this][.gridControl1 = [new] Syncfusion.Windows.Forms.Grid.[GridControl]();] |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [// Set the number of rows and columns.]                                                                                                                     |
|                                                                                                                                                                                                                |
| [this][.gridControl1.ColCount = 10;]                                                                                      |
|                                                                                                                                                                                                                |
| [this][.gridControl1.RowCount = 100;]                                                                                     |
|                                                                                                                                                                                                                |
| [                        ]                                                                                                                                                 |
|                                                                                                                                                                                                                |
| [// Position it on the form.]                                                                                                                                |
|                                                                                                                                                                                                                |
| [this][.gridControl1.Location = [new] System.Drawing.[Point](20, 20);]       |
|                                                                                                                                                                                                                |
| [this][.gridControl1.Size = [new] System.Drawing.[Size](344, 200);]          |
|                                                                                                                                                                                                                |
| [                        ]                                                                                                                                                 |
|                                                                                                                                                                                                                |
| [// Add it to the form\'s controls.]                                                                                                                         |
|                                                                                                                                                                                                                |
| [this][.Controls.Add([this].gridControl1);]                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [\' Create the Essential Grid.]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                |
| [Private WithEvents][ gridControl1 ][As][ GridControl]                                                                   |
|                                                                                                                                                                                                                                                                                                                                |
| [        \....]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                |
| [Me][.gridControl1 = ][New][ Syncfusion.Windows.Forms.Grid.GridControl()]                                                |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [\' Set the number of rows and columns.]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                |
| [ ][Me][.gridControl1.ColCount = 10]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [ ][Me][.gridControl1.RowCount = 100]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [\' Position it on the form.]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                |
| [ ][Me][.gridControl1.Location = ][New][ System.Drawing.Point(20, 15)] |
|                                                                                                                                                                                                                                                                                                                                |
| [ ][Me][.gridControl1.Size = ][New][ System.Drawing.Size(344, 150)]    |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [\' Add it to the form\'s controls.]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [Me][.Controls.Add(Me.gridControl1)]                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[Through Designer]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#p40} 

 

[]{#related-topics}

