---
title: populatingdatatopivotgrid.md
original_path: WinForms_Docs/04_Controls/Grid/populatingdatatopivotgrid.md
created_at: 2025-08-05
---








  









### Populating Data to PivotGrid {#populating-data-to-pivotgrid style="tab-stops: 0pt"}

 

PivotGrid requires the following information in order to populate data.

[·      ]**ItemSource** - The data source for the pivot table. This object should be either an IEnumerable list or a DataTable.

[·      ]**PivotRows** - Elements that need to be added in PivotGrid rows.

[·      ]**PivotColumns** - Elements that need to be added in PivotGrid columns.

[·      ]**PivotCalculations** - Calculation values that appear as value cells in PivotGrid.

 

Refer to  for more information.

To populate a **PivotGrid** with the sample IList data, refer to the code below.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [protected][ [void] MainPage_Loaded([object] sender, [RoutedEventArgs] e)]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [// Specifying the ItemSource for Pivot Grid.]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [            [this].PivotGridControl1.ItemSource = [ProductSales].GetSalesData();]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [            [// Adding Pivot Rows to Grid.]]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [            [this].PivotGridControl1.PivotRows.Add([new] [PivotItem] { FieldMappingName = [\"Product\"], TotalHeader = [\"Total\"] });]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [            [this].PivotGridControl1.PivotRows.Add([new] [PivotItem] { FieldMappingName = [\"Year\"], TotalHeader = [\"Total\"] });]                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [            [// Adding Pivot Colums to Grid.]]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [            [this].PivotGridControl1.PivotColumns.Add([new] [PivotItem] { FieldMappingName = [\"Country\"], TotalHeader = [\"Total\"] });]                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [            [this].PivotGridControl1.PivotColumns.Add([new] [PivotItem] { FieldMappingName = [\"State\"], TotalHeader = [\"Total\"] });]                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [            [// Adding PivotCalculations to Grid.]]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [            [this].PivotGridControl1.PivotCalculations.Add([new] [PivotComputationInfo] { FieldName = [\"Amount\"],Format=[\"C\"] , SummaryType = [SummaryType].DoubleTotalSum });] |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [            [this].PivotGridControl1.PivotCalculations.Add([new] [PivotComputationInfo] { FieldName = [\"Quantity\"], Format =[\"#,##0\"]});]                                                               |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [            [this].PivotGridControl1.Refresh();]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [Protected][ [Sub] MainPage_Loaded([ByVal] sender [As] [Object], [ByVal] e [As] RoutedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                      |
| [\' Specifying the ItemSource for Pivot Grid.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                      |
| [                  [Me].PivotGridControl1.ItemSource = ProductSales.GetSalesData()]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                      |
| [                  [\' Adding Pivot Rows to Grid.]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                      |
| [                  [Me].PivotGridControl1.PivotRows.Add([New] PivotItem [With] {.FieldMappingName = \"Product\", .TotalHeader = \"Total\"})]                                                                      |
|                                                                                                                                                                                                                                                                                                                      |
| [                  [Me].PivotGridControl1.PivotRows.Add([New] PivotItem [With] {.FieldMappingName = \"Year\", .TotalHeader = \"Total\"})]                                                                         |
|                                                                                                                                                                                                                                                                                                                      |
| [                  [\' Adding Pivot Colums to Grid.]]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                      |
| [                  [Me].PivotGridControl1.PivotColumns.Add([New] PivotItem [With] {.FieldMappingName = \"Country\", .TotalHeader = \"Total\"})]                                                                   |
|                                                                                                                                                                                                                                                                                                                      |
| [                  [Me].PivotGridControl1.PivotColumns.Add([New] PivotItem [With] {.FieldMappingName = \"State\", .TotalHeader = \"Total\"})]                                                                     |
|                                                                                                                                                                                                                                                                                                                      |
| [                  [\' Adding PivotCalculations to Grid.]]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                      |
| [                  [Me].PivotGridControl1.PivotCalculations.Add([New] PivotComputationInfo [With] {.FieldName = \"Amount\", .Format=\"C\", .SummaryType = SummaryType.DoubleTotalSum})]                           |
|                                                                                                                                                                                                                                                                                                                      |
| [                  [Me].PivotGridControl1.PivotCalculations.Add([New] PivotComputationInfo [With] {.FieldName = \"Quantity\", .Format =\"#,##0\"})]                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [                   [Me].PivotGridControl1.Refresh()]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the above code runs, the following output will be generated.

 

{border="0"}

Figure 8: PivotGrid Control loaded with IList Data

 

 

[]{#related-topics}

