---
title: customizingtheappearance.md
original_path: WinForms_Docs/02_Concepts/customizingtheappearance.md
created_at: 2025-08-05
---






#### Customizing the appearance {#customizing-the-appearance style="tab-stops: 0pt"}

You can customize the appearance of the progress bar using Builder, or the properties model, as shown in the code snippets below.\
\


Note: The Progress Bar doesn't support the built-in skins as other controls do, since it is designed using the Canvas element in HTML 5.


 

In order for you to get familiar with the properties we use here, refer to the [properties table].

1.   In **View**, invoke the ProgressBar helper with the control ID as an argument and define the appearance properties of the ProgressBar.

 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[View\]]**                                                                              |
|                                                                                                                                 |
| [\<%][{]                                                        |
|                                                                                                                                 |
| [          Html.Syncfusion().ProgressBar(][\"Progress\"][)] |
|                                                                                                                                 |
| [          .Value(75)]                                                                                    |
|                                                                                                                                 |
| [          .ProgressBarBorderColor(][\"Black\"][)]          |
|                                                                                                                                 |
| [          .ProgressBarColor(][\"green\"][)]                |
|                                                                                                                                 |
| [          .ProgressBarFontFamily(][\"Arial\"][)]           |
|                                                                                                                                 |
| [          .ProgressBarTextColor(][\"White\"][)]            |
|                                                                                                                                 |
| [          .ProgressBarTextFontSize(18)]                                                                  |
|                                                                                                                                 |
| [          .BackgroundColor(][\"white\"][)]                 |
|                                                                                                                                 |
| [          .BorderColor(][\"black\"][)]                     |
|                                                                                                                                 |
| [          .Height(22)]                                                                                   |
|                                                                                                                                 |
| [          .Width(500)]                                                                                   |
|                                                                                                                                 |
| [          .Render();]                                                                                    |
|                                                                                                                                 |
| [      } [%\>]]                                                               |
|                                                                                                                                 |
|                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                           |
|                                                                                                                                 |
| []                                                                                    |
|                                                                                                                                 |
| [\@{][] |
|                                                                                                                                 |
| [          Html.Syncfusion().ProgressBar(][\"Progress\"][)] |
|                                                                                                                                 |
| [          .Value(75)]                                                                                    |
|                                                                                                                                 |
| [          .ProgressBarBorderColor(][\"Black\"][)]          |
|                                                                                                                                 |
| [          .ProgressBarColor(][\"green\"][)]                |
|                                                                                                                                 |
| [          .ProgressBarFontFamily(][\"Arial\"][)]           |
|                                                                                                                                 |
| [          .ProgressBarTextColor(][\"White\"][)]            |
|                                                                                                                                 |
| [          .ProgressBarTextFontSize(18)]                                                                  |
|                                                                                                                                 |
| [          .BackgroundColor(][\"white\"][)]                 |
|                                                                                                                                 |
| [          .BorderColor(][\"black\"][)]                     |
|                                                                                                                                 |
| [          .Height(22)]                                                                                   |
|                                                                                                                                 |
| [          .Width(500)]                                                                                   |
|                                                                                                                                 |
| [          .Render();]                                                                                    |
|                                                                                                                                 |
| [}][]   |
|                                                                                                                                 |
| []                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application.

 

Using PropertiesModel

1.   In the controller, create an instance of the ProgressBarPropertiesModel

2.   Define the appearance properties and pass the instance through the view-specific data to the view.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Controller\]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [public][ ][ActionResult][ Index()]                                                                                                                                |
|                                                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [            ][ProgressBarPropertiesModel][ model = ][new][ ][ProgressBarPropertiesModel][();] |
|                                                                                                                                                                                                                                                             |
| [            model.Value = 75;]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [            model.BackgroundColor = ][\"white\"][;]                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [            model.BorderColor = ][\"black\"][;]                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [            model.ProgressBarBorderColor = ][\"Black\"][;]                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [            model.ProgressBarColor = ][\"green\"][;]                                                                                                                                   |
|                                                                                                                                                                                                                                                             |
| [            model.ProgressBarFontFamily = ][\"Arial\"][;]                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [            model.ProgressBarTextColor = ][\"White\"][;]                                                                                                                               |
|                                                                                                                                                                                                                                                             |
| [            model.ProgressBarTextFontSize = 18;]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [            model.Width = 500;]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [            model.Height = 22;]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [            ViewData\[][\"Progress\"][\] = model;]                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [            ][return][ View();]                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In View, invoke the ProgressBar helper with the view data key as the control ID.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[View\]]**                                                                                                                                                         |
|                                                                                                                                                                                                            |
| [    [\<%]{ Html.Syncfusion().ProgressBar(][\"Progress\"][).Render(); } [%\>]] |
|                                                                                                                                                                                                            |
|                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [\@{][]                                                                                                |
|                                                                                                                                                                                                                                |
| [          Html.Syncfusion().ProgressBar(][\"Progress\"][).Render(); ] |
|                                                                                                                                                                                                                                |
| [}][]                                                                                                  |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build the output. You will get the following result:

 

{border="0"}

Figure 175: Progress Bar with customized appearance**[]**

 

[]{#related-topics}

