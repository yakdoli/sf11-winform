---
title: deploymentrequirements65.md
original_path: WinForms_Docs/01_Getting_Started/deploymentrequirements65.md
created_at: 2025-08-05
---








  









### Deployment Requirements {#deployment-requirements style="TEXT-ALIGN: justify; tab-stops: 0pt"}

This section provides information and instructions for deploying ASP.NET Mobile MVC applications that use Essential Gauge Mobile MVC. 

**[Marking the Application Directory ]**

The directory where the project files are usually saved, must be marked as an **Application** in the IIS.

**[Referencing Syncfusion Assemblies]**

The Syncfusion assemblies can either be deployed in the server\'s GAC (Global Assembly Cache), or in the Application\'s bin folder.

**[General Instructions]**

**[Data Files]**

If you have XML, .mdb or other data files, ensure that they have sufficient security permissions. The **Authenticated Users** should have access to the files and the directory to give the ASP.NET code enough permission to open the file at runtime. 

**[Deploying in Medium Trust or Partial Trust Scenarios ]**

There are two scenarios in which the Syncfusion assemblies can be deployed:

1.   Syncfusion Assemblies in the GAC (Global Assembly Cache) and Application running in medium trust\
- This means the Syncfusion assemblies are running in full trust which is explained in the Default Deployment Pattern. This scenario is fully supported and there are no additional steps necessary.

2.   Syncfusion Assemblies in the application bin folder and Application running in medium trust\
- This means both the Syncfusion assemblies and the application code are running in partial trust which is explained in Fast Deployment Pattern. In this case, the control's **DeprecateFunctionalityToRunInPartialTrust** property should be turned on for the control to work properly. This will also mean that some features might not be available. See control\'s documentation for more info.

[]{#related-topics}

