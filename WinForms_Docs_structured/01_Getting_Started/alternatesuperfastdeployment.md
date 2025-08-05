---
title: alternatesuperfastdeployment.md
original_path: WinForms_Docs/01_Getting_Started/alternatesuperfastdeployment.md
created_at: 2025-08-05
---








  









### Alternate Super Fast deployment {#alternate-super-fast-deployment style="tab-stops: 0pt"}

[] 

Alternatively, you can delete the Syncfusion assembly GAC entries in your development machine. Then, when you drag and drop the Syncfusion controls on to your form in the designer, the referenced assemblies will be copied over to the bin folder and the following entries will be added to your aspx:

[] 

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\<%][@][ [Register] [Assembly][=\"Syncfusion.Chart.Web\"] [Namespace][=\"Syncfusion.Web.UI.WebControls.Chart\"] [TagPrefix][=\"syncfusion\"] [%\>]]
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[] 


 

{border="0"}Note: Since the Chart OutputFormat is Handler by default, Handler entry will be made in the Web.Config file once you drag and drop the control into a designer as follows.


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][httpHandlers][\> ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][add][ ][verb][=][\"[\*]\"[ ][path][=]\"[syncfusion_generate.ashx]\"[ ][type][=]\"[Syncfusion.Web.UI.WebControls.Chart.ChartWebHandler,Syncfusion.Chart.Web, Version=X.X.X.X, culture=Neutral,PublicKeyToken=3d67ed1f87d44c89]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][httpHandlers][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.


[] 

With this setup you can deploy your application as is, using the VS.NET deployment tools, as the necessary dlls are already copied over to the bin folder.

[] 

Data files

[] 

If you have XML, .mdb or other data files, ensure that they have sufficient security permissions. The Authenticated Users should have access to the files and the directory to give the ASP.NET code enough permission to open the file at run time.

[] 

Supporting Netscape/FireFox/Mozilla

[] 

Ensure that the machine.config\'s (of the deployed system) \<browsercaps\> section includes appropriate entries for Mozilla, etc., The default entries deem these browsers as downlevel and hence will not render Syncfusion and your controls properly. You can get the appropriate entries here.

[] 

Deploying in Medium Trust or Partial Trust Scenarios

**[]** 

There are 2 such scenarios in which Syncfusion assemblies might be deployed.

[] 

1.   Syncfusion Assemblies in the GAC (Global Assembly Cache) and Application running in medium trust:

[] 

This means the Syncfusion assemblies are running in full trust. This scenario is fully supported and there are no additional steps necessary.

[] 

2.   Syncfusion Assemblies in the application bin folder and Application running in medium trust:

[] 

This means both the Syncfusion assemblies and the application code are running in partial trust. In this case, the control's **DeprecateFunctionalityToRunInPartialTrust** property should be turned on for the control to work properly. This will also mean some features might not be available. See control's documentation for more info.

[]{#p8} 

[]{#related-topics}

