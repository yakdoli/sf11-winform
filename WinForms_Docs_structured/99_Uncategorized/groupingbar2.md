---
title: groupingbar2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\groupingbar2.md
created_at: 2025-07-03
---








  









## Grouping Bar {#grouping-bar style="tab-stops: 0pt"}

The PivotGrid Grouping Bar enables the drag and drop feature of fields between different areas such as column, row, value and filter. By using the Grouping Bar, you can add, rearrange, or remove fields to show data in the PivotGrid exactly the way you want.

The Grouping Bar has field headers that identify fields in the pivot grid. One field header contains:

[·      ]Caption string - identifies the field\'s content

[·      ]Sort indicator -  identifies the sort order applied to the field\'s values

[·      ]Filter button - end-users can use it to filter field values

 

The headers of all visible fields are contained within header areas. The headers of row and column fields are displayed within the row header and column header areas, respectively. The headers of data fields are displayed within the data header area.

[] 

Use Case Scenarios

At times, you may expect the Grid to perform sorting and filtering at run-time.

**[]** 

Adding Grouping Bar

By default, Grouping Bar is enabled. It can be disabled by setting *ShowGroupBar* property of PivotGrid to *False*.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [// Instantiating PivotGridControl][]                                                                                                                                    |
|                                                                                                                                                                                                                                                                |
| [PivotGridControl][ pivotGridControl1 = [new] [PivotGridControl]();]                                                      |
|                                                                                                                                                                                                                                                                |
| [// Adding PivotRows][]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                |
| [pivotGridControl1.PivotRows.Add([new] [PivotItem] { FieldHeader = [\"Product\"] });]                                                                 |
|                                                                                                                                                                                                                                                                |
| [pivotGridControl1.PivotColumns.Add([new] [PivotItem] { FieldHeader = [\"Date\"] });]                                                                 |
|                                                                                                                                                                                                                                                                |
| [// Adding PivotColumns][]                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [pivotGridControl1.PivotColumns.Add([new] [PivotItem] { FieldHeader = [\"Country\"] });]                                                              |
|                                                                                                                                                                                                                                                                |
| [pivotGridControl1.PivotColumns.Add([new] [PivotItem] { FieldHeader = [\"State\"] });]                                                                |
|                                                                                                                                                                                                                                                                |
| [// Adding PivotCalculations][]                                                                                                                                          |
|                                                                                                                                                                                                                                                                |
| [pivotGridControl1.PivotCalculations.Add([new] [PivotComputationInfo] { FieldName=[\"Amount\"] , Format=[\"C\"]});]           |
|                                                                                                                                                                                                                                                                |
| [pivotGridControl1.PivotCalculations.Add([new] [PivotComputationInfo] { FieldName = [\"Quantity\"], Format = [\"#,##0\"] });] |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                            |
|                                                                                                                                                                                                             |
| [\' Instantiating PivotGridControl][]                                                                                 |
|                                                                                                                                                                                                             |
| [Dim][ pivotGridControl1 [As] PivotGridControl = [New] PivotGridControl()]   |
|                                                                                                                                                                                                             |
| [\' Adding PivotRows][]                                                                                               |
|                                                                                                                                                                                                             |
| [pivotGridControl1.PivotRows.Add([New] PivotItem [With] {.FieldHeader = \"Product\"})]                                        |
|                                                                                                                                                                                                             |
| [pivotGridControl1.PivotColumns.Add([New] PivotItem [With] {.FieldHeader = \"Date\"})]                                        |
|                                                                                                                                                                                                             |
| [\' Adding PivotColumns][]                                                                                            |
|                                                                                                                                                                                                             |
| [pivotGridControl1.PivotColumns.Add([New] PivotItem [With] {.FieldHeader = \"Country\"})]                                     |
|                                                                                                                                                                                                             |
| [pivotGridControl1.PivotColumns.Add([New] PivotItem [With] {.FieldHeader = \"State\"})]                                       |
|                                                                                                                                                                                                             |
| [\' Adding PivotCalculations][]                                                                                       |
|                                                                                                                                                                                                             |
| [pivotGridControl1.PivotCalculations.Add([New] PivotComputationInfo [With] {.FieldName=\"Amount\", .Format=\"C\"})]           |
|                                                                                                                                                                                                             |
| [pivotGridControl1.PivotCalculations.Add([New] PivotComputationInfo [With] {.FieldName = \"Quantity\", .Format = \"#,##0\"})] |
|                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 10: PivotGrid Grouping Bar

More:







