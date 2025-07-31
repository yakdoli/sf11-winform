---
title: creatingawindowsphoneapplication1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingawindowsphoneapplication1.md
created_at: 2025-07-03
---








  









## Creating a Windows Phone Application {#creating-a-windows-phone-application style="tab-stops: 0pt"}

[] 

This section illustrates the step-by-step procedure to create a Windows Phone application and deploy Essential Gauge to it. It has the following sections:

[] 

1.   Creating a Windows Phone Application

2.   Deploying Essential Gauge to the Application

[] 

Creating a Windows Phone Application

[] 

1.   Open Microsoft Visual Studio, go to File menu and click New Project.

[] 

{border="0"}

Figure 10: Creating new Windows Phone Application[]

[] 

2.   In the New Project dialog, select Windows Phone Application template, name the project and click OK.

[] 

[{border="0"}]

Figure 11: Choosing the Windows Phone Application Template

 

[] 

[] 

A new Windows Phone Application is created.[]

 

Deploying Essential Gauge to the Application

[] 

3.   Go to Solution Explorer. Right-click **References** folder and click **Add Reference**.

[] 

{border="0"}

Figure 12: Solution Explorer

 

[] 

4.   Add the following assemblies to the project **References** folder.

[] 

[·      ]Syncfusion.Gauge.Phone.dll

 

{border="0"}

Figure 13: References folder

 

**[]** 

5.   Add assembly reference in the XAML and C# code as follows:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                            |
| [xmlns][:][syncfusion][=\"clr-namespace:Syncfusion.Phone.Gauge;assembly=Syncfusion.Gauge.Phone\"][ ] |
|                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                         |
|                                                                                                                        |
| []                                                                                 |
|                                                                                                                        |
| [using][ Syncfusion.Phone.Gauge;] |
|                                                                                                                        |
| []                                                                                 |
+------------------------------------------------------------------------------------------------------------------------+

[] 

Essential Gauge is deployed in your application.

[] 

See Also

[] 

[Creating a Circular Gauge]{.UGHyperlink}[, ]{.UGHyperlink}[Creating a Linear Gauge]{.UGHyperlink}[, ]{.UGHyperlink}[Creating a Digital Gauge]{.UGHyperlink}[, ]{.UGHyperlink}[Creating a Rolling Gauge]{.UGHyperlink}[]{.UGHyperlink}

[[]]{.UGHyperlink} 

[]{#p12} 

 

[]{#related-topics}

