---
title: scatterconnecttype.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\scatterconnecttype.md
created_at: 2025-07-03
---






#### ScatterConnectType {#scatterconnecttype style="tab-stops: 0pt"}

**[]** 

Specifies the connection type of the Scatter Charts.

[] 


+---------------------------------------+-----------------------------------------------+
| **[]**              |
|                                                                                       |
| Details                                                                               |
+---------------------------------------+-----------------------------------------------+
| Possible Values                       | None - Scatter Connect Type will be none.     |
|                                       |                                               |
|                                       | Line - Scatter Connect Type will be Line.     |
|                                       |                                               |
|                                       | Spline - Scatter Connect Type will be spline. |
+---------------------------------------+-----------------------------------------------+
| Default Value                         | None                                          |
+---------------------------------------+-----------------------------------------------+
| 2D / 3D Limitations                   | No                                            |
+---------------------------------------+-----------------------------------------------+
| Applies to Chart Element              | All series                                    |
+---------------------------------------+-----------------------------------------------+
| Applies to Chart Types                | Scatter Chart                                 |
+---------------------------------------+-----------------------------------------------+


**[]** 

**[]** 

Scatter Line Chart

**[]** 

Optionally, you can connect the points in the series through straight lines using the **ScatterConnectType** property as shown below.

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                    |
|                                                                                                                   |
| **[]**                                                          |
|                                                                                                                   |
| [series.ScatterConnectType = [ScatterConnectType].Line;] |
+-------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                               |
|                                                                                                                  |
| **[]**                                                         |
|                                                                                                                  |
| [series.ScatterConnectType = [ScatterConnectType].Line] |
+------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 183: Scatter Line Chart

[] 

Scatter Spline Chart

**[]** 

Alternatively, you can connect the points in the series through splines using the **ScatterConnectType** property as shown below.

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                      |
|                                                                                                                     |
| **[]**                                                            |
|                                                                                                                     |
| [series.ScatterConnectType = [ScatterConnectType].Spline;] |
|                                                                                                                     |
| [series.ScatterSplineTension = 1; [// Default is 0]]      |
+---------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                 |
|                                                                                                                    |
| **[]**                                                           |
|                                                                                                                    |
| [series.ScatterConnectType = [ScatterConnectType].Spline] |
|                                                                                                                    |
| [series.ScatterSplineTension = 1 \'[ Default is 0]]      |
+--------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 184: Scatter Spline Chart

**[]** 

See Also

[] 

[Scatter Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p142} 

[]{#related-topics}

