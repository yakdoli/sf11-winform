---
title: columnspan.md
original_path: WinForms_Docs/99_Uncategorized/columnspan.md
created_at: 2025-08-05
---








  









### Column Span {#column-span style="tab-stops: 0pt"}

[] 

GridGroupingControl allows the user to span a column across multiple grid rows or columns. This is possible through the GridColumnSpanDescriptor, which provides information about a column that can span multiple grid rows or columns.

[] 

Creating Column Span

**[]** 

Through Designer

[] 

**GridColumnSpanDescriptor[ ]**Collection Editor is used to span the columns, which are returned by the **ColumnSets** property from the TableDescriptor.

[] 

{border="0"}

Figure 52

[] 

Through Code

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                |
| [GridColumnSetDescriptor][ gridColumnSetDescriptor1 = [new] [GridColumnSetDescriptor]();]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                |
| [// Add columns and specify span behavior]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                |
| [gridColumnSetDescriptor1.ColumnSpans.AddRange([new] [GridColumnSpanDescriptor]\[\] { [new]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                |
| [GridColumnSpanDescriptor][([\"FirstName\"], [\"R0C0\"]),[new] [GridColumnSpanDescriptor]([\"LastName\"], [\"R1C1\"])});] |
|                                                                                                                                                                                                                                                                                                                                                                |
| [// Add GridColumnDescriptor to the GridGroupingControl]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                |
| [this][.GridGroupingControl1.TableDescriptor.ColumnSets.AddRange([new] [GridColumnSetDescriptor]\[\] {gridColumnSetDescriptor1});]                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Dim][ gridColumnSetDescriptor1 [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridColumnSetDescriptor = [New] GridColumnSetDescriptor()]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\' Add columns and specify span behavior]                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [gridColumnSetDescriptor1.ColumnSpans.AddRange([New] GridColumnSpanDescriptor() { [New] GridColumnSpanDescriptor([\"FirstName\"], [\"R0C0\"]),[New] GridColumnSpanDescriptor([\"LastName\"], [\"R1C1\"])})] |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\' Add GridColumnDescriptor to the GridGroupingControl]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Me][.GridGroupingControl1.TableDescriptor.ColumnSets.AddRange([New] GridColumnSetDescriptor() {gridColumnSetDescriptor1})]                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 53

[]{#p41} 

[]{#related-topics}

