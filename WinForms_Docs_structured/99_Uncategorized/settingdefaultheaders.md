---
title: settingdefaultheaders.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\settingdefaultheaders.md
created_at: 2025-07-03
---






#### Setting Default Headers {#setting-default-headers style="tab-stops: 0pt"}

 

The tab control supports setting default headers that will be selected when loading.

Property

 

 


  ---------- ------------------------------------------------------------- ------------------ -------------------------------------------------------------------------------- ------------
  Name       Description                                                   Type of property   Value it accepts                                                                 Dependency
  Selected   Used to set the default header to be selected when loading.   int                A zero-indexed number representing the index of the tab header to be selected.   NA
  ---------- ------------------------------------------------------------- ------------------ -------------------------------------------------------------------------------- ------------


 

Using Builder

 

The following steps explain how to set the default header through the builder.

1.   In **View**, create the contents of the tab with *ul* and *li* (for headers) and *div* tags (for content) and invoke the tab helper with the control ID as the first argument, followed by the **Selected** method with the desired header's index as an argument.[]

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
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [       [\</][div][\>]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().Tab([\"myTab\"])]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [.TargetControlId([\"tabContents\"])]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [.**Selected(1)[%]**[\>]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

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
| [\@{][ Html.Syncfusion().Tab([\"myTab\"])]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [.TargetControlId([\"tabContents\"])]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [.**Selected(1)**.Render();**[}]**[]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

2.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain how to set default headers through the properties model.

1.   In the controller, create an instance of **TabModel**.**

2.   Set the **Selected** property and pass the instance through the **view-specific data** to the **View**.

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Controller\]]**                                                                                                       |
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
| [            myModel.Selected = 1;]                                                                                         |
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

[] 

3.   In **View**, create the contents of the tab with *ul* and *li* (for headers) and *div* tags (for content), and invoke the tab helper with the view data key as the control ID.**

*[[]]{.underline}* 

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
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [       [\</][div][\>]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().Tab([\"myTab\"])[%\>]]                                                                                                                                |
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
| [\@{][ Html.Syncfusion().Tab([\"myTab\"]).Render();[}]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

4.   Build and run the application.

[] 

After following the previous steps, the tab control will be loaded with the second tab selected and its content displayed.

{border="0"}

Figure 265:Tab with Default Header

*[]* 

[]{#related-topics}

