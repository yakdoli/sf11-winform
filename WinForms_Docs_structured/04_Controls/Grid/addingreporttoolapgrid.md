---
title: addingreporttoolapgrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\addingreporttoolapgrid.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Adding report to OLAP Grid {#adding-report-to-olap-grid style="tab-stops: 0pt"}

Adding an OLAP report to OLAP Grid control in design time is described in the following code snippet:

 

+-------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                  |
|                                                                                                 |
|                     <                                                                           |
|                     syncfusion                                                                  |
|                     :                                                                           |
|                     OlapGrid                                                                    |
|                      x                                                                          |
|                     :                                                                           |
|                     Name                                                                        |
|                     ="olapGrid"                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                           HorizontalAlignment                                   |
|                     ="Stretch"                                                                  |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                      ReportName                                                                 |
|                     ="SalesReport"                                                              |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                 CurrentCubeName                                                 |
|                     ="Adventure Works"                                                          |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                           SharedDataManagerName                                 |
|                     ="localManager"                                                             |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                           olapshared                                            |
|                     :                                                                           |
|                     DataSource.DataManagerName                                                  |
|                     ="localManager"                                                             |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                     olapshared                                                                  |
|                     :                                                                           |
|                     DataSource.ConnectionString                                                 |
|                     ="datasource=localhost; initial catalog=adventure works dw">                |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                     <!- Adding Elements to Categorical Axis -->                                 |
|                                                                                                 |
|                                                                                                 |
|                     <                                                                           |
|                     syncfusion                                                                  |
|                     :                                                                           |
|                     OlapGrid.CategoricalAxis                                                    |
|                     >                                                                           |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                     <                                                                           |
|                     syncfusion                                                                  |
|                     :                                                                           |
|                     Dimension                                                                   |
|                      Name                                                                       |
|                     ="Date"                                                                     |
|                      HierarchyName                                                              |
|                     ="Fiscal"                                                                   |
|                      LevelName                                                                  |
|                     ="Fiscal Year"                                                              |
|                      IncludeMembers                                                             |
|                     ="FY 2002, FY 2003"                                                         |
|                                                                                                 |
|                      />                                                                         |
|                                                                                                 |
|                     <!- Multiple Members where specified by comma separate -->                  |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                     <                                                                           |
|                     syncfusion                                                                  |
|                     :                                                                           |
|                     Kpi                                                                         |
|                      Name                                                                       |
|                     ="Revenue"                                                                  |
|                      ShowGoal                                                                   |
|                     ="True"                                                                     |
|                      ShowStatus                                                                 |
|                     ="True"                                                                     |
|                      ShowValue                                                                  |
|                     ="True"                                                                     |
|                      ShowTrend                                                                  |
|                     ="True" />                                                                  |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                     </                                                                          |
|                     syncfusion                                                                  |
|                     :                                                                           |
|                     OlapGrid.CategoricalAxis                                                    |
|                     >                                                                           |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                     <!- Adding Elements to Series Axis -->                                      |
|                                                                                                 |
|                                                                                                 |
|                     <                                                                           |
|                     syncfusion                                                                  |
|                     :                                                                           |
|                     OlapGrid.SeriesAxis                                                         |
|                     >                                                                           |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                     <                                                                           |
|                     syncfusion                                                                  |
|                     :                                                                           |
|                     Dimension                                                                   |
|                      Name                                                                       |
|                     ="Sales Channel"                                                            |
|                      HierarchyName                                                              |
|                     ="Sales Channel"                                                            |
|                      LevelName                                                                  |
|                     ="Sales Channel" />                                                         |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                     <                                                                           |
|                     syncfusion                                                                  |
|                     :                                                                           |
|                     Dimension                                                                   |
|                      Name                                                                       |
|                     ="Product"                                                                  |
|                      HierarchyName                                                              |
|                     ="Product Model Lines"                                                      |
|                      LevelName                                                                  |
|                     ="Product Line"                                                             |
|                      IncludeMembers                                                             |
|                     ="Road" />                                                                  |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                     </                                                                          |
|                     syncfusion                                                                  |
|                     :                                                                           |
|                     OlapGrid.SeriesAxis                                                         |
|                     >                                                                           |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                     </                                                                          |
|                     syncfusion                                                                  |
|                     :                                                                           |
|                     OlapGrid                                                                    |
|                     >                                                                           |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
| []                                                          |
+-------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 12: OLAP Grid with SalesReport created by XAML code

 

[] 

Sample Link\
\

To access a XAML Configuration Demo sample:

1.  Open the Syncfusion Dashboard

2.  Select **Business Intelligence**

3.  Click the **WPF** drop-down list and select **Explore Samples**

4.  Navigate to **OlapGrid.WPF** -\> **Samples** -\> **Defining Reports** -\> **XAML Configuration Demo**

[Or]

[] 

[Navigate to:]

**..\\Syncfusion\\EssentialStudio\\\<Versionnumber\>\\BI\\WPF\\OlapGrid.WPF\\Samples\\Defining Reports\\XAML Configuration Demo**

[ [] ]{.UGHyperlink} 

[]{#related-topics}

