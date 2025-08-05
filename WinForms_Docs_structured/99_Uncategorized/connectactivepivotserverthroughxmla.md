---
title: connectactivepivotserverthroughxmla.md
original_path: WinForms_Docs/99_Uncategorized/connectactivepivotserverthroughxmla.md
created_at: 2025-08-05
---








  









## Connect ActivePivot Server through XMLA {#connect-activepivot-server-through-xmla style="tab-stops: 0pt"}

The user can connect the Active Pivot server through XMLA (XML for Analysis) services using the OlapDataManager in our OLAP controls.

The following code illustrates how to connect to Active Pivot server:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                       |
| [// Connecting to Active Pivot ][S][erver][]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                       |
|     OlapDataManager DataManager = new OlapDataManager(@"Data Source=http://localhost:8081/var_s/xmla;  Initial Catalog=VaRCubes; User ID=; Password=; Transport Compression=None;");                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                       |
| [DataManager][.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.][Providers][.ActivePivot;][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]][]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [\' Connecting to Active Pivot ][S][erver][ ][]                                           |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Dim DataManager As OlapDataManager = New OlapDataManager(\"Data Source=http://localhost:8081/var**\_**s/xmla;  Initial Catalog=VaRCubes; User ID=; Password=; Transport Compression=None;\")]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                   |
| [DataManager][.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.][Providers][.ActivePivot][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[[Click here]](http://quartetfs.com/) for more information about Active Pivot server.

[]{#related-topics}

