---
title: deploymentrequirements66.md
original_path: WinForms_Docs/01_Getting_Started/deploymentrequirements66.md
created_at: 2025-08-05
---








  









## [Deployment Requirements]{#_Ref316471117} {#deployment-requirements style="tab-stops: 0pt"}

This section provides information and instructions for deploying ASP.NET applications that use the ChartAdv control.

**Marking the Application Directory**

The appropriate directory usually where the **.aspx** file is saved must be marked as an Application in IIS.

**Referencing Syncfusion Assemblies**

The Syncfusion assemblies can either be deployed in the server\'s GAC (Global Assembly Cache) or deployed in the application\'s **bin** folder.

**a) Default Deployment Pattern**

Our installation installs our assemblies in the GAC in your development machine. So, when you drag and drop the chart control into your form, the assembly references in your application will be set up such that the Syncfusion assemblies will have to be manually deployed in the GAC or in the application bin folder in your target machine.

On drag and drop, one or more of the following **Register** tags will be added to the .aspx:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<%][@][ [Register] [Assembly][=\"Syncfusion.Chart.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\"]] |
|                                                                                                                                                                                                                                                                                                                                             |
| [Namespace][=\"Syncfusion.Web.UI.WebControls.ChartAdv\"][ [TagPrefix][=\"syncfusion\"] [%\>]]                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[{border="0"}]**[Note: X.X.X.X in the code above corresponds to the correct version number of the Essential Studio version that you are currently using.]***

***[{border="0"}]**[Note: The TagPrefix for Chart.Web Assembly is changed to Syncfusion.]***

And your app\'s **web.config** file will include references to a list of Syncfusion assemblies that you will be linking to as follows.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][configuration][\>]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][system.web][\>]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][compilation][\>]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][assemblies][\>]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][add][ ][assembly][=][\"[Syncfusion.Chart.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][add][ ][assembly][=][\"[Syncfusion.Core, Version=X.X.X.X, Culture=neutral, PublicKeyToken=632609B4D040F6B4]\"[/\>]]      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][assemblies][\>]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][compilation][\>]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\... ]                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][system.web][\>]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][configuration][\>]                                                                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[{border="0"}]**[Note: X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.]***

Also, no DLLs will be copied over to your application\'s **bin** folder.

Now when it\'s time to deploy your application, there is an additional step you need to perform. You have to ensure that the above referenced assemblies (in your **web.config** files) are either present in the GAC or in the application\'s **bin** folder in the deployed server.

The above referenced assemblies can be found in our installation usually in the following path:

\"\[System Drive\]:\\Program Files\\Syncfusion\\Essential Studio\\\<version number \>\\PrecompiledAssemblies\\2.0\".

**b) Alternate Fast Deployment**

Alternatively, you can delete the Syncfusion assembly GAC entries in your development machine. Then, when you drag and drop the Syncfusion controls on to your form in the designer, the referenced assemblies will be copied over to the **bin** folder and the following entries will be added to your .aspx file:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\<%][@][ [Register] [Assembly][=\"Syncfusion.Chart.Web\"] [Namespace][=\"Syncfusion.Web.UI.WebControls.ChartAdv\"] [TagPrefix][=\"syncfusion\"] [%\>]]
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

***[{border="0"}]**[Note: X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.]***

With this setup you can deploy your application as is, using the VS.NET deployment tools, as the necessary DLLs are already copied over to the **bin** folder.

**Data Files**

If you have XML, .mdb, or other data files, ensure that they have sufficient security permissions. The authenticated users should have access to the files and the directory to give the ASP.NET code enough permission to open the file at run time.

**Supporting Netscape/Firefox/Mozilla**

Ensure that the **machine.config**\'s (of the deployed system) **\<browsercaps\>** section includes appropriate entries for Mozilla, etc. The default entries deem these browsers as **downlevel** and hence will not render Syncfusion and your controls properly. You can get the appropriate entries here.

**Deploying in Medium Trust or Partial Trust Scenarios**

There are two such scenarios in which Syncfusion assemblies might be deployed.

1\. Syncfusion assemblies in the GAC (Global Assembly Cache) and application running in medium trust: This means the Syncfusion assemblies are running in full trust. This scenario is fully supported and there are no additional steps necessary.

2\. Syncfusion assemblies in the application **bin** folder and application running in medium trust:

This means both the Syncfusion assemblies and the application code are running in partial trust. In this case, the control's **DeprecateFunctionalityToRunInPartialTrust** property should be turned on for the control to work properly. This will also mean some features might not be available. See the control's documentation for more info.

[]{#p8}[[{border="0" width="17" height="12"}]](http://help.syncfusion.com/ug_94/User%20Interface/ASP.NET/Chart/Documents/231dlls.htm)[2.3.1 DLLs]

[[{border="0" width="17" height="12"}]](http://help.syncfusion.com/ug_94/User%20Interface/ASP.NET/Chart/Documents/232toolboxentries.htm)[2.3.2 Toolbox Entries]

 

More:







