---
title: behaviorsettings7.md
original_path: WinForms_Docs/99_Uncategorized/behaviorsettings7.md
created_at: 2025-08-05
---






##### Behavior Settings {#behavior-settings style="tab-stops: 0pt"}

[] 

Behavior Settings

[] 

The popup window can be initially displayed when the **InitiallyShown** property is enabled. This shows the popup by default until clicking anywhere on the page.

 

The popup control can be associated with any parent control, i.e., it can be popped up along any of the control in that page, by setting the **ParentControlID** property to the id of that parent control.

[] 


  -------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
           Property          Description
  InitiallyShown             Specifies whether to show the popup initially. Default value is false.
  ParentControlID            Client side id of the element to which PopupContainer is bound. With this property set, when you call ShowPopup in the client, the *PositionHorizontal* and *PositionVertical* properties will dictate how the popup will be positioned.
  -------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                   |
| **[]**                                                                        |
|                                                                                                                   |
| [PopupControlContainer1.InitiallyShown = [true];]        |
|                                                                                                                   |
| [PopupControlContainer1.ParentControlID = [\"div1\"];] |
+-------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                            |
|                                                                                                                                                                             |
| **[]**                                                                                                                                  |
|                                                                                                                                                                             |
| [Private][ PopupControlContainer1.InitiallyShown = [True]]        |
|                                                                                                                                                                             |
| [Private][ PopupControlContainer1.ParentControlID = [\"div1\"]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Popup Alignment

[] 

The alignment can be set for the popup control relative to the parent control using the **PopupHorizontal** and **PopupVertical** properties.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| PositionHorizontal                | The horizontal position relative to the parent control. Default value is Near. The options included are as follows:  |
|                                   |                                                                                                                      |
|                                   | [·      ]Near                                                                           |
|                                   |                                                                                                                      |
|                                   | [·      ]Far                                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| PositionVertical                  | The vertical position relative to the parent control. Default value is Bottom. The options included are as follows:  |
|                                   |                                                                                                                      |
|                                   | [·      ]Bottom                                                                         |
|                                   |                                                                                                                      |
|                                   | [·      ]Top                                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                      |
|                                                                                                                                       |
| **[]**                                                                                            |
|                                                                                                                                       |
| [PopupControlContainer1.PositionHorizontal = [PopupPositionHorizontal].Far;] |
|                                                                                                                                       |
| [PopupControlContainer1.PositionVertical = [PopupPositionVertical].Bottom;]  |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                         |
|                                                                                                                                                                          |
| **[]**                                                                                                                               |
|                                                                                                                                                                          |
| [Private][ PopupControlContainer1.PositionHorizontal = PopupPositionHorizontal.Far] |
|                                                                                                                                                                          |
| [Private][ PopupControlContainer1.PositionVertical = PopupPositionVertical.Bottom]  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Text and Content Alignment

[] 

The contents inside the popup control can be aligned by using the **Direction** and the **HorizontalAlign** properties. Direction allows you to specify the direction in which the text should be displayed inside the popup control and the HorizontalAlign allows you to set how the contents inside the control should be aligned.

**GroupingText** when set, appears on the top of the popup control. While applying Direction property to the control, the grouping text will also change it\'s text flow.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                     |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Direction                         | Specifies the direction of the text in the panel. Default value is NotSet. The options included are as follows: |
|                                   |                                                                                                                 |
|                                   | [·      ]NotSet                                                                    |
|                                   |                                                                                                                 |
|                                   | [·      ]LeftToRight                                                               |
|                                   |                                                                                                                 |
|                                   | [·      ]RightToLeft                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| GroupingText                      | Specifies the head text for the control.                                                                        |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+
| HorizontalAlign                   | Specifies the alignment for the content. Default value is NotSet. The options included are as follows:          |
|                                   |                                                                                                                 |
|                                   | [·      ]NotSet                                                                    |
|                                   |                                                                                                                 |
|                                   | [·      ]Left                                                                      |
|                                   |                                                                                                                 |
|                                   | [·      ]Center                                                                    |
|                                   |                                                                                                                 |
|                                   | [·      ]Right                                                                     |
|                                   |                                                                                                                 |
|                                   | [·      ]Justify                                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                               |
| **[]**                                                                                    |
|                                                                                                                               |
| [PopupControlContainer1.HorizontalAlign = [HorizontalAlign].Left;]   |
|                                                                                                                               |
| [PopupControlContainer1.Direction = [ContentDirection].LeftToRight;] |
|                                                                                                                               |
| [PopupControlContainer1.GroupingText = [\"Header Text\"];]         |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                |
|                                                                                                                                                                                 |
| **[]**                                                                                                                                      |
|                                                                                                                                                                                 |
| [Private][ PopupControlContainer1.HorizontalAlign = HorizontalAlign.Left]                  |
|                                                                                                                                                                                 |
| [Private][ PopupControlContainer1.Direction = ContentDirection.LeftToRight]                |
|                                                                                                                                                                                 |
| [Private][ PopupControlContainer1.GroupingText = [\"Header Text\"]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Scrollbars

[] 

Scrollbars can be set for the control, to allow scrolling through the contents, when the contents exceeds the height or width of the control. There are options that could be chosen to apply scrollbars as required.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+
| ScrollBars                        | Specifies the type of scroll bars to set. Default value is None. The options included are as follows: |
|                                   |                                                                                                       |
|                                   | [·      ]None                                                            |
|                                   |                                                                                                       |
|                                   | [·      ]Horizontal                                                      |
|                                   |                                                                                                       |
|                                   | [·      ]Vertical                                                        |
|                                   |                                                                                                       |
|                                   | [·      ]Both                                                            |
|                                   |                                                                                                       |
|                                   | [·      ]Auto                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------+


[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                      |
|                                                                                                                       |
| **[]**                                                                            |
|                                                                                                                       |
| [PopupControlContainer1.ScrollBars = [ScrollBars].Vertical;] |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                   |
|                                                                                                                                                                                                    |
| **[]**                                                                                                                                                         |
|                                                                                                                                                                                                    |
| **[Private][ PopupControlContainer1]**[.ScrollBars = ScrollBars.Vertical] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

