---
title: creatingolapdatamanagerincontrollerandpassingittoview.md
original_path: WinForms_Docs/03_Data_Binding/creatingolapdatamanagerincontrollerandpassingittoview.md
created_at: 2025-08-05
---








  









### Creating OlapDataManager in Controller and Passing it to View {#creating-olapdatamanager-in-controller-and-passing-it-to-view style="tab-stops: 0pt"}

 

To create OLAP DataManager in Controller and pass it to View:

1.   Add the following code in the HomeController:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[CS\]]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                 |
| [private][ [OlapDataManager] GetOlapDataManger([bool] isGetRequest)]                                                                                |
|                                                                                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [            [var] manager = [new] [OlapDataManager]([this].GetConnectionString());]                                                                                    |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [            [if] (isGetRequest)]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                 |
| [                manager.SetCurrentReport(CreateOlapReport());]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [            [return] manager;]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [        [private] [OlapReport] CreateOlapReport()]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                 |
| [            [OlapReport] olapReport = [new] [OlapReport]();]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [            olapReport.CurrentCubeName = [\"Adventure Works\"];]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [            [DimensionElement] dimensionElement = [new] [DimensionElement]() { Name = [\"Customer\"], HierarchyName = [\"Customer\"] };] |
|                                                                                                                                                                                                                                                                                                                 |
| [            dimensionElement.AddLevel([\"Customer Geography\"], [\"Country\"]);]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                 |
| [            olapReport.SeriesElements.Add(dimensionElement);]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [            dimensionElement = [new] [DimensionElement]() { Name = [\"Date\"] };]                                                                                                        |
|                                                                                                                                                                                                                                                                                                                 |
| [            dimensionElement.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                 |
| [            olapReport.CategoricalElements.Add(dimensionElement);]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [            [MeasureElements] measureElementColumn = [new] [MeasureElements]();]                                                                                                         |
|                                                                                                                                                                                                                                                                                                                 |
| [            measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Internet Sales Amount\"] });]                                                                           |
|                                                                                                                                                                                                                                                                                                                 |
| [            olapReport.CategoricalElements.Add(measureElementColumn);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [            [return] olapReport;]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Run the application.

 

[] 

**[4.3 Appearance and][ [Structure of the Control]]**

The appearance and structure of the control is displayed in the screenshot below:

{border="0"}

[]{#related-topics}

