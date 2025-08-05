---
title: fastdeploymentpattern15.md
original_path: WinForms_Docs/01_Getting_Started/fastdeploymentpattern15.md
created_at: 2025-08-05
---








  









### Fast Deployment Pattern {#fast-deployment-pattern style="tab-stops: 0pt"}

[] 

Follow the steps below to deploy the application in development server by referencing the dll in application\'s bin folder.

 

1.   Delete the Syncfusion assembly GAC entries in your development machine. The referenced assemblies will be copied over to the bin folder.

2.  Web.config file should be configured according to the referenced dlls. For more information on the web.config file configuration please refer the following link.

[[Configuring Web.Config file]]{.underline}  [[]]{.underline}

***[{border="0"}]**[Note: If you do not want to delete Syncfusion assembly GAC entries, then in Web.config file, please remove the Culture, Version and PublicKeyToken attributes used in all ]**[\<]**[assemblies]**[\>,\<]**[httpHandlers]**[\>]**[ and ]**[\<]**[handlers]**[\> ]**[nodes.]***

***[]*** 

[]{#related-topics}

