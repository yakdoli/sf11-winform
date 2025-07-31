---
title: deploymentprocedures1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\01_Getting_Started\deploymentprocedures1.md
created_at: 2025-07-03
---








  









## Deployment Procedures {#deployment-procedures style="tab-stops: 0pt"}

 

Deployment Requirements

 

When deploying an application that references Syncfusion Essential Maps Silverlight assembly, the following dependencies must be included in the distribution:

[·      ]Syncfusion.Maps.Silverlight.dll

 

Default Deployment Pattern

 

The following steps are involved to deploy Essential Maps for Silverlight from Global Assembly Cache (GAC).

 

1.   In Visual Studio, on Solution Explorer, right-click References and select Add Reference.

 

{border="0"}

Figure 5: Adding Reference in Visual Studio

[] 

2.   The **Add Reference** window will open.

3.   Select the **.Net Components** tab. Now a list of assemblies will be displayed, which is available in GAC.

4.   Then select **Syncfusion.Maps.Silverlight.dll**.

{border="0"}

Figure 6: Adding Syncfusion.Maps.Silverlight.dll

 

Fast Deployment Pattern

 

In Visual Studio Integrated Development Environment (IDE), at Solution Explorer, right click the "bin" folder and add the Syncfusion.Maps.Silverlight from the following location.

\[Root Folder\]:\\Program Files\\Syncfusion\\Essential Studio\\\[Version number\]\\Assemblies\\4.0

Then, add the reference of Syncfusion.Maps.Silverlight.dlll from the bin folder.

 

Partial/Medium Trust Support

 

Partial Deployment was not supported.

 

[]{#related-topics}

