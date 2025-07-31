---
title: deploymentprocedures17.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\deploymentprocedures17.md
created_at: 2025-07-03
---








  









## Deployment Procedures {#deployment-procedures style="tab-stops: 0pt"}

[]{#_CreateNewReport(_)}[]{#_RemoveReport}[]{#_RemoveReport(_)}[]{#_SaveReport}[]{#_SaveReport(_)}[]{#_GetReportStream(_)} 

Deployment Requirements

 

1.    to refer to the list of software and hardware requirements for deploying the control in your system.

2.   The following dlls need to be referenced in your application for using *Essential OLAP Chart Web*.

 

[·      ]Syncfusion.Core

[·      ]Syncfusion.DocIO.Base

[]{#_About_OLAP}[·      ]Syncfusion.XlsIO.Base

[·      ]Syncfusion.Pdf.Base

[·      ]Syncfusion.Chart.Base

[·      ]Syncfusion.Chart.Web

[·      ]Syncfusion.Shared.Base

[·      ]Syncfusion.Shared.Web

[·      ]Syncfusion.Olap.Base

[·      ]Syncfusion.OlapChart.Web

[·      ]Syncfusion.OlapShared.Web

[·      ]Syncfusion.Tools.Web

 

Default Deployment Pattern

 

On installing Essential Studio, the Syncfusion assemblies would be automatically placed in the GAC. So, when you drag and drop the OLAP Chart control into a web form, the related assemblies would be automatically added and referred (if and only if they are present in GAC).

On drag and drop, add the following register tag to the ASPX page.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<%][@][ [Register] [Assembly][=\"Syncfusion.OlapChart.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\" ][Namespace][=\"Syncfusion.Web.UI.WebControls.Chart.Olap\"] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [TagPrefix][=\"syncfusion\"][ [%\>]]                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[{border="0"}][Note:][ ]x.x.x.x in the above code snippet refers to the current version of the Essential Studio running in your system.


 

The application's web.config file would include reference to a list of Syncfusion assemblies related to the control.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[web.config\]]**                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][compilation][ ][debug][=][\"[true]\"[\>]\                                                                       |
| [          \<][assemblies][\>]\                                                                                                                                                                                                                                                                                                                     |
| [                  \<][add][ ][assembly][=]\"[Syncfusion.Shared.Web, Version=x.x.x.x, Culture=neutral, ]]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                      |
| [        \<][add][ ][assembly][=]\"[Syncfusion.Olap.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                      |
| [        \<][add][ ][assembly][=]\"[Syncfusion.Tools.Web, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                      |
| [        \<][add][ ][assembly][=]\"[Syncfusion.OlapChart.Web, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        \<][add][ ][assembly][=][\"[Syncfusion.OlapShared.Web, Version= x.x.x.x, Culture=neutral, ]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                      |
| [        \<][add][ ][assembly][=]\"[Syncfusion.Pdf.Web, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                      |
| [        \<][add][ ][assembly][=]\"[Syncfusion.Chart.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                      |
| [        \<][add][ ][assembly][=]\"[Syncfusion.DocIO.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                      |
| [        \<][add][ ][assembly][=]\"[Syncfusion.XlsIO.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                      |
| [        \<][add][ ][assembly][=]\"[Syncfusion.Chart.Web, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                      |
| [        \<][add][ ][assembly][=]\"[Syncfusion.Shared.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                      |
| [        \<][add][ ][assembly][=]\"[Syncfusion.Core, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [PublicKeyToken=632609B4D040F6B4][\"[/\>]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [          \</][assemblies][\>]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][compilation][\>]                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                                                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: x.x.x.x in the above code snippet refers to the current version of the Essential Studio running in your system.


At the time of deploying the application, there is an additional step you need to do. You have to ensure that the above referenced assemblies (in your web.config files) are either present in the GAC or in the application\'s bin folder.

 

The above referenced assemblies can be found in our installation usually in the following path: \"C:\\Program Files\\Syncfusion\\Essential Studio\\\<Version Number\>\\Assemblies\\\".

 

Fast Deployment Pattern

 

Alternatively, you can delete the Syncfusion assembly GAC entries in your development machine. Then, when you drag and drop the Syncfusion control on to your form in the designer, the referenced assembliesare copied over to the application's bin folder and the following entries are added to your ASPX page:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<%][@][ [Register] [Assembly][=\"Syncfusion.OlapChart.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\" ][Namespace][=\"Syncfusion.Web.UI.WebControls.Chart.Olap\"] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [TagPrefix][=\"syncfusion\"][ [%\>]][]                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 


{border="0"}Note: x.x.x.x in the above code snippet refers to the current version of the Essential Studio running in your system.


[]{#related-topics}

