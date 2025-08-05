---
title: olapdatamanager.md
original_path: WinForms_Docs/03_Data_Binding/olapdatamanager.md
created_at: 2025-08-05
---








  









## OlapDataManager {#olapdatamanager style="tab-stops: 0pt"}

OlapDataManager is the most important class in the whole OLAP Base. All the information transfers from the control to OLAP base will happen through this class and this will retain the current state of the base objects. The connection is established in the Data provider of the OLAP Base, but the information required in establishing the connection is given to the data provider through the **OlapDataManager**.

**[]** 

Table 3: Constructors


  Constructors                         Description                                                                                                                  Parameters          Return Type   Reference Link
  ------------------------------------ ---------------------------------------------------------------------------------------------------------------------------- ------------------- ------------- ----------------
  OlapDataManager()                    Default constructor                                                                                                          \-                  Void          \-
  OlapDataManager(string)              Accepts the connection string as argument and passes it to the Data Provider to establish the connection with data source.   String              Void          \-
  OlapDataManager(AdomdDataProvider)   Accepts the Data Provider as argument and processes the cube that is connected with the given data provider.                 AdomdDataProvider   Void          \-


[] 

Establishing connection with the SSAS server

The following code snippet describes establishing connection with the server:

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [\                                                                                                                                                                                                                                                             |
| [OlapDataManager] olapDataManager = [new] [OlapDataManager]([\"DataSource=localhost; Initial Catalog=Adventure Works DW\"]);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                           |
|                                                                                                                                                                                                            |
| [OlapDataManager olapDataManager = [New] OlapDataManager(\"[DataSource=localhost; Initial Catalog=Adventure Works DW]\")] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Or

 

Establishing Connection with the SSAS server through Data Provider

The following code snippet describes establishing connection with the server:

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [AdomdDataProvider][ dataProvider = [new] [AdomdDataProvider]([\"DataSource=localhost; Initial Catalog=Adventure Works DW\"]);] |
|                                                                                                                                                                                                                                                                                              |
| [OlapDataManager][ olapDataManager = [new] [OlapDataManager](dataProvider);]                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                              |
| [Dim][ dataProvider [As] AdomdDataProvider = [New] AdomdDataProvider(\"[DataSource=localhost; Initial Catalog=Adventure Works DW]\")] |
|                                                                                                                                                                                                                                                                                              |
| [Dim][ olapDataManager [As] OlapDataManager = [New] OlapDataManager(dataProvider)]                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 Establishing connection with the offline cube

The following code snippet describes establishing connection with the offline cube:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                  |
| [\                                                                                                                                                                                                                                                                                               |
| [OlapDataManager] olapDataManager = [new] [OlapDataManager]([@\"Data Source = C:\\ Common\\Data\\OfflineCube\\Adventure_Works_Ext.cub; Provider = MSOLAP;\"]);] |
|                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                   |
| [OlapDataManager olapDataManager = [New] OlapDataManager([\"Data Source = C:\\\\ Common\\\\Data\\\\OfflineCube\\\\Adventure_Works_Ext.cub; Provider = MSOLAP;\"])][ ] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Establishing connection with XMLA Server:

XML for Analysis (XMLA) is a standard that allows the client applications to transfer multi-dimensional or OLAP data sources, which is available in the Mondrian Server. The back and forth communication is done using the web standards -- HTTP, SOAP, and XML.  The query language used is MDX, is most widely supported for reporting from multi-dimensional data stores.

Use Case Scenarios

XMLA provides the most efficient way to access an OLAP database over the Internet.

Connecting to Mondrian Server

 The following code illustrates how to connect to the Mondrian server:

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [// Connecting to Mondrian ][S][erver][]                                             |
|                                                                                                                                                                                                                                                                                              |
| [OlapDataManager DataManager = new OlapDataManager(][\"Data Source = http://localhost:8080/mondrian/xmla; Initial Catalog = FoodMart;\"][);]                     |
|                                                                                                                                                                                                                                                                                              |
| [DataManager][.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.][Providers][.Mondrian;] |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]][]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [\' Connecting to Mondrian ][S][erver][ ][] |
|                                                                                                                                                                                                                                                                                                     |
| [Dim DataManager As OlapDataManager = New OlapDataManager(\"Datasource = http://bi.syncfusion.com:8080/mondrian/xmla; Initial Catalog=FoodMart;\")]                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [DataManager][.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.][Providers][.Mondrian]         |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[Click here](http://mondrian.pentaho.com/) for more information about Mondrian XMLA configurations.

 

Connecting to Active Pivot Server

 The following code illustrates how to connect to Active Pivot server:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                 |
| [// Connecting to Active Pivot ][S][erver][]                                            |
|                                                                                                                                                                                                                                                                                                 |
|     OlapDataManager DataManager = new OlapDataManager(@"Data Source=http://localhost:8081/var_s/xmla;  Initial Catalog=VaRCubes; User ID=; Password=; Transport Compression=None;");                                                                                                            |
|                                                                                                                                                                                                                                                                                                 |
| [DataManager][.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.][Providers][.ActivePivot;] |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]][]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| [\' Connecting to Active Pivot ][S][erver][ ][] |
|                                                                                                                                                                                                                                                                                                         |
| [Dim DataManager As OlapDataManager = New OlapDataManager(\"Data Source=http://localhost:8081/var**\_**s/xmla;  Initial Catalog=VaRCubes; User ID=; Password=; Transport Compression=None;\")]                                                                      |
|                                                                                                                                                                                                                                                                                                         |
| [DataManager][.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.][Providers][.ActivePivot]          |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[Click here](http://quartetfs.com/) for more information on Active Pivot server.

 

More:











