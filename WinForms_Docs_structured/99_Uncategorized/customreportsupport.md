---
title: customreportsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customreportsupport.md
created_at: 2025-07-03
---








  









## Custom Report Support {#custom-report-support style="tab-stops: 0pt"}

OLAP Client allows you to view your own report created using the report creation Application Programming Interfaces (APIs). There are two ways to view custom report in OLAP client:

 

You can view the custom report by binding it to the OlapDataManager before assigning the OlapDataManager to the OlapClient's OlapDataManager property.

You can also use AddCustomReport method of OlapClient to view the custom report. This method will get the report and add it to the current session's report list and set the newly added report as the current report.

Code snippet

Binding Custom Report

 

+------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                         |
|                                                                                          |
| [//// Initializing OlapDataManager]                  |
|                                                                                          |
| [OlapDataManager OlapDataManager = new OlapDataManager();\                               |
| OlapDataManager.DataProvider = this.DataProvider;\                                       |
|  \                                                                                       |
|  //// Binding Custom Report with OlapDataManager\                                        |
|  OlapDataManager.SetCurrentReport(CreateOlapReport());\                                  |
|  this.OlapClient.OlapDataManager = OlapDataManager;] |
|                                                                                          |
| []                                                   |
+------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                     |
|                                                                                                      |
| [\'Initializing OlapDataManager]                                 |
|                                                                                                      |
| [Dim OlapDataManager As OlapDataManager = New OlapDataManager()] |
|                                                                                                      |
| [OlapDataManager.DataProvider = Me.DataProvider]                 |
|                                                                                                      |
| []                                                               |
|                                                                                                      |
| [ \'Binding Custom Report with OlapDataManager]                  |
|                                                                                                      |
| [ OlapDataManager.SetCurrentReport(CreateOlapReport())]          |
|                                                                                                      |
| [ Me.OlapClient.OlapDataManager = OlapDataManager]               |
+------------------------------------------------------------------------------------------------------+

 

Adding Custom Report

 

+------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                            |
| [//// To add custom report\                                                                                |
| this.OlapClient.AddCustomReport(\"SalesReport\", CreateOlapReport());] |
|                                                                                                            |
| []                                                                     |
+------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                         |
|                                                                                                          |
| [\'To add custom report]                                             |
|                                                                                                          |
| [Me.OlapClient.AddCustomReport(\"SalesReport\", CreateOlapReport())] |
+----------------------------------------------------------------------------------------------------------+

 

Custom Report

 

+------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                     |
|                                                                                                      |
| [        /// \<summary\>\                                                                            |
|         /// Creates an olap report.\                                                                 |
|         /// \</summary\>\                                                                            |
|         /// \<returns\>\</returns\>\                                                                 |
|         private Syncfusion.OlapSilverlight.Reports.OlapReport CreateOlapReport()\                    |
|         {\                                                                                           |
|             OlapReport olapReport = new OlapReport();\                                               |
|             olapReport.Name = \"Sales Report\";\                                                     |
|             olapReport.CurrentCubeName = \"Adventure Works\";\                                       |
|  \                                                                                                   |
|             DimensionElement dimensionElementColumn = new DimensionElement();\                       |
|             //Specifying the Name for the Dimension Element\                                         |
|             dimensionElementColumn.Name = \"Date\";\                                                 |
|             //Adding the level elemnet along with the Hierarchy Name\                                |
|             dimensionElementColumn.AddLevel(\"Fiscal\", \"Fiscal Year\");\                           |
|  \                                                                                                   |
|             DimensionElement dimensionElementRow = new DimensionElement();\                          |
|             //Specifying the Name for the Dimension Element\                                         |
|             dimensionElementRow.Name = \"Customer\";\                                                |
|             //Adding the level elemnet along with the Hierarchy Name\                                |
|             dimensionElementRow.AddLevel(\"Customer Geography\", \"Country\");\                      |
|  \                                                                                                   |
|             //// Creating a Measure element\                                                         |
|             MeasureElements measureElement = new MeasureElements();\                                 |
|             measureElement.Elements.Add(new MeasureElement { Name = \"Internet Sales Amount\" });\   |
|  \                                                                                                   |
|             ////Adding Diemnsion element to categorical axis\                                        |
|             olapReport.CategoricalElements.Add(new Item { ElementValue = dimensionElementColumn });\ |
|  \                                                                                                   |
|             ////Adding Measure element to categorical axis\                                          |
|             olapReport.CategoricalElements.Add(new Item { ElementValue = measureElement });\         |
|  \                                                                                                   |
|             ///Adding Dimenions element to series axis\                                              |
|             olapReport.SeriesElements.Add(new Item { ElementValue = dimensionElementRow });\         |
|  \                                                                                                   |
|             return olapReport;\                                                                      |
|         }]                                                       |
|                                                                                                      |
| []                                                               |
+------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                   |
|                                                                                                                                                    |
| [            \'\'\' \<summary\>]                                                                               |
|                                                                                                                                                    |
| [            \'\'\' Creates an olap report.]                                                                   |
|                                                                                                                                                    |
| [            \'\'\' \</summary\>]                                                                              |
|                                                                                                                                                    |
| [            \'\'\' \<returns\>\</returns\>]                                                                   |
|                                                                                                                                                    |
| [            Private Function CreateOlapReport() As Syncfusion.OlapSilverlight.Reports.OlapReport]             |
|                                                                                                                                                    |
| [                  Dim olapReport As OlapReport = New OlapReport()]                                            |
|                                                                                                                                                    |
| [                  olapReport.Name = \"Sales Report\"]                                                         |
|                                                                                                                                                    |
| [                  olapReport.CurrentCubeName = \"Adventure Works\"]                                           |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [                  Dim dimensionElementColumn As DimensionElement = New DimensionElement()]                    |
|                                                                                                                                                    |
| [                  \'Specifying the Name for the Dimension Element]                                            |
|                                                                                                                                                    |
| [                  dimensionElementColumn.Name = \"Date\"]                                                     |
|                                                                                                                                                    |
| [                  \'Adding the level elemnet along with the Hierarchy Name]                                   |
|                                                                                                                                                    |
| [                  dimensionElementColumn.AddLevel(\"Fiscal\", \"Fiscal Year\")]                               |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [                  Dim dimensionElementRow As DimensionElement = New DimensionElement()]                       |
|                                                                                                                                                    |
| [                  \'Specifying the Name for the Dimension Element]                                            |
|                                                                                                                                                    |
| [                  dimensionElementRow.Name = \"Customer\"]                                                    |
|                                                                                                                                                    |
| [                  \'Adding the level elemnet along with the Hierarchy Name]                                   |
|                                                                                                                                                    |
| [                  dimensionElementRow.AddLevel(\"Customer Geography\", \"Country\")]                          |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [                  \'// Creating a Measure element]                                                            |
|                                                                                                                                                    |
| [                  Dim measureElement As MeasureElements = New MeasureElements()]                              |
|                                                                                                                                                    |
| [.Elements.Add(New MeasureElement With {.Name = \"Internet Sales Amount\"})]                                   |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [                  \'//Adding Diemnsion element to categorical axis]                                           |
|                                                                                                                                                    |
| [                  olapReport.CategoricalElements.Add(New Item With {.ElementValue = dimensionElementColumn})] |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [                  \'//Adding Measure element to categorical axis]                                             |
|                                                                                                                                                    |
| [                  olapReport.CategoricalElements.Add(New Item With {.ElementValue = measureElement})]         |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [                  \'\'\'Adding Dimenions element to series axis]                                              |
|                                                                                                                                                    |
| [\'TODO: INSTANT VB TODO TASK: Assignments within expressions are not supported in VB.NET]                     |
|                                                                                                                                                    |
| [\'ORIGINAL LINE: olapReport.SeriesElements.Add(New Item { ElementValue = dimensionElementRow });]             |
|                                                                                                                                                    |
| [                  olapReport.SeriesElements.Add(New Item With {.ElementValue = dimensionElementRow})]         |
|                                                                                                                                                    |
| []                                                                                                             |
|                                                                                                                                                    |
| [                  Return olapReport]                                                                          |
|                                                                                                                                                    |
| [            End Function]                                                                                     |
|                                                                                                                                                    |
| []                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

 

Use Case Scenarios

Custom Report Support will be useful when users want to view reports that were created for an OLAP control using Report Creation API, in OLAP Client.

[]{#related-topics}

