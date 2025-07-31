---
title: addingolapchartcontroltoanapplication.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\addingolapchartcontroltoanapplication.md
created_at: 2025-07-03
---








  









## Adding OLAP Chart Control to an Application {#adding-olap-chart-control-to-an-application style="tab-stops: 0pt"}

To create an OLAP Chart for web:

 

1.  Click[[ ]]{.apple-converted-space}**Start**[**[ ]**]{.apple-converted-space}**\>**[**[ ]**]{.apple-converted-space}**All Programs**[**[ ]**]{.apple-converted-space}**\>**[**[ ]**]{.apple-converted-space}**Microsoft Visual Studio 2010.**

2.  Create a new[[ ]]{.apple-converted-space}**ASP.NET Web Site.**

3.  [Drag the[ ]{.apple-converted-space}**OlapChart**[ ]{.apple-converted-space}control from the[ ]{.apple-converted-space}**Syncfusion BI Web Toolbox**[ ]{.apple-converted-space}onto the[ ]{.apple-converted-space}**Design**[ ]{.apple-converted-space}page.]

{border="0"}

 

Figure 5: OLAP Chart control in Source Page

 

 

{border="0"}

 

Figure 6: OLAP Chart control in Design Page

[4.   Add the following namespaces in the code-behind:]

[·      ][Syncfusion.Web.UI.WebControls.Chart.Olap]

[·      ][Syncfusion.Olap.Manager]

[·      ][Syncfusion.Olap.Reports]

[·      ][Syncfusion.Olap.DataProvider]

[] 

[To bind the OlapChart control with cube data, initiate the][[ ]]{.apple-converted-space}[**[OlapDataManager]**](http://help.syncfusion.com/UG/Business%20Intelligence/OLAP%20Common/Common/default.htm#!documents/42olapdatamanager.htm)[[ ]]{.apple-converted-space}[using the methods provided in the following link.][]

[] 

**[Methods for instantiating OlapDataManager]**[]

[2.   After instantiating the OlapDataManager*,[ ]{.apple-converted-space}*create an[ ]{.apple-converted-space}][[OlapReport]](http://help.syncfusion.com/UG/Business%20Intelligence/OLAP%20Common/Common/default.htm#!documents/4311creatingtheolapr.htm)[[ ]]{.apple-converted-space}[and add it to the OlapDataManager either[* *]{.apple-converted-space}through the[ ]{.apple-converted-space}**SetCurrentReport(OlapReport)**[ ]{.apple-converted-space}method or by the[ ]{.apple-converted-space}**CurrentReport**[ ]{.apple-converted-space}property.]

[3.   Now the OlapReport[* *]{.apple-converted-space}is assigned to the OlapChart control's[** **]{.apple-converted-space}**OlapDataManager**[* *]{.apple-converted-space}and the[ ]{.apple-converted-space}**DataBind()**[ ]{.apple-converted-space}method is called to render the OLAP Chart with the current report information.]

[] 

[The OlapDataManager can be bound to the OlapChart using the following code:]

 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| []{#OLE_LINK2}[**[\[C#\]]**]{#OLE_LINK1}                                                            |
|                                                                                                                                         |
| [DataManager.SetCurrentReport([this].CreateReport());]                         |
|                                                                                                                                         |
| [this][.olapChart1.OlapDataManager = DataManager;] |
|                                                                                                                                         |
| [this][.olapChart1.DataBind();]                    |
+-----------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                     |
|                                                                                                                                      |
| [DataManager.SetCurrentReport([Me].CreateReport())]                         |
|                                                                                                                                      |
| [Me][.olapChart1.OlapDataManager = DataManager] |
|                                                                                                                                      |
| [Me][.olapChart1.DataBind()]                    |
+--------------------------------------------------------------------------------------------------------------------------------------+

[] 

[Also,][[ ]]{.apple-converted-space}[[click here]](http://help.syncfusion.com/UG/Business%20Intelligence/OLAP%20Common/Common/default.htm#!documents/43olapreport.htm)[[ ]]{.apple-converted-space}[for more sample reports.][ ]OLAP Chart control uses HttpHandler by default to procure the images of chart, label and legend each time. Therefore, it's required to include the handler in the httphandlers section of web.config file.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Web.Config\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [\<httpHandlers\>]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [      \.....]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [      \<add path=\"syncfusion_generate.ashx\" verb=\"\*\" type=\"Syncfusion.Web.UI.WebControls.Chart.ChartWebHandler,Syncfusion.Chart.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\"/\>] |
|                                                                                                                                                                                                                                                                      |
| [\</httpHandlers\>]                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 


{border="0"}Note: x.x.x.x in the above code snippet refers to the current version of Essential Studio running in your system.


Run the application. The following output is generated.

 

{border="0"}

 

Figure 7: Chart displaying OLAP Data

[]{#related-topics}

