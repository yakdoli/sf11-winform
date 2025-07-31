---
title: axislabelcustomization.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\axislabelcustomization.md
created_at: 2025-07-03
---






#### Axis Label Customization {#axis-label-customization style="tab-stops: 0pt"}

 

The font family, font size and font style of the axis label can be set using the Font property along the respective axis. In case of column type chart, the axis label customization is carried along Y-axis whereas in case of bar type chart, the axis label customization is carried along X-axis.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| [this][.olapChart1.PrimaryYAxis.Font = [new] [Font]([\"Arial\"], 9f, [FontStyle].Underline);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [Me][.olapChart1.PrimaryYAxis.Font = [New] Font([\"Arial\"], 9f, [FontStyle].Underline)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 10: Axis label customization

[]{#related-topics}

