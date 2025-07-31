---
title: totalsummary.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\totalsummary.md
created_at: 2025-07-03
---








  









### Total Summary {#total-summary style="tab-stops: 0pt"}

[] 

Summaries can be created in the following two ways.

[] 

[·      ]Though Designer

[·      ]Through Code

[] 

Through Designer

[] 

This section deals with creation of summaries through the designer.

**[]** 

[·      ]**GridSummaryRowDescriptor[ ]**Collection Editor is used to add summary rows to the Grid control.

[] 

{border="0"}

Figure 98

[] 

[·      ]On the same window, clicking on the \"SummaryColumns\" field will open the **SummaryColumnDescriptor** Collection Editor, for adding Summary Columns to the selected Summary Row.

[] 

{border="0"}

Figure 99

[] 

The following properties can be set for the Summary Rows by using the SummaryColumnDescriptor Collection Editor.

[] 


+-------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Properties in GridSummaryColumnDescriptor Collection Editor | Description                                                                       |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Format                                                      | Specifies the format for the summary column. The options included are as follows: |
|                                                             |                                                                                   |
|                                                             |                                                                                   |
|                                                             |                                                                                   |
|                                                             | [·      ]Maximum                                     |
|                                                             |                                                                                   |
|                                                             | [·      ]Average                                     |
|                                                             |                                                                                   |
|                                                             | [·      ]Minimum                                     |
|                                                             |                                                                                   |
|                                                             | [·      ]Sum                                         |
|                                                             |                                                                                   |
|                                                             | [·      ]Count                                       |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Style                                                       | Specifies the style. The options included are as follows:                         |
|                                                             |                                                                                   |
|                                                             |                                                                                   |
|                                                             |                                                                                   |
|                                                             | [·      ]Hidden                                      |
|                                                             |                                                                                   |
|                                                             | [·      ]FillRow                                     |
|                                                             |                                                                                   |
|                                                             | [·      ]Column                                      |
|                                                             |                                                                                   |
|                                                             |                                                                                   |
|                                                             |                                                                                   |
|                                                             | The default value is FillRow.                                                     |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Appearance                                                  | Specifies the appearance of the column.                                           |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+
| SummaryType                                                 | Specifies the summary type. The options included are as follows:                  |
|                                                             |                                                                                   |
|                                                             | [·      ]Count                                       |
|                                                             |                                                                                   |
|                                                             | [·      ]BooleanAggregate                            |
|                                                             |                                                                                   |
|                                                             | [·      ]ByteAggregate                               |
|                                                             |                                                                                   |
|                                                             | [·      ]CharAggregate                               |
|                                                             |                                                                                   |
|                                                             | [·      ]DoubleAggregate                             |
|                                                             |                                                                                   |
|                                                             | [·      ]Int32Aggregate                              |
|                                                             |                                                                                   |
|                                                             | [·      ]StringAggregate                             |
|                                                             |                                                                                   |
|                                                             | [·      ]MaxLength                                   |
|                                                             |                                                                                   |
|                                                             | [·      ]Vector                                      |
|                                                             |                                                                                   |
|                                                             | [·      ]DoubleVector                                |
|                                                             |                                                                                   |
|                                                             | [·      ]Custom                                      |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+
| DataMember                                                  | Specifies the data member for which you want to display the summary.              |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+
| DisplayColumn                                               | Specifies the column to be displayed.                                             |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+
| IgnoreRecordFilter                                          | Specifies whether to ignore the record filter.                                    |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+


[] 

Through Code

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                              |
| [GridSummaryColumnDescriptor][ scd = [new] [GridSummaryColumnDescriptor]();]                                                                                                  |
|                                                                                                                                                                                                                                                                                                              |
| [scd.Name = [\"SummaryColumn\"];]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                              |
| [scd.DataMember = [\"Col1\"];]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                              |
| [scd.DisplayColumn = [\"Col1\"];]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                              |
| [scd.Format = [\"{Sum:#}\"];]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                              |
| [scd.SummaryType = SummaryType.Int32Aggregate;]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                              |
| [this][.GridGroupingControl1.TableDescriptor.SummaryRows.Add([new] [GridSummaryRowDescriptor]([\"Row 1\"], [\"Total\"], scd));] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [Dim][ scd [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridSummaryColumnDescriptor = [New] GridSummaryColumnDescriptor()]                     |
|                                                                                                                                                                                                                                                                                   |
| [scd.Name = [\"SummaryColumn\"]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                   |
| [scd.DataMember = [\"Col1\"]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                   |
| [scd.DisplayColumn = [\"Col1\"]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                   |
| [scd.Format = [\"{Sum:#}\"]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [scd.SummaryType = SummaryType.Int32Aggregate]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                   |
| [Me][.GridGroupingControl1.TableDescriptor.SummaryRows.Add([New] GridSummaryRowDescriptor([\"Row 1\"],[\"Total\"], scd))] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p77} 

[]{#related-topics}

