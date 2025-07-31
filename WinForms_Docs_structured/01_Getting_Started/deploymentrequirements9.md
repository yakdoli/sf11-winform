---
title: deploymentrequirements9.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\deploymentrequirements9.md
created_at: 2025-07-03
---








  









## Deployment Requirements {#deployment-requirements style="tab-stops: 0pt"}

This section provides information and instructions for deploying ASP.NET MVC applications that use Essential Grid MVC.

 

Marking the Application Directory

[] 

The appropriate directory usually where the project file is saved, must be marked as an **Application** in IIS.

 

Referencing Syncfusion Assemblies

 

The Syncfusion assemblies can either be deployed in the server\'s GAC (Global Assembly Cache) or, in the Application\'s bin folder.

 

General Instructions

Data Files

 

If you have XML, .mdb or other data files, ensure that they have sufficient security permissions. The **Authenticated Users** should have access to the files and the directory to give the ASP.NET code enough permission to open the file at runtime.

[] 

Supporting Netscape / FireFox / Mozilla

[] 

Ensure that the machine.config\'s (of the deployed system) \<browsercaps\> section includes appropriate entries for Mozilla, and so on. The default entries consider these browsers as **downlevel** and hence will not render Syncfusion and your controls properly.

[] 

Deploying in Medium Trust or Partial Trust Scenarios

[] 

There are two such scenarios in which Syncfusion assemblies might be deployed:

[] 

1.   Syncfusion Assemblies in the GAC (Global Assembly Cache) and Application running in medium trust.

[] 

       - This means the Syncfusion assemblies are running in full trust which is explained in [Default Deployment Pattern]{.UGHyperlink}. This scenario is fully supported and there are no additional steps necessary.

[] 

2.   Syncfusion Assemblies in the application bin folder and Application running in medium trust.

[] 

       - This means both the Syncfusion assemblies and the application code are running in partial trust which is explained in [Fast Deployment Pattern]{.UGHyperlink}. In this case, the control's **DeprecateFunctionalityToRunInPartialTrust** property should be turned on for the control to work properly. This will also mean some features might not be available. See control\'s documentation for more info.

[] 

[]{#_Default_Deployment_Pattern}Default Deployment Pattern

[] 

Follow the steps below to deploy the application in the development server by referencing the dll in GAC:

1.   Web.config file should be configured according to the referenced dlls. For more information on the web.config file configuration please refer to the following link:

[Configuring Web.Config file][  **[]**]

3.   Now, when it\'s time to deploy your application, there is an additional step you need to perform. You have to ensure that the above referenced assemblies (in your web.config files) are present in the GAC.

[]{#_Fast_Deployment_Pattern} 

Fast Deployment Pattern

[] 

Follow the steps below to deploy the application in development server by referencing the dll in application\'s bin folder:

 

1.   Delete the Syncfusion assembly GAC entries in your development machine. The referenced assemblies will be copied over to the bin folder.

2.   Web.config file should be configured according to the referenced dlls. For more information on the web.config file configuration please refer the following link:

[Configuring Web.Config file][  []]


{border="0"}Note: If you do not want to delete the Syncfusion assembly GAC entries, then in Web.config file, please remove the Culture, Version and PublicKeyToken attributes used in all [\<][assemblies][\>,\<][httpHandlers][\>] and [\<][handlers][\> ]nodes.


[] 

More:





