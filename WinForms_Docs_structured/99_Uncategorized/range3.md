---
title: range3.md
original_path: WinForms_Docs/99_Uncategorized/range3.md
created_at: 2025-08-05
---






#### Range {#range style="tab-stops: 0pt"}

This feature allows you to set the minimum, maximum and the increment values of the ProgressBar.

The Minimum value specifies the value at which the progress bar shows the process to have started.

The Maximum value specifies the value at which the progress bar shows the process to have completed.

The Step value specifies the value at which the progress bar shows the next step of the process to have started---it is an increment value.

For more details, refer to the [properties table].

You can implement the range of the progress bar in the following ways:

Using Builder

1.   In **View**, invoke the ProgressBar helper with the control ID as an argument, followed by the range method, with the desired value as an argument.

 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[View\]]**                                                                              |
|                                                                                                                                 |
| [  [\<%]{]                                                                    |
|                                                                                                                                 |
| [          Html.Syncfusion().ProgressBar(][\"Progress\"][)] |
|                                                                                                                                 |
| [           .Maximum(100)]                                                                                |
|                                                                                                                                 |
| [           .Minimum(10)]                                                                                 |
|                                                                                                                                 |
| [           .Value(15)]                                                                                   |
|                                                                                                                                 |
| [           .StepValue(0)]                                                                                |
|                                                                                                                                 |
| [           .Render();]                                                                                   |
|                                                                                                                                 |
| [      } [%\>]]                                                               |
|                                                                                                                                 |
| []                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                           |
|                                                                                                                                 |
| []                                                                                    |
|                                                                                                                                 |
| [\@{][] |
|                                                                                                                                 |
| [       Html.Syncfusion().ProgressBar(][\"Progress\"][)]    |
|                                                                                                                                 |
| [       .Maximum(100)]                                                                                    |
|                                                                                                                                 |
| [       .Minimum(10)]                                                                                     |
|                                                                                                                                 |
| [       .Value(15)]                                                                                       |
|                                                                                                                                 |
| [       .StepValue(0)]                                                                                    |
|                                                                                                                                 |
| [       .Render();]                                                                                       |
|                                                                                                                                 |
| [}][]   |
|                                                                                                                                 |
| []                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application.

 

Using PropertiesModel

1.   In the controller, create an instance of the ProgressBarPropertiesModel

2.   Define the Range property and pass the instance through the view-specific data to the view.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [ ][public][ ][ActionResult][ Index()]                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [            ][ProgressBarPropertiesModel][ model = ][new][ ][ProgressBarPropertiesModel][();] |
|                                                                                                                                                                                                                                                             |
| [            model.Minimum = 10;]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [            model.Maximum = 100;]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [            model.Value = 15;]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [            model.StepValue = 0;]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [            ViewData\[][\"Progress\"][\] = model;]                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [            ][return][ View();]                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In View, invoke the ProgressBar helper with the view data key as the control ID

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[View\]]**                                                                                                                                                         |
|                                                                                                                                                                                                            |
| [    [\<%]{ Html.Syncfusion().ProgressBar(][\"Progress\"][).Render(); } [%\>]] |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| [\@{][]                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [               ][Html.Syncfusion().ProgressBar(][\"Progress\"][).Render(); ] |
|                                                                                                                                                                                                                                                                              |
| [}][]                                                                                                                                                |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application, the output will be as follows:

 

{border="0"}

Figure 172: ProgressBar with range set

 

**[]** 

[]{#related-topics}

