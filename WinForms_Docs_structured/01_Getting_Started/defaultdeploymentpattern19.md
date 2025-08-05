---
title: defaultdeploymentpattern19.md
original_path: WinForms_Docs/01_Getting_Started/defaultdeploymentpattern19.md
created_at: 2025-08-05
---








  









### Default Deployment Pattern {#default-deployment-pattern style="tab-stops: 0pt"}

Follow the steps below to deploy the application in the development server by referencing the DLL in the GAC.

[1.   The **Web.config** file should be configured according to the referenced DLLs. For more information on the **Web.config** file configuration please refer to the following link:]

[[Configuring Web.Config file]{.ughyperlink}](http://help.syncfusion.com/ug_94/User%20Interface/Mobile%20MVC/Tools/Documents/433addingcodestothew.htm) 

[2.   Now, when it\'s time to deploy your application, there is an additional step you will need to perform\--you will have to ensure that the above referenced assemblies (in your web.config files) are present in the GAC.]

[]{#related-topics}

