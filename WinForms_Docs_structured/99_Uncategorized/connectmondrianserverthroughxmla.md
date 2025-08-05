---
title: connectmondrianserverthroughxmla.md
original_path: WinForms_Docs/99_Uncategorized/connectmondrianserverthroughxmla.md
created_at: 2025-08-05
---








  









## Connect Mondrian Server through XMLA {#connect-mondrian-server-through-xmla style="tab-stops: 0pt"}

 The following code illustrates how to connect to the Mondrian server:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                    |
| [// Connecting to Mondrian ][S][erver][]                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                    |
| [OlapDataManager DataManager = new OlapDataManager(][\"Data Source = http://localhost:8080/mondrian/xmla; Initial Catalog = FoodMart;\"][);]                                                           |
|                                                                                                                                                                                                                                                                                                                                    |
| [DataManager][.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.][Providers][.Mondrian;][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]][]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                |
| [\' Connecting to Mondrian ][S][erver][ ][]                                                                        |
|                                                                                                                                                                                                                                                                                                                                                |
| [Dim DataManager As OlapDataManager = New OlapDataManager(\"Datasource = http://bi.syncfusion.com:8080/mondrian/xmla; Initial Catalog=FoodMart;\")]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                |
| [DataManager][.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.][Providers][.Mondrian][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[Click here](http://mondrian.pentaho.com/) for more information about Mondrian XMLA configurations.

[]{#related-topics}

