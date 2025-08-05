---
title: establishtheconnectionforacubefile.md
original_path: WinForms_Docs/99_Uncategorized/establishtheconnectionforacubefile.md
created_at: 2025-08-05
---








  









## Establish the connection for a Cube file {#establish-the-connection-for-a-cube-file style="tab-stops: 0pt"}

A valid string is required to establish connection for an OlapDataManager.

Here is the code snippet that demonstrates how to connect cube file by using connection string:

+---------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                              |
|                                                                                                               |
|     OlapDataManager dataManager = new OlapDataManager("DataSource= AdventureWorks_Ext.cub; Provider=MSOLAP"); |
+---------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                  |
|                                                                                                   |
|     Dim dataManager As New OlapDataManager("DataSource= AdventureWorks_Ext.cub; Provider=MSOLAP") |
+---------------------------------------------------------------------------------------------------+

Or

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                          |
|     Syncfusion.Olap.DataProvider.IDataProvider dataProvider = new Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource= AdventureWorks_Ext.cub; Provider=MSOLAP"); |
|                                                                                                                                                                          |
|     OlapDataManager dataManager = new OlapDataManager(dataProvider);                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                               |
|                                                                                                                                                                                |
|     Dim dataProvider As Syncfusion.Olap.DataProvider.IDataProvider = New Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource= AdventureWorks_Ext.cub; Provider=MSOLAP") |
|                                                                                                                                                                                |
|     Dim dataManager As New OlapDataManager(dataProvider)                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

