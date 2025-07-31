---
title: defaultdeploymentpattern22.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\defaultdeploymentpattern22.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Default Deployment Pattern {#default-deployment-pattern style="tab-stops: 0pt"}

[] 

Follow the steps below to deploy the application in the development server by referencing the dll in GAC.

1.   Web.config file should be configured according to the referenced dlls. For more information on the web.config file configuration please refer the following link.

[Configuring Web.Config file]{.UGHyperlink}   []{.UGHyperlink}

2.   Now, when it\'s time to deploy your application, there is an additional step you need to perform. You have to ensure that the above referenced assemblies (in your web.config files) are  present in the GAC.

[]{#_Fast_Deployment_Pattern} **[]**  

[]{#related-topics}

