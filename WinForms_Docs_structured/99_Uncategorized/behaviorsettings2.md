---
title: behaviorsettings2.md
original_path: WinForms_Docs/99_Uncategorized/behaviorsettings2.md
created_at: 2025-08-05
---






##### Behavior Settings {#behavior-settings style="tab-stops: 0pt"}

[] 

Text settings for browser and the control

[] 

Custom text can be displayed on the browser window by setting the text to the **StatusBarText** property.

The **GroupingText** allows you to enter some text like a caption to the callback panel when the text is set to this property.

[] 


+-----------------------------------+------------------------------------------------------------------+
|                                   |                                                                  |
|                                   |                                                                  |
| Property                          | Description                                                      |
+-----------------------------------+------------------------------------------------------------------+
| GroupingText                      | Specifies the groupbox text around the control\'s contents.      |
+-----------------------------------+------------------------------------------------------------------+
| StatusBarText                     | Specifies the text to display on the status bar during callback. |
+-----------------------------------+------------------------------------------------------------------+


[] 

Alignment Settings

[] 

To change the direction in which the data is displayed, the **Direction** property can be set, which displays the entire contents (i.e., along with the GroupingText and ShowLoadingIndicatorOnCallback if set) inside the callback panel in the specified direction.

 

To align only the controls placed inside callback panel, the **Horizontal** property can be set.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                    |
|                                   |                                                                                                                    |
| Property                          | Description                                                                                                        |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Direction                         | Specifies direction for the text in the panel. Default value is NotSet. The options included are as follows:       |
|                                   |                                                                                                                    |
|                                   |                                                                                                                    |
|                                   |                                                                                                                    |
|                                   | [·      ]NotSet                                                                       |
|                                   |                                                                                                                    |
|                                   | [·      ]LeftToRight                                                                  |
|                                   |                                                                                                                    |
|                                   | [·      ]RightToLeft                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+
| HorizontalAlign                   | Specifies whether to align the content horizontally. Default value is NotSet. The options included are as follows: |
|                                   |                                                                                                                    |
|                                   |                                                                                                                    |
|                                   |                                                                                                                    |
|                                   | [·      ]NotSet                                                                       |
|                                   |                                                                                                                    |
|                                   | [·      ]Left                                                                         |
|                                   |                                                                                                                    |
|                                   | [·      ]Right                                                                        |
|                                   |                                                                                                                    |
|                                   | [·      ]Center                                                                       |
|                                   |                                                                                                                    |
|                                   | [·      ]Justify                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+


[] 

ScrollBar settings

[] 

Scrollbars can be displayed for the control automatically when the contents exceed the height of the callback panel by setting the **Scrollbars** property to one of the options.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                                                                             |
|                                   |                                                                                                                                                                             |
| Property                          | Description                                                                                                                                                                 |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ScrollBars                        | Specifies whether to include scroll bars automatically for the panel when the text exceeds the panel\'s height. Default value is None. The options included are as follows: |
|                                   |                                                                                                                                                                             |
|                                   | [·      ]None                                                                                                                                  |
|                                   |                                                                                                                                                                             |
|                                   | [·      ]Horizontal                                                                                                                            |
|                                   |                                                                                                                                                                             |
|                                   | [·      ]Vertical                                                                                                                              |
|                                   |                                                                                                                                                                             |
|                                   | [·      ]Both                                                                                                                                  |
|                                   |                                                                                                                                                                             |
|                                   | [·      ]Auto                                                                                                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

[]{#related-topics}

