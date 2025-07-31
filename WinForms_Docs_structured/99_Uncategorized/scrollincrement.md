---
title: scrollincrement.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\scrollincrement.md
created_at: 2025-07-03
---






##### Scroll Increment {#scroll-increment style="tab-stops: 0pt"}

This feature allows you to choose the number of items you can scroll the list by.

[[[]]]{.underline} 

**Properties**


+-----------------+-------------------------------------+------------------+---------------------------------+-------------------------------------------------------------------------------------+
| Name            | Description                         | Type of property | Value it accepts                | Dependency                                                                          |
+-----------------+-------------------------------------+------------------+---------------------------------+-------------------------------------------------------------------------------------+
| ScrollIncrement | The number items to be scrolled by. | int              | Number of items to be scrolled. | Depends on Total number of Items and number of Visible Items.                       |
|                 |                                     |                  |                                 |                                                                                     |
|                 |                                     |                  | Default value is 1              | ScrollIncrement should be less than (Total number of Items-number of Visible Items) |
+-----------------+-------------------------------------+------------------+---------------------------------+-------------------------------------------------------------------------------------+


[[[]]]{.underline} 

You can choose and set the number of items to scroll by making use of the following code snippets:

**[Using Builder]**

[The following steps guide you in configuring the ]ScrollIncrement[ through Builder.]

[1.   In **View**, create ul-li hierarchy of ]rotator[ items and invoke the rotator helper with the rotator Contents ID as the first argument and enable the ]**ScrollIncrement**[ method with the desired option as argument.]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][ul][ [id][=\"rotatoritems\"] [style][=\"][visibility][: hidden\"\>]][]                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [\<][li] [\>]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/Images/1.jpg\")[%\>][\'] [/\>\</][li][\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [\<][li] [\>]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/Images/2.jpg\")[%\>][\'] [/\>\</][li][\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [\<][li] [\>]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/Images/3.jpg\")[%\>][\'] [/\>\</][li][\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [\<][li] [\>]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/Images/4.jpg\")[%\>][\'] [/\>\</][li][\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [\<][li] [\>]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/Images/5.jpg\")[%\>][\'] [/\>\</][li][\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [\<][li] [\>]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/Images/6.jpg\")[%\>][\'] [/\>\</][li][\>]            ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [               ]                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][ul][\>][]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Rotator([\"rotatoritems\"]).AutoFormat([Skins].Sandune)]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [ . ScrollIncrement(1) [%\>]]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [   ]                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[2.   Run the application.]

**[]** 

**[Using Properties Model]**

[The following steps will guide you in setting the ScrollIncrement through the Properties model.]

[1.   In the **Controller**, create an instance of RotatorModel, define the **ScrollIncrement** property and pass the instance through view-specific data to View as given below.]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[]                                                                          |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [public][ [ActionResult] Index()]                          |
|                                                                                                                                                                         |
| [        {]                                                                                                                         |
|                                                                                                                                                                         |
| [            [RotatorModel] myModel = [new] [RotatorModel]();] |
|                                                                                                                                                                         |
| [            myModel.ScrollIncrement=1;][]                                                      |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [              myModel.AutoFormat=[Skins].Sandune;]                                                         |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [            ViewData\[[\"myRotatorModel\"]\] = myModel;]                                                   |
|                                                                                                                                                                         |
| [            [return] View();]                                                                                 |
|                                                                                                                                                                         |
| [        }]                                                                                                                         |
|                                                                                                                                                                         |
| []                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[2.   In **View**, create ul-li hierarchy of rotator items and invoke the rotator helper with the rotator content ID as the first argument and view data key as the second argument. ]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][ul][ [id][=\"rotatoritems\"] [style][=\"][visibility][: hidden\"\>]][]                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [\<][li] [\>]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/Images/1.jpg\")[%\>][\'] [/\>\</][li][\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [\<][li] [\>]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/Images/2.jpg\")[%\>][\'] [/\>\</][li][\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [\<][li] [\>]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/Images/3.jpg\")[%\>][\'] [/\>\</][li][\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [\<][li] [\>]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/Images/4.jpg\")[%\>][\'] [/\>\</][li][\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [\<][li] [\>]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/Images/5.jpg\")[%\>][\'] [/\>\</][li][\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            [\<][li] [\>]]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/Images/6.jpg\")[%\>][\'] [/\>\</][li][\>]            ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [               ]                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][ul][\>][]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Rotator([\"rotatoritems\"], [\"myRotatorModel\"])[%\>]]                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

