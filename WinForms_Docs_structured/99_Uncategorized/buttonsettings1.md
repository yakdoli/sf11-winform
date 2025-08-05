---
title: buttonsettings1.md
original_path: WinForms_Docs/99_Uncategorized/buttonsettings1.md
created_at: 2025-08-05
---






#### Button Settings {#button-settings style="tab-stops: 0pt"}

[] 

The buttons settings of the CommandBar control are given below.

[] 

Close and DropDown Button

[] 

The close button of CommandBar gets displayed when it is in the float state whereas the dropdown button gets displayed both in the dock and float state.

[] 

Table 8: Button Settings


  ---------------------------- ---------------------------------------------------------------------------
  CommandBar Property          Description
  HideCloseButton              Determines whether the CommandBar will have a close button when floating.
  HideDropDownButton           Draws the CommandBar with / without the dropdown button.
  ---------------------------- ---------------------------------------------------------------------------


[] 


{border="0"}Note: Popup Menu can be displayed from the dropdown button of the CommandBar. Refer [Popup Menu] topic.


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [this][.commandBar1.HideCloseButton=[true];]    |
|                                                                                                                                                           |
| [this][.commandBar1.HideDropDownButton=[true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                     |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [Me][.commandBar1.HideCloseButton=[True]]    |
|                                                                                                                                                        |
| [Me][.commandBar1.HideDropDownButton=[True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 17: \"DropDown Button\" and \"Close Button\" of CommandBar in Float State

[] 

{border="0"}

[] 

Figure 18: \"DropDown Button\" of CommandBar in Dock State

[] 

The methods associated with the above properties is given below.

[] 

Table 9: Button Settings - Methods


  --------------------- --------------------------------------------------------------------
  Methods               Description
  GetCloseButtonState   Gets visual state for the close button of the floating CommandBar.
  GetDropDownState      Gets visual state for the dropdown button of the CommandBar.
  --------------------- --------------------------------------------------------------------


 

A sample which demonstrates the DropDown Button settings of the CommandBar control is available in the below sample installation path.

 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\CommandBars Package\\CommandBars

[]{#related-topics}

