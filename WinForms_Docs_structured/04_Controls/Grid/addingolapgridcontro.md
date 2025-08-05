---
title: addingolapgridcontro.md
original_path: WinForms_Docs/04_Controls/Grid/addingolapgridcontro.md
created_at: 2025-08-05
---








  





## Adding OlapGrid Control to an Application {#adding-olapgrid-control-to-an-application style="tab-stops: 0pt"}

The steps to get started are as follows:

1.   Click **Start** \> **All Programs** \> **Microsoft Visual Studio 2010**.

2.   Create a new **ASP.NET Web Site**.

3.   Drag the **OlapGrid** control from the **Syncfusion BI Web Toolbox** onto the **Design** page.

 

{border="0"}

Figure 5: OLAP Grid in the Source Page

 

{border="0"}

Figure 6: OLAP Grid Appearance in the Design Page

 

4.   Add the following namespaces in the code-behind part.

[·      ]Syncfusion.Web.UI.WebControls.Grid.Olap

[·      ]Syncfusion.Olap.Manager

[·      ]Syncfusion.Olap.Reports

[·      ]Syncfusion.Olap.DataProvider

 

To bind the OlapGrid control with cube data, initiate the [**OlapDataManager**](http://help.syncfusion.com/UG/Business%20Intelligence/OLAP%20Common/Common/default.htm#!documents/42olapdatamanager.htm) using the methods provided in the following link

 

[**Methods for instantiating OlapDataManager**](http://help.syncfusion.com/UG/Business%20Intelligence/OLAP%20Common/Common/default.htm#!documents/42olapdatamanager.htm)**[]**

[] 

5.   After instantiating the OlapDataManager*,* create an [OlapReport](http://help.syncfusion.com/UG/Business%20Intelligence/OLAP%20Common/Common/default.htm#!documents/4311creatingtheolapr.htm) and add it to the OlapDataManager either through the **SetCurrentReport(OlapReport)** method or by the **CurrentReport** property.

6.   Now the OlapReport is assigned to the OlapGrid control's **OlapDataManager** and the **DataBind()** method is called to render the OLAP grid with the current report information.

 

The OlapDataManager can be bound to the OlapGrid using the following code:

 

+----------------------------------------------------------------------------------------------------------------------------------------+
| []{#OLE_LINK2}[**[\[C#\]]**]{#OLE_LINK1}                                                           |
|                                                                                                                                        |
| [DataManager.SetCurrentReport([this].CreateReport());]                        |
|                                                                                                                                        |
| [this][.olapGrid1.OlapDataManager = DataManager;] |
|                                                                                                                                        |
| [this][.olapGrid1.DataBind();]                    |
+----------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                    |
|                                                                                                                                     |
| [DataManager.SetCurrentReport([Me].CreateReport())]                        |
|                                                                                                                                     |
| [Me][.olapGrid1.OlapDataManager = DataManager] |
|                                                                                                                                     |
| [Me][.olapGrid1.DataBind()]                    |
+-------------------------------------------------------------------------------------------------------------------------------------+

 

Also, [click here](http://help.syncfusion.com/UG/Business%20Intelligence/OLAP%20Common/Common/default.htm#!documents/43olapreport.htm) for more sample reports. The OlapGrid control uses **HttpHandler** by default to procure data from the OLAP Server on the member drill-down and for the header cell ToolTip. Therefore, it requires **OlapDataHandler** to be included in the **httpHandlers** section in **Web.config** file.[ [\
\
]]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Web.Config\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<httpHandlers\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [      \.....]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][add][ ][path][=][\"[\*UpdateOlap\*]\" [verb][=]\"[GET]\"[   ][type][=]\"[Syncfusion.Web.UI.WebControls.Grid.Olap.Handlers.OLAPDataHandler, Syncfusion.OlapGrid.Web,Version=x.x.x.x, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</httpHandlers\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[{border="0"}][Note:][ ]x.x.x.x in the above code snippet refers to the current version of the Essential Studio running in your system.


Run the application. The following output is generated.

 

{border="0"}

Figure 7: OlapGrid Control with OLAP Data

[]{#related-topics}

