---
title: howtohidethenumberedrowandcolumnheaderswhileprintingorprintpreviewingingridcontrol.md
original_path: WinForms_Docs/04_Controls/Grid/howtohidethenumberedrowandcolumnheaderswhileprintingorprintpreviewingingridcontrol.md
created_at: 2025-08-05
---








  









### How to hide the numbered row and column headers while printing or print previewing in GridControl {#how-to-hide-the-numbered-row-and-column-headers-while-printing-or-print-previewing-in-gridcontrol style="tab-stops: 0pt"}

[] 

You have to set the **PrintRowHeader** and **PrintColHeader** properties to *False,* to hide the row and column headers while printing or print previewing in GridControl.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [private][ [void] button2_Click([object] sender, [EventArgs] e)]                                        |
|                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [this][.gridControl1.Model.Properties.PrintRowHeader = [false];]                                                                                  |
|                                                                                                                                                                                                                                                             |
| [this][.gridControl1.Model.Properties.PrintColHeader = [false];]                                                                                  |
|                                                                                                                                                                                                                                                             |
| [if][ ([this].gridControl1 != [null])]                                                                                       |
|                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [try]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [GridPrintDocument][ pd = [new] [GridPrintDocument]([this].gridControl1, [true]);] |
|                                                                                                                                                                                                                                                             |
| [PrintDialog][ dlg = [new] [PrintDialog]();]                                                                                 |
|                                                                                                                                                                                                                                                             |
| [dlg.Document = pd;]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [if][ (dlg.ShowDialog() == [DialogResult].OK)]                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [pd.Print();]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [catch][ ([Exception] ex)]                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [MessageBox][.Show([\"An error occurred attempting to print the grid - \"] + ex.Message);]                                                      |
|                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] button2_Click([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs) [Handles] button2.Click] |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Me][.gridControl1.Model.Properties.PrintRowHeader = [False]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Me][.gridControl1.Model.Properties.PrintColHeader = [False]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                         |
| [If][ [Me].gridControl1 [IsNot] [Nothing] [Then]]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Try]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ pd [As] GridPrintDocument = [New] GridPrintDocument([Me].gridControl1, [True])]                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ dlg [As] PrintDialog = [New] PrintDialog()]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                         |
| [dlg.Document = pd]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                         |
| [If][ dlg.ShowDialog() = System.Windows.Forms.DialogResult.OK [Then]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                         |
| [pd.Print()]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [If]]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                         |
| [Catch][ ex [As] Exception]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                         |
| [MessageBox.Show([\"An error occurred attempting to print the grid - \"] & ex.Message)]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Try]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [If]]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p557} 

 

[]{#related-topics}

