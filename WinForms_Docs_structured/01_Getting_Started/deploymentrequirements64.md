---
title: deploymentrequirements64.md
original_path: WinForms_Docs/01_Getting_Started/deploymentrequirements64.md
created_at: 2025-08-05
---








  









### Deployment Requirements {#deployment-requirements style="tab-stops: 0pt"}

This section provides information and instructions for deploying ASP.NET MVC applications that use Essential Grid for Mobile MVC.

Marking the Application Directory

The directory where project files are usually saved must be marked as an **Application** in the IIS.

 

Referencing Syncfusion Assemblies

The Syncfusion assemblies can either be deployed in the server\'s GAC (Global Assembly Cache), or in the application\'s **bin** folder.

 

General Instructions

Data Files

If you have XML, .mdb, or other data files, ensure that they have sufficient security permissions. The **Authenticated Users** should have access to the files and the directory to give the ASP.NET code enough permission to open the file at run time.

Supporting Netscape/Firefox/Mozilla 

Ensure that the **machine.config**\'s (of the deployed system) **\<browsercaps\>** section includes appropriate entries for Mozilla, and so on. The default entries consider these browsers as **downlevel** and hence will not render Syncfusion and your controls properly.

 

Deploying in Medium Trust or Partial Trust Scenarios 

There are 2 such scenarios in which Syncfusion assemblies might be deployed:

 

1.  [Syncfusion Assemblies in the GAC (Global Assembly Cache) and application running in medium trust.]

This means the Syncfusion assemblies are running in full trust which is explained in . This scenario is fully supported and there are no additional steps necessary.

 

[2.   Syncfusion Assemblies in the application's **bin** folder and application running in medium trust.]

This means both the Syncfusion assemblies and the application code are running in partial trust which is explained in . In this case, the control's **DeprecateFunctionalityToRunInPartialTrust** property should be turned on for the control to work properly. This will also mean some features might not be available. See control\'s documentation for more info.

[]{#related-topics}

