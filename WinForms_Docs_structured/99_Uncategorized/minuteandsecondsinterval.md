---
title: minuteandsecondsinterval.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\minuteandsecondsinterval.md
created_at: 2025-07-03
---






#### Minute and Seconds Interval {#minute-and-seconds-interval style="tab-stops: 0pt"}

The TimePicker control allows you to set the minute and second intervals to be displayed in the time picker.

 

**Properties**

+-----------------------+-----------------------+-----------------------------------+
| **Name**              | **Type**              | **Description**                   |
+-----------------------+-----------------------+-----------------------------------+
| MinuteInterval        | Int                   | Defines the interval for minutes. |
|                       |                       |                                   |
|                       | Default: 15           |                                   |
+-----------------------+-----------------------+-----------------------------------+
| SecondInterval        | Int                   | Defines the interval for seconds. |
|                       |                       |                                   |
|                       | Default: 15           |                                   |
+-----------------------+-----------------------+-----------------------------------+

 

 

You can enable this property in the following two ways:

 

**[Using Builder]**

[The following steps guide you in configuring the minute and second interval through Builder.]

[1.   In the **view**, invoke the **TimePicker** helper with the time picker ID as the first argument and enable the **MinuteInterval** and **SecondInterval** methods with the desired options as the arguments.]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().TimePicker([\"TimePicker\"])][.Value([\"10:10:10\"])] |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [.Format([\"hh:mm:ss tt\"]).**MinuteInterval**(10).**SecondInterval**(15)]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [.AutoFormat([Skins].Midnight)]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [ [ %\>]]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [   ][]                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[][] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**[ ]                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| [@(][Html.Syncfusion().TimePicker([\"TimePicker\"]).Value([\"10:10:10\"])] |
|                                                                                                                                                                                                                                     |
| [.Format([\"hh:mm:ss tt\"]).**MinuteInterval**(10).**SecondInterval**(15) ]                                                                                |
|                                                                                                                                                                                                                                     |
| [.AutoFormat([Skins].Midnight)][)]                                                                 |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [   ]                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[2.   Run the application.]

**[]** 

**[Using Properties Model]**

[The following steps will guide you in setting the minute and second interval through the properties model.]

[1.   In the **controller**, create an instance of **TimePickerModel**, define the **MinuteInterval** and **SecondInterval** properties, and pass the instance through **view-specific data** to the **view** as given below.]

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                           |
| [public][ [ActionResult] Index()]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                           |
| [        {]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                           |
| [            [TimePickerModel] myModel = [new] [TimePickerModel]();]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                           |
| [            myModel**.**Value **=**][ ][new][ [DateTime](2012,01,01,10,10,10);] |
|                                                                                                                                                                                                                                                                                                                           |
| [              myModel.Format= [\"hh:mm:ss tt\"];]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                           |
|                         [myModel.AutoFormat=[Skins].Midnight;]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                           |
|                         [myModel.MinuteInterval= 10;]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                           |
| [              myModel.SecondInterval= 15;]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                           |
| [            ViewData\[[\"myTimePickerModel\"]\] = myModel;]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                           |
| [            [return] View();]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                           |
| [        }]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[2.   In the **view**, invoke the **TimePicker** helper with the time picker ID as the first argument and view data key as the second argument. ]

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ASPX]**[]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().TimePicker([\"TimePicker\"],[\"myTimePickerModel\"])[%\>]] |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[{border="0"}]**[Note: The second argument of the above TimePicker helper should match the view data key from the controller to fetch the properties.]***

[3.   Run the application.]

 

{border="0"}

Figure 285: Minute and Seconds Interval Properties Applied to TimePicker

 

[]{#related-topics}

