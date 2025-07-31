---
title: usingpropertiesmodel108.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel108.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain the handling of the client side events of the tab through the Properties model:

1.   In the **Controller**, create an instance of **MobTabModel**, define the the event handler properties and pass the instance through **View Specific Data** to **View** as given below:**

**[]**  

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                      |
|                                                                                                                                                                     |
| [         public] [ [ActionResult] Tab()]              |
|                                                                                                                                                                     |
| [        {]                                                                                                                     |
|                                                                                                                                                                     |
| [            [MobTabModel] tModel = [new][MobTabModel]();] |
|                                                                                                                                                                     |
| [            ] **[tModel.OnTabsDisable = [\"OnTabsDisable\"];]**    |
|                                                                                                                                                                     |
| **[            tModel.OnTabsEnable = [\"OnTabsEnable\"];]**                                             |
|                                                                                                                                                                     |
| **[            tModel.OnTabsLoad = [\"OnTabsLoad\"];]**                                                 |
|                                                                                                                                                                     |
| **[            tModel.OnTabsSelect = [\"OnTabsSelect\"];]**                                             |
|                                                                                                                                                                     |
| [            tModel.TabStyle = [TabStyle].Closed;]                                                      |
|                                                                                                                                                                     |
| [            ViewData\[[\"tabModel\"]\] = tModel;]                                                      |
|                                                                                                                                                                     |
| [            [return] View();]                                                                             |
|                                                                                                                                                                     |
| [        }]                                                                                                                     |
|                                                                                                                                                                     |
| []                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

2.   In **View**, invoke the Tab helper with the **View Data** key as the first argument and add the tab items through items Add() method.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                               |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [\<%] [Html.MobSyncfusion().Tab([\"tabModel\"])]                             |
|                                                                                                                                                                                                  |
| [              .Items(tabitem =\>]                                                                                                                           |
|                                                                                                                                                                                                  |
| [              {]                                                                                                                                            |
|                                                                                                                                                                                                  |
| [                  tabitem.Add()]                                                                                                                            |
|                                                                                                                                                                                                  |
| [                      .Text([\"Christiano Ronaldo\"])]                                                                              |
|                                                                                                                                                                                                  |
| [                      .Content((Tab) =\>]                                                                                                                   |
|                                                                                                                                                                                                  |
| [                      {[%\>][\<][div][\>]]                     |
|                                                                                                                                                                                                  |
| [                          [\<][br][/\>]]                                                   |
|                                                                                                                                                                                                  |
| [                          [\<][br][/\>]]                                                   |
|                                                                                                                                                                                                  |
| [                          [\<][div][class][=\"pInfo\"\>]]              |
|                                                                                                                                                                                                  |
| [                              [\<][div][class][=\"pTitle\"\>]]         |
|                                                                                                                                                                                                  |
| [                                  Full Name:[\</][div][\>]]                                |
|                                                                                                                                                                                                  |
| [                              [\<][div][class][=\"playerDesc\"\>]]     |
|                                                                                                                                                                                                  |
| [                                  Cristiano Ronaldo dos Santos Aveiro[\</][div][\>]]       |
|                                                                                                                                                                                                  |
| [                              [\<][br][/\>]]                                               |
|                                                                                                                                                                                                  |
| [                              [\<][br][/\>]]                                               |
|                                                                                                                                                                                                  |
| [                              [\<][div][class][=\"pTitle\"\>]]         |
|                                                                                                                                                                                                  |
| [                                  Date of Birth :[\</][div][\>]]                           |
|                                                                                                                                                                                                  |
| [                              [\<][div][class][=\"playerDesc\"\>]]     |
|                                                                                                                                                                                                  |
| [                                  5 February 1985 (age 25)[\</][div][\>]]                  |
|                                                                                                                                                                                                  |
| [                              [\<][br][/\>]]                                               |
|                                                                                                                                                                                                  |
| [                              [\<][br][/\>]]                                               |
|                                                                                                                                                                                                  |
| [                              [\<][div][class][=\"pTitle\"\>]]         |
|                                                                                                                                                                                                  |
| [                                  Description:[\</][div][\>]]                              |
|                                                                                                                                                                                                  |
| [                              [\<][div][class][=\"playerDesc\"\>]]     |
|                                                                                                                                                                                                  |
| [                                  Ronaldo is a Portuguese footballer who plays as a winger for Spanish club Real Madrid.]                                   |
|                                                                                                                                                                                                  |
| [                              [\</][div][\>]]                                              |
|                                                                                                                                                                                                  |
| [                              [\<][br][/\>]]                                               |
|                                                                                                                                                                                                  |
| [                              [\<][br][/\>]]                                               |
|                                                                                                                                                                                                  |
| [                          [\</][div][\>]]                                                  |
|                                                                                                                                                                                                  |
| [                      [\</][div][\>]]                                                      |
|                                                                                                                                                                                                  |
| [    [\<%]});]                                                                                                                   |
|                                                                                                                                                                                                  |
| [                  tabitem.Add()]                                                                                                                            |
|                                                                                                                                                                                                  |
| [                .Text([\"Villa\"])]                                                                                                 |
|                                                                                                                                                                                                  |
| [                 .Content((Tab) =\>]                                                                                                                        |
|                                                                                                                                                                                                  |
| [                 {[%\>][\<][div][\>]]                          |
|                                                                                                                                                                                                  |
| [                     [\<][br][/\>]]                                                        |
|                                                                                                                                                                                                  |
| [                     [\<][br][/\>]]                                                        |
|                                                                                                                                                                                                  |
| [                     [\<][div][class][=\"pInfo\"\>]]                   |
|                                                                                                                                                                                                  |
| [                         [\<][div][class][=\"pTitle\"\>]]              |
|                                                                                                                                                                                                  |
| [                             Full Name:[\</][div][\>]]                                     |
|                                                                                                                                                                                                  |
| [                         [\<][div][class][=\"playerDesc\"\>]]          |
|                                                                                                                                                                                                  |
| [                             David Villa Sánchez[\</][div][\>]]                            |
|                                                                                                                                                                                                  |
| [                         [\<][br][/\>]]                                                    |
|                                                                                                                                                                                                  |
| [                         [\<][br][/\>]]                                                    |
|                                                                                                                                                                                                  |
| [                         [\<][div][class][=\"pTitle\"\>]]              |
|                                                                                                                                                                                                  |
| [                             Date of Birth :[\</][div][\>]]                                |
|                                                                                                                                                                                                  |
| [                         [\<][div][class][=\"playerDesc\"\>]]          |
|                                                                                                                                                                                                  |
| [                             3 December 1981 (age 29)[\</][div][\>]]                       |
|                                                                                                                                                                                                  |
| [                         [\<][br][/\>]]                                                    |
|                                                                                                                                                                                                  |
| [                         [\<][br][/\>]]                                                    |
|                                                                                                                                                                                                  |
| [                         [\<][div][class][=\"pTitle\"\>]]              |
|                                                                                                                                                                                                  |
| [                             Description:[\</][div][\>]]                                   |
|                                                                                                                                                                                                  |
| [                         [\<][div][class][=\"playerDesc\"\>]]          |
|                                                                                                                                                                                                  |
| [                             David Villa is a Spanish footballer who currently plays as a striker for FC Barcelona and the Spanish national football team.] |
|                                                                                                                                                                                                  |
| [                         [\</][div][\>]]                                                   |
|                                                                                                                                                                                                  |
| [                         [\<][br][/\>]]                                                    |
|                                                                                                                                                                                                  |
| [                         [\<][br][/\>]]                                                    |
|                                                                                                                                                                                                  |
| [                     [\</][div][\>]]                                                       |
|                                                                                                                                                                                                  |
| [                 [\</][div][\>]]                                                           |
|                                                                                                                                                                                                  |
| [    [\<%]});]                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [                  tabitem.Add()]                                                                                                                            |
|                                                                                                                                                                                                  |
| [               .Text([\"Rooney\"])]                                                                                                 |
|                                                                                                                                                                                                  |
| [                .Content((Tab) =\>]                                                                                                                         |
|                                                                                                                                                                                                  |
| [                {[%\>][\<][div][\>]]                           |
|                                                                                                                                                                                                  |
| [          [\<][br][/\>]]                                                                   |
|                                                                                                                                                                                                  |
| [          [\<][br][/\>]]                                                                   |
|                                                                                                                                                                                                  |
| [          [\<][div][class][=\"pInfo\"\>]]                              |
|                                                                                                                                                                                                  |
| [              [\<][div][class][=\"pTitle\"\>]]                         |
|                                                                                                                                                                                                  |
| [                  Full Name:[\</][div][\>]]                                                |
|                                                                                                                                                                                                  |
| [              [\<][div][class][=\"playerDesc\"\>]]                     |
|                                                                                                                                                                                                  |
| [                  Wayne Mark Rooney[\</][div][\>]]                                         |
|                                                                                                                                                                                                  |
| [              [\<][br][/\>]]                                                               |
|                                                                                                                                                                                                  |
| [              [\<][br][/\>]]                                                               |
|                                                                                                                                                                                                  |
| [              [\<][div][class][=\"pTitle\"\>]]                         |
|                                                                                                                                                                                                  |
| [                  Date of Birth :[\</][div][\>]]                                           |
|                                                                                                                                                                                                  |
| [              [\<][div][class][=\"playerDesc\"\>]]                     |
|                                                                                                                                                                                                  |
| [                  24 October 1985 (age 25)[\</][div][\>]]                                  |
|                                                                                                                                                                                                  |
| [              [\<][br][/\>]]                                                               |
|                                                                                                                                                                                                  |
| [              [\<][br][/\>]]                                                               |
|                                                                                                                                                                                                  |
| [              [\<][div][class][=\"pTitle\"\>]]                         |
|                                                                                                                                                                                                  |
| [                  Description:[\</][div][\>]]                                              |
|                                                                                                                                                                                                  |
| [              [\<][div][class][=\"playerDesc\"\>]]                     |
|                                                                                                                                                                                                  |
| [                  Rooney is an English footballer who plays as a striker for Premier League club Manchester United and the England national team.]          |
|                                                                                                                                                                                                  |
| [              [\</][div][\>]]                                                              |
|                                                                                                                                                                                                  |
| [              [\<][br][/\>]]                                                               |
|                                                                                                                                                                                                  |
| [              [\<][br][/\>]]                                                               |
|                                                                                                                                                                                                  |
| [          [\</][div][\>]]                                                                  |
|                                                                                                                                                                                                  |
| [      [\</][div][\>]]                                                                      |
|                                                                                                                                                                                                  |
| [    [\<%]});]                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [              })]                                                                                                                                           |
|                                                                                                                                                                                                  |
| [      .Render();]                                                                                                                                           |
|                                                                                                                                                                                                  |
| [    [%\>]]                                                                                                                      |
|                                                                                                                                                                                                  |
| []                                                                                                                                       |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| **[\[Razor\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                          |
| [\@{] [Html.MobSyncfusion().Tab([\"tabModel\"])]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [    .Items(tabitem =\>]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [    {]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                          |
| [        tabitem.Add()]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                          |
| [            .Text([\"Christiano Ronaldo\"])]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [            .Content([@][\<][div][\>]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [                          [\<][br][/\>\<][br][/\>]]                                                                                                    |
|                                                                                                                                                                                                                                                                                                          |
| [                          [\<][div][class][=\"pInfo\"\>]]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                          |
| [                              [\<][div][class][=\"pTitle\"\>]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [                                  Full Name:[\</][div][\>]]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| [                              [\<][div][class][=\"playerDesc\"\>]]                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [                                  Cristiano Ronaldo dos Santos Aveiro[\</][div][\>\<][br][/\>\<][br][/\>]] |
|                                                                                                                                                                                                                                                                                                          |
| [                              [\<][div][class][=\"pTitle\"\>]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [                                  Date of Birth :[\</][div][\>]]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [                              [\<][div][class][=\"playerDesc\"\>]]                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [                                  5 February 1985 (age 25)[\</][div][\>\<][br][/\>\<][br][/\>]]            |
|                                                                                                                                                                                                                                                                                                          |
| [                              [\<][div][class][=\"pTitle\"\>]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [                                  Description:[\</][div][\>]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                          |
| [                              [\<][div][class][=\"playerDesc\"\>]]                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [                                  Ronaldo is a Portuguese footballer who plays as a winger for Spanish club Real Madrid.]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| [                              [\</][div][\>\<][br][/\>\<][br][/\>]]                                        |
|                                                                                                                                                                                                                                                                                                          |
| [                          [\</][div][\>]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                          |
| [                      [\</][div][\>]);]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [        tabitem.Add()]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                          |
| [      .Text([\"Villa\"])]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [       .Content([@][\<][div][\>]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                          |
| [          [\<][br][/\>\<][br][/\>]]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                          |
| [           [\<][div][class][=\"pInfo\"\>]]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [               [\<][div][class][=\"pTitle\"\>]]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [                   Full Name:[\</][div][\>]]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| [               [\<][div][class][=\"playerDesc\"\>]]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                          |
| [                   David Villa Sánchez[\</][div][\>\<][br][/\>\<][br][/\>]]                                |
|                                                                                                                                                                                                                                                                                                          |
| [               [\<][div][class][=\"pTitle\"\>]]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [                   Date of Birth :[\</][div][\>]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [               [\<][div][class][=\"playerDesc\"\>]]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                          |
| [                   3 December 1981 (age 29)[\</][div][\>\<][br][/\>\<][br][/\>]]                           |
|                                                                                                                                                                                                                                                                                                          |
| [               [\<][div][class][=\"pTitle\"\>]]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [                   Description:[\</][div][\>]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [               [\<][div][class][=\"playerDesc\"\>]]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                          |
| [                   David Villa is a Spanish footballer who currently plays as a striker for FC Barcelona and the Spanish national football team.]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [               [\</][div][\>\<][br][/\>\<][br][/\>]]                                                       |
|                                                                                                                                                                                                                                                                                                          |
| [           [\</][div][\>]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [       [\</][div][\>]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [    );]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [        tabitem.Add()]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                          |
| [     .Text([\"Rooney\"])]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [      .Content([@][\<][div][\>]]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| [         [\<][br][/\>\<][br][/\>]]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [          [\<][div][class][=\"pInfo\"\>]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                          |
| [              [\<][div][class][=\"pTitle\"\>]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [                  Full Name:[\</][div][\>]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| [              [\<][div][class][=\"playerDesc\"\>]]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [                  Wayne Mark Rooney[\</][div][\>\<][br][/\>\<][br][/\>]]                                   |
|                                                                                                                                                                                                                                                                                                          |
| [              [\<][div][class][=\"pTitle\"\>]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [                  Date of Birth :[\</][div][\>]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [              [\<][div][class][=\"playerDesc\"\>]]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [                  24 October 1985 (age 25)[\</][div][\>\<][br][/\>\<][br][/\>]]                            |
|                                                                                                                                                                                                                                                                                                          |
| [              [\<][div][class][=\"pTitle\"\>]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [                  Description:[\</][div][\>]]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                          |
| [              [\<][div][class][=\"playerDesc\"\>]]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [                  Rooney is an English footballer who plays as a striker for Premier League club Manchester United and the England national team.               ]                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [              [\</][div][\>\<][br][/\>\<][br][/\>]]                                                        |
|                                                                                                                                                                                                                                                                                                          |
| [          [\</][div][\>]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                          |
| [      [\</][div][\>]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                          |
| [    ] [);]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                          |
| [    })]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [.Render();]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   In Javascript, define the handlers as given below:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| **[\[Javascript\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [        [function]] [OnTabsLoad] [(event, TabModel) {] []    |
|                                                                                                                                                                                                                                    |
| [            [//event             - event object.]]                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [            [//TabModel             - tab model object.]]                                                                                                           |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function]] [OnTabsSelect] [(event, data) {] []      |
|                                                                                                                                                                                                                                    |
| [            [//event             - event object.]]                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [            [//data:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [// selectedItemIndex-- selected item index]]                                                                                                           |
|                                                                                                                                                                                                                                    |
| [            // lastSelectedItemIndex-- last selected item index] []                                                                     |
|                                                                                                                                                                                                                                    |
| [            [// items-- list of tab items]]                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function]] [OnTabsEnable] [(event, data) {] []      |
|                                                                                                                                                                                                                                    |
| [            [//event             - event object.]]                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [            [//data:]]                                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [// enabledItemsIndex -- list of items index which are in enabled state]]                                                                               |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function]] [OnTabsDisable] [(event, data) {] []     |
|                                                                                                                                                                                                                                    |
| [            [//event             - event object.]]                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [            [//ui:]]                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [// disabledItemsIndex -- list of items index which are in disabled state]]                                                                             |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [\</][script][\>][]]                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

You can observe the handlers getting invoked when the corresponding event is triggered.

[]{#related-topics}

