---
title: datetimepickerevents.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\datetimepickerevents.md
created_at: 2025-07-03
---






##### DateTimePicker Events {#datetimepicker-events style="tab-stops: 0pt"}

[]{#p326}[] 

Following are the events of DateTimePickerAdv control.

[] 


  ------------------------------ --------------------------------------------------------------------
  DateTimePickerAdv Properties   Description
  BeforePopup                    Handled just before the popup is displayed.
  BindableValueChanged           Handled when the BindingValue property is changed.
  CheckBoxCheckedChanged         Handled when the checked state of the Checkbox changes.
  OnPopup                        Handled when the popup is displayed.
  PopupClosed                    Handled when the popup is closed. It uses PopupClosedEventHandler.
  StretchDropDownImageChanged    Handled when the StretchDropDownImage property changes.
  ValueChanged                   Event is handled when the Value property changes.
  ------------------------------ --------------------------------------------------------------------


[] 

###### []{#p327}[]{#_PopupClosed_Event}3.3.3.2.4.1 PopupClosed Event {#popupclosed-event style="tab-stops: 0pt"}

[] 

This event is handled when the popup is closed. Using the PopupCloseType member of the PopupClosedEventHandler, we can identify the type of closing.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [private][ [void] dateTimePickerAdv1_PopupClosed([object] sender, [PopupClosedEventArgs] e)] |
|                                                                                                                                                                                                                                                  |
| [{            ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                  |
| [    [//Canceled - User cancels the updates if any.]]                                                                                                                                  |
|                                                                                                                                                                                                                                                  |
| [    [//Deactivated - If the user moves the focus to some other window]]                                                                                                               |
|                                                                                                                                                                                                                                                  |
| [    [//Done - If the user wants the changes to be applied to the control]]                                                                                                            |
|                                                                                                                                                                                                                                                  |
| [    [Console].WriteLine(e.PopupCloseType.ToString());]                                                                                                                                 |
|                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] dateTimePickerAdv1_PopupClosed([ByVal] sender [As] [Object], [ByVal] e [As] PopupClosedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                        |
| [    [\'Canceled - User cancels the updates if any. ]]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                        |
| [    [\'Deactivated - If the user moves the focus to some other window ]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                        |
| [    [\'Done - If the user wants the changes to be applied to the control ]]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                        |
| [    Console.WriteLine(e.PopupCloseType.ToString())]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

