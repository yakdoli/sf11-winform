---
title: clientsideevents29.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents29.md
created_at: 2025-07-03
---






#### Client Side Events {#client-side-events style="tab-stops: 0pt"}

Date picker supports client side event handling.

 

Events

+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+------------------------------+
| Name              | Description                                                                                                                                                                                                                                                      | Arguments         | Reference Link               |
+===================+==================================================================================================================================================================================================================================================================+===================+==============================+
| BeforeShow        | This event is triggered just before the datepicker is displayed. Can be a function that takes an input field and current datepicker instance and returns an options object to update the datepicker with                                                         | input, inst       | \-[] |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+------------------------------+
| BeforeShowDay     | This event is triggered for each day in the datepicker before it is displayed. The function takes a date as a parameter and must return an array with:                                                                                                           | date              | \-[] |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
|                   | \[0\] equal to true/false indicating whether or not this date is selectable                                                                                                                                                                                      |                   |                              |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
|                   | \[1\] equal to a CSS class name(s) or \'\' for the default presentation, and                                                                                                                                                                                     |                   |                              |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
|                   | \[2\] an optional popup tooltip for this date                                                                                                                                                                                                                    |                   |                              |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+------------------------------+
| OnChangeMonthYear | This event is triggered when the datepicker moves to a new month and/or year. The function receives the selected year, month (1-12), and the datepicker instance as parameters. [T]his refers to the associated input field. | year, month, inst | \-[] |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
|                   |                                                                                                                                                                                                                                                                  |                   | []   |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+------------------------------+
| OnClose           | This event is triggered when  when a datepicker is closed, whether or not a date is selected                                                                                                                                                                     | dateText, inst    | \-[] |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
|                   |                                                                                                                                                                                                                                                                  |                   | []   |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+------------------------------+
| OnSelect          | This event is triggered when the datepicker is selected. The function receives the selected date as text and the datepicker instance as parameters. [T]his refers to the associated input field.                             | dateText, inst    | \-[] |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
|                   |                                                                                                                                                                                                                                                                  |                   | []   |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
|                   |                                                                                                                                                                                                                                                                  |                   |                              |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+------------------------------+

 

User Builder

The following section explains the handling of the client side events of the *Date Picker* through Builder.

1.   In **View**, invoke the date picker helper followed by the the **BeforeShow, OnChangeMonthYear, OnClose** and **OnSelect** methods with the desired handlers as arguments.

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().DatePicker([\"myDatPicker\"])] |
|                                                                                                                                                                                                                                |
| [.**BeforeShow([\"BeforeShowHandler\"])**]                                                                                                                         |
|                                                                                                                                                                                                                                |
| **[.OnChangeMonthYear([\"MonthYearHandler\"])]**                                                                                                                   |
|                                                                                                                                                                                                                                |
| **[.OnClose([\"CloseHandler\"])]**                                                                                                                                 |
|                                                                                                                                                                                                                                |
| **[.OnSelect([\"SelectHandler\"])]**[%\>]                                                                  |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [\@{][ ][Html.Syncfusion().DatePicker([\"myDatPicker\"])] |
|                                                                                                                                                                                                                                |
| [.**BeforeShow([\"BeforeShowHandler\"])**]                                                                                                                         |
|                                                                                                                                                                                                                                |
| **[.OnChangeMonthYear([\"MonthYearHandler\"])]**                                                                                                                   |
|                                                                                                                                                                                                                                |
| **[.OnClose([\"CloseHandler\"])]**                                                                                                                                 |
|                                                                                                                                                                                                                                |
| **[.OnSelect([\"SelectHandler\"])]**[.Render();][}]                    |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   In the **Javascript**, define the handlers as given below:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [function] BeforeShowHandler(input, inst) {]                                                                                                                 |
|                                                                                                                                                                                                                                |
| [            [//input - input field as the DOM element]]                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [//inst  - instance of the date picker client side object model]]                                                                                   |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] MonthYearHandler(year, month, inst) {]                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//year  - current year of the date picker]]                                                                                                        |
|                                                                                                                                                                                                                                |
| [            [//month - current month of the date picker]]                                                                                                       |
|                                                                                                                                                                                                                                |
| [            [//inst  - instance of the date picker client side object model]]                                                                                   |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] CloseHandler(dateText, inst) {]                                                                                                                   |
|                                                                                                                                                                                                                                |
| [            [//dateText  - current date as text]]                                                                                                               |
|                                                                                                                                                                                                                                |
| [            [//inst  - instance of the date picker client side object model]]                                                                                   |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] SelectHandler(dateText, inst) {]                                                                                                                  |
|                                                                                                                                                                                                                                |
| [            [//dateText  - current date as text]]                                                                                                               |
|                                                                                                                                                                                                                                |
| [            [//inst  - instance of the date picker client side object model]]                                                                                   |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [      [\</][script][\>]]                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

**[]** 

**[Using Properties Model]**

The following section explains the handling of the client side events of the *DatePpicker* using the *Properties* model.

1.   In the **Controller**, create an instance of the **DatePickerModel**, define the **BeforeShow, OnChangeMonthYear, OnClose** and **OnSelect** properties and pass the instance through **View Specific Data** to **View** as given below.**

*[[[]]]{.underline}* 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                      |
|                                                                                                                                                                               |
| **[]**                                                                                                                                    |
|                                                                                                                                                                               |
| [public][ [ActionResult] Index()]                                |
|                                                                                                                                                                               |
| [        {]                                                                                                                               |
|                                                                                                                                                                               |
| [            [//create an instance of DatePickerModel]]                                                             |
|                                                                                                                                                                               |
| [            [DatePickerModel] myModel = [new] [DatePickerModel]();] |
|                                                                                                                                                                               |
| [            **myModel.BeforeShow = [\"BeforeShowHandler\"];**]                                                   |
|                                                                                                                                                                               |
| **[            myModel.OnChangeMonthYear = [\"MonthYearHandler\"];]**                                             |
|                                                                                                                                                                               |
| **[            myModel.OnClose = [\"CloseHandler\"];]**                                                           |
|                                                                                                                                                                               |
| **[            myModel.OnSelect = [\"SelectHandler\"];]**                                                         |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [            [//pass the instance through view data to the view]]                                                   |
|                                                                                                                                                                               |
| [            ViewData\[[\"myDatePicker\"]\] = myModel;]                                                           |
|                                                                                                                                                                               |
| [            [return] View();]                                                                                       |
|                                                                                                                                                                               |
| [        }]                                                                                                                               |
|                                                                                                                                                                               |
| []                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, invoke the date picker helper with the **View Data** key as the Control ID.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPXView\[aspx\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().DatePicker([\"myDatePicker\"]) [%\>]] |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                            |
|                                                                                                                                                                                                                       |
| [\@{][ Html.Syncfusion().DatePicker([\"myDatePicker\"]).Render();[}]] |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In the Javascript, define the handlers as given below:

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [function] BeforeShowHandler(input, inst) {]                                                                                                                 |
|                                                                                                                                                                                                                                |
| [            [//input - input field as the DOM element]]                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [//inst  - instance of the date picker client side object model]]                                                                                   |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] MonthYearHandler(year, month, inst) {]                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//year  - current year of the date picker]]                                                                                                        |
|                                                                                                                                                                                                                                |
| [            [//month - current month of the date picker]]                                                                                                       |
|                                                                                                                                                                                                                                |
| [            [//inst  - instance of the date picker client side object model]]                                                                                   |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] CloseHandler(dateText, inst) {]                                                                                                                   |
|                                                                                                                                                                                                                                |
| [            [//dateText  - current date as text]]                                                                                                               |
|                                                                                                                                                                                                                                |
| [            [//inst  - instance of the date picker client side object model]]                                                                                   |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] SelectHandler(dateText, inst) {]                                                                                                                  |
|                                                                                                                                                                                                                                |
| [            [//dateText  - current date as text]]                                                                                                               |
|                                                                                                                                                                                                                                |
| [            [//inst  - instance of the date picker client side object model]]                                                                                   |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [      [\</][script][\>]]                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

You can observe the handlers getting invoked on the corresponding event triggers.

[]{#related-topics}

