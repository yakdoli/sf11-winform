---
title: expressionfield.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\expressionfield.md
created_at: 2025-07-03
---








  









### Expression Field {#expression-field style="tab-stops: 0pt"}

[] 

Generally, Expressions are variables, functions, or some combination of these. You can create such columns in the GridGroupingControl.

Expression Fields allows the user to add new columns with Excel-like formula expressions. These expressions use values in other bound fields like variables.

[] 

Creating Expression Fields

**[]** 

Through Designer

[] 

**GridExpressionFieldDescriptor** Collection Editor is used to add Expression Fields to the GridGroupingControl. This Collection Editor can be viewed by clicking on the **GridExpressionFields** property from the TableDescriptor.

[] 

{border="0"}

Figure 48

[] 

This will add an additional field with the name \"Expr 1\" and the values will be calculated using the expression \"\[Col2\] + 500\". Here \"Col2\", another bound field, is used as a variable of the expression.

[] 

Through Code

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| [GridExpressionFieldDescriptor][ efd = [new] [GridExpressionFieldDescriptor]();] |
|                                                                                                                                                                                                                       |
| [efd.Expression = [\" \[Col2\]+ 500\"];]                                                                                                                  |
|                                                                                                                                                                                                                       |
| [efd.Name = [\"Expr1\"];]                                                                                                                                 |
|                                                                                                                                                                                                                       |
| [// Adding Expression fields to the collection]                                                                                                                     |
|                                                                                                                                                                                                                       |
| [this][.GridGroupingControl1.TableDescriptor.ExpressionFields.Add(efd);]                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [\' Adds an expression property that adds 500 to column Salary   ]                                                                                                                                              |
|                                                                                                                                                                                                                                                                   |
| [Dim][ efd [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridExpressionFieldDescriptor = [New] GridExpressionFieldDescriptor()] |
|                                                                                                                                                                                                                                                                   |
| [efd.Expression = [\" \[Col2\]+ 500\"]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                   |
| [efd.Name = [\"Expr1\"]]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [\' Adding Expression fields to the collection]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                   |
| [Me][.GridGroupingControl1.TableDescriptor.ExpressionFields.Add(efd)]                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 49

[]{#p37} 

More:







