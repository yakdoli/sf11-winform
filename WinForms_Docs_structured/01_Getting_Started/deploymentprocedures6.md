---
title: deploymentprocedures6.md
original_path: WinForms_Docs/01_Getting_Started/deploymentprocedures6.md
created_at: 2025-08-05
---








  









## Deployment Procedures {#deployment-procedures style="tab-stops: 0pt"}

Deployment Requirements

When deploying an application that references Syncfusion Essential Maps WPF assembly, the following dependencies must be included in the distribution:

[·      ]Syncfusion.Maps.Wpf.dll

 

Default Deployment Pattern

The steps involved to deploy the Essential Maps for WPF from GAC are as follows:

 

1.   In Visual Studio, Solution Explorer, right click on the References and select Add Reference.

 

{border="0"}

Figure 5: [Adding Reference in Visual Studio]

[] 

2.   The **Add Reference** window will open.

3.   Select the .Net Components Tab, a list of assemblies will be displayed which will be available in GAC. Finally select **Syncfusion.Maps.Wpf.dll**.

 

{border="0"}[]

Figure 6: Adding Syncfusion.Maps.Wpf.dll

 

Fast Deployment Pattern

In Visual Studio Integrated Development Environment (IDE), Solution Explorer, right click  the "bin" folder and add the Syncfusion.Maps.Wpf from the following location.

\[Root Folder\]:\\Program Files\\Syncfusion\\Essential Studio\\\[Version number\]\\Assemblies\\4.0

Then add the reference of Syncfusion.Maps.Wpf.dlll from the bin folder.

 

Partial/Medium Trust Support

[Partial Deployment was not supported.]

[] 

[] 

[]{#related-topics}

