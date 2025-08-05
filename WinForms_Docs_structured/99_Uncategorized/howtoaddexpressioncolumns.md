---
title: howtoaddexpressioncolumns.md
original_path: WinForms_Docs/99_Uncategorized/howtoaddexpressioncolumns.md
created_at: 2025-08-05
---






#### How to add Expression columns {#how-to-add-expression-columns style="tab-stops: 0pt"}

[] 

Expression fields allows you to add a column that holds calculated values based on other fields in the same record. These expression columns can be used in grouping and sorting. This also can be employed as summary fields for summary rows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                                       |
| []                                                                                                                  |
|                                                                                                                                                                       |
| [using][  Syncfusion.Grouping;]                                                  |
|                                                                                                                                                                       |
| [using][  Syncfusion.Windows.Forms.Grid;]                                        |
|                                                                                                                                                                       |
| [using][  Syncfusion.Windows.Forms.Grid.Grouping;]                               |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [// Declare an ExpressionFieldDescriptor]                                                                           |
|                                                                                                                                                                       |
| [ExpressionFieldDescriptor expression1 = [new] ExpressionFieldDescriptor();]                                 |
|                                                                                                                                                                       |
| [expression1.Name = [\"Sum of all columns\"];]                                                             |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [// Simple expression to add the values in the columns ]                                                            |
|                                                                                                                                                                       |
| [// For all the valid Expression syntax, refer the ]                                                                |
|                                                                                                                                                                       |
| [// EssentialGrid UserGuide \--\> Essential Grid Tutorials \-\--\> ]                                                |
|                                                                                                                                                                       |
| [//Adding Expression Fields \-\--\> Valid Expression Syntax ]                                                       |
|                                                                                                                                                                       |
| [expression1.Expression = [\"\[Col0\] + \[Col1\] + \[Col2\] + \[Col3\]\"];]                                |
|                                                                                                                                                                       |
| [            ]                                                                                                                    |
|                                                                                                                                                                       |
| [//Add the Expression column to the grid]                                                                           |
|                                                                                                                                                                       |
| [this][.gridGroupingControl1.TableDescriptor.ExpressionFields.Add(expression1);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                                           |
| [Imports][ Syncfusion.Grouping]                                                                      |
|                                                                                                                                                                                           |
| [Imports][ Syncfusion.Windows.Forms.Grid]                                                            |
|                                                                                                                                                                                           |
| [Imports][ Syncfusion.Windows.Forms.Grid.Grouping]                                                   |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [\' Declare an ExpressionFieldDescriptor]                                                                                               |
|                                                                                                                                                                                           |
| [Dim][ expression1 [As] [New] ExpressionFieldDescriptor()] |
|                                                                                                                                                                                           |
| [expression1.Name = [\"Sum of all columns\"]]                                                                                  |
|                                                                                                                                                                                           |
| []                                                                                                                                     |
|                                                                                                                                                                                           |
| [\' Simple expression to add the values in the columns ]                                                                                |
|                                                                                                                                                                                           |
| [\' For all the valid Expression syntax, refer the ]                                                                                    |
|                                                                                                                                                                                           |
| [\' EssentialGrid UserGuide \--\> Essential Grid Tutorials \-\--\> ]                                                                    |
|                                                                                                                                                                                           |
| [\' Adding Expression Fields \-\--\> Valid Expression Syntax ]                                                                          |
|                                                                                                                                                                                           |
| [expression1.Expression = [\"\[Col0\] + \[Col1\] + \[Col2\] + \[Col3\]\"]]                                                     |
|                                                                                                                                                                                           |
| []                                                                                                                                     |
|                                                                                                                                                                                           |
| [\'Add the Expression column to the grid]                                                                                               |
|                                                                                                                                                                                           |
| [Me][.gridGroupingControl1.TableDescriptor.ExpressionFields.Add(expression1)]                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p687} 

 

[]{#related-topics}

