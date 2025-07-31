---
title: fastdeploymentpattern14.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\fastdeploymentpattern14.md
created_at: 2025-07-03
---








  









### Fast Deployment Pattern {#fast-deployment-pattern style="tab-stops: 0pt"}

Follow the steps below to deploy the application in the development server by referencing the DLL in the application\'s **Bin** folder.

 

1.   Delete the Syncfusion assembly GAC entries in your development machine. The referenced assemblies will be copied over to the **Bin** folder.

2.   The Web.config file should be configured according to the referenced DLLs. For more information on the Web.config file configuration please refer to the following link.

[Configuring Web.Config file]{.UGHyperlink}[  ]{.UGHyperlink}[[]]{.UGHyperlink}


{border="0"}Note: If you do not want to delete Syncfusion assembly GAC entries then in the Web.config file please remove the Culture, Version, and PublicKeyToken attributes used in all [\<][assemblies][\>][, ][\<][httpHandlers][\>][,] and [\<][handlers][\>][ ]nodes.


 

[]{#related-topics}

