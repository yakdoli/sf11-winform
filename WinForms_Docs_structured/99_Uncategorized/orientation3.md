---
title: orientation3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\orientation3.md
created_at: 2025-07-03
---






##### Orientation {#orientation style="tab-stops: 0pt"}

The Rotator control supports both horizontal and vertical orientations:

 

**Properties**

 

+-------------+------------------------------------------------------------------+------------------+-----------------------------+-------------+
| Name        | Description                                                      | Type of property | Value it accepts            | Dependency  |
+-------------+------------------------------------------------------------------+------------------+-----------------------------+-------------+
| Orientation | Specifies the orientation of the Rotator: vertical or horizontal | Enum             | Horizontal                  | NA          |
|             |                                                                  |                  |                             |             |
|             | Orientation.Horizontal                                           |                  | Vertical                    |             |
|             |                                                                  |                  |                             |             |
|             | Orientation.Vertical                                             |                  | Default value is Horizontal |             |
+-------------+------------------------------------------------------------------+------------------+-----------------------------+-------------+

 

You can orient the Rotator Control in two different ways-

**[Using Builder]**

The following steps guide you in configuring the orientation through Builder.

1.   In **View**, create ul-li hierarchy of rotator items and invoke the rotator helper with the rotator Contents ID as the first argument and enable the **Orientation** method with the desired option as argument.

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
| [ .Orientation([RotatorModel].[RotatorOrientation].Horizontal) [%\>]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [   ]                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Run the application.

**[]** 

**[Using Properties Model]**

[The following steps will guide you in setting the orientation through the Properties model.]

1.   In the **Controller**, create an instance of RotatorModel, define the **Orientation** property and pass the instance through view-specific data to View as given below.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Controller\]]**[]                                                                                                             |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [public][ [ActionResult] Index()]                                                              |
|                                                                                                                                                                                                             |
| [        {]                                                                                                                                                             |
|                                                                                                                                                                                                             |
| [            [RotatorModel] myModel = [new] [RotatorModel]();]                                     |
|                                                                                                                                                                                                             |
| [            myModel.Orientation=[RotatorModel].[RotatorOrientation].Horizontal;][] |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [              myModel.AutoFormat=[Skins].Sandune;]                                                                                             |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [            ViewData\[[\"myRotatorModel\"]\] = myModel;]                                                                                       |
|                                                                                                                                                                                                             |
| [            [return] View();]                                                                                                                     |
|                                                                                                                                                                                                             |
| [        }]                                                                                                                                                             |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

 

The following figures show the output:

 

{border="0"}[]

Figure 225: Horizontal Rotator Control

 

{border="0"}

 

Figure 226: Vertical Rotator Control

 

[]{#related-topics}

