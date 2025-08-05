---
title: usingbuilder136.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder136.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how you can collapse theTabItem content:

1.   In **View**, invoke the TabHelper with the Control ID as the first argument and set the Collapsible() to True:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                           |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\<%] [Html.MobSyncfusion().Tab([\"tabModel\"])]                         |
|                                                                                                                                                                                              |
| [          .TabStyle([TabStyle].Closed)]                                                                                         |
|                                                                                                                                                                                              |
| [          **.Collapsible([true])**]                                                                                                |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [              .Items(tabitem =\>]                                                                                                                       |
|                                                                                                                                                                                              |
| [              {]                                                                                                                                        |
|                                                                                                                                                                                              |
| [                  tabitem.Add()]                                                                                                                        |
|                                                                                                                                                                                              |
| [                      .Text([\"Christiano Ronaldo\"])]                                                                          |
|                                                                                                                                                                                              |
| [                      .Content((Tab) =\>]                                                                                                               |
|                                                                                                                                                                                              |
| [                      {[%\>][\<][div][\>]]                 |
|                                                                                                                                                                                              |
| [                          [\<][br][/\>]]                                               |
|                                                                                                                                                                                              |
| [                          [\<][br][/\>]]                                               |
|                                                                                                                                                                                              |
| [                          [\<][div][class][=\"pInfo\"\>]]          |
|                                                                                                                                                                                              |
| [                              [\<][div][class][=\"pTitle\"\>]]     |
|                                                                                                                                                                                              |
| [                                  Full Name:[\</][div][\>]]                            |
|                                                                                                                                                                                              |
| [                              [\<][div][class][=\"playerDesc\"\>]] |
|                                                                                                                                                                                              |
| [                                  Cristiano Ronaldo dos Santos Aveiro[\</][div][\>]]   |
|                                                                                                                                                                                              |
| [                              [\<][br][/\>]]                                           |
|                                                                                                                                                                                              |
| [                              [\<][br][/\>]]                                           |
|                                                                                                                                                                                              |
| [                              [\<][div][class][=\"pTitle\"\>]]     |
|                                                                                                                                                                                              |
| [                                  Date of Birth :[\</][div][\>]]                       |
|                                                                                                                                                                                              |
| [                              [\<][div][class][=\"playerDesc\"\>]] |
|                                                                                                                                                                                              |
| [                                  5 February 1985 (age 25)[\</][div][\>]]              |
|                                                                                                                                                                                              |
| [                              [\<][br][/\>]]                                           |
|                                                                                                                                                                                              |
| [                              [\<][br][/\>]]                                           |
|                                                                                                                                                                                              |
| [                              [\<][div][class][=\"pTitle\"\>]]     |
|                                                                                                                                                                                              |
| [                                  Description:[\</][div][\>]]                          |
|                                                                                                                                                                                              |
| [                              [\<][div][class][=\"playerDesc\"\>]] |
|                                                                                                                                                                                              |
| [                                  Ronaldo is a Portuguese footballer who plays as a winger for Spanish club Real Madrid.]                               |
|                                                                                                                                                                                              |
| [                              [\</][div][\>]]                                          |
|                                                                                                                                                                                              |
| [                              [\<][br][/\>]]                                           |
|                                                                                                                                                                                              |
| [                              [\<][br][/\>]]                                           |
|                                                                                                                                                                                              |
| [                          [\</][div][\>]]                                              |
|                                                                                                                                                                                              |
| [                      [\</][div][\>]]                                                  |
|                                                                                                                                                                                              |
| [    [\<%]});]                                                                                                               |
|                                                                                                                                                                                              |
| [                  tabitem.Add()]                                                                                                                        |
|                                                                                                                                                                                              |
| [                .Text([\"Villa\"])]                                                                                             |
|                                                                                                                                                                                              |
| [                 .Content((Tab) =\>]                                                                                                                    |
|                                                                                                                                                                                              |
| [                 {[%\>][\<][div][\>]]                      |
|                                                                                                                                                                                              |
| [                     [\<][br][/\>]]                                                    |
|                                                                                                                                                                                              |
| [                     [\<][br][/\>]]                                                    |
|                                                                                                                                                                                              |
| [                     [\<][div][class][=\"pInfo\"\>]]               |
|                                                                                                                                                                                              |
| [                         [\<][div][class][=\"pTitle\"\>]]          |
|                                                                                                                                                                                              |
| [                             Full Name:[\</][div][\>]]                                 |
|                                                                                                                                                                                              |
| [                         [\<][div][class][=\"playerDesc\"\>]]      |
|                                                                                                                                                                                              |
| [                             David Villa Sánchez[\</][div][\>]]                        |
|                                                                                                                                                                                              |
| [                         [\<][br][/\>]]                                                |
|                                                                                                                                                                                              |
| [                         [\<][br][/\>]]                                                |
|                                                                                                                                                                                              |
| [                         [\<][div][class][=\"pTitle\"\>]]          |
|                                                                                                                                                                                              |
| [                             Date of Birth :[\</][div][\>]]                            |
|                                                                                                                                                                                              |
| [                         [\<][div][class][=\"playerDesc\"\>]]      |
|                                                                                                                                                                                              |
| [                             3 December 1981 (age 29)[\</][div][\>]]                   |
|                                                                                                                                                                                              |
| [                         [\<][br][/\>]]                                                |
|                                                                                                                                                                                              |
| [                         [\<][br][/\>]]                                                |
|                                                                                                                                                                                              |
| [                         [\<][div][class][=\"pTitle\"\>]]          |
|                                                                                                                                                                                              |
| [                             Description:[\</][div][\>]]                               |
|                                                                                                                                                                                              |
| [                         [\<][div][class][=\"playerDesc\"\>]]      |
|                                                                                                                                                                                              |
| [                             David Villa is a Spanish footballer who currently plays as a striker for FC Barcelona]                                     |
|                                                                                                                                                                                              |
| [                             and the Spanish national football team.]                                                                                   |
|                                                                                                                                                                                              |
| [                         [\</][div][\>]]                                               |
|                                                                                                                                                                                              |
| [                         [\<][br][/\>]]                                                |
|                                                                                                                                                                                              |
| [                         [\<][br][/\>]]                                                |
|                                                                                                                                                                                              |
| [                     [\</][div][\>]]                                                   |
|                                                                                                                                                                                              |
| [                 [\</][div][\>]]                                                       |
|                                                                                                                                                                                              |
| [    [\<%]});]                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [                  tabitem.Add()]                                                                                                                        |
|                                                                                                                                                                                              |
| [               .Text([\"Rooney\"])]                                                                                             |
|                                                                                                                                                                                              |
| [                .Content((Tab) =\>]                                                                                                                     |
|                                                                                                                                                                                              |
| [                {[%\>][\<][div][\>]]                       |
|                                                                                                                                                                                              |
| [          [\<][br][/\>]]                                                               |
|                                                                                                                                                                                              |
| [          [\<][br][/\>]]                                                               |
|                                                                                                                                                                                              |
| [          [\<][div][class][=\"pInfo\"\>]]                          |
|                                                                                                                                                                                              |
| [              [\<][div][class][=\"pTitle\"\>]]                     |
|                                                                                                                                                                                              |
| [                  Full Name:[\</][div][\>]]                                            |
|                                                                                                                                                                                              |
| [              [\<][div][class][=\"playerDesc\"\>]]                 |
|                                                                                                                                                                                              |
| [                  Wayne Mark Rooney[\</][div][\>]]                                     |
|                                                                                                                                                                                              |
| [              [\<][br][/\>]]                                                           |
|                                                                                                                                                                                              |
| [              [\<][br][/\>]]                                                           |
|                                                                                                                                                                                              |
| [              [\<][div][class][=\"pTitle\"\>]]                     |
|                                                                                                                                                                                              |
| [                  Date of Birth :[\</][div][\>]]                                       |
|                                                                                                                                                                                              |
| [              [\<][div][class][=\"playerDesc\"\>]]                 |
|                                                                                                                                                                                              |
| [                  24 October 1985 (age 25)[\</][div][\>]]                              |
|                                                                                                                                                                                              |
| [              [\<][br][/\>]]                                                           |
|                                                                                                                                                                                              |
| [              [\<][br][/\>]]                                                           |
|                                                                                                                                                                                              |
| [              [\<][div][class][=\"pTitle\"\>]]                     |
|                                                                                                                                                                                              |
| [                  Description:[\</][div][\>]]                                          |
|                                                                                                                                                                                              |
| [              [\<][div][class][=\"playerDesc\"\>]]                 |
|                                                                                                                                                                                              |
| [                  Rooney is an English footballer who plays as a striker for Premier League club Manchester]                                            |
|                                                                                                                                                                                              |
| [                  United and the England national team.]                                                                                                |
|                                                                                                                                                                                              |
| [              [\</][div][\>]]                                                          |
|                                                                                                                                                                                              |
| [              [\<][br][/\>]]                                                           |
|                                                                                                                                                                                              |
| [              [\<][br][/\>]]                                                           |
|                                                                                                                                                                                              |
| [          [\</][div][\>]]                                                              |
|                                                                                                                                                                                              |
| [      [\</][div][\>]]                                                                  |
|                                                                                                                                                                                              |
| [    [\<%]});]                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [              })]                                                                                                                                       |
|                                                                                                                                                                                              |
| [      .Render();]                                                                                                                                       |
|                                                                                                                                                                                              |
| [    [%\>]]                                                                                                                  |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                          |
| [\@{] [Html.MobSyncfusion().Tab([\"tabModel\"])]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [         .TabStyle([TabStyle].Closed)]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                          |
| [          **.Collapsible([true])**]                                                                                                                                                                                                            |
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
| [                              [\<][div][class][=\"pTitle\"\>]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [                                  Full Name:[\</][div][\>]]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| [                              [\<][div][class][=\"playerDesc\"\>]]                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [                                  Cristiano Ronaldo dos Santos Aveiro[\</][div][\>\<][br][/\>\<][br][/\>]] |
|                                                                                                                                                                                                                                                                                                          |
| [                              [\<][div][class][=\"pTitle\"\>]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [                                  Date of Birth :[\</][div][\>]]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [                              [\<][div][class][=\"playerDesc\"\>]]                                                                                                             |
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
| [                              [\</][div][\>\<][br][/\>\<][br][/\>]]                                        |
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
| [                   3 December 1981 (age 29)[\</][div][\>\<][br][/\>\<][br][/\>]]                           |
|                                                                                                                                                                                                                                                                                                          |
| [               [\<][div][class][=\"pTitle\"\>]]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                          |
| [                   Description:[\</][div][\>]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [               [\<][div][class][=\"playerDesc\"\>]]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                          |
| [                   David Villa is a Spanish footballer who currently plays as a striker for FC Barcelona]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                          |
| [                   and the Spanish national football team.]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| [               [\</][div][\>\<][br][/\>\<][br][/\>]]                                                       |
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
| [              [\<][div][class][=\"playerDesc\"\>]]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [                  Rooney is an English footballer who plays as a striker for Premier League club Manchester]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                          |
| [                  United and the England national team.]                                                                                                                                                                                                            |
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

 

2.   Build and run the application in emulator.

 

{border="0"}

Figure 150:Tab -- with Expanded item

3.   Click the selected tab item to collapse it.

 

[] 

[ {border="0"} ]

Figure 151: Tab - with Collapsed item[]

 

 

[]{#related-topics}

