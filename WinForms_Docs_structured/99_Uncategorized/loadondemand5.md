---
title: loadondemand5.md
original_path: WinForms_Docs/99_Uncategorized/loadondemand5.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Load-on-demand {#load-on-demand style="tab-stops: 0pt"}

Th load-on-demand feature helps you to load the tab content only on demand (on selecting).

 

+-----------------+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-------------+----------------+-----------------+
| Method          | Description                                                                                       | Parameters                                                                                                         | Type        | Return Type    | Reference links |
+-----------------+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-------------+----------------+-----------------+
| LoadAjaxContent | Allows you specify the to controller and action name from which the content is loaded using Ajax. | Overloads:                                                                                                         | Server side | TabItemBuilder | NA              |
|                 |                                                                                                   |                                                                                                                    |             |                |                 |
|                 |                                                                                                   | [·      ](string value)                                                               |             |                |                 |
|                 |                                                                                                   |                                                                                                                    |             |                |                 |
|                 |                                                                                                   | [·      ](string actionName, string controllerName)                                   |             |                |                 |
|                 |                                                                                                   |                                                                                                                    |             |                |                 |
|                 |                                                                                                   | [·      ](string actionName, string controllerName, object routeValues)               |             |                |                 |
|                 |                                                                                                   |                                                                                                                    |             |                |                 |
|                 |                                                                                                   | [·      ](string actionName, string controllerName, RouteValueDictionary routeValues) |             |                |                 |
+=================+===================================================================================================+====================================================================================================================+=============+================+=================+

**[]**  

The following steps explain how you can load the TabItem content on demand:

1.   In **View**, invoke the TabHelper with the Control ID as the first argument and set the LoadAjaxContent(), (which contains the action name and controller name) to load the TabItemContents on demand:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                     |
|                                                                                                                                                                                |
| **[\[ASPX\]]**                                                                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                     |
|                                                                                                                                                                                |
| [\<%] [Html.MobSyncfusion().Tab([\"tabModel1\"])]          |
|                                                                                                                                                                                |
| [          .AutoFormat([MobSkins].BlueLight)]                                                                      |
|                                                                                                                                                                                |
| [          .TabStyle([TabStyle].Closed)]                                                                           |
|                                                                                                                                                                                |
| [            .Items(tabitem =\>]                                                                                                           |
|                                                                                                                                                                                |
| [            {]                                                                                                                            |
|                                                                                                                                                                                |
| [                tabitem.Add()]                                                                                                            |
|                                                                                                                                                                                |
| [                .Value([\"messi\"])]                                                                              |
|                                                                                                                                                                                |
| [                .Text([\"Lionel Messi\"])]                                                                        |
|                                                                                                                                                                                |
| [                .Content((t) =\>]                                                                                                         |
|                                                                                                                                                                                |
| [                {[%\>]]                                                                                       |
|                                                                                                                                                                                |
| [        [\<][div][\>]]                                                   |
|                                                                                                                                                                                |
| [            [\<][br][/\>]]                                               |
|                                                                                                                                                                                |
| [            [\<][br][/\>]]                                               |
|                                                                                                                                                                                |
| [            [\<][div][class][=\"pInfo\"\>]]          |
|                                                                                                                                                                                |
| [                [\<][div][class][=\"pTitle\"\>]]     |
|                                                                                                                                                                                |
| [                    Full Name:[\</][div][\>]]                            |
|                                                                                                                                                                                |
| [                [\<][div][class][=\"playerDesc\"\>]] |
|                                                                                                                                                                                |
| [                    Cristiano Ronaldo dos Santos Aveiro[\</][div][\>]]   |
|                                                                                                                                                                                |
| [                [\<][br][/\>]]                                           |
|                                                                                                                                                                                |
| [                [\<][br][/\>]]                                           |
|                                                                                                                                                                                |
| [                [\<][div][class][=\"pTitle\"\>]]     |
|                                                                                                                                                                                |
| [                    Date of Birth :[\</][div][\>]]                       |
|                                                                                                                                                                                |
| [                [\<][div][class][=\"playerDesc\"\>]] |
|                                                                                                                                                                                |
| [                    5 February 1985 (age 25)[\</][div][\>]]              |
|                                                                                                                                                                                |
| [                [\<][br][/\>]]                                           |
|                                                                                                                                                                                |
| [                [\<][br][/\>]]                                           |
|                                                                                                                                                                                |
| [                [\<][div][class][=\"pTitle\"\>]]     |
|                                                                                                                                                                                |
| [                    Description:[\</][div][\>]]                          |
|                                                                                                                                                                                |
| [                [\<][div][class][=\"playerDesc\"\>]] |
|                                                                                                                                                                                |
| [                    Ronaldo is a Portuguese footballer who plays as a winger for Spanish club Real Madrid.]                               |
|                                                                                                                                                                                |
| [                [\</][div][\>]]                                          |
|                                                                                                                                                                                |
| [                [\<][br][/\>]]                                           |
|                                                                                                                                                                                |
| [                [\<][br][/\>]]                                           |
|                                                                                                                                                                                |
| [            [\</][div][\>]]                                              |
|                                                                                                                                                                                |
| [        [\</][div][\>]]                                                  |
|                                                                                                                                                                                |
| [        [\<%]});]                                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [                tabitem.Add()]                                                                                                            |
|                                                                                                                                                                                |
| [                 .Text([\"CristianoRonaldo\"])]                                                                   |
|                                                                                                                                                                                |
| [                 .Value([\"ronaldo\"])]                                                                           |
|                                                                                                                                                                                |
| **[                 .LoadAjaxContent([\"Villa\"], [\"Home\"]);]**                          |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [                tabitem.Add()]                                                                                                            |
|                                                                                                                                                                                |
| [                  .Text([\"Ricardo Leite\"])]                                                                     |
|                                                                                                                                                                                |
| [                  .Value([\"kaka\"])]                                                                             |
|                                                                                                                                                                                |
| [                  **.LoadAjaxContent([\"Rooney\"], [\"Home\"]);**]                        |
|                                                                                                                                                                                |
| [            })]                                                                                                                           |
|                                                                                                                                                                                |
| [      .Render();]                                                                                                                         |
|                                                                                                                                                                                |
| [        [%\>]]                                                                                                |
|                                                                                                                                                                                |
| []                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                         |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                         |
| [\@{] [ Html.MobSyncfusion().Tab([\"tabModel1\"])]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [          .AutoFormat([MobSkins].BlueLight)]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                         |
| [          .TabStyle([TabStyle].Closed)]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [            .Items(tabitem =\>]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                         |
| [                tabitem.Add()]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                         |
| [                .Value([\"messi\"])]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                         |
| [                .Text([\"Lionel Messi\"])]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                         |
| [                .Content(] [@] [\<] [div] [\>] [] |
|                                                                                                                                                                                                                                                                                                                                         |
| [            [\<][br][/\>]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                         |
| [            [\<][br][/\>]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                         |
| [            [\<][div][class][=\"pInfo\"\>]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][div][class][=\"pTitle\"\>]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                         |
| [                    Full Name:[\</][div][\>]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][div][class][=\"playerDesc\"\>]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                         |
| [                    Cristiano Ronaldo dos Santos Aveiro[\</][div][\>]]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][br][/\>]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][br][/\>]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][div][class][=\"pTitle\"\>]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                         |
| [                    Date of Birth :[\</][div][\>]]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][div][class][=\"playerDesc\"\>]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                         |
| [                    5 February 1985 (age 25)[\</][div][\>]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][br][/\>]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][br][/\>]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][div][class][=\"pTitle\"\>]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                         |
| [                    Description:[\</][div][\>]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][div][class][=\"playerDesc\"\>]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                         |
| [                    Ronaldo is a Portuguese footballer who plays as a winger for Spanish club Real Madrid.]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\</][div][\>]]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][br][/\>]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [                [\<][br][/\>]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [            [\</][div][\>]]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                         |
| [        [\</][div][\>]);]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                         |
| [                tabitem.Add()]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                         |
| [                 .Text([\"CristianoRonaldo\"])]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [                 .Value([\"ronaldo\"])]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| **[                 .LoadAjaxContent([\"Villa\"], [\"Home\"]);]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [                tabitem.Add()]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                         |
| [                  .Text([\"Ricardo Leite\"])]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                         |
| [                  .Value([\"kaka\"])]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| [                  **.LoadAjaxContent([\"Rooney\"], [\"Home\"]);**]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                         |
| [            })]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [      .Render();]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [        [}]]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   Build and run the application in emulator.

 

The output is displayed in the following screenshot:

[] 

[ {border="0"} ]

Figure 159: Tab -- preloaded content

3.   Select the next tab item which will load its content through ajax call.

 

[ {border="0"} ]

Figure 160: Tab - Content loaded on demand[]

 

[] 

 

[]{#related-topics}

