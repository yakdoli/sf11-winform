---
title: conceptsandfeaturesofthetimepickercontrol.md
original_path: WinForms_Docs/02_Concepts/conceptsandfeaturesofthetimepickercontrol.md
created_at: 2025-08-05
---








  









### Concepts and Features of the TimePicker Control {#concepts-and-features-of-the-timepicker-control style="tab-stops: 0pt"}

 

Properties

+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| **Name**              | **Type**                                 | **Description**                                                                            |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| Value                 | DateTime?                                | Gets/sets the value for the time picker.                                                   |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| MinValue              | DateTime                                 | Gets/sets the minimum time that can be selected in the time picker.                        |
|                       |                                          |                                                                                            |
|                       | Default: Today                           |                                                                                            |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| MaxValue              | DateTime                                 | Gets/sets the maximum time that can be selected in the time picker.                        |
|                       |                                          |                                                                                            |
|                       | Default: Today                           |                                                                                            |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| Format                | String                                   | Gets/sets the Format option for the time picker.                                           |
|                       |                                          |                                                                                            |
|                       | Default: DateTimeFormat.ShortTimePattern |                                                                                            |
|                       |                                          |                                                                                            |
|                       |  "h:mm tt"                               |                                                                                            |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| Enable                | Bool                                     | Gets/sets the bool value indicating whether to enable/disable the time picker.             |
|                       |                                          |                                                                                            |
|                       | Default: true                            |                                                                                            |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| MinuteInterval        | Int                                      | Defines the interval for minutes.                                                          |
|                       |                                          |                                                                                            |
|                       | Default: 15                              |                                                                                            |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| SecondInterval        | Int                                      | Defines the interval for seconds.                                                          |
|                       |                                          |                                                                                            |
|                       | Default: 15                              |                                                                                            |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| AutoFormat            | Enum Skins                               | Gets/sets AutoFormat.                                                                      |
|                       |                                          |                                                                                            |
|                       | Default: Office2007Blue                  |                                                                                            |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| ClientSideEvents      | Class                                    | Gets/sets the client-side event functions for the TimePicker control.                      |
|                       |                                          |                                                                                            |
|                       |                                          |                                                                                            |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| HtmlAttributes        | IDictionary\<string,object\>             | Defines the HTML attributes for the TimePicker control.                                    |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| LiveUpdate            | Boolean                                  | Gets/sets the Boolean value indicating whether to update the value on the mouseover event. |
|                       |                                          |                                                                                            |
|                       | Default: true                            |                                                                                            |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+
| OpenOn                | String:                                  | Define the trigger event for loading the time picker.                                      |
|                       |                                          |                                                                                            |
|                       | Default: mouseover                       |                                                                                            |
+-----------------------+------------------------------------------+--------------------------------------------------------------------------------------------+

 

The various features of the TimePicker control are invariably associated with the properties of the control. This section will help you understand the use of these properties in detail, and will help you on how to implement, disable, or customize them in the control.

The features of the TimePicker control are:

1.  Value and format

2.  Minimum value and maximum value

3.  Minute interval and second interval

4.  Live update

5.  Enable and AutoFormat

More:















