---
title: gridawaretextbox.md
original_path: WinForms_Docs/04_Controls/Grid/gridawaretextbox.md
created_at: 2025-08-05
---








  









## Grid Aware Text Box {#grid-aware-text-box style="tab-stops: 0pt"}

[] 

This class is derived from the textbox and will allow you to bind it to the **CurrentCell** of either a Grid control or a Grid Data Bound Grid. The standard use for such a text box is to provide a special edit bar for editing grid cells. This is similar to the FormulaBar in Excel. In Essential Grid\'s Formula Grid sample, a similar Formula Bar is implemented by using a Grid Aware Text Box.

 

Drag the Grid Aware Text Box from your toolbox and drop it on a form along with either a Grid control or a Grid Data Bound Grid. Finally, in your Form_Load handler, add a call to the GridAwareTextBox.WireGrid to bind the Grid Aware Text Box to the grid. Here are some code samples that will show you how this is done.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [private][ [void] Form1_Load([object] sender, System.[EventArgs] e)] |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [    [// Bind Grid Aware Text Box to grid.]]                                                                                                                      |
|                                                                                                                                                                                                                             |
| [    [this].gridAwareTextBox1.WireGrid([this].gridControl1);]                                                                                 |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private Sub][ Form1_Load(sender][ As Object][, e ][As][ System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Bind Grid Aware Text Box to grid.]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.gridAwareTextBox1.WireGrid(][Me][.gridControl1)]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [End Sub][ ]                                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p529} 

 

[]{#related-topics}

