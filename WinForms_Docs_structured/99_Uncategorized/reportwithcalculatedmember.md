---
title: reportwithcalculatedmember.md
original_path: WinForms_Docs/99_Uncategorized/reportwithcalculatedmember.md
created_at: 2025-08-05
---






##### Report with calculated member {#report-with-calculated-member style="tab-stops: 0pt"}

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [olapReport.CurrentCubeName = [\"Adventure Works\"];\                                                                                                                 |
|  \                                                                                                                                                                                            |
| [DimensionElement] dimensionElementColumn = [new] [DimensionElement]();\                                                 |
| [//Specifying the Name for the Dimension Element]\                                                                                                                      |
| dimensionElementColumn.Name = [\"Customer\"];\                                                                                                                        |
| dimensionElementColumn.HierarchyName = [\"Customer Geography\"];\                                                                                                     |
| dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"]);\                                                                    |
|  \                                                                                                                                                                                            |
| [DimensionElement] internalDimension = [new] [DimensionElement]();\                                                      |
| internalDimension.Name = [\"Product\"];\                                                                                                                              |
| internalDimension.AddLevel([\"Product Categories\"], [\"Category\"]);\                                                                        |
|  \                                                                                                                                                                                            |
| [//// Calculated Measure]\                                                                                                                                              |
| [CalculatedMember] calculatedMeasure1 = [new] [CalculatedMember]();\                                                     |
| calculatedMeasure1.Name = [\"Oder on Discount\"];\                                                                                                                    |
| calculatedMeasure1.Expression = [\"\[Measures\].\[Order Quantity\] + (\[Measures\].\[Order Quantity\] \* 0.10)\"];\                                                   |
| calculatedMeasure1.AddElement([new] [MeasureElement] { Name = [\"Order Quantity\"] }); \                                 |
|  \                                                                                                                                                                                            |
| [//// Calculated Measure]\                                                                                                                                              |
| [CalculatedMember] calculatedMeasure2 = [new] [CalculatedMember]();\                                                     |
| calculatedMeasure2.Name = [\"Sales Range\"];\                                                                                                                         |
| calculatedMeasure2.AddElement([new] [MeasureElement] { Name = [\"Sales Amount\"] });\                                    |
| calculatedMeasure2.Expression = [\"IIF(\[Measures\].\[Sales Amount\]\>200000,\\\"High\\\",\\\"Low\\\")\"];\                                                           |
|  \                                                                                                                                                                                            |
| [// Calculated Dimension]\                                                                                                                                              |
| [CalculatedMember] calculateDimension = [new] [CalculatedMember]();\                                                     |
| calculateDimension.Name = [\"Bikes & Components\"];\                                                                                                                  |
| calculateDimension.Expression = [\"(\[Product\].\[Product Categories\].\[Category\].\[Bikes\] + \[Product\].\[Product Categories\].\[Category\].\[Components\] )\"];\ |
| calculateDimension.AddElement(internalDimension);\                                                                                                                                            |
|  \                                                                                                                                                                                            |
| [MeasureElements] measureElementColumn = [new] [MeasureElements]();\                                                     |
| measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Sales Amount\"] });\                                |
| measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Order Quantity\"] });\                              |
|  \                                                                                                                                                                                            |
| [DimensionElement] dimensionElementRow = [new] [DimensionElement]();\                                                    |
| [//Specifying the Dimension Name]\                                                                                                                                      |
| dimensionElementRow.Name = [\"Date\"];\                                                                                                                               |
| dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);\                                                                               |
|  \                                                                                                                                                                                            |
|  \                                                                                                                                                                                            |
| [//// Adding Calculated members in calculated member collection]\                                                                                                       |
| olapReport.CalculatedMembers.Add(calculatedMeasure1);\                                                                                                                                        |
| olapReport.CalculatedMembers.Add(calculateDimension);\                                                                                                                                        |
| olapReport.CalculatedMembers.Add(calculatedMeasure2);\                                                                                                                                        |
|  \                                                                                                                                                                                            |
| [///][ Adding Column Members]\                                                                                                                     |
| olapReport.CategoricalElements.Add(dimensionElementColumn);\                                                                                                                                  |
| olapReport.CategoricalElements.Add(calculateDimension);\                                                                                                                                      |
| [///][Adding Measure Element]\                                                                                                                     |
| olapReport.CategoricalElements.Add(measureElementColumn);\                                                                                                                                    |
| olapReport.CategoricalElements.Add(calculatedMeasure1);\                                                                                                                                      |
| olapReport.CategoricalElements.Add(calculatedMeasure2);\                                                                                                                                      |
|  \                                                                                                                                                                                            |
| [///][Adding Row Members]\                                                                                                                         |
| olapReport.SeriesElements.Add(dimensionElementRow);]                                                                                                      |
|                                                                                                                                                                                               |
| [                               ]                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [Dim][ dimensionElementColumn [As] DimensionElement = [New] DimensionElement()] |
|                                                                                                                                                                                                                |
| [\'Specifying the Name for the Dimension Element][]                                                                      |
|                                                                                                                                                                                                                |
| [dimensionElementColumn.Name = \"Customer\"]                                                                                                                               |
|                                                                                                                                                                                                                |
| [dimensionElementColumn.HierarchyName = \"Customer Geography\"]                                                                                                            |
|                                                                                                                                                                                                                |
| [dimensionElementColumn.AddLevel(\"Customer Geography\", \"Country\")]                                                                                                     |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [Dim][ internalDimension [As] DimensionElement = [New] DimensionElement()]      |
|                                                                                                                                                                                                                |
| [internalDimension.Name = \"Product\"]                                                                                                                                     |
|                                                                                                                                                                                                                |
| [internalDimension.AddLevel(\"Product Categories\", \"Category\")]                                                                                                         |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\'// Calculated Measure][]                                                                                              |
|                                                                                                                                                                                                                |
| [Dim][ calculatedMeasure1 [As] CalculatedMember = [New] CalculatedMember()]     |
|                                                                                                                                                                                                                |
| [calculatedMeasure1.Name = \"Oder on Discount\"]                                                                                                                           |
|                                                                                                                                                                                                                |
| [calculatedMeasure1.Expression = \"\[Measures\].\[Order Quantity\] + (\[Measures\].\[Order Quantity\] \* 0.10)\"]                                                          |
|                                                                                                                                                                                                                |
| [calculatedMeasure1.AddElement([New] MeasureElement [With] {.Name = \"Order Quantity\"})]                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\'// Calculated Measure][]                                                                                              |
|                                                                                                                                                                                                                |
| [Dim][ calculatedMeasure2 [As] CalculatedMember = [New] CalculatedMember()]     |
|                                                                                                                                                                                                                |
| [calculatedMeasure2.Name = \"Sales Range\"]                                                                                                                                |
|                                                                                                                                                                                                                |
| [calculatedMeasure2.AddElement([New] MeasureElement [With] {.Name = \"Sales Amount\"})]                                          |
|                                                                                                                                                                                                                |
| [calculatedMeasure2.Expression = \"IIF(\[Measures\].\[Sales Amount\]\>200000,\"\"High\"\",\"\"Low\"\")\"]                                                                  |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\' Calculated Dimension][]                                                                                              |
|                                                                                                                                                                                                                |
| [Dim][ calculateDimension [As] CalculatedMember = [New] CalculatedMember()]     |
|                                                                                                                                                                                                                |
| [calculateDimension.Name = \"Bikes & Components\"]                                                                                                                         |
|                                                                                                                                                                                                                |
| [calculateDimension.Expression = \"(\[Product\].\[Product Categories\].\[Category\].\[Bikes\] + \[Product\].\[Product Categories\].\[Category\].\[Components\] )\"]        |
|                                                                                                                                                                                                                |
| [calculateDimension.AddElement(internalDimension)]                                                                                                                         |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [Dim][ measureElementColumn [As] MeasureElements = [New] MeasureElements()]     |
|                                                                                                                                                                                                                |
| [measureElementColumn.Elements.Add([New] MeasureElement [With] {.Name = \"Sales Amount\"})]                                      |
|                                                                                                                                                                                                                |
| [measureElementColumn.Elements.Add([New] MeasureElement [With] {.Name = \"Order Quantity\"})]                                    |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [Dim][ dimensionElementRow [As] DimensionElement = [New] DimensionElement()]    |
|                                                                                                                                                                                                                |
| [\'Specifying the Dimension Name][]                                                                                      |
|                                                                                                                                                                                                                |
| [dimensionElementRow.Name = \"Date\"]                                                                                                                                      |
|                                                                                                                                                                                                                |
| [dimensionElementRow.AddLevel(\"Fiscal\", \"Fiscal Year\")]                                                                                                                |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\'// Adding Calculated members in calculated member collection][]                                                       |
|                                                                                                                                                                                                                |
| [olapReport.CalculatedMembers.Add(calculatedMeasure1)]                                                                                                                     |
|                                                                                                                                                                                                                |
| [olapReport.CalculatedMembers.Add(calculateDimension)]                                                                                                                     |
|                                                                                                                                                                                                                |
| [olapReport.CalculatedMembers.Add(calculatedMeasure2)]                                                                                                                     |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\'\'\' Adding Column Members][]                                                                                         |
|                                                                                                                                                                                                                |
| [olapReport.CategoricalElements.Add(dimensionElementColumn)]                                                                                                               |
|                                                                                                                                                                                                                |
| [olapReport.CategoricalElements.Add(calculateDimension)]                                                                                                                   |
|                                                                                                                                                                                                                |
| [\'\'\'Adding Measure Element][]                                                                                         |
|                                                                                                                                                                                                                |
| [olapReport.CategoricalElements.Add(measureElementColumn)]                                                                                                                 |
|                                                                                                                                                                                                                |
| [olapReport.CategoricalElements.Add(calculatedMeasure1)]                                                                                                                   |
|                                                                                                                                                                                                                |
| [olapReport.CategoricalElements.Add(calculatedMeasure2)]                                                                                                                   |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\'\'\'Adding Row Members][]                                                                                             |
|                                                                                                                                                                                                                |
| [olapReport.SeriesElements.Add(dimensionElementRow)]                                                                                                                       |
|                                                                                                                                                                                                                |
| [                                              ]                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

