---
title: skins2.md
original_path: WinForms_Docs/99_Uncategorized/skins2.md
created_at: 2025-08-05
---








  









### Skins {#skins style="tab-stops: 0pt"}

Essential Chart has several built-in skins that make styling extremely easy. It is also possible to easily format the data displayed in the chart. **[]**

 

Essential Chart for ASP.NET MVC contains 14 built-in skins to easily customize the appearance. Essential Chart\'s AutoFormat property allows you to apply predefined skins to the control. Some of the available skins are illustrated in detail in the Built-in Skin Styles topic.

[] 

[] 


+------------------------------+-----------------------------------+
| Details                                                          |
+------------------------------+-----------------------------------+
| Possible values              | ChartModelSkins Enumerable values |
+------------------------------+-----------------------------------+
| Default value                | None                              |
+------------------------------+-----------------------------------+
| 2D/3D limitations            | No                                |
+------------------------------+-----------------------------------+
| Application to chart element | All series                        |
+------------------------------+-----------------------------------+
| Application to chart types   | All chart types.                  |
+------------------------------+-----------------------------------+


 

This property affects the ChartAreaInterior, ChartInterior, and BackInterior properties.

 

The following screenshot shows the 14 ChartModel skins:

[] 

{border="0"}

Figure 304: Chart Skins

[] 

**[]** 

 

Properties


+-------------+----------------------------+-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| Property    | Description                | Property Type               | Value it Accepts                                                                                                                                                  | Any Other Dependencies/Sub-properties Associated |
+=============+============================+=============================+===================================================================================================================================================================+==================================================+
| Skins       | Sets the ChartModel Skins. | [enum] | [ChartModelSkins][.Almond]                      | [NA]                     |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.Blueberry]                   |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.Monochrome]                  |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.VS2010]                      |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.Office2007Blue]              |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.Office2007Black]             |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.Blend]                       |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.Midnight]                    |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.Marble]                      |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.Office2007Silver]            |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.Sandune]                     |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.Olive]                       |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.Vista]                       |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.Turquoise]                   |                                                  |
|             |                            |                             |                                                                                                                                                                   |                                                  |
|             |                            |                             | [ChartModelSkins][.None][] |                                                  |
+-------------+----------------------------+-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+


Applying skins in any chart can be created through two ways:

[·      ]Builder

[·      ]ChartModel

More:







