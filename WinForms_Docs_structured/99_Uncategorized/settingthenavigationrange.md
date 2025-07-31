---
title: settingthenavigationrange.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\settingthenavigationrange.md
created_at: 2025-07-03
---






#### Setting the navigation range {#setting-the-navigation-range style="tab-stops: 0pt"}

Date Picker supports limiting the navigation range that the end-user can navigate.

 

Properties

 

+-------------+------------------------------------------------------------+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+-------------+
| Name        | Description                                                | Type of property                                                                                 | Value it accepts                                                                           | Dependency  |
+-------------+------------------------------------------------------------+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+-------------+
| MaxDate     | Used to define the maximum date, the calendar can navigate | [[struct]]{.UGHyperlink} | [DateTime].MinValue to [DateTime].MaxValue | NA          |
|             |                                                            |                                                                                                  |                                                                                            |             |
|             |                                                            |                                                                                                  |                                                                                            |             |
+-------------+------------------------------------------------------------+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+-------------+
| MinDate     | Used to define the minimum date, the calendar can navigate | [[struct]]{.UGHyperlink} | [DateTime].MinValue to [DateTime].MaxValue | NA          |
|             |                                                            |                                                                                                  |                                                                                            |             |
|             |                                                            |                                                                                                  |                                                                                            |             |
+-------------+------------------------------------------------------------+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+-------------+

*[[]]{.underline}* 

Using Builder

The following section explains the setting of the navigation range of the date picker the Builder.

1.   In **View**, invoke the date picker helper followed by the **MaxDate** and **MinDate** methods with the desired dates as arguments.

 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().DatePicker([\"myDatePicker\"])] |
|                                                                                                                                                                                                                                 |
| **[.MaxDate([DateTime].Now.AddMonths(3))]**                                                                                                                         |
|                                                                                                                                                                                                                                 |
| **[.MinDate([DateTime].Now.AddMonths(-3))]**[%\>]                                                           |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [\@{][ Html.Syncfusion().DatePicker([\"myDatePicker\"])]                                        |
|                                                                                                                                                                                                                     |
| **[.MaxDate([DateTime].Now.AddMonths(3))]**                                                                                                             |
|                                                                                                                                                                                                                     |
| **[.MinDate([DateTime].Now.AddMonths(-3)).]**[Render();][}] |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

2.   Build and run the application.

**[]** 

Using Properties Model

The following section explains the setting of the navigation range of the Date Picker using Properties model.

1.   In the Controller, create an instance of the DatePickerModel, set the **MaxDate** and **MinDate** properties and pass the instance through the **view specific data** to **View** as given below.**

 

*[[]]{.underline}* 

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
| [            myModel.MinDate = [DateTime].Now.AddMonths(-3);]                                                     |
|                                                                                                                                                                               |
| [            myModel.MaxDate = [DateTime].Now.AddMonths(3);]                                                      |
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
| []                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[[[]]]{.underline}* 

[] 

2.   In **View**, invoke the date picker helper with the view data key as the Control ID.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().DatePicker([\"myDatePicker\"]) [%\>]] |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                           |
|                                                                                                                                                                                                                      |
| [\@{][Html.Syncfusion().DatePicker([\"myDatePicker\"]).Render();[}]] |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

3.   Build and run the application.

A date picker will be rendered with its navigation restricted to the defined minimum and maximum dates.

 

[]{#related-topics}

