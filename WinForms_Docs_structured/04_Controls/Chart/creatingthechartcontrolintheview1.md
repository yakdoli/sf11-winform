---
title: creatingthechartcontrolintheview1.md
original_path: WinForms_Docs/04_Controls/Chart/creatingthechartcontrolintheview1.md
created_at: 2025-08-05
---








  









### Creating the Chart control in the View {#creating-the-chart-control-in-the-view style="tab-stops: 0pt"}

To create the Chart control in the View:*[]*

1.   Right-click the **Views/Home** folder.

2.   Click **Add**, and then select **View**.

3.   Name the View, **SimpleChart**.

4.   Add the following code in the SimpleChart.cshtml file, to create the Chart control in the View page.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [    [\@{][ ]Html.Chart([\"SimpleChart\"])]                                              |
|                                                                                                                                                                                                       |
| [        .Skins([ChartModelSkins].Office2007Blue)]                                                                                        |
|                                                                                                                                                                                                       |
| [        .ShowLegend([false])]                                                                                                               |
|                                                                                                                                                                                                       |
| [        .SmoothingMode(System.Drawing.Drawing2D.[SmoothingMode].AntiAlias)]                                                              |
|                                                                                                                                                                                                       |
| [        .BorderAppearance(borderApp =\> {            borderApp.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);] |
|                                                                                                                                                                                                       |
| [        }).Render();]                                                                                                                                            |
|                                                                                                                                                                                                       |
| [    [}]]                                                                                                                             |
|                                                                                                                                                                                                       |
| []                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Open \~/Controllers/HomeController.cs.

4.   Include the following namespaces in the HomeController:

 

[·      ]Syncfusion.Mvc.Chart

[·      ]Syncfusion.Mvc.Shared

[·      ]Syncfusion.Windows.Forms.Chart

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                |
| **[]**                                                                                                                                                     |
|                                                                                                                                                                                                |
| [using][ Syncfusion.Mvc.Chart;]                                                                           |
|                                                                                                                                                                                                |
| [using][ Syncfusion.Mvc.Shared;]                                                                          |
|                                                                                                                                                                                                |
| [using][ Syncfusion.Windows.Forms.Chart;][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Add the action displayed below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [///][ ][\<summary\>][]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [///][ Used to create the simple chart][]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [///][ ][\</summary\>][]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [///][ ][\<returns\>][View page, it displays the Chart][\</returns\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [public][ [ActionResult] ][SimpleChart][()]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [return][ View();]                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [}[]]                                                                                                                                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Run the application.

[] 

The following screenshot illustrates the sample output.

[] 

[] 

{border="0"}

*[]* 

Figure 56: Chart control added to the application

***[]*** 

[]{#related-topics}

