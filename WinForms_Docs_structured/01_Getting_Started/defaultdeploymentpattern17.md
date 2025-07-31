---
title: defaultdeploymentpattern17.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\defaultdeploymentpattern17.md
created_at: 2025-07-03
---








  









### Default Deployment Pattern {#default-deployment-pattern style="tab-stops: 0pt"}

Follow the steps below to deploy the application in the development server by referencing the dynamic-link library in GAC.

1.   The Web.config file should be configured according to the referenced DLLs. For more information on the Web.config file configuration please refer to the following link.

[[]]{.UGHyperlink} 

[Configuring the Web.config file]{.UGHyperlink}[  ]{.UGHyperlink}

[[]]{.UGHyperlink} 

2.   When it is time to deploy your application there is an additional step you need to perform. You have to ensure that the above referenced assemblies (in your Web.config files) are present in the GAC.

[]{#_Fast_Deployment_Pattern} 

[]{#related-topics}

