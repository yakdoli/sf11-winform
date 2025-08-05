---
title: howtosetconditionalformattinginthegroupinggrid.md
original_path: WinForms_Docs/04_Controls/Grid/howtosetconditionalformattinginthegroupinggrid.md
created_at: 2025-08-05
---






#### How to set conditional formatting in the GroupingGrid {#how-to-set-conditional-formatting-in-the-groupinggrid style="tab-stops: 0pt"}

[] 

To set up a conditional formatting in the GroupingGrid, use the following code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| []                                                                                                           |
|                                                                                                                                                                  |
| [// Declaring a conditional format descriptor.]                                                                |
|                                                                                                                                                                  |
| [GridConditionalFormatDescriptor gcfd = [new] GridConditionalFormatDescriptor();]                       |
|                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                  |
| [// Setting some properties]                                                                                   |
|                                                                                                                                                                  |
| [gcfd.Appearance.AnyRecordFieldCell.Font.Bold = [true];]                                                |
|                                                                                                                                                                  |
| [gcfd.Appearance.AnyRecordFieldCell.Interior = [new] BrushInfo(Color.LightGreen);]                      |
|                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                  |
| [//Expression which is applied on the table data.]                                                             |
|                                                                                                                                                                  |
| [gcfd.Expression = [\"\[ColumnName\] like \\\'true\\\'\"];]                                           |
|                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                  |
| [// Setting name to the conditional format and adding it to the grid.]                                         |
|                                                                                                                                                                  |
| [gcfd.Name = [\"gcfd\"];]                                                                             |
|                                                                                                                                                                  |
| [this][.gridGroupingControl1.TableDescriptor.ConditionalFormats.Add(gcfd);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                                            |
| [\' Declaring a conditional format descriptor.]                                                                                                                          |
|                                                                                                                                                                                                                            |
| [Dim][ gcfd [As] GridConditionalFormatDescriptor = [New] GridConditionalFormatDescriptor()] |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [\' Setting some properties]                                                                                                                                             |
|                                                                                                                                                                                                                            |
| [gcfd.Appearance.AnyRecordFieldCell.Font.Bold = [True]]                                                                                                           |
|                                                                                                                                                                                                                            |
| [gcfd.Appearance.AnyRecordFieldCell.Interior = [New] BrushInfo(Color.LightGreen)]                                                                                 |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [\' Expression which is applied on the table data.]                                                                                                                      |
|                                                                                                                                                                                                                            |
| [gcfd.Expression = [\"\[ColumnName\] like \'true\'\"]]                                                                                                          |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                            |
| [\' Setting name to the conditional format and adding it to the grid.]                                                                                                   |
|                                                                                                                                                                                                                            |
| [gcfd.Name = [\"gcfd\"]]                                                                                                                                        |
|                                                                                                                                                                                                                            |
| [Me][.gridGroupingControl1.TableDescriptor.ConditionalFormats.Add(gcfd)]                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p681} 

 

[]{#related-topics}

