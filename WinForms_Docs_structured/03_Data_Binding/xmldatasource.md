---
title: xmldatasource.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\xmldatasource.md
created_at: 2025-07-03
---








  









### XML DataSource {#xml-datasource style="tab-stops: 0pt"}

[] 

Binding to an XML File

[] 

Through Designer

[] 

To bind an XML file with GridGroupingControl, follow the steps given below.

[] 

1.   Drag-and-drop the **XMLDataSource** component from the **Data** tab in the toolbox.

[] 

{border="0"}

Figure 38

[] 

2.   Select the **Configure DataSource** option from the smart tag as shown below.

[] 

{border="0"}

Figure 39

[] 

3.   You can specify the XML file in the dialog shown below. You can also set the expression to filter the XML data in the same dialog.

[] 

{border="0"}

 

Figure 40

[] 

Through Code

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][sfwg][:][GridGroupingControl][ [ID][=\"GridGroupingControl1\"] [runat][=\"server\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][sfwg][:][GridGroupingControl][\>]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][asp][:][XmlDataSource][ [ID][=\"XmlDataSource1\"] [runat][=\"server\"\>]]              |
|                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][asp][:][XmlDataSource][\>]                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [if][ (!IsPostBack)]                                                                                                             |
|                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [this][.XmlDataSource1.DataFile = Server.MapPath([\"\\\\Syncfusion\\\\Web\\\\Data\\\\Catalog.xml\"]);]   |
|                                                                                                                                                                                                                       |
| [this][.GridGroupingControl1.DataSource = XmlDataSource1;]                                                                       |
|                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [Protected][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                          |
| [If][ [Not] IsPostBack [Then]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                          |
| [Me][.XmlDataSource1.DataFile = Server.MapPath([\"\\Syncfusion\\Web\\Data\\Catalog.xml\"])]                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [Me][.GridGroupingControl1.DataSource = XmlDataSource1]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [End][ [If]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p24} 

[]{#related-topics}

