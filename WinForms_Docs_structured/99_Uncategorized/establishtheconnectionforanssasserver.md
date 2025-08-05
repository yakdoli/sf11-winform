---
title: establishtheconnectionforanssasserver.md
original_path: WinForms_Docs/99_Uncategorized/establishtheconnectionforanssasserver.md
created_at: 2025-08-05
---








  









## Establish the connection for an SSAS Server {#establish-the-connection-for-an-ssas-server style="tab-stops: 0pt"}

A valid string is required to establish connection for an OlapDataManager.

Here is the code snippet that demonstrates how to connect SSAS by using connection string:

+--------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                    |
|     OlapDataManager dataManager = new OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW"); |
+--------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                       |
|                                                                                                        |
|     Dim dataManager As New OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW") |
+--------------------------------------------------------------------------------------------------------+

Or

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                               |
|     Syncfusion.Olap.DataProvider.IDataProvider dataProvider = new Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource=localhost; Initial Catalog=Adventure Works DW"); |
|                                                                                                                                                                               |
|     OlapDataManager dataManager = new OlapDataManager(dataProvider);                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ dataProvider [As] Syncfusion.Olap.DataProvider.IDataProvider = [New] Syncfusion.Olap.DataProvider.AdomdDataProvider([\"DataSource=localhost; Initial Catalog=Adventure Works DW\"])] |
|                                                                                                                                                                                                                                                                                                                                                    |
|     Dim dataManager As New OlapDataManager(dataProvider)                                                                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

