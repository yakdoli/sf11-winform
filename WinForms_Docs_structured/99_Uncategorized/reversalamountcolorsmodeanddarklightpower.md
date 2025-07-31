---
title: reversalamountcolorsmodeanddarklightpower.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\reversalamountcolorsmodeanddarklightpower.md
created_at: 2025-07-03
---






#### ReversalAmount, ColorsMode and DarkLightPower {#reversalamount-colorsmode-and-darklightpower style="tab-stops: 0pt"}

**[]** 

ReversalAmount:

ReversalAmount gets or sets the reversal amount for the Financial charts.


+------------------------------+------------------------------------------------------------------------------+
| Details                                                                                                     |
+------------------------------+------------------------------------------------------------------------------+
| Possible values              | Any numeric value.                                                           |
+------------------------------+------------------------------------------------------------------------------+
| Default value                | 1                                                                            |
+------------------------------+------------------------------------------------------------------------------+
| 2D/3D limitations            | No                                                                           |
+------------------------------+------------------------------------------------------------------------------+
| Application to chart element | Any series                                                                   |
+------------------------------+------------------------------------------------------------------------------+
| Application to chart types   | Kagi chart, Three Line Break chart, Point and Figure chart, and Renko chart. |
+------------------------------+------------------------------------------------------------------------------+


**[]** 

{border="0"}

Figure 235: Renko chart with default ReversalAmount value

[] 

{border="0"}

Figure 236: Renko chart with ReversalAmount value 3.0

ColorsMode

ColorsMode gets or sets the ColorsMode of the boxes in the Financial chart types.


+-------------------------------------+---------------------------------------------------------------------+
| Details                                                                                                   |
+-------------------------------------+---------------------------------------------------------------------+
| Possible values                     | **DarkLight** - Draws series data points as a DarkLight colorsmode. |
|                                     |                                                                     |
|                                     | **Fixed** - Draws series data points as a Fixed colorsmode.         |
|                                     |                                                                     |
|                                     | **Mixed** - Draws series data points as a Mixed colorsmode.         |
+-------------------------------------+---------------------------------------------------------------------+
| Default value                       | Fixed                                                               |
+-------------------------------------+---------------------------------------------------------------------+
| 2D/3D limitations                   | None                                                                |
+-------------------------------------+---------------------------------------------------------------------+
| Application to chart element        | All series                                                          |
+-------------------------------------+---------------------------------------------------------------------+
| Application to chart types          | Renko chart (Financial chart)                                       |
+-------------------------------------+---------------------------------------------------------------------+


**[]** 

{border="0"}

Figure 237: Renko chart with ColorsMode DarkLight

{border="0"}

Figure 238: Renko chart with ColorsMode Mixed

DarkLightPower

DarkLightPower gets or sets the intensity of the dark and light colors used in the DarkLight color mode.

 


+------------------------------+--------------------------------+
| Details                                                       |
+------------------------------+--------------------------------+
| Possible values              | Ranges from 0 to 255 bytes.    |
+------------------------------+--------------------------------+
| Default value                | 100                            |
+------------------------------+--------------------------------+
| 2D/3D limitations            | No                             |
+------------------------------+--------------------------------+
| Application to chart element | All series                     |
+------------------------------+--------------------------------+
| Application to chart types   | Renko chart (Financial charts) |
+------------------------------+--------------------------------+


 

{border="0"}

Figure 239: Renko chart with DarklightPower 200

[] 

Implementation:

Renko chart with ColorsMode, DarkLightPower, and ReversalAmount can be created through two ways:

[·      ]Builder

[·      ]ChartModel

More:







