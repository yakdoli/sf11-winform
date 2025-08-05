---
title: syncfusionthemes3.md
original_path: WinForms_Docs/02_Concepts/syncfusionthemes3.md
created_at: 2025-08-05
---






##### Syncfusion Themes {#syncfusion-themes style="tab-stops: 0pt"}

 

The tab control supports fourteen built-in Syncfusion themes to enhance the control's look and feel.**

**[]** 

**[Properties]**

**[]** 

 

+-------------+--------------------------------------+------------------+--------------------------------------------------------------+-------------+
| Name        | Description                          | Type of property | Value it accepts                                             | Dependency  |
+-------------+--------------------------------------+------------------+--------------------------------------------------------------+-------------+
| AutoFormat  | Used to define the Syncfusion theme. | Enum             | [·      ]Skins.Office2007Blue   | NA          |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.Office2007Silver |             |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.Office2007Black  |             |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.Vista            |             |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.Almond           |             |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.Blueberry        |             |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.Blend            |             |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.Olive            |             |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.Turquoise        |             |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.Monochrome       |             |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.Sandune          |             |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.VS2010           |             |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.Marble           |             |
|             |                                      |                  |                                                              |             |
|             |                                      |                  | [·      ]Skins.Midnight         |             |
+-------------+--------------------------------------+------------------+--------------------------------------------------------------+-------------+

*[[]]{.underline}* 

Using Builder

 

The following steps explain how to set Syncfusion themes for the tab control through the builder.

1.   In **View**, create the contents of the tabs with *ul* and *li* (for headers) and *div* tags (for content), and invoke the tab helper with the control ID as the first argument, followed by the **AutoFormat** method with the desired theme as an argument.[]

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
| [\<%][=][Html.Syncfusion().Tab([\"myTab\"])]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [.TargetControlId([\"tabContents\"])]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| **[.AutoFormat([Skins].VS2010)]**[%\>]                                                                                                                                                                                                                        |
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
| [\@{][ Html.Syncfusion().Tab([\"myTab\"])]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [.TargetControlId([\"tabContents\"])]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| **[.AutoFormat([Skins].VS2010)]**[.Render();][}]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.**

*[[]]{.underline}* 

Using Properties Model

The following steps explain how to set Syncfusion themes for the tab control through the properties model.

1.   In the controller, create an instance of **TabModel**.**

2.   Define the **AutoFormat** property and pass the instance through the **view-specific data** to the **View**.**

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
| [            myModel.AutoFormat = [Skins].VS2010;]                                                  |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [            [//Pass the instance through view data to the view.]]                                    |
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

3.   In **View**, create the contents of the tabs with *ul* and *li* (for headers) and *div* tags (for content) and invoke the tab helper with the **view data** key as the control ID.**

[] 

[       ]

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
| []                                                                                                                                                                                                                                                                                                                                            |
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
| [\@{][ Html.Syncfusion().Tab([\"myTab\"]).Render();[}]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application.

The following figure shows the output of the tabs with a Syncfusion Theme.

{border="0"}

Figure 269:Tabs with Syncfusion Theme

 

[]{#related-topics}

