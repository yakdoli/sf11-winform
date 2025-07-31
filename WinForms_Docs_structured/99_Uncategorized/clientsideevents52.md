---
title: clientsideevents52.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents52.md
created_at: 2025-07-03
---








  









### Client-Side Events {#client-side-events style="TEXT-JUSTIFY: inter-ideograph; TEXT-ALIGN: justify; tab-stops: 0pt"}

The TimePicker control supports client-side events.

**Client-Side Events**

+-----------------------+-----------------------+--------------------------------------------------------------+
| **Name**              | **Arguments**         | **Description**                                              |
+-----------------------+-----------------------+--------------------------------------------------------------+
| OnLoad                | Sender                | This event is triggered before the dialog is closed.         |
|                       |                       |                                                              |
|                       |                       |                                                              |
+-----------------------+-----------------------+--------------------------------------------------------------+
| OnClose               | Sender, args          | This event is triggered after the time picker is closed.     |
|                       |                       |                                                              |
|                       |                       |                                                              |
+-----------------------+-----------------------+--------------------------------------------------------------+
| OnOpen                | Sender, args          | This event is triggered while the time picker is opened.     |
|                       |                       |                                                              |
|                       |                       |                                                              |
+-----------------------+-----------------------+--------------------------------------------------------------+
| OnChange              | Sender, args          | This event is triggered while the time picker value changes. |
|                       |                       |                                                              |
|                       |                       |                                                              |
+-----------------------+-----------------------+--------------------------------------------------------------+

 

**[Using Builder]**

The following steps will guide you on handling client-side events through Builder.

1.   In the **view**, invoke the **TimePicker** helper with the time picker ID as the first argument and enable the **OnOpen**, **OnClose**, **Onload**, and **OnChange **events with the respective handlers as shown below.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                             |
| [\<%][=][ Html.Syncfusion().TimePicker([\"TimePicker\"])] |
|                                                                                                                                                                                                                                             |
| [          .Value([\"10:10:10\"])]                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [          .ClientSideEvents(events=\>{]                                                                                                                                                   |
|                                                                                                                                                                                                                                             |
| [              events.OnOpen([\"OnOpen\"]);]                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [              events.OnLoad([\"OnLoad\"]);]                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [              events.OnChange([\"OnChange\"]);]                                                                                                                   |
|                                                                                                                                                                                                                                             |
| [              events.OnClose([\"OnClose\"]);]                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [          })]**[]**                                                                                                                                   |
|                                                                                                                                                                                                                                             |
| **[ ]**[%\>][ ]                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[][] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**[ ]                                                                                            |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [@(][Html.Syncfusion().TimePicker([\"TimePicker\"])] |
|                                                                                                                                                                                       |
| [          .Value([\"10:10:10\"])]                                                                           |
|                                                                                                                                                                                       |
| [          .ClientSideEvents(events=\>{]                                                                                             |
|                                                                                                                                                                                       |
| [              events.OnOpen([\"OnOpen\"]);]                                                                 |
|                                                                                                                                                                                       |
| [              events.OnLoad([\"OnLoad\"]);]                                                                 |
|                                                                                                                                                                                       |
| [              events.OnChange([\"OnChange\"]);]                                                             |
|                                                                                                                                                                                       |
| [              events.OnClose([\"OnClose\"]);})][)]  |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Define the callback methods in the script to handle the specified events.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**[]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                 |
| [        [function] OnLoad(inst) {]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [             //inst - instance of TimePicker object][]                                                                                   |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnOpen(inst) {]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of TimePicker object]]                                                                                                                |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnClose(inst) {]                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of TimePicker object]]                                                                                                                |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnChange(inst, args) {]                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of TimePicker object]]                                                                                                                |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentValue -- currently selected value]]                                                                                           |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_previousValue - PreviousValue of time                                                  picker.]]                                     |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Using Properties Model       

[The following steps will guide you in handling client-side events through the properties model.]

[1.  In the **controller**, create an instance of **TimePickerModel**, define the **ClientSideOnLoded**, **ClientSideOnClick**, **ClientSideOnMouseOver**, and **ClientSideOnMouseOut** events and pass the instance through **view-specific data** to the **view** as given below.]

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                                                                 |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| [public][ [ActionResult] Index()]                                                                                             |
|                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| [            [TimePicker][Model] myModel = [new] [TimePicker][Model]();]          |
|                                                                                                                                                                                                                                            |
| [            myModel.][ClientSideEvents.OnLoad][ =[\"OnLoad\"];]       |
|                                                                                                                                                                                                                                            |
| [            myModel.][ ClientSideEvents.OnOpen][ =[\"OnOpen\"];]      |
|                                                                                                                                                                                                                                            |
| [            myModel.][ ClientSideEvents.OnClose][ =[\"OnClose\"];]    |
|                                                                                                                                                                                                                                            |
| [            myModel.][ ClientSideEvents.OnChange][ =[\"OnChange\"];]  |
|                                                                                                                                                                                                                                            |
| [            ViewData\[[\"myModel\"]\] = myModel;]                                                                                                                             |
|                                                                                                                                                                                                                                            |
| [            [return] View();]                                                                                                                                                    |
|                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().TimePicker([\"TimePicker\"],([TimePickerModel])ViewData\[[\"]][myModel][\"][\])]**[ ]**[%\>][ ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Define the callback methods in the script to handle the specified events.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**[]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                 |
| [        [function] OnLoad(inst) {]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [             //inst - instance of TimePicker object][]                                                                                   |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnOpen(inst) {]                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of TimePicker object]]                                                                                                                |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnClose(inst) {]                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of TimePicker object]]                                                                                                                |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnChange(inst, args) {]                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of TimePicker object]]                                                                                                                |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentValue -- currently selected value]]                                                                                           |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_previousValue - PreviousValue of time                                                  picker.]]                                     |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Run the application.

[You can observe the callback methods being triggered when the corresponding events are raised.][]

[]{#related-topics}

