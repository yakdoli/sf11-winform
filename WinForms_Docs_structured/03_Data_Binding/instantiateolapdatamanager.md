---
title: instantiateolapdatamanager.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\instantiateolapdatamanager.md
created_at: 2025-07-03
---








  









## Instantiate OlapDataManager {#instantiate-olapdatamanager style="tab-stops: 0pt"}

To instantiate the OlapDataManager, we shall use any of the following methods.

**[]** 

Binding OLAP Client to the Server:

**[]** 

+----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                |
| [OlapDataManager olapDataManager = new OlapDataManager(connectionString);] |
|                                                                                                                |
| [this.olapClient1.OlapDataManager = olapDataManager;]                      |
|                                                                                                                |
| [this.olapClient1.DataBind();][]                  |
+----------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                     |
|                                                                                                                      |
| [Dim olapDataManager As OlapDataManager = New OlapDataManager(connectionString)] |
|                                                                                                                      |
| [Me.olapClient1.OlapDataManager = olapDataManager]                               |
|                                                                                                                      |
| [Me.olapClient1.DataBind()][]                           |
+----------------------------------------------------------------------------------------------------------------------+

**[]** 

Binding OLAP Client to the Offline Cube:

**[]** 

+-----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                |
|                                                                                                                 |
| [OlapDataManager olapDataManager = new OlapDataManager(connectionString); ] |
|                                                                                                                 |
| [this.olapClient1.OlapDataManager = olapDataManager;]                       |
|                                                                                                                 |
| [this.olapClient1.DataBind();][]                   |
+-----------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                     |
|                                                                                                                      |
| [Dim olapDataManager As OlapDataManager = New OlapDataManager(connectionString)] |
|                                                                                                                      |
| [Me.olapClient1.OlapDataManager = olapDataManager]                               |
|                                                                                                                      |
| [Me.olapClient1.DataBind()][]                           |
+----------------------------------------------------------------------------------------------------------------------+

**[]** 

Binding OLAP Client to the Server using Data Provider:

**[]** 

+-----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                |
|                                                                                                                 |
| [AdomdDataProvider dataProvider = new AdomdDataProvider(connectionString);] |
|                                                                                                                 |
| [OlapDataManager olapDataManager = new OlapDataManager(dataProvider);]      |
|                                                                                                                 |
| [this.olapClient1.OlapDataManager = olapDataManager;]                       |
|                                                                                                                 |
| [this.olapClient1.DataBind();][]                   |
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
| [Me.olapClient1.DataBind()][]                            |
+-----------------------------------------------------------------------------------------------------------------------+

**[]** 

[]{#related-topics}

