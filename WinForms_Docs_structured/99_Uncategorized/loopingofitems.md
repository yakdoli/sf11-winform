---
title: loopingofitems.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\loopingofitems.md
created_at: 2025-07-03
---






##### Looping of items {#looping-of-items style="tab-stops: 0pt"}

The Rotator control allows you to view items in a loop if you enable the Circular property.

**Properties**

+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------+-------------+
| Name        | Description                                                                                                                               | Type of property | Value it accepts       | Dependency  |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------+-------------+
| Circular    | [Specifies whether to repeat the slides after a complete tour of slides has been exhibited. Default value is true.] | Boolean          | True                   | NA          |
|             |                                                                                                                                           |                  |                        |             |
|             |                                                                                                                                           |                  | False                  |             |
|             |                                                                                                                                           |                  |                        |             |
|             |                                                                                                                                           |                  | Default value is False |             |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------+-------------+

 

You can enable this property in the following two ways-

 

**[Using Builder]**

[The following steps guide you in configuring the circular through Builder.]

1.   In **View**, create ul-li hierarchy of rotator items and invoke the rotator helper with the rotator Contents ID as the first argument and enable the **Circular** method with the desired option as argument.

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
| [\<%][=][Html.Syncfusion().Rotator([\"rotatoritems\"]).Circular([true]) [ %\>]]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [   ]                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Run the application.

**[]** 

**[Using Properties Model]**

[The following steps will guide you in setting the circular through the Properties model.]

1.   In the **Controller**, create an instance of RotatorModel, define the **Circular** property and pass the instance through view-specific data to View as given below.

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
| [            **myModel.Circular =**[ true]**;**]                                                               |
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

2.   In **View**, create ul-li hierarchy of rotator items and invoke the rotator helper with the rotator content ID as the first argument and view data key as the second argument. 

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

***[{border="0"}]**[Note: The second argument of the above rotator helper should match the view data key from the controller to fetch the properties.]***

3.   Run the application.

[]{#related-topics}

