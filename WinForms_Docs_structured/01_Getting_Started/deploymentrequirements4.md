---
title: deploymentrequirements4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\deploymentrequirements4.md
created_at: 2025-07-03
---








  






[ \> ]{.d2h_breadcrumbsLinkSeparator}[Essential Tools]{.d2h_breadcrumbsContentsOnly}


# Deployment Requirements {#deployment-requirements style="tab-stops: 0pt"}

 

This section provides information and instructions for deploying ASP.NET applications that use Essential Tools.

 

Marking the Application directory

 

The appropriate directory usually where the aspx is saved, must be marked as an **Application** in IIS.

 

Referencing Syncfusion Assemblies

 

The Syncfusion assemblies can either be deployed the server\'s GAC (Global Assembly Cache) or deployed in the Application\'s bin folder.

 

**a) Default Deployment Pattern**

 

Our installation installs our assemblies in the GAC in your development machine. So, when you drag and drop a tools control into your form, the assembly references in your application will be setup such that the Syncfusion assemblies will have to be manually deployed in the GAC or in the application bin folder in your target machine.

 

On drag-and-drop, one or more of the following Register tags will be added to the ASP.

 

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\<%][@][ [Register] [TagPrefix][=\"syncfusion\"] [Namespace][=\"Syncfusion.Web.UI.WebControls.Tools\"] [Assembly][=\"Syncfusion.Shared.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\"] [%\>] ]
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 


{border="0"}Note: The TagPrefix for Shared.Web and Tools.Web Assemblies are changed to syncfusion.


 

And your app\'s web.config file will include references to a list of Syncfusion assemblies that you will be linking to, as follows.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<configuration][\>]                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [   [\<][system.web][\>]]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [     \<][compilation][\>]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [      \<][assemblies][\>]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [          \<][add][ ][assembly][=][\"[Syncfusion.Shared.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [          \<][add][ ][assembly][=][\"[Syncfusion.Core, Version=x.x.x.x, Culture=neutral, PublicKeyToken=632609B4D040F6B4]\"[/\>]]        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [          \<][add][ ][assembly][=][\"[Syncfusion.Shared.Base, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [          \<][add][ ][assembly][=][\"[Syncfusion.Tools.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [          \<][add][ ][assembly][=][\"[Syncfusion.Tools.Base, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [          \<][add][ ][assembly][=][\"[Syncfusion.Grid.Base, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [      \</][assemblies][\>]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [     \</][compilation][\>]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [  \...                ]                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [  [\</][system.web][\>]]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\</][configuration][\>]                                                                                                                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


{border="0"}Note: Note that the version numbers in the above references will vary depending on the version you are linking to.


 

Also, no dlls will be copied over to your application\'s bin folder.

Now when it\'s time to deploy your application, there is an additional step you need to perform. You have to ensure that the above referenced assemblies (in your web.config files) are either present in the GAC or in the application\'s bin folder in the deployed server.

The above referenced assemblies can be found in our installation usually in the following path: \"C:\\Program Files\\Syncfusion\\Essential Studio\\***\<version number\>***\\PrecompiledAssemblies\\2.0\".

 

**b) Alternate Super Fast deployment**

 

Alternatively, you can delete the Syncfusion assembly GAC entries in the your development machine. Then, when you drag and drop the Syncfusion controls on to your form in the designer, the referenced assemblies will be copied over to the bin folder and one or more entries like this will be added to your aspx.

 

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\<%][@][ [Register] [TagPrefix][=\"syncfusion\"] [Namespace][=\"Syncfusion.Web.UI.WebControls.Tools\"] [Assembly][=\"Syncfusion.Shared.Web\"] [%\>] ]
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

With this setup you can deploy your application as is using the VS .NET deployment tools as the necessary dlls are already copied over to the bin folder.

 

Data files

 

If you have XML, .mdb or other data files, ensure that they have sufficient security permissions. The **Authenticated Users** should have access to the files and the directory to give the ASP.NET code enough permission to open the file at run time.

 

Web Config file

 

Make sure to include any control specific http handlers in the application\'s web.config file. For example, if you use the **ImageHolder** type to link to images created in memory  then make sure to include the following http handler in your web.config. Below is a sample http handler entry.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<configuration][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [   [\<][system.web][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [  \...                ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [   \<][httpHandlers][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [      ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [      \<][add][ ][verb][=][\"[\*]\"[ ][path][=]\"[syncfusion_image_generate.ashx]\"[ ][type][=]\"[Syncfusion.Web.UI.WebControls.Tools.ImageRenderHandler,Syncfusion.Shared.Web, Version=x.x.x.x, culture=Neutral,PublicKeyToken=3d67ed1f87d44c89]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [   \</][httpHandlers][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [  [\</][system.web][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][configuration][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


Note: Remember to replace the version number with the right version in the above entry.


 

[Supporting Netscape / FireFox / Mozilla]

 

Ensure that the machine.config\'s (of the deployed system) \<browsercaps\> section includes appropriate entries for Mozilla, etc. The default entries deem these browsers as **downlevel** and hence will not render Syncfusion and your controls properly. You can get the appropriate entries [[here]](../../../../../../../../Documents%20and%20Settings/sheryljohn/Desktop/svn%20ug/ui/aspnet/tools/866).

[] 

[Deploying in Medium Trust or Partial Trust Scenarios]

 

There are two such scenarios in which Syncfusion assemblies might be deployed.

 

1.   Syncfusion Assemblies in the GAC (Global Assembly Cache) and Application running in medium trust.

 

This means the Syncfusion assemblies are running in full trust. This scenario is fully supported and there are no additional steps necessary.

 

2.   Syncfusion Assemblies in the application bin folder and Application running in medium trust.

 

This means both the Syncfusion assemblies and the application code are running in partial trust. In this case, the control**'**s **DeprecateFunctionalityToRunInPartialTrust** property should be turned on for the control to work properly. This will also mean some features might not be available. See control\'s documentation for more info.

[]{#p8} 

More:







