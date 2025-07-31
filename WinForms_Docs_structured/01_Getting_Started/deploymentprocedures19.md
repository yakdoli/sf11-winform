---
title: deploymentprocedures19.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\deploymentprocedures19.md
created_at: 2025-07-03
---








  









## Deployment Procedures {#deployment-procedures style="tab-stops: 0pt"}

[]{#_CreateNewReport(_)}[]{#_RemoveReport}[]{#_RemoveReport(_)}[]{#_SaveReport}[]{#_SaveReport(_)}[]{#_GetReportStream(_)}Deployment Requirements

1.    to refer the list of software and hardware requirements for deploying the control in your system.

2.   The following assemblies are required to be referenced in your application to make use of Essential BI Grid for the Web.

[·      ]Syncfusion.Core

[·      ]Syncfusion.DocIO.Web

[·      ]Syncfusion.XlsIO.Base

[·      ]Syncfusion.Pdf.Base

[·      ]Syncfusion.Shared.Web

[·      ]Syncfusion.Olap.Base

[·      ]Syncfusion.OlapGrid.Web

[·      ]Syncfusion.OlapShared.Web

 

Default Deployment Pattern

On installing Essential Studio, the Syncfusion assemblies will be automatically placed in the GAC. When you drag and drop the OlapGrid control into a Web form, the related assemblies will be automatically added and referred (if and only if they are present in the GAC).

On drag and drop, the following register tag will be added to the ASPX page.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<%][@ [Register] [Assembly]=\"Syncfusion.OlapGrid.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\" [Namespace]=\"Syncfusion.Web.UI.WebControls.Grid.Olap\"  ] |
|                                                                                                                                                                                                                                                                                                                                                    |
| [TagPrefix][=\"syncfusion\" [%\>]]                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[{border="0"}][Note:][ ]x.x.x.x in the above code snippet refers to the current version of the Essential Studio running in your system.


The application's **Web.config** file will include a list of Syncfusion assemblies related to the control.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Web.config\]]**                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][compilation][ ][debug][=][\"[true]\"[\>]\                                                                     |
| [          \<][assemblies][\>]\                                                                                                                                                                                                                                                                                                                   |
| [                  \<][add][ ][assembly][=]\"[Syncfusion.Shared.Web, Version=x.x.x.x, Culture=neutral, ]]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                    |
| [      \<][add][ ][assembly][=]\"[Syncfusion.Olap.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                    |
| [      \<][add][ ][assembly][=]\"[Syncfusion.OlapGrid.Web, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [      \<][add][ ][assembly][=][\"[Syncfusion.OlapShared.Web, Version= x.x.x.x, Culture=neutral, ]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [      \<][add][ ][assembly][=][\"[Syncfusion.DocIO.Base, Version= x.x.x.x, Culture=neutral, ]]     |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                    |
| [      \<][add][ ][assembly][=]\"[Syncfusion.XlsIO.Base, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [      \<][add][ ][assembly][=][\"[Syncfusion.Shared.Base, Version= x.x.x.x, Culture=neutral, ]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                    |
| \                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [      \<][add][ ][assembly][=]\"[Syncfusion.Shared.Web, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [PublicKeyToken=3D67ED1F87D44C89][\"[/\>]\                                                                                                                                                                                                                                                                                                    |
| [      \<][add][ ][assembly][=]\"[Syncfusion.Core, Version= x.x.x.x, Culture=neutral, ]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [PublicKeyToken=632609B4D040F6B4][\"[/\>]]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [          \</][assemblies][\>]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][compilation][\>]                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[{border="0"}][Note:][ ]x.x.x.x in the above code snippet refers to the current version of Essential Studio running in your system.


When it\'s time to deploy your application, there is an additional step you need to perform. You have to ensure that the above referenced assemblies (in your **Web.config** files) are either present in the GAC or in the application\'s **bin** folder.

The above referenced assemblies can be found in the installation, usually in the following path: **C:\\Program Files\\Syncfusion\\Essential Studio\\\<Version Number\>\\Assemblies\\**

 

Fast Deployment Pattern

Alternatively, you can delete the Syncfusion assembly GAC entries in your development machine. Then, when you drag and drop the Syncfusion control onto your form in the designer, the referenced assemblies will be copied over to the application's **bin** folder and the following entries will be added to your ASPX page:

[] 

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\<%][@ [Register] [Assembly]=\"Syncfusion.OlapGrid.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\" [Namespace]=\"Syncfusion.Web.UI.WebControls.Grid.Olap\" [TagPrefix]=\"syncfusion\" [%\>]][]
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[{border="0"}]Note[:][ ]x.x.x.x in the above code snippet refers to the current version of Essential Studio running in your system.[]


[]{#related-topics}

