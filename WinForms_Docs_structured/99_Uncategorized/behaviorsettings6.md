---
title: behaviorsettings6.md
original_path: WinForms_Docs/99_Uncategorized/behaviorsettings6.md
created_at: 2025-08-05
---






##### Behavior Settings {#behavior-settings style="tab-stops: 0pt"}

[] 

Display Speed

[] 

The **CharDelay** property can be set to change the speed of the ticker control. It accepts the duration in milliseconds. By default it will take the value as **100 milliseconds**. The speed with which it displays decreases with increase in value.

[] 

AutoStart

[] 

The text can be set such that it would display character by character, on page load by enabling the **AutoStart** property.

[] 

Loop and Delay Settings

[] 

The text display can be repeated in cycles by setting the **Loop** property, thereby iteratively displaying the text.

The time interval for which the full text should be displayed before recurring the next loop can be quantified using **LineDelay** property. By default it will take the value as **100 milliseconds**.

[] 


  ----------- -------------------------------------------------------------------------------------------------------------------
  Property    Description
  AutoStart   Specifies whether the scroll should automatically start when the page gets loaded. Default value is true.
  CharDelay   Specifies the interval between each character. Default value is 100.
  LineDelay   Specifies the time interval before starting to repeat the loop. Default value is 100.
  Loop        Specifies whether to repeat the slides after a complete tour of slides has been exhibited. Default value is true.
  ----------- -------------------------------------------------------------------------------------------------------------------


[] 

Programmatically the properties can be set as follows.

[] 

+--------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                         |
|                                                                                                        |
| [    ]                               |
|                                                                                                        |
| [ticker1.CharDelay = 100;]                         |
|                                                                                                        |
| [ticker1.AutoStart = [true];] |
|                                                                                                        |
| [ticker1.Loop = [true];]      |
|                                                                                                        |
| [ticker1.LineDelay = 200;]                         |
+--------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                         |
|                                                                                                        |
| [    ]                               |
|                                                                                                        |
| [ticker1.CharDelay = 100;]                         |
|                                                                                                        |
| [ticker1.AutoStart = [true];] |
|                                                                                                        |
| [ticker1.Loop = [true];]      |
|                                                                                                        |
| [ticker1.LineDelay = 200;]                         |
+--------------------------------------------------------------------------------------------------------+

[]{#p472} 

[]{#related-topics}

