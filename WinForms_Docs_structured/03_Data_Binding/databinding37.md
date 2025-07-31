---
title: databinding37.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\databinding37.md
created_at: 2025-07-03
---








  









## Data Binding {#data-binding style="tab-stops: 0pt"}

To instantiate the OlapDataManager and to bind the cube data in client control, we shall use any of the following method.

 

Binding OLAP Client to the Server:

+----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                |
| [OlapDataManager olapDataManager = new OlapDataManager(connectionString);] |
|                                                                                                                |
| [this.olapClient1.OlapDataManager = olapDataManager;]                      |
|                                                                                                                |
| [this.olapClient1.DataBind();]                                             |
+----------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                     |
|                                                                                                                      |
| [Dim olapDataManager As OlapDataManager = New OlapDataManager(connectionString)] |
|                                                                                                                      |
| [Me.olapClient1.OlapDataManager = olapDataManager]                               |
|                                                                                                                      |
| [Me.olapClient1.DataBind()]                                                      |
+----------------------------------------------------------------------------------------------------------------------+

 

Binding OLAP Client to the Offline Cube:

+-----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                |
|                                                                                                                 |
| [OlapDataManager olapDataManager = new OlapDataManager(connectionString); ] |
|                                                                                                                 |
| [this.olapClient1.OlapDataManager = olapDataManager;]                       |
|                                                                                                                 |
| [this.olapClient1.DataBind();]                                              |
+-----------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                     |
|                                                                                                                      |
| [Dim olapDataManager As OlapDataManager = New OlapDataManager(connectionString)] |
|                                                                                                                      |
| [Me.olapClient1.OlapDataManager = olapDataManager]                               |
|                                                                                                                      |
| [Me.olapClient1.DataBind()]                                                      |
+----------------------------------------------------------------------------------------------------------------------+

[] 

Binding OLAP Client to the Server using Data Provider:

+-----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                |
|                                                                                                                 |
| [AdomdDataProvider dataProvider = new AdomdDataProvider(connectionString);] |
|                                                                                                                 |
| [OlapDataManager olapDataManager = new OlapDataManager(dataProvider);]      |
|                                                                                                                 |
| [this.olapClient1.OlapDataManager = olapDataManager;]                       |
|                                                                                                                 |
| [this.olapClient1.DataBind();]                                              |
+-----------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                      |
|                                                                                                                       |
| [Dim dataProvider As AdomdDataProvider = New AdomdDataProvider(connectionString)] |
|                                                                                                                       |
| [Dim olapDataManager As OlapDataManager = New OlapDataManager(dataProvider)]      |
|                                                                                                                       |
| [Me.olapClient1.OlapDataManager = olapDataManager]                                |
|                                                                                                                       |
| [Me.olapClient1.DataBind()]                                                       |
+-----------------------------------------------------------------------------------------------------------------------+

[]{#_Display_Mode} 

Table 12: Properties


  --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------- -----------------------
  Property              Description                                                                                                                                           Type          Data type           Reference link
  AdomdDataProvider     Multidimensional data provider uses ADOMD for .NET to connect and retrieve data from the multidimensional data source                                 Server side   AdomdDataProvider                       -
  OlapDataManager       Sets the cube mode. It contains connection proprerty, current report, cube name, cube schema and pivot engine for rendering chart and grid controls   Server side   OlapDataManager     \-
  --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ------------------- -----------------------


 

Table 13: DataBind() Method


  ------------ ---------------------------------------------------------------------------------------------------- ------------ ------------- ------------- ----------------
  Methods      Description                                                                                          Parameters   Type          Return type   Reference link
  DataBind()   The method is used to fill or bind data present in the DataManager into the chart and grid control   \-           Server side   void          \-
  ------------ ---------------------------------------------------------------------------------------------------- ------------ ------------- ------------- ----------------


 

Sample Link

A sample demo is available at the following link:

**..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\Web\\OlapClient.Web\\Samples\\3.5\\OlapClient\\ OlapClientDemo**

[]{#related-topics}

