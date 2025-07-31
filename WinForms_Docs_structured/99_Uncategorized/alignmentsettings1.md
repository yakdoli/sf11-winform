---
title: alignmentsettings1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\alignmentsettings1.md
created_at: 2025-07-03
---






##### Alignment Settings {#alignment-settings style="tab-stops: 0pt"}

[] 

Setting the parent control

[] 

The waiting popup can be set to any html element or to the browser window using **PositionParent** property.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| PositionParent                    | Specifies whether to position the popup relative to the screen or to the control. Default value is Element. The options included are as follows: |
|                                   |                                                                                                                                                  |
|                                   | [·      ]Element                                                                                                    |
|                                   |                                                                                                                                                  |
|                                   | [·      ]Screen                                                                                                     |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                       |
|                                                                                                                        |
| **[]**                                                                             |
|                                                                                                                        |
| [WaitingPopup1.PositionParent = [PopupPositionType].Element;] |
+------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                          |
|                                                                                                                                                           |
| **[]**                                                                                                                |
|                                                                                                                                                           |
| [Private][ WaitingPopup1.PositionParent = PopupPositionType.Element] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Aligning popup to the parent control

[] 

The position of the popup can be set to one of the pre-defined options, such that the popup element will be aligned to that position with respect to the parent control. Setting **Alignment**, will align the popup control with respect to the browser, when parent is set as **Screen**, and it\'ll be aligned relative to the parent control, when set to **Element**.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Alignment                         | Specifies the alignment of the popup relative to the parent control. Default value is TopLeft. The options included are as follows: |
|                                   |                                                                                                                                     |
|                                   | [·      ]TopLeft                                                                                       |
|                                   |                                                                                                                                     |
|                                   | [·      ]TopCenter                                                                                     |
|                                   |                                                                                                                                     |
|                                   | [·      ]TopRight                                                                                      |
|                                   |                                                                                                                                     |
|                                   | [·      ]BottomLeft                                                                                    |
|                                   |                                                                                                                                     |
|                                   | [·      ]BottomCenter                                                                                  |
|                                   |                                                                                                                                     |
|                                   | [·      ]BottomRight                                                                                   |
|                                   |                                                                                                                                     |
|                                   | [·      ]MiddleLeft                                                                                    |
|                                   |                                                                                                                                     |
|                                   | [·      ]MiddleCenter                                                                                  |
|                                   |                                                                                                                                     |
|                                   | [·      ]MiddleRight                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+


[] 

The distance along the X and Y axis from the control can be set using the **OffsetX** and **OffsetY** properties.

[] 


  ---------- --------------------------------------------------------------------------------------------
  Property   Description
  OffSetX    Specifies the distance from the X axis while aligning,  in pixel. The default value is 0.
  OffSetY    Specifies the distance from the Y axis while aligning,  in pixels. The default value is 0.
  ---------- --------------------------------------------------------------------------------------------


**[]** 

The alignment and offset properties can be set through code as given below.

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                     |
| **[]**                                                                          |
|                                                                                                                     |
| [WaitingPopup1.OffsetX = 50;]                                                   |
|                                                                                                                     |
| [WaitingPopup1.OffsetY = 20;]                                                   |
|                                                                                                                     |
| [WaitingPopup1.Alignment = [PopupAlignType].MiddleCentre;] |
+---------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                       |
|                                                                                                                                                        |
| **[]**                                                                                                             |
|                                                                                                                                                        |
| [Private][ WaitingPopup1.OffsetX = 50]                            |
|                                                                                                                                                        |
| [Private][ WaitingPopup1.OffsetY = 20]                            |
|                                                                                                                                                        |
| [Private][ WaitingPopup1.Alignment = PopupAlignType.MiddleCentre] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Content Alignment

[] 

Text can be set for the control through **GroupingText** property which will appear on top of the control.

The contents inside the control can be aligned by using the **HorizontalAlign** property and the flow direction of the contents can be changed using the **Direction** property.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
| Direction                         | Specifies the text flow direction. Default value is NotSet. The options included are as follows:            |
|                                   |                                                                                                             |
|                                   | [·      ]NotSet                                                                |
|                                   |                                                                                                             |
|                                   | [·      ]LeftToRight                                                           |
|                                   |                                                                                                             |
|                                   | [·      ]RightToLeft                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
| GroupingText                      | Specifies the groupbox text around the popup control\'s content.                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+
| HorizontalAlign                   | Specifies the alignment of the popup content. Default value is NotSet. The options included are as follows: |
|                                   |                                                                                                             |
|                                   | [·      ]Left                                                                  |
|                                   |                                                                                                             |
|                                   | [·      ]Center                                                                |
|                                   |                                                                                                             |
|                                   | [·      ]Right                                                                 |
|                                   |                                                                                                             |
|                                   | [·      ]Justify                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------+


[] 

Programmatically the properties can be set as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                      |
|                                                                                                                       |
| **[]**                                                                            |
|                                                                                                                       |
| [WaitingPopup1.Direction = [ContentDirection].RightToLeft;]  |
|                                                                                                                       |
| [WaitingPopup1.GroupingText = [\"Process Loading\....\"];] |
|                                                                                                                       |
| [WaitingPopup1.HorizontalAlign = [HorizontalAlign].Center;]  |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                |
|                                                                                                                                                                                 |
| **[]**                                                                                                                                      |
|                                                                                                                                                                                 |
| [Private][ WaitingPopup1.Direction = ContentDirection.RightToLeft]                         |
|                                                                                                                                                                                 |
| [Private][ WaitingPopup1.GroupingText = [\"Process Loading\....\"]] |
|                                                                                                                                                                                 |
| [Private][ WaitingPopup1.HorizontalAlign = HorizontalAlign.Center]                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

