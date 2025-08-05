---
title: settingtheflowdirectionforfontlistcombobox.md
original_path: WinForms_Docs/99_Uncategorized/settingtheflowdirectionforfontlistcombobox.md
created_at: 2025-08-05
---






#### Setting the Flow Direction for FontListComboBox {#setting-the-flow-direction-for-fontlistcombobox style="tab-stops: 0pt"}

 

Flow Direction of the FontListComboBox is set by using the **FlowDirection** property.

 


+-----------------------------------+------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| FlowDirection                     | Sets the flow direction for the FontListComboBox control. The options provided are as follows. |
|                                   |                                                                                                |
|                                   | []           |
|                                   |                                                                                                |
|                                   | [·      ]LeftToRight                                              |
|                                   |                                                                                                |
|                                   | [·      ]RightToLeft                                              |
+-----------------------------------+------------------------------------------------------------------------------------------------+


 

Use the following code snippet to set this property.

 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                                              |
| []                                                                                       |
|                                                                                                                                              |
| [// Flow Direction from Left to Right]                                     |
|                                                                                                                                              |
| [fontlistcombobox1.FlowDirection = [FlowDirection].LeftToRight;] |
|                                                                                                                                              |
| []                                                                         |
|                                                                                                                                              |
| [// Flow Direction from Right to Left]                                     |
|                                                                                                                                              |
| [fontlistcombobox1.FlowDirection = [FlowDirection].RightToLeft;] |
+----------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p283} 

[]{#related-topics}

