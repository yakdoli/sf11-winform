---
title: creatingansampleapplicationwitholap.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\creatingansampleapplicationwitholap.md
created_at: 2025-07-03
---








  









### Creating an Sample Application with OLAP {#creating-an-sample-application-with-olap style="tab-stops: 0pt"}

The steps to create a new WPF application in Visual Studio 2008 are as follows:

1.   Open **Visual Studio IDE** (either 2008 or 2010. In this sample, we have used visual studio 2010). From the **File** menu, select **New Project**.

 

{border="0"}

Figure 7: File -\> New -\> Project

 

2.   In the **New Project** Dialog box, click the **Windows** tab and select **WPF Application**.

[3.   ]Then, type a name for the application and click **OK**. In this example, the name of the application is typed as **SampleApplication***[.]*[]

{border="0"}

Figure 8: New Project Dialog -- WPF Application

 

4.   A new WPF application is created. Now, add the OlapChart control to this application.

 

The steps to add the OlapChart to the application are as follows:

1.   From the **Visual Studio** Toolbox, drag and drop the **OlapChart** under the Syncfusion **BI WPF** band. It will automatically add the required referenced assemblies.

{border="0"}

 

Figure 9: OlapChart added from the Toolbox[]

[] 

2.   Alternatively, you can add the OlapChart to an application by using any of the following code snippets:

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                  |
|                                                                                                                                                                                               |
|                                                                                                                                                                                               |
|                                                                                                                                                                                               |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapChart1\" /\>] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                        |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [OlapChart] olapChart = [new] [OlapChart](); |
+-------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                                            |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
| [Dim] olapChart [As] [OlapChart] = [New] [OlapChart]() |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Then, ensure that the following assemblies are included in the project reference:

[·      ]Syncfusion.Chart.WPF

[·      ]Syncfusion.Core

[·      ]Syncfusion.Olap.Base

[·      ]Syncfusion.OlapChart.WPF

[·      ]Syncfusion.OlapShared.WPF

[·      ]Syncfusion.Shared.WPF

 

4.   Include the following namespaces:

[·      ]Syncfusion.Olap.Reports

[·      ]Syncfusion.Olap.Manager

 

5.   Declare a member variable for OlapDataManager, as shown below.

 

+-------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                |
|                                                                                           |
|                                                                                           |
|                                                                                           |
| [private][ OlapDataManager] olapDataManager; |
+-------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **            \[VB\]**                                                                                                   |
|                                                                                                                          |
|                                                                                                                          |
|                                                                                                                          |
| [      Private] olapDataManager [As] [OlapDataManager] |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

6.   In the window's default constructor include the following codes, to initialize the connection:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [string][ connectionString = ]                                                                                                                                        |
|                                                                                                                                                                                                                  |
| [@\"Data source=.;Initial Catalog=Adventure Works DW\"][;]                                                                                                         |
|                                                                                                                                                                                                                  |
| [               ]                                                                                                                                                                          |
|                                                                                                                                                                                                                  |
| [// Created connection is assigned to data manager][                ]                                                                                                |
|                                                                                                                                                                                                                  |
| [if][ (connectionString != ][\"\"][)                    ]                                                               |
|                                                                                                                                                                                                                  |
| [   this.][olapDataManager = ][new][ ][OlapDataManager][(connectionString);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **            \[VB\]**                                                                                                                      |
|                                                                                                                                             |
|                                                                                                                                             |
|                                                                                                                                             |
| [      Dim] connectionString [As] [String] =                                 |
|                                                                                                                                             |
|       [\"Data source=.;Initial Catalog=Adventure Works DW\"]                                                        |
|                                                                                                                                             |
|                                                                                                                                             |
|                                                                                                                                             |
| [      \' Created connection is assigned to data manager                ]                                             |
|                                                                                                                                             |
| [      If] connectionString \<\> \"\" [Then]                                                      |
|                                                                                                                                             |
|          [Me].olapDataManager = [New] [OlapDataManager](connectionString) |
|                                                                                                                                             |
| [      End] [If]                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Include the following method, which contains a simple report created from the Adventure works cube:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                          |
|                                                                                                                                                                                     |
|                                                                                                                                                                                     |
|                                                                                                                                                                                     |
| [        private] [OlapReport] SimpleDimensions()\                                                                                     |
|         {\                                                                                                                                                                          |
|             [OlapReport] olapReport = [new] [OlapReport]();\                                                   |
|             olapReport.CurrentCubeName = [\"Adventure Works\"];\                                                                                            |
|             [DimensionElement] dimensionElementColumn = [new] [DimensionElement]();\                           |
|  \                                                                                                                                                                                  |
|             [//Specifying the Column Name for the Dimension and measure elements]\                                                                            |
|             dimensionElementColumn.Name = [\"Customer\"];\                                                                                                  |
|             dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"]);\                                              |
|             [MeasureElements] measureElementColumn = [new] [MeasureElements]();\                               |
|             measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Internet Sales Amount\"] });\ |
|  \                                                                                                                                                                                  |
|             [//Specifying the Row Name for the Dimension element]\                                                                                            |
|             [DimensionElement] dimensionElementRow = [new] [DimensionElement]();\                              |
|             dimensionElementRow.Name = [\"Date\"];\                                                                                                         |
|             dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"]);\                                                         |
|  \                                                                                                                                                                                  |
|             [///][ Adding Column Members]\                                                                                               |
|             olapReport.CategoricalElements.Add(dimensionElementColumn);\                                                                                                            |
|             [///][Adding Measure Element]\                                                                                               |
|             olapReport.CategoricalElements.Add(measureElementColumn);\                                                                                                              |
|             [///][Adding Row Members]\                                                                                                   |
|             olapReport.SeriesElements.Add(dimensionElementRow);\                                                                                                                    |
|             [return] olapReport;\                                                                                                                              |
|         }                                                                                                                                                                           |
|                                                                                                                                                                                     |
|                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **            \[VB\]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
| [      ][Private] [Function] SimpleDimensions() [As] [OlapReport]\                                                         |
|                                      [Dim] olapReport [As] [OlapReport] = [New] [OlapReport]()\                         |
|                                      olapReport.CurrentCubeName = [\"Adventure Works\"]\                                                                                                                       |
|  \                                                                                                                                                                                                                                     |
|                                      [Dim] dimensionElementColumn [As] [DimensionElement] = [New] [DimensionElement]()\ |
|                                      [\'Specifying the Name for the Dimension Element]\                                                                                                                          |
|                                      dimensionElementColumn.Name = [\"Customer\"]\                                                                                                                             |
|             dimensionElementColumn.AddLevel([\"Customer Geography\"], [\"Country\"])\                                                                                                  |
|  \                                                                                                                                                                                                                                     |
|                                      [Dim] measureElementColumn [As] [MeasureElements] = [New] [MeasureElements]()\     |
|             measureElementColumn.Elements.Add([New] [MeasureElement] [With] {.Name = [\"Internet Sales Amount\"]})\                          |
|  \                                                                                                                                                                                                                                     |
|                                      [Dim] dimensionElementRow [As] [DimensionElement] = [New] [DimensionElement]()\    |
|                                      [\'Specifying the Dimension Name]\                                                                                                                                          |
|                                      dimensionElementRow.Name = [\"Date\"]\                                                                                                                                    |
|             dimensionElementRow.AddLevel([\"Fiscal\"], [\"Fiscal Year\"])\                                                                                                             |
|  \                                                                                                                                                                                                                                     |
|             [\'\'\'Adding Column Members]\                                                                                                                                                                       |
|             olapReport.CategoricalElements.Add(dimensionElementColumn)\                                                                                                                                                                |
|                                      [\'\'\'Adding Measure Element]\                                                                                                                                             |
|             olapReport.CategoricalElements.Add(measureElementColumn)\                                                                                                                                                                  |
|                                      [\'\'\'Adding Row Members]\                                                                                                                                                 |
|             olapReport.SeriesElements.Add(dimensionElementRow)\                                                                                                                                                                        |
|                                      [Return] olapReport\                                                                                                                                                         |
|                         [End] [Function]                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

8.   In the window's loaded event include the following code snippet, to bind the report with the control:

 

+-------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                              |
|                                                                                                                         |
|                                                                                                                         |
|                                                                                                                         |
|                 [if] ([this].olapDataManager != [null])\ |
|                 {\                                                                                                      |
|                     [// Reports are set to data manager]\                                         |
|                     [this].olapDataManager.SetCurrentReport(SimpleDimensions());                   |
|                                                                                                                         |
| \                                                                                                                       |
|                     [// The chart gets the data from data manager now]\                           |
|                     [this].olapchart1.OlapDataManager = olapDataManager;                           |
|                                                                                                                         |
| \                                                                                                                       |
|                     [// Data Binding is done]\                                                    |
|                     [this].olapchart1.DataBind();\                                                 |
|                 }                                                                                                       |
|                                                                                                                         |
|                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                         |
|                                                                                                                                                    |
|                                                                                                                                                    |
|                                                                                                                                                    |
|                 [If] olapDataManager [IsNot] [Nothing] [Then]\ |
|                     olapDataManager.SetCurrentReport(SimpleDimensions())\                                                                          |
|                     [Me].olapchart1.OlapDataManager = olapDataManager\                                                        |
|                     [Me].olapchart1.DataBind()\                                                                               |
|                 [End] [If]                                                                               |
|                                                                                                                                                    |
|                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

9.   Run the application.

[]{#related-topics}

