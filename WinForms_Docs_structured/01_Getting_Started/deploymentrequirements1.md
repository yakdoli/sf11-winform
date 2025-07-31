---
title: deploymentrequirements1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\deploymentrequirements1.md
created_at: 2025-07-03
---








  









## Deployment Requirements[] {#deployment-requirements style="tab-stops: 0pt"}

[] 

This section provides information and instructions for deploying ASP.NET applications that use Essential Diagram.

[] 

Marking the Application Directory

[] 

The appropriate directory usually where the aspx is saved, must be marked as an Application in the IIS.

**[]** 

Referencing Syncfusion Assemblies

**[]** 

The Syncfusion assemblies can either be deployed in the server\'s GAC (Global Assembly Cache) or deployed in the application\'s bin folder.

[] 

a\) Default Deployment Pattern

[] 

Our installation installs our assemblies in the GAC in your development machine. So, when you drag and drop the diagram control onto your form, the assembly references in your application will be setup such that the Syncfusion assemblies will have to be manually deployed in the GAC or in the application bin folder in your target machine.

 

On drag and drop, one or more of the following Register tags will be added to the ASPX.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<%][@][ [Register] [Assembly][=\"Syncfusion.Diagram.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\"]] |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [Namespace][=\"Syncfusion.Web.UI.WebControls.Diagram\"] [TagPrefix][=\"syncfusion\"] [%\>]]                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}[Note:][ ]X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.


[] 


{border="0"}[Note][:] The TagPrefix for Diagram.Web assembly is changed to syncfusion.


[] 

And your application\'s web.config file will include references to a list of Syncfusion assemblies that you will be linking to as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<configuration][\>]                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [   ][\<][system.web][\>]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [     \<][compilation][\>]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [      \<][assemblies][\>]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][add][ ][assembly][=][\"[Syncfusion.Diagram.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]]                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][add][ ][assembly][=][\"[Syncfusion.Shared.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]]                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][add][ ][assembly][=][\"[Syncfusion.Diagram.Base, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]]                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][add][ ][assembly][=][\"[Syncfusion.Tools.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]]                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][add][ ][assembly][=][\"[Syncfusion.Core, Version=X.X.X.X, Culture=neutral, PublicKeyToken=632609B4D040F6B4]\"[/\>]]                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][add][ ][assembly][=][\"[Syncfusion.Shared.Base, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>\</][assemblies][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [     \</][compilation][\>]                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [  \...                ]                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [  ][\</][system.web][\>]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][configuration][\>]                                                                                                                                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}[Note][:][ ]Diagram assembly contains the Web PaletteGroupBar control, which is a derived control from the Tools Web GroupBar control. Hence Tools.Web assembly also gets added along with the diagram dependent assemblies when PaletteGroupBar is used.

{border="0"}[Note:][ ]X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.


[] 

Also, no dlls will be copied over to your application\'s bin folder.

 

Now, when it\'s time to deploy your application, there is an additional step you need to perform. You have to ensure that the above referenced assemblies (in your web.config files) are either present in the GAC or in the application\'s bin folder in the deployed server.

 

The above referenced assemblies can be found in our installation usually in the following path: \"C:\\Program Files\\Syncfusion\\Essential Studio\\\<version number\>\\PrecompiledAssemblies\\2.0\".

**[]** 

b\) Alternate Super Fast Deployment

[] 

Alternatively, you can delete the Syncfusion assembly GAC entries in your development machine. Then, when you drag and drop the Syncfusion controls onto your form in the designer, the referenced assemblies will be copied over to the bin folder, and the following entries will be added to your aspx:

[] 

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\<%][@][ [Register] [Assembly][=\"Syncfusion.Diagram.Web\"] [Namespace][=\"Syncfusion.Web.UI.WebControls.Diagram\"] [TagPrefix][=\"syncfusion\"] [%\>]]
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[] 

With this setup, you can deploy your application using the VS.NET deployment tools as the necessary dlls are already copied over to the bin folder.

[] 

Data Files

[] 

If you have an XML, .mdb or other data files, ensure that they have sufficient security permissions. The **Authenticated** **Users** should have access to the files and directories to give the ASP.NET code enough permission to open the file at run-time.

[] 

Web Config File

[] 

Make sure to include any control specific http handlers in the application\'s web.config file. For example, if you are specifying the **OutputFormat** property to Handler, you have to insert the following code after the globalization segment in the application\'s web.config file. Below is a sample http handler entry.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<configuration][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [   ][\<][system.web][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [  \...                ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [   \<][httpHandlers][\>       ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][add][ ][verb][=][\"[\*]\"[ ][path][=]\"[ImgRequest.aspx]\"[ ][type][=]\"[Syncfusion.Web.UI.WebControls.Diagram.NodeRenderHandler,Syncfusion.Diagram.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89]\"[/\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][add][ ][verb][=][\"[\*]\"[ ][path][=]\"[PaletteImgRequest.aspx]\"[ ][type][=]\"[Syncfusion.Web.UI.WebControls.Diagram.ThumbNodeRenderHandler,Syncfusion.Diagram.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [  \</][httpHandlers][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [  ][\</][system.web][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][configuration][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}][Note:][ ]X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.


**[]** 

Supporting Netscape / FireFox / Mozilla

[] 

Ensure that the machine.config\'s (of the deployed system) \<browsercaps\> section includes appropriate entries for Mozilla, etc. The default entries deem these browsers as downlevel, and hence will not render Syncfusion and your controls properly.

[] 

Deploying in Medium Trust or Partial Trust Scenarios

[] 

There are two such scenarios in which Syncfusion assemblies might be deployed.

[] 

1.   Syncfusion Assemblies in the GAC (Global Assembly Cache) and Application running in medium trust.

[] 

This means the Syncfusion assemblies are running in full trust. This scenario is fully supported and no additional steps are necessary.

[] 

2.   Syncfusion Assemblies in the Application bin folder and Application running in medium trust.

[] 

This means both the Syncfusion assemblies and the application code are running in partial trust. In this case, the control's DeprecateFunctionalityToRunInPartialTrust property should be turned on for the control to work properly. This will also mean  that some features might not be available. See the control's documentation for more information.

More:







