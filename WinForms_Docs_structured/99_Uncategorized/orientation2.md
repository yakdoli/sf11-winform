---
title: orientation2.md
original_path: WinForms_Docs/99_Uncategorized/orientation2.md
created_at: 2025-08-05
---






#### Orientation {#orientation style="tab-stops: 0pt"}

You can set the orientation of the Progress bar, using the following code that implements the properties from the [properties table].

Using Builder

1.   In **View**, invoke the ProgressBar helper with the control ID as an argument, followed by the Orientation method, with the desired orientation as an argument.

 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[View\]]**                                                                                  |
|                                                                                                                                     |
| [ [\<%]{]                                                                         |
|                                                                                                                                     |
| [          Html.Syncfusion().ProgressBar(][\"Progress\"][)]     |
|                                                                                                                                     |
| [            .Orientation(][ProgressBarOrientation][.Vertical)] |
|                                                                                                                                     |
| [            .Width(250)]                                                                                     |
|                                                                                                                                     |
| [            .Render();]                                                                                      |
|                                                                                                                                     |
| [      } [%\>]]                                                                   |
|                                                                                                                                     |
|                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                           |
|                                                                                                                                 |
| []                                                                                    |
|                                                                                                                                 |
| [\@{][] |
|                                                                                                                                 |
| [       Html.Syncfusion().ProgressBar(][\"Progress\"][)]    |
|                                                                                                                                 |
| [       .Orientation(][ProgressBarOrientation][.Vertical)]  |
|                                                                                                                                 |
| [       .Width(250)]                                                                                      |
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

1.   In the controller, create an instance of the **ProgressBarPropertiesModel.**

2.   Define the Orientation property and pass the instance through the view-specific data to the view.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [public][ ][ActionResult][ Index()]                                                                                                                                |
|                                                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [            ][ProgressBarPropertiesModel][ model = ][new][ ][ProgressBarPropertiesModel][();] |
|                                                                                                                                                                                                                                                             |
| [            model.Orientation = ][ProgressBarOrientation][.Vertical;]                                                                                                                  |
|                                                                                                                                                                                                                                                             |
| [            model.Width = 250;]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [            ViewData\[][\"Progress\"][\] = model;]                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [            ][return][ View();]                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                 |
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

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                             |
| [\@{][]                                                                                             |
|                                                                                                                                                                                                                             |
| [       Html.Syncfusion().ProgressBar(][\"Progress\"][).Render(); ] |
|                                                                                                                                                                                                                             |
| [}][]                                                                                               |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application, the output will be as follows:

{border="0"}

Figure 173: ProgressBar with a vertical orientation**[]**

 

[]{#related-topics}

