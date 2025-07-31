---
title: defaultdeploymentpattern20.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\defaultdeploymentpattern20.md
created_at: 2025-07-03
---








  









### Default Deployment Pattern {#default-deployment-pattern style="TEXT-ALIGN: justify; tab-stops: 0pt"}

Follow the steps given below to deploy the application in the development server by referencing the dll in GAC.

1.   Web.config file should be configured according to the referenced dlls. For more information on the web.config file configuration refer to the following link.\
\
[Configuring Web.Config file] \
\

2.   At the time of deployment, ensure that the above referenced assemblies (in your web.config files) are present in the GAC.

[]{#related-topics}

