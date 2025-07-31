---
title: deploymentprocedures18.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\deploymentprocedures18.md
created_at: 2025-07-03
---








  









## Deployment Procedures {#deployment-procedures style="tab-stops: 0pt"}

[]{#_CreateNewReport(_)}[]{#_RemoveReport}[]{#_RemoveReport(_)}[]{#_SaveReport}[]{#_SaveReport(_)}[]{#_GetReportStream(_)}Deployment Requirements

 

1.    to refer the list of the software and hardware requirements for deploying the control in your system.

2.   The following dlls are required to be referenced in your application to use the Essential OLAP Client Web.

[·      ]Syncfusion.Core

[·      ]Syncfusion.DocIO.Base

[·      ]Syncfusion.XlsIO.Base

[·      ]Syncfusion.Linq.Base

[]{#_About_OLAP}[·      ]Syncfusion.Chart.Base

[·      ]Syncfusion.Chart.Web

[·      ]Syncfusion.Shared.Base

[·      ]Syncfusion.Shared.Web

[·      ]Syncfusion.Olap.Base

[·      ]Syncfusion.OlapChart.Web

[·      ]Syncfusion.OlapGrid.Web

[·      ]Syncfusion.OlapSampleUtils

[·      ]Syncfusion.Tools.Web

 

Default deployment pattern

 

On installing Essential Studio, the Syncfusion assemblies would be automatically placed in the GAC. So, when you drag and drop the OLAP Client control into a web form, the related assemblies would be automatically added and referred (if and only if they are present in GAC).

On drag and drop, the following register tag would be added to the ASPX page.

[] 

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\<%][@][ [Register] [Assembly][=\"Syncfusion.OlapClient.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\" ][Namespace][=\"Syncfusion.Web.UI.WebControls.Client.Olap\"]  [TagPrefix][=\"cc1\"] [%\>]]
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 

{border="0"}Note: x.x.x.x in the above code snippet refers to the current version of the Essential Studio running in your system.


The application's web.config file would include reference to a list of Syncfusion assemblies related to the control.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[web.config\]]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                 |
| [\<][compilation][ ][debug][=][\"[true]\"[\>]\ |
| [          \<][assemblies][\>]\                                                                                                                                                                                                                                               |
| [                  \<][add][ ][assembly][=]\"[Syncfusion.Shared.Web, Version=x.x.x.x, Culture=neutral, ]]                                                                   |
|                                                                                                                                                                                                                                                                                                                                                 |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                |
| [      \<][add][ ][assembly][=]\"[Syncfusion.Olap.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                 |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                |
| [      \<][add][ ][assembly][=]\"[Syncfusion.Tools.Web, Version= x.x.x.x, Culture=neutral, ]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                 |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                |
| [      \<][add][ ][assembly][=]\"[Syncfusion.OlapChart.Web, Version= x.x.x.x, Culture=neutral, ]]                                                                           |
|                                                                                                                                                                                                                                                                                                                                                 |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                |
| [      \<][add][ ][assembly][=]\"[Syncfusion.OlapGrid.Web, Version= x.x.x.x, Culture=neutral, ]]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                 |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                |
| [      \<][add][ ][assembly][=]\"[Syncfusion.Chart.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                              |
|                                                                                                                                                                                                                                                                                                                                                 |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                |
| [      \<][add][ ][assembly][=]\"[Syncfusion.DocIO.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                              |
|                                                                                                                                                                                                                                                                                                                                                 |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                |
| [      \<][add][ ][assembly][=]\"[Syncfusion.XlsIO.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                              |
|                                                                                                                                                                                                                                                                                                                                                 |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                |
| [      \<][add][ ][assembly][=]\"[Syncfusion.Chart.Web, Version= x.x.x.x, Culture=neutral, ]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                 |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                |
| [      \<][add][ ][assembly][=]\"[Syncfusion.Linq.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                 |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                |
| [      \<][add][ ][assembly][=]\"[Syncfusion.Shared.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                 |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                |
| [      \<][add][ ][assembly][=]\"[Syncfusion.Core, Version= x.x.x.x, Culture=neutral, ]]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                 |
| [PublicKeyToken=632609B4D040F6B4][\"[/\>]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                 |
| [          \</][assemblies][\>]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                 |
| [\</][compilation][\>]                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: x.x.x.x in the above code snippet refers to the current version of the Essential Studio running in your system.


Now when it\'s time to deploy your application, there is an additional step you need to perform. You have to ensure that the above referenced assemblies (in your web.config files) are either present in the GAC or in the application\'s bin folder.

 

The above referenced assemblies can be found in our installation usually in the following path: \"C:\\Program Files\\Syncfusion\\Essential Studio\\\<Version Number\>\\Assemblies\\\".

 

Fast deployment pattern

 

Alternatively, you can delete the Syncfusion assembly GAC entries in your development machine. Then, when you drag and drop the Syncfusion control on to your form in the designer, the referenced assemblies will be copied over to the application's bin folder and the following entries will be added to your ASPX page:

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\<%][@][ [Register] [Assembly][=\"Syncfusion.OlapClient.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\" ][Namespace][=\"Syncfusion.Web.UI.WebControls.Client.Olap\"] [TagPrefix][=\"cc1\"] [%\>]][]
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 

{border="0"}Note: x.x.x.x in the above code snippet refers to the current version of the Essential Studio running in your system.


[]{#related-topics}

