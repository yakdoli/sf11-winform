---
title: webapplicationdeployment.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\webapplicationdeployment.md
created_at: 2025-07-03
---








  









### Web Application Deployment {#web-application-deployment style="tab-stops: 0pt"}

 

Web application by default is deployed in full trust mode. This section discusses the deployment in medium or partial trust scenarios.

 

Deploying in Medium Trust or Partial Trust Scenarios

 

There are two such scenarios in which Syncfusion assemblies might be deployed.

 

Example 1

 

If the Syncfusion Assemblies are in GAC (Global Assembly Cache), and the Web Application is running in *medium* trust, then the Syncfusion assemblies actually runs in full trust. Hence this scenario is fully supported and there are no additional steps necessary for deployment.

 

Example 2

 

Say, the Syncfusion Assemblies are present in the application\'s bin folder and the Web Application is running in *medium* trust, then the Syncfusion assemblies will run in medium trust.

 

**Essential Calculate** allows working in medium trust by using following assemblies.

 

[·      ]Syncfusion.Core.dll

[·      ]Syncfusion.Compression.Base.dll

[·      ]Syncfusion.Calculate.Web.dll

[]{#related-topics}

