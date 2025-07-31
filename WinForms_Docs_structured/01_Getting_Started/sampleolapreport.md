---
title: sampleolapreport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\sampleolapreport.md
created_at: 2025-07-03
---








  









## Sample OlapReport {#sample-olapreport style="tab-stops: 0pt"}

[] 

This report uses the "Adventure Works" cube for dimension and measures definition.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                      |
| [///][ ][\<summary\>]                                            |
|                                                                                                                                                                                                                      |
| [///][ Defining OlapReport with Dimensions and Measures]                                                          |
|                                                                                                                                                                                                                      |
| [///][ ][\</summary\>]                                           |
|                                                                                                                                                                                                                      |
| [///][ ][\<returns\>\</returns\>]                                |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [private][ [OlapReport] ][CreateOlapReport()]                       |
|                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [        [OlapReport] olapReport = [new] [OlapReport]();]                                                   |
|                                                                                                                                                                                                                      |
| [        [// Selecting the Cube]]                                                                                                                          |
|                                                                                                                                                                                                                      |
| [        olapReport.CurrentCubeName = [\"Adventure Works\"];]                                                                                            |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [        [DimensionElement] dimensionElementColumn = [new] [DimensionElement]();]                           |
|                                                                                                                                                                                                                      |
| [        [// Specifying the Name for Column Dimension Element]]                                                                                            |
|                                                                                                                                                                                                                      |
| [        dimensionElementColumn.Name = [\"Customer\"];]                                                                                                  |
|                                                                                                                                                                                                                      |
| [        [// Specifying the Hierarchy and Level Element Name]]                                                                                             |
|                                                                                                                                                                                                                      |
| [        dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"]);]                                              |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [        [MeasureElements] measureElementColumn = [new] [MeasureElements]();]                               |
|                                                                                                                                                                                                                      |
| [        [//Specifying the Measure Elements]]                                                                                                              |
|                                                                                                                                                                                                                      |
| [        measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Internet Sales Amount\"] });] |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [        [DimensionElement] dimensionElementRow = [new] [DimensionElement]();]                              |
|                                                                                                                                                                                                                      |
| [        [//Specifying the Name for Row Dimension Element]]                                                                                                |
|                                                                                                                                                                                                                      |
| [        dimensionElementRow.Name = [\"Date\"];]                                                                                                         |
|                                                                                                                                                                                                                      |
| [        [// Specifying the Hierarchy and Level Element Name]]                                                                                             |
|                                                                                                                                                                                                                      |
| [        dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);]                                                         |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [        [///][Adding Column Members]]                                                                                                |
|                                                                                                                                                                                                                      |
| [        olapReport.CategoricalElements.Add(dimensionElementColumn);]                                                                                                            |
|                                                                                                                                                                                                                      |
| [        [///][Adding Measure Element]]                                                                                               |
|                                                                                                                                                                                                                      |
| [        olapReport.CategoricalElements.Add(measureElementColumn);]                                                                                                              |
|                                                                                                                                                                                                                      |
| [        [///][Adding Row Members]]                                                                                                   |
|                                                                                                                                                                                                                      |
| [        olapReport.SeriesElements.Add(dimensionElementRow);]                                                                                                                    |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [        [return] olapReport;    ]                                                                                                                          |
|                                                                                                                                                                                                                      |
| [ }]                                                                                                                                                                             |
|                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[] 

[] 

[] 

[] 

[] 

[] 

[] 

[] 

[] 

[] 

 

 

 

 

 

 

 

 

 

 

 

 

 

**Workflow Information**

Before submitting this content to the Documentation team, make sure Fields 1-4 and Field 7 have been filled out. Do not delete this page.

+-------------------------------------+-----------------------------------------+
|                                                                               |
|                                                                               |
| **Feature Request ID:5373**                                                   |
|                                                                               |
|                                                                               |
+-------------------------------------+-----------------------------------------+
| **1.   Content Contributor:**       | Bharath and Sylvia Praveen              |
+-------------------------------------+-----------------------------------------+
| **2.   Team Lead:**                 | Rajadurai C                             |
+-------------------------------------+-----------------------------------------+
| **3.   Technical Reviewer:**        | Rajadurai C                             |
+-------------------------------------+-----------------------------------------+
| **4.   Date Reviewed:**             | 14^th^ Oct 2011                         |
+-------------------------------------+-----------------------------------------+
| **Comments:**                       | Please accept changes made in document. |
+-------------------------------------+-----------------------------------------+
| **5.   Content Editor:**            | Sylvia Praveen                          |
+-------------------------------------+-----------------------------------------+
| **6.   Date Reviewed:**             | 14^th^ Oct 2011                         |
+-------------------------------------+-----------------------------------------+
| **Comments:**                       |                                         |
+-------------------------------------+-----------------------------------------+
| **Location in the UG**              | New UG                                  |
+-------------------------------------+-----------------------------------------+
| **7.   Status:**                    | **Content Review Completed**            |
+-------------------------------------+-----------------------------------------+

 

 

[] 

[]{#related-topics}

