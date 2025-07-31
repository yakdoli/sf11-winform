---
title: howtobindtheolapgrid1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtobindtheolapgrid1.md
created_at: 2025-07-03
---








  





## How to Bind the OLAP Grid {#how-to-bind-the-olap-grid style="tab-stops: 0pt"}

The OLAP grid requires the **OlapDataManager** for the data source to bind OLAP data and relational data.

 

Binding SSAS Data

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                       |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [        [// Specifying the connection string.]]                                                                                                            |
|                                                                                                                                                                                                                       |
| [        [string] connectionString = [\"DataSource = localhost;Initial Catalog=Adventure Works DW\"];]                               |
|                                                                                                                                                                                                                       |
| [        [// Instantiating the OlapDataManager with connection string.]]                                                                                    |
|                                                                                                                                                                                                                       |
| [        [OlapDataManager] olapDataManager = [new] [OlapDataManager](connectionString);]                     |
|                                                                                                                                                                                                                       |
| [        [// Set current report to OlapDataManager.  ]]                                                                                                     |
|                                                                                                                                                                                                                       |
| [        olapDataManager.SetCurrentReport(CreateOlapReport());]                                                                                                                   |
|                                                                                                                                                                                                                       |
| [        [// Specifying the DataSource for OlapGrid.]]                                                                                                      |
|                                                                                                                                                                                                                       |
| [        [this].OlapGrid1.OlapDataManager = olapDataManager;]                                                                                                |
|                                                                                                                                                                                                                       |
| [        [// DataBinding.]]                                                                                                                                 |
|                                                                                                                                                                                                                       |
| [        [this].OlapGrid1.DataBind();]                                                                                                                       |
|                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [Protected][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                          |
| [            [\' Specifying the connection string.]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| [            [Dim] connectionString [As] [String] = [\"DataSource = localhost;Initial Catalog=Adventure Works DW\"]]                                                          |
|                                                                                                                                                                                                                                                                                                          |
| [            [\' Instantiating the OlapDataManager with connection string.]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [            [Dim] olapDataManager [As] OlapDataManager = [New] OlapDataManager(connectionString)]                                                                                                    |
|                                                                                                                                                                                                                                                                                                          |
| [            [\' Set current report to OlapDataManager.  ]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                          |
| [            olapDataManager.SetCurrentReport(CreateOlapReport())]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [            [\' Specifying the DataSource for OlapGrid.]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [            [Me].OlapGrid1.OlapDataManager = olapDataManager]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [            [\' DataBinding.]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [            [Me].OlapGrid1.DataBind()]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Binding Relational Data

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                       |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [  [// Instantiating the OlapDataManager.]]                                                                                                                 |
|                                                                                                                                                                                                                       |
| [  [OlapDataManager] olapDataManager = [new] [OlapDataManager]();]                                           |
|                                                                                                                                                                                                                       |
| [  [//Preserving the ItemSource for OlapDatamanger \[ItemSource -- Either  ]]                                                                               |
|                                                                                                                                                                                                                       |
| [  IList or DataTable\].]                                                                                                                                           |
|                                                                                                                                                                                                                       |
| [  olapDataManager.ItemSource = ItemSource;]                                                                                                                                      |
|                                                                                                                                                                                                                       |
| [  [// Sets Current report for OlapDataManager.]]                                                                                                           |
|                                                                                                                                                                                                                       |
| [  olapDataManager.SetCurrentReport(CreateOlapReport());]                                                                                                                         |
|                                                                                                                                                                                                                       |
| [  [// Specifying the DataSource for OlapGrid.]]                                                                                                            |
|                                                                                                                                                                                                                       |
| [  [this].OlapGrid1.DataSource = olapDataManager;]                                                                                                           |
|                                                                                                                                                                                                                       |
| [  [// Data Binding.]]                                                                                                                                      |
|                                                                                                                                                                                                                       |
| [  [this].OlapGrid1.DataBind();]                                                                                                                             |
|                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [Protected][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                          |
| [  [\' Instantiating the OlapDataManager.]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                          |
| [  [Dim] olapDataManager [As] OlapDataManager = [New] OlapDataManager()]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                          |
| [  [\'Preserving the ItemSource for OlapDatamanger \[ItemSource -- Either  ]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [  IList or DataTable\].]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                          |
| [  olapDataManager.ItemSource = ItemSource]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                          |
| [  [\' Sets Current report for OlapDataManager.]]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                          |
| [  olapDataManager.SetCurrentReport(CreateOlapReport())]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [  [\' Specifying the DataSource for OlapGrid.]]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| [  [Me].OlapGrid1.DataSource = olapDataManager]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [  [\' Data Binding.]]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [  [Me].OlapGrid1.DataBind()]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

