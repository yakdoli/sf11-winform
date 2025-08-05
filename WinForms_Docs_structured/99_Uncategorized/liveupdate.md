---
title: liveupdate.md
original_path: WinForms_Docs/99_Uncategorized/liveupdate.md
created_at: 2025-08-05
---






#### Live Update {#live-update style="tab-stops: 0pt"}

The TimePicker control allows you to update the time value in the time picker on mouseover.

 

**Properties**

+-----------------------+-----------------------+----------------------------------------------------------------------------------------+
| **Name**              | **Type**              | **Description**                                                                        |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------+
| LiveUpdate            | Boolean               | Gets/sets the Boolean value indicating whether to update the value on mouseover event. |
|                       |                       |                                                                                        |
|                       | Default: true         |                                                                                        |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------+

 

You can enable this property in the following two ways:

 

**[Using Builder]**

[The following steps guide you in configuring the live update feature through Builder.]

[1.   In the **view**, invoke the **TimePicker** helper with the time picker ID as the first argument and enable the **LiveUpdate** method with the desired option as an argument.]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().TimePicker([\"TimePicker\"])][.Value([\"10:10:10\"])] |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [.Format([\"hh:mm:ss tt\"]).**LiveUpdate**([true]).AutoFormat([Skins].Midnight)]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [ [ %\>]]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [   ][]                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[][] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**[ ]                                                                                          |
|                                                                                                                                                                                     |
| [@(][Html.Syncfusion().TimePicker([\"TimePicker)]] |
|                                                                                                                                                                                     |
| [.Format([\"hh:mm:ss tt\"]).AutoFormat([Skins].Midnight)]                          |
|                                                                                                                                                                                     |
| [.**LiveUpdate**([true])][)]                          |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [   ]                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[2.   Run the application.]

**[]** 

**[Using Properties Model]**

[The following steps will guide you in setting the **LiveUpdate** property through the properties model.]

[1.   In the **controller**, create an instance of **TimePickerModel**, define the **LiveUpdate** property and pass the instance through **view-specific data** to the **view** as given below.]

 

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
| [              myModel.Format= [\"hh:mm:ss tt\"];]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                           |
|                         [myModel.AutoFormat=[Skins].Midnight;]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                           |
|                         [myModel.**LiveUpdate**= [true];]                                                                                                                                                                                           |
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

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                                                     |
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

Figure 286: LiveUpdate Property Applied to a Time Picker

 

 

[]{#related-topics}

