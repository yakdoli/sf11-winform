---
title: usingbuilder135.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder135.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how you can set the TabItem content using the Content method:

1.   In **View**, invoke the TabHelper with the Control ID as the first argument and set the ContentPosition() using desired value as an argument:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                   |
|                                                                                                                                                                                              |
| **[\[ASPX\]]**                                                                                                                                           |
|                                                                                                                                                                                              |
| []                                                                                                                                   |
|                                                                                                                                                                                              |
| [\<%] [Html.MobSyncfusion().Tab([\"tabModel\"])]                         |
|                                                                                                                                                                                              |
| [          .TabStyle([TabStyle].Closed)]                                                                                         |
|                                                                                                                                                                                              |
| [          **.ContentPosition([Position].Top)**]                                                                                 |
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
| [                          [\<][div][class][=\"pInfo\"\>]]          |
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
| [                              [\<][br][/\>]]                                           |
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
| [                              [\<][br][/\>]]                                           |
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
| [                     [\<][div][class][=\"pInfo\"\>]]               |
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
| [                         [\</][div][\>]]                                               |
|                                                                                                                                                                                              |
| [                         [\<][br][/\>]]                                                |
|                                                                                                                                                                                              |
| [                         [\<][br][/\>]]                                                |
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
| [                  Description:[\</][div][\>]]                                          |
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
| [          [\</][div][\>]]                                                              |
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
| []                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Razor:]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [\@{] [Html.MobSyncfusion().Tab([\"tabModel\"])]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [          **.ContentPosition([Position].Top)**]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [    .TabStyle([TabStyle].Closed)]                                                                                                                                                                                                           |
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
| [                                  Date of Birth :[\</][div][\>]]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [                              [\<][div][class][=\"playerDesc\"\>]]                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [                                  5 February 1985 (age 25)[\</][div][\>\<][br][/\>\<][br][/\>]]            |
|                                                                                                                                                                                                                                                                                                          |
| [                              [\<][div][class][=\"pTitle\"\>]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [                                  Description:[\</][div][\>]]                                                                                                                                      |
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
| **[]**                                                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

 

 

2.   Build and run the application in emulator.

[ {border="0"} ]

Figure 148: Tab with content placed at top[]

[] 

 

 

[]{#related-topics}

