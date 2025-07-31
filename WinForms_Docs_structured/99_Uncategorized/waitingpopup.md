---
title: waitingpopup.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\waitingpopup.md
created_at: 2025-07-03
---








  









### Waiting Pop-up {#waiting-pop-up style="tab-stops: 0pt"}

[] 

The Schedule control supports a waiting pop-up during callback. A transparent background and a waiting pop-up image are used to provide feedback about the callback process.

This section discusses how the waiting pop-up can be displayed in the Schedule control.

All functionalities in the Schedule control like dragging appointments, navigating resources and dates, and so on, can be performed via callbacks. On callback, you can disable the Schedule control and display a transparent background by using the **ShowWaitingPopupOnCallback** property given below.

[] 


  ---------------------------- ----------------------------------------------------------------------------------------------------------------------------------
  Schedule Property            Description
  ShowWaitingPopupOnCallback   Specifies whether a \"Waiting\...\" text and image should be shown on the disabled element when the callback is being processed.
  ---------------------------- ----------------------------------------------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][syncfusion][:][Schedule][ [ID][=\"Schedule1\"] [runat][=\"server\"] [ShowWaitingPopupOnCallback][=\"true\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][syncfusion][:][Schedule][\>]                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                          |
|                                                                                                           |
| []                                                                    |
|                                                                                                           |
| [Schedule1.ShowWaitingPopupOnCallback = [true];] |
+-----------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                         |
|                                                                                                          |
| []                                                                   |
|                                                                                                          |
| [Schedule1.ShowWaitingPopupOnCallback = [True]] |
+----------------------------------------------------------------------------------------------------------+

[] 

{border="0"}[]

[] 

{border="0"}[]

Figure 36: Waiting Pop-up Images

[]{#p29} 

[]{#related-topics}

