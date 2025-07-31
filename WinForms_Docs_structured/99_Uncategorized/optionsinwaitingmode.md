---
title: optionsinwaitingmode.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\optionsinwaitingmode.md
created_at: 2025-07-03
---






##### Options in Waiting Mode {#options-in-waiting-mode style="tab-stops: 0pt"}

[] 

[] 

ProgressBar control when used in WaitingMode, the following properties can be set.

[] 

Text and width

[] 

The **WaitingBarText** property when set to some text, will be displayed on the control. The **WaitingBarWidth** can be used to control the width of the progress bar.

 

The progress of the value in the progress bar control can be customized and set to any image indicating the progress of the process update. For this set the custom image to the **WaitingImageUrl** property.

[] 


  ----------------- ---------------------------------------------------------------------------------------------------------------
  Property          Description
  WaitingBarText    Specifies the text to be displayed on the control, when the ProgressStyle is set to WaitingMode.
  WaitingBarWidth   Specifies the width of the control, in pixels, when ProgressStyle is set to WaitingMode. Default value is 30.
  ----------------- ---------------------------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                |
| []                                                            |
|                                                                                                                |
| [ProgressBar1.WaitingBarText = [\"Progress\...\"];] |
|                                                                                                                |
| [ProgressBar1.WaitingBarWidth = 30;]                                       |
+----------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                         |
|                                                                                                                                                                          |
| []                                                                                                                      |
|                                                                                                                                                                          |
| [Private][ ProgressBar1.WaitingBarText = [\"Progress\...\"]] |
|                                                                                                                                                                          |
| [Private][ ProgressBar1.WaitingBarWidth = 30]                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Image

[] 

The progress of the value in the progress bar control can be customized and set to any image indicating the progress of the process update. For this set the custom image to the **WaitingImageUrl** property.

[] 


  ----------------- ---------------------------------------------------------------------------------------------------
  Property          Description
  WaitingImageUrl   Specifies the path of the image to use for the control, when ProgressStyle is set to WaitingMode.
  ----------------- ---------------------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                         |
| []                                                                     |
|                                                                                                                         |
| [ProgressBar1.WaitingImageUrl = [\"images/star_blue.png\"];] |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                   |
| []                                                                                                                               |
|                                                                                                                                                                                   |
| [Private][ ProgressBar1.WaitingImageUrl = [\"images/star_blue.png\"]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Refreshing the control

[] 

The control can be updated every time after the specified **WaitingInterval**. This updates and refreshes the content without postback.

[] 


  ----------------- -----------------------------------------------------------------------------------------------------------------------------------------------------
  Property          Description
  WaitingInterval   Specifies the frequency in which the control should update itself without a postback, when ProgressStyle is set to WaitingMode. Default value is 1.
  ----------------- -----------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------+
| **[\[C#\]]**                         |
|                                                                          |
| []                      |
|                                                                          |
| [ProgressBar1.WaitingInterval = 10;] |
+--------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                   |
|                                                                                                                                    |
| []                                                                                |
|                                                                                                                                    |
| [Private][ ProgressBar1.WaitingInterval = 10] |
+------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

