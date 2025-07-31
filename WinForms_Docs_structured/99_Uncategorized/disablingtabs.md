---
title: disablingtabs.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\disablingtabs.md
created_at: 2025-07-03
---






#### Disabling Tabs {#disabling-tabs style="tab-stops: 0pt"}

 

The tab control allows you to disable one or more tabs when loading.

Property

 

  ---------- ------------------------------------------------ ------------------ ----------------------------------------------------------------------- ------------
  Name       Description                                      Type of property   Value it accepts                                                        Dependency
  Disabled   Used to disable one or more tabs when loading.   int\[\]            An array of integers representing the indices of the tabs to disable.   NA
  ---------- ------------------------------------------------ ------------------ ----------------------------------------------------------------------- ------------

 

Using Builder

 

The following steps explain how to disable one or more tabs through the builder when loading.

1.   In **View**, create the contents of the tab with *ul* and *li* (for headers) and *div* tags (for content), and invoke the tab helper with the control ID as the first argument, followed by the **Disabled** method with the indices of the tab content to be disabled as argument.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][div][ [id][=\"tabContents\"] [style][=\"][visibility][: hidden\"\>]]                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][ul][\>]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#tools\"\>]Essential Tools[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#chart\"\>]Essential Chart[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#grid\"\>]Essential Grid[\</][a][\>\</][li][\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][ul][\>]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"tools\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Tools is a collection of user-interface components used to create interactive ASP.NET MVC applications.]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"chart\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Chart is a business-oriented charting component. Essential Chart features an advanced styles architecture that makes complex multi-level formatting very easy.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"grid\"\>]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential MVC Grid offers a full-featured grid control with extensive support for grouping and displaying hierarchical data.]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [       [\</][div][\>]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().Tab([\"myTab\"]).TargetControlId([\"tabContents\"])]                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| **[.Disabled([new] [int]\[\]{1,2})]**[%\>]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][div][ [id][=\"tabContents\"] [style][=\"][visibility][: hidden\"\>]]                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][ul][\>]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#tools\"\>]Essential Tools[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#chart\"\>]Essential Chart[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#grid\"\>]Essential Grid[\</][a][\>\</][li][\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][ul][\>]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"tools\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Tools is a collection of user-interface components used to create interactive ASP.NET MVC applications.]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"chart\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Chart is a business-oriented charting component. Essential Chart features an advanced styles architecture that makes complex multi-level formatting very easy.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"grid\"\>]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential MVC Grid offers a full-featured grid control with extensive support for grouping and displaying hierarchical data.]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [       [\</][div][\>]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\@{][ Html.Syncfusion().Tab([\"myTab\"]).TargetControlId([\"tabContents\"])]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| **[.Disabled([new] [int]\[\]{1,2})]**[.Render();][}]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

**[]** 

Using Properties Model

 

The following steps explain how to disable one or more tabs, through the properties model, when loading.

1.   In the controller, create an instance of **TabModel**.**

2.   Define the **Disabled** property and pass the instance through the view-specific data to the view.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                        |
|                                                                                                                                                                 |
| [public][ [ActionResult] Index()]                  |
|                                                                                                                                                                 |
| [        {]                                                                                                                 |
|                                                                                                                                                                 |
| [            [//Create an instance of TabModel.]]                                                     |
|                                                                                                                                                                 |
| [            [TabModel] myModel = [new] [TabModel]();] |
|                                                                                                                                                                 |
| [            myModel.TargetControlId = [\"tabContents\"];]                                          |
|                                                                                                                                                                 |
| [            **myModel.Disabled = [new] [int]\[\] { 1, 2 };**]                    |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [            [//Pass the instance through the view data to the view.]]                                |
|                                                                                                                                                                 |
| [            ViewData\[[\"myTab\"]\] = myModel;]                                                    |
|                                                                                                                                                                 |
| [            [return] View();]                                                                         |
|                                                                                                                                                                 |
| [        }]                                                                                                                 |
|                                                                                                                                                                 |
| []                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

***[[[]]]{.underline}*** 

3.   In **View**, create the contents of the tabs with *ul* and *li* (for headers) and *div* tags (for content), and invoke the tab helper with the view data key as the control ID.**

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[Aspx\]**                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][div][ [id][=\"tabContents\"] [style][=\"][visibility][: hidden\"\>]]                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][ul][\>]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#tools\"\>]Essential Tools[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#chart\"\>]Essential Chart[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#grid\"\>]Essential Grid[\</][a][\>\</][li][\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][ul][\>]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"tools\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Tools is a collection of user-interface components used to create interactive ASP.NET MVC applications.]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"chart\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Chart is a business-oriented charting component. Essential Chart features an advanced styles architecture that makes complex multi-level formatting very easy.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"grid\"\>]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential MVC Grid offers a full-featured grid control with extensive support for grouping and displaying hierarchical data.]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [       [\</][div][\>]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().Tab([\"myTab\"])[%\>]]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| **[[[]]]{.underline}**                                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

*[[]]{.underline}* 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][div][ [id][=\"tabContents\"] [style][=\"][visibility][: hidden\"\>]]                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][ul][\>]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#tools\"\>]Essential Tools[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#chart\"\>]Essential Chart[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#grid\"\>]Essential Grid[\</][a][\>\</][li][\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][ul][\>]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"tools\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Tools is a collection of user-interface components used to create interactive ASP.NET MVC applications.]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"chart\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Chart is a business-oriented charting component. Essential Chart features an advanced styles architecture that makes complex multi-level formatting very easy.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"grid\"\>]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential MVC Grid offers a full-featured grid control with extensive support for grouping and displaying hierarchical data.]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [       [\</][div][\>]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\@{][ Html.Syncfusion().Tab([\"myTab\"]).Render();[}]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| **[[[]]]{.underline}**                                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

***[[[]]]{.underline}*** 

4.   Build and run the application.

The following figure shows the output of the tab control with disabled headers.

 

{border="0"}

Figure 266:Tab with Disabled Headers

 

[]{#related-topics}

