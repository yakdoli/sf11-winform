---
title: customization4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customization4.md
created_at: 2025-07-03
---






#### Customization {#customization style="tab-stops: 0pt"}

The style of the TabControlExt control can be customized by the customization properties. The following table lists the details of the customization properties.

 

Table 17: Customization Properties


+----------------------------+------------------------------------------------------------------+---------------------+-----------------+
| Property                   | Description                                                      | Type                | Data Type       |
+----------------------------+------------------------------------------------------------------+---------------------+-----------------+
| TabItemSelectedBackground  | Used to set the background color of the selected tab item.       | Dependency property | Brush           |
|                            |                                                                  |                     |                 |
|                            |                                                                  |                     |                 |
+----------------------------+------------------------------------------------------------------+---------------------+-----------------+
| TabItemSelectedBorderBrush | Used to set the border color of the selected tab item.           | Dependency property | Brush           |
|                            |                                                                  |                     |                 |
|                            |                                                                  |                     |                 |
+----------------------------+------------------------------------------------------------------+---------------------+-----------------+
| TabItemSelectedForeground  | Used to set the foreground color of the selected tab item.       | Dependency property | Brush           |
|                            |                                                                  |                     |                 |
|                            |                                                                  |                     |                 |
+----------------------------+------------------------------------------------------------------+---------------------+-----------------+
| TabItemHoverBackground     | Used to set the background color of the tab item in Hover state. | Dependency property | Brush           |
|                            |                                                                  |                     |                 |
|                            |                                                                  |                     |                 |
+----------------------------+------------------------------------------------------------------+---------------------+-----------------+
| TabItemHoverBorderBrush    | Used to set the border color of the tab item in Hover state.     | Dependency property | Brush           |
|                            |                                                                  |                     |                 |
|                            |                                                                  |                     |                 |
+----------------------------+------------------------------------------------------------------+---------------------+-----------------+
| TabItemHoverForeground     | Used to set the foreground color of the tab item in Hover state. | Dependency property | Brush           |
|                            |                                                                  |                     |                 |
|                            |                                                                  |                     |                 |
+============================+==================================================================+=====================+=================+


 

The following code example shows how to use the customization properties in the TabControlExt control.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][sync][:][TabControlExt][ TabItemSelectedBackground][=\"Gold\"][ Height][=\"100\"][ Margin][=\"100\"][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                           [ TabItemSelectedBorderBrush][=\"BlueViolet\"] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                           [ TabItemSelectedForeground][=\"Black\"] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                           [ TabItemHoverBackground][=\"Goldenrod\"] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                           [ TabItemHoverBorderBrush][=\"BlueViolet\"] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                           [ TabItemHoverForeground][=\"Yellow\"\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                ][\<][sync][:][TabItemExt][ Header][=\"TabItem1\"/\>][]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                ][\<][sync][:][TabItemExt][ Header][=\"TabItem2\"/\>][]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                ][\<][sync][:][TabItemExt][ Header][=\"TabItem3\"/\>][              ][]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][sync][:][TabControlExt][\>]                                                                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following screenshot is the sample output for the above code example.

 

{border="0"}

Figure 1013: TabControlExt - Customization

 

[]{#related-topics}

