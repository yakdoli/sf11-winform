---
title: clientsideevents39.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents39.md
created_at: 2025-07-03
---






#### Client-side events {#client-side-events style="LINE-HEIGHT: 115%; MARGIN: 10pt 0pt 0pt; tab-stops: 0pt"}

 


  --------------------- ----------------------------------------------------------------------- ----------- -----------------
  Name                  Description                                                             Arguments   Reference Links
  ClientSideClick       This event is called when you click on the Rotator Items.               inst,args   NA
  ClientSideMouseOut    This event is raised upon mouse-out of the visible item.                inst,args   NA
  ClientSideMouseOver   This event is raised upon mouse-over of any of the visible items.       inst,args   NA
  ClientSideOnLoaded    This event is raised when the control is loaded from the client-side.   inst,args   NA
  --------------------- ----------------------------------------------------------------------- ----------- -----------------


[] 

You can handle client-side events using the following two ways-

 

**[Using Builder]**

The following steps guide in handling client side events through Builder:

1.   In **View**, create ul-li (Unordered list) hierarchy of rotator items and invoke the rotator helper with rotator contents ID as the first argument and enable the **ClientSideOnClick** and **ClientSideOnMouseOver **with the respective handlers as:

 

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
| [\<%][=][Html.Syncfusion().Rotator([\"rotatoritems\"])]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [       **.ClientSideOnLoded([\"OnLoaded\"])**]                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[       .ClientSideOnClick([\"OnClick\"])]**[]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[       .ClientSideOnMouseOut([\"OnMouseOut\"])]**[]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[       .ClientSideOnMouseOver([\"OnMouseOver\"])]**[%\>][]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Define the call back methods in the script to handle the specified events.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**[]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                 |
| [        [function] OnLoaded() {[]]                                                                                                              |
|                                                                                                                                                                                                                                 |
| [                    }]                                                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| [        [function] OnMouseOver(inst, args) {]                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of rotator object]]                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentItem   - current rotator item]]                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_itemIndex     - rotator item index ]]                                                                                                |
|                                                                                                                                                                                                                                 |
| [              ]                                                                                                                                                              |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnMouseOut(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of rotator object]]                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentItem   - current rotator item]]                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_itemIndex     - rotator item index ]]                                                                                                |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnClick(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of rotator object]]                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentItem   - current rotator item]]                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_itemIndex     - rotator item index ]]                                                                                                |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Run the application.

[] 

Using Properties Model

[The following steps guide in handling client side events through the Properties model.]

1.   In Controller, create an instance of RotatorModel, define the **ClientSideOnLoded**,**ClientSideOnClick**, **ClientSideOnMouseOver** and **ClientSideOnMouseOut** events and pass the instance through **view-specific data** to **View** as given below.

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
| [            myModel.ClientSideOnLoded=[\"OnLoaded\"];]                                                     |
|                                                                                                                                                                         |
| [            myModel.ClientSideOnClick=[\"OnClick\"];]                                                      |
|                                                                                                                                                                         |
| [            myModel.ClientSideOnMouseOut=[\"OnMouseOut\"];]                                                |
|                                                                                                                                                                         |
| [            myModel.ClientSideOnMouseOver = [\"OnMouseOver\"];]                                            |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [            ViewData\[[\"myRotatorModel\"]\] = myModel;]                                                   |
|                                                                                                                                                                         |
| [            [return] View();]                                                                                 |
|                                                                                                                                                                         |
| [        }]                                                                                                                         |
|                                                                                                                                                                         |
| []                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, create ul-li hierarchy of rotator items and invoke the rotator helper with Rotator contents ID as the first argument and view data key as the second argument.

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
| [\<%][=][Html.Syncfusion().Rotator([\"rotatoritems\"], [\"myRotatorModel\"])[%\>]]                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Define the call back methods in the script to handle the specified events.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**[]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                 |
| [        [function] OnLoaded() {]                                                                                                                                      |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnMouseOver(inst, args) {]                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of rotator object]]                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentItem   - current rotator item]]                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_itemIndex     - rotator item index ]]                                                                                                |
|                                                                                                                                                                                                                                 |
| [              ][]                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnMouseOut(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of rotator object]]                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentItem   - current rotator item]]                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_itemIndex     - rotator item index ]]                                                                                                |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnClick(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of rotator object]]                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentItem   - current rotator item]]                                                                                               |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_itemIndex     - rotator item index ]]                                                                                                |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [  ]                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Run the application.

 

[]{#related-topics}

