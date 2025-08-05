---
title: scrollingintervalforautoplay.md
original_path: WinForms_Docs/99_Uncategorized/scrollingintervalforautoplay.md
created_at: 2025-08-05
---






##### Scrolling interval for Autoplay {#scrolling-interval-for-autoplay style="tab-stops: 0pt"}

If you enable the Autoplay mode for scrolling through the items on your list, the Rotator control allows you to set the lengths of intervals between each auto-scroll.

Time intervals are measured by default in milliseconds.

**[Properties]**

+----------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+-----------------------+-------------+
| Name           | Description                                                                                                                   | Type of property | Value it accepts      | Dependency  |
+----------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+-----------------------+-------------+
| AnimationSpeed | [Specifies the interval speed of scrolling. The time interval is specified in milliseconds by default.] | int              | Any integer           | NA          |
|                |                                                                                                                               |                  |                       |             |
|                |                                                                                                                               |                  | Default value is 2000 |             |
+----------------+-------------------------------------------------------------------------------------------------------------------------------+------------------+-----------------------+-------------+

[[[]]]{.underline} 

 

You can choose how long you want your scrolling interval to be, and set it using any one of the following methods:

**[Using Builder]**

[The following steps guide you in configuring the animation speed through Builder.]

[1. In **View**, create ul-li hierarchy of rotator items and invoke the rotator helper with the rotator Contents ID as the first argument and enable the **AnimationSpeed** method with the desired option as argument.]

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
| [ .AnimationSpeed(1500)[%\>]]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [   ]                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[2.   Run the application.]

**[]** 

**[Using Properties Model]**

[The following steps will guide you in setting the animation speed through the Properties model.]

[1.   In the **Controller**, create an instance of RotatorModel, define the **AnimationSpeed** property and pass the instance through view-specific data to View as given below.]

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
| [            myModel.AnimationSpeed=1500;][]                                                    |
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

[] 

[]{#related-topics}

