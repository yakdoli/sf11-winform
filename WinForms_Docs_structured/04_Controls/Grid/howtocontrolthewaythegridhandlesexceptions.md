---
title: howtocontrolthewaythegridhandlesexceptions.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtocontrolthewaythegridhandlesexceptions.md
created_at: 2025-07-03
---








  









### How to Control the Way the Grid Handles Exceptions {#how-to-control-the-way-the-grid-handles-exceptions style="tab-stops: 0pt"}

[] 

Introduction

[] 

Syncfusion.Windows.Forms.ExceptionManager has static members which, you can use to control how the grid handles exceptions.

[] 

Example

[] 

To suspend the grid\'s error handling, try.

[] 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                         |
|                                                                                                                        |
| []                                                                                               |
|                                                                                                                        |
| [// Suspend Grid\'s Error Handling.]                                 |
|                                                                                                                        |
| [Syncfusion.Windows.Forms.ExceptionManager.SuspendCatchExceptions()] |
+------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                     |
|                                                                                                                        |
| []                                                                                               |
|                                                                                                                        |
| [\' Suspend Grid\'s Error Handling.]                                 |
|                                                                                                                        |
| [Syncfusion.Windows.Forms.ExceptionManager.SuspendCatchExceptions()] |
+------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: You can also subscribe to an event (Syncfusion.Windows.Forms.ExceptionManager.ExceptionCatched) to get any exception thrown and handle them by yourself or re-throw them.


 

[]{#p614} 

 

[]{#related-topics}

