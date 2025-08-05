---
title: inserttables.md
original_path: WinForms_Docs/99_Uncategorized/inserttables.md
created_at: 2025-08-05
---






#### Insert Tables {#insert-tables style="tab-stops: 0pt"}

Table support for the RichTextBoxAdv control has been implemented as in MS Word. This is used to insert tables with user-defined rows and columns, and it also allows the user to insert multiple tables for every cell.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  **[\[XAML\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                               |
| [     ]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                               |
| [               \<][syncfusion][:][TableAdv][\>][\ |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [  [                        ][\<][syncfusion][:][TableRowAdv][\>]\                                                                                                     |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [  [                            ][\<][syncfusion][:][TableCellAdv][\>]\                                                                                                |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [  [                                ][\<][syncfusion][:][ParagraphAdv][\>]\                                                                                            |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [  [                                    ][\<][syncfusion][:][SpanAdv][ Text][=\"Table support\"/\>]\                                               |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [  [                                ][\</][syncfusion][:][ParagraphAdv][\>]\                                                                                           |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [  [                            ][\</][syncfusion][:][TableCellAdv][\>]\                                                                                               |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [  [                        ][\</][syncfusion][:][TableRowAdv][\>]\                                                                                                    |
| \                                                                                                                                                                                                                                                                                                             |
| ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                               |
| [  [                    ][\</][syncfusion][:][TableAdv][\>]]                                                                       |
|                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                   |
| **[          ]**[TableAdv][ table = [new] [TableAdv]();] |
|                                                                                                                                                                                                                                   |
| [          [TableRowAdv] row = [new] [TableRowAdv]();]                                                                   |
|                                                                                                                                                                                                                                   |
| [          [TableCellAdv] cell = [new] [TableCellAdv]();]                                                                |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [          [ParagraphAdv] paragraph = [new] [ParagraphAdv]();]                                                           |
|                                                                                                                                                                                                                                   |
| [          [SpanAdv] span = [new] [SpanAdv]();]                                                                          |
|                                                                                                                                                                                                                                   |
| [          span.Text = [\"Table support\"];]                                                                                                                          |
|                                                                                                                                                                                                                                   |
| [          paragraph.Inlines.Add(span);]                                                                                                                                                      |
|                                                                                                                                                                                                                                   |
| [          cell.Blocks.Add(paragraph);]                                                                                                                                                       |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [          row.Cells.Add(cell);]                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [          table.Rows.Add(row);]                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| **[      ]**                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

More:





















