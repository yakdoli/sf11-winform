---
title: defaultdeploymentpattern.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\defaultdeploymentpattern.md
created_at: 2025-07-03
---








  









### Default Deployment Pattern {#default-deployment-pattern style="tab-stops: 0pt"}

[] 

Our installation installs our assemblies in the GAC in your development machine. So, when you drag the grid control onto your form, the assembly references in your application will be setup such that the Syncfusion assemblies will have to be manually deployed in the GAC or in the application bin folder in your target machine.

 

On dragging the grid control, one or more of the following Register tags will be added to the ASPX.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<%][@][ [Register] [Assembly][=\"Syncfusion.Grid.Grouping.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\"]] |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    Namespace][=\"Syncfusion.Web.UI.WebControls.Grid.Grouping\"][ [TagPrefix][=\"syncfusion\"] [%\>]]                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<%][@][ [Register] [Assembly][=\"Syncfusion.Shared.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\"]]        |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    [Namespace][=\"Syncfusion.Web.UI.WebControls.Tools\"] [TagPrefix][=\"syncfusion\"] [%\>]]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<%][@][ [Register] [Assembly][=\"Syncfusion.Shared.Base, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\"]]       |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    [Namespace][=\"Syncfusion.Styles\"] [TagPrefix][=\"cc1\"] [%\>]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<%][@][ [Register] [Assembly][=\"Syncfusion.Grid.Windows, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\"]]      |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    [Namespace][=\"Syncfusion.Windows.Forms.Grid\"] [TagPrefix][=\"cc2\"] [%\>]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<%][@][ [Register] [Assembly][=\"Syncfusion.Grouping.Base, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\"]]     |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    [Namespace][=\"Syncfusion.Grouping\"] [TagPrefix][=\"cc3\"] [%\>]]                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.


[] 


{border="0"}Note: The TagPrefix for Shared.Web and Grid.Grouping.Web assemblies are changed to \"syncfusion\".


[] 

Multiple register tags are added because the types referenced by the grid are defined in more than one assembly.

And your app\'s web.config file will include references to a list of Syncfusion assemblies that you will be linking to, as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Web.Config\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
| [\<][configuration][\>]                                                           |
|                                                                                                                                                                                                                                                                                         |
| [         [\<][system.web][\>]]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                         |
| [         [\<][compilation][\>]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                         |
| [            [\<][assemblies][\>]]                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
| [              [\<][add] [assembly][=\"Syncfusion.Grid.Grouping.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89\"/\>]] |
|                                                                                                                                                                                                                                                                                         |
| [              [\<][add] [assembly][=\"Syncfusion.Grid.Windows, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89\"/\>]]      |
|                                                                                                                                                                                                                                                                                         |
| [              [\<][add] [assembly][=\"Syncfusion.Grouping.Base, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89\"/\>]]     |
|                                                                                                                                                                                                                                                                                         |
| [              [\<][add] [assembly][=\"Syncfusion.Shared.Base, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89\"/\>]]       |
|                                                                                                                                                                                                                                                                                         |
| [              [\<][add] [assembly][=\"Syncfusion.Shared.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89\"/\>]]        |
|                                                                                                                                                                                                                                                                                         |
| [              [\<][add] [assembly][=\"Syncfusion.Core, Version=X.X.X.X, Culture=neutral, PublicKeyToken=632609B4D040F6B4\"/\>]      ]        |
|                                                                                                                                                                                                                                                                                         |
| [            [\</][assemblies][\>]]                                                                                                                               |
|                                                                                                                                                                                                                                                                                         |
| [         [\</][compilation][\>]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                         |
| [        \...                ]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                         |
| [        [\</][system.web][\>]]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                         |
| [\</][configuration][\>]                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.


[] 

Also, no assemblies will be copied over to your application\'s bin folder.

Now, when it\'s time to deploy your application, there is an additional step you need to perform. You have to ensure that the above referenced assemblies (in your web.config files) are either present in the GAC or in the application\'s bin folder in the deployed server.

The above referenced assemblies can be found in our installation usually in the following path: \"C:\\Program Files\\Syncfusion\\Essential Studio\\***Version Number***\\PrecompiledAssemblies\\2.0\".

[]{#p11} 

[]{#related-topics}

