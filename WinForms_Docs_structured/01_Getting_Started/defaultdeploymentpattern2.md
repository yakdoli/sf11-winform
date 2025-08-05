---
title: defaultdeploymentpattern2.md
original_path: WinForms_Docs/01_Getting_Started/defaultdeploymentpattern2.md
created_at: 2025-08-05
---








  









### Default Deployment Pattern {#default-deployment-pattern style="tab-stops: 0pt"}

Follow the steps below to deploy the application in the development server by referencing the DLL in the GAC.

1.   The **Web.config** file should be configured according to the referenced DLLs. For more information on the **Web.config** file configuration please refer to the following link: Configuring Web.config file.

2.   Now, when it's time to deploy your application, there is an additional step you need to perform. You have to ensure that the above referenced assemblies (in your **Web.config** files) are present in the GAC.

[]{#related-topics}

