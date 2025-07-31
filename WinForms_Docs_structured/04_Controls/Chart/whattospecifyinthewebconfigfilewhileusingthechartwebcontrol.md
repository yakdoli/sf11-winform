---
title: whattospecifyinthewebconfigfilewhileusingthechartwebcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\whattospecifyinthewebconfigfilewhileusingthechartwebcontrol.md
created_at: 2025-07-03
---








  









## What to specify in the web.config file while using the ChartWebControl? {#what-to-specify-in-the-web.config-file-while-using-the-chartwebcontrol style="tab-stops: 0pt"}

[] 

When using the ChartWebControl and specifying the **OutputFormat** property to **Handler**, the user has to insert the following code after the globalization segment in the application\'s web.config file.

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XML\]]**                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][httpHandlers][\>]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [    [\<][add] [verb][=\"\*\"] [path][=\"syncfusion_generate.ashx\"] [type][=\"Syncfusion.Web.UI.WebControls.Chart.ChartWebHandler,Syncfusion.Chart.Web, Version=X.X.X.X, culture=Neutral,PublicKeyToken=3d67ed1f87d44c89\"/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][httpHandlers][\>]                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.


[]{#p278} 

[]{#related-topics}

