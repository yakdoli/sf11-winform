---
title: defaultdeploymentpattern16.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\defaultdeploymentpattern16.md
created_at: 2025-07-03
---








  









### Default Deployment Pattern {#default-deployment-pattern style="tab-stops: 0pt"}

[] 

Our installation installs our assemblies in the GAC in your development machine. So, when you drag and drop the chart control into your form, the assembly references in your application will be setup such that the Syncfusion assemblies will have to be manually deployed in the GAC or in the application bin folder in your target machine.

 

On drag and drop, one or more of the following Register tags will be added to the ASPX:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<%][@][ [Register] [Assembly][=\"Syncfusion.Chart.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\"]]                |
|                                                                                                                                                                                                                                                                                                                                                            |
| [    ][Namespace][=\"Syncfusion.Web.UI.WebControls.Chart\"][ [TagPrefix][=\"syncfusion\"] [%\>]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.

{border="0"}Note: The TagPrefix for Chart.Web Assembly is changed to syncfusion.


[] 

And your app\'s web.config file will include references to a list of Syncfusion assemblies that you will be linking to as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][configuration][\>]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [     [\<][system.web][\>]]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [         [\<][compilation][\>]]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [            [\<][assemblies][\>]]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        \<][add][ ][assembly][=][\"[Syncfusion.Chart.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        \<][add][ ][assembly][=][\"[Syncfusion.Shared.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        \<][add][ ][assembly][=][\"[Syncfusion.Chart.Base, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        \<][add][ ][assembly][=][\"[Syncfusion.Tools.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        \<][add][ ][assembly][=][\"[Syncfusion.Shared.Base, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        \<][add][ ][assembly][=][\"[Syncfusion.Core, Version=X.X.X.X, Culture=neutral, PublicKeyToken=632609B4D040F6B4]\"[/\>]]        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [      \</][assemblies][\>]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [          ]                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    \</][compilation][\>]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [      \...                ]                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [      ]                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [  \</][system.web][\>]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][configuration][\>]                                                                                                                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.


[] 

Also, no dlls will be copied over to your application\'s bin folder.

 

Now when it\'s time to deploy your application, there is an additional step you need to perform. You have to ensure that the above referenced assemblies (in your web.config files) are either present in the GAC or in the application\'s bin folder in the deployed server.

 

The above referenced assemblies can be found in our installation usually in the following path: \"C:\\Program Files\\Syncfusion\\Essential Studio\\\<version number\>\\PrecompiledAssemblies\\2.0\".

**[]** 

[]{#related-topics}

