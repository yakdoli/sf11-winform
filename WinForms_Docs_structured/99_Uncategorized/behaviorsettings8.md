---
title: behaviorsettings8.md
original_path: WinForms_Docs/99_Uncategorized/behaviorsettings8.md
created_at: 2025-08-05
---






##### Behavior Settings {#behavior-settings style="tab-stops: 0pt"}

[] 

Showing / Hiding Popup

[] 

The WaitingPopup can be displayed by default when a page is loaded by enabling the **InitiallyShown** property or it can be invoked on user or system action.

 

The popup can be closed automatically, after some specific time interval by setting the **CloseTimeOut** property to the time interval.

[] 


  ---------------- ------------------------------------------------------------------------------------------------------------------------
  Property         Description
  CloseTimeOut     Specifies time, in milliseconds, after which to close the popup.
  InitiallyShown   Gets/sets boolean value, whether to display the control initially or after the page is loaded. Default value is false.
  ---------------- ------------------------------------------------------------------------------------------------------------------------


[] 

Programmatically the properties can be set as follows.

[] 

+---------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                  |
|                                                                                                   |
| **[]**                                                        |
|                                                                                                   |
| [WaitingPopup1.InitiallyShown = [true];] |
|                                                                                                   |
| [WaitingPopup1.CloseTimeOut = 2000;]                          |
+---------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                            |
|                                                                                                                                                             |
| **[]**                                                                                                                  |
|                                                                                                                                                             |
| [Private][ WaitingPopup1.InitiallyShown = [True]] |
|                                                                                                                                                             |
| [Private][ WaitingPopup1.CloseTimeOut = 2000]                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Disabling control

[] 

When the popup is displayed on some user action indicating the progress of some process, to avoid the user from accessing any of the control, the id of that control can be set to the **DisabledOnShowElementID** property of the popup control.

 

Also optionally color can be applied, which will appear like a mask over the parent control when **DisabledBackgroundColor** is set.

[] 


  ------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Property                  Description
  DisabledOnShowElementID   Specifies the id of the control to be disabled when the popup is shown. If no id is specified the entire screen will be disabled when the waiting popup is shown.
  ------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

Programmatically the properties can be set as follows.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                     |
| **[]**                                                                                          |
|                                                                                                                                     |
| [WaitingPopup1.DisableOnShowElementID = [\"panel1\"];]                   |
|                                                                                                                                     |
| [WaitingPopup1.DisabledBackgroundColor = System.Drawing.[Color].Cornsilk;] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                            |
|                                                                                                                                                                             |
| **[]**                                                                                                                                  |
|                                                                                                                                                                             |
| [Private][ WaitingPopup1.DisableOnShowElementID = [\"panel1\"]] |
|                                                                                                                                                                             |
| [Private][ WaitingPopup1.DisabledBackgroundColor = System.Drawing.Color.Cornsilk]      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

