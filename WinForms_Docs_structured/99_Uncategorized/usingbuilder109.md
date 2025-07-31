---
title: usingbuilder109.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder109.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps guide in handling client side events through Builder:

[1.   ]In **View**, [invoke the ProgressBar helper with the **ProgressBarid** as the first argument ]followed[ by the][ ]**[Client side events]**[.][ ]

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                        |
|                                                                                                                                                                                                           |
| [\<%] [Html.MobSyncfusion().ProgressBar([\"progressBar\"])] |
|                                                                                                                                                                                                           |
| [       .Value(30)]                                                                                                                                      |
|                                                                                                                                                                                                           |
| [      **.ClientSideOnChange([\"OnChange\"])**]                                                                                  |
|                                                                                                                                                                                                           |
| **[      .ClientSideOnComplete([\"OnComplete\"])]**                                                                              |
|                                                                                                                                                                                                           |
| **[      .ClientSideOnCreate([\"OnCreate\"])]**                                                                                  |
|                                                                                                                                                                                                           |
| **[      .ClientSideOnCustomTextRendering([\"onCustomText\"])]**                                                                 |
|                                                                                                                                                                                                           |
| [      .Render();]                                                                                                                                       |
|                                                                                                                                                                                                           |
| [    [%\>]]                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ ] **[\[Razor\]]**                                                                              |
|                                                                                                                                                               |
| ```                                                                                                                              |
|                                                                                                                                                               |
|                                                                                                                                                               |
| ```                                                                                                                                                           |
|                                                                                                                                                               |
| ```                                                                                                                              |
|                 @{                                                                                                                                            |
|                                                                                                                                                               |
|                                                                                                                                                               |
| ```                                                                                                                                                           |
|                                                                                                                                                               |
| [      ] [Html.MobSyncfusion().ProgressBar([\"progressBar\"])] |
|                                                                                                                                                               |
| [       .Value(30)]                                                                                          |
|                                                                                                                                                               |
| [      **.ClientSideOnChange([\"OnChange\"])**]                                      |
|                                                                                                                                                               |
| **[      .ClientSideOnComplete([\"OnComplete\"])]**                                  |
|                                                                                                                                                               |
| **[      .ClientSideOnCreate([\"OnCreate\"])]**                                      |
|                                                                                                                                                               |
| **[      .ClientSideOnCustomTextRendering([\"onCustomText\"])]**                     |
|                                                                                                                                                               |
| [      .Render();]                                                                                           |
|                                                                                                                                                               |
| [}] []                                |
|                                                                                                                                                               |
| []                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In JavaScript, define the handlers.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]** []                                                                                           |
|                                                                                                                                                                                           |
| [\<[script][type]=\"text/javascript\"\>]                                                                   |
|                                                                                                                                                                                           |
| ```                                                                                                                                       |
|                 function                                                                                                                                                                  |
|                  onComplete(sender, args)                                                                                                                                                 |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                       |
|                  {                                                                                                                                                                        |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                       |
|                             //args:                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                       |
|             //  _Value             - Value of the ProgressBar                                                                                                                             |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                       |
|             // _ProgressBar        -Details of the ProgressBar                                                                                                                            |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                 }                                                                                                                                                                         |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                 function                                                                                                                                                                  |
|                  onCreate(sender, args)                                                                                                                                                   |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                  {                                                                                                                                                                        |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| [            //args:] []                                                                        |
|                                                                                                                                                                                           |
| [            [//  \_Value             - Value of the ProgressBar]]                                                          |
|                                                                                                                                                                                           |
| [            [// \_ProgressBar        -Details of the ProgressBar]]                                                         |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                 }                                                                                                                                                                         |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                 function                                                                                                                                                                  |
|                  onChange(sender, args)                                                                                                                                                   |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                 {                                                                                                                                                                         |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| [            //args:] []                                                                        |
|                                                                                                                                                                                           |
| [            [//  \_Value             - Value of the ProgressBar]]                                                          |
|                                                                                                                                                                                           |
| [            [// \_ProgressBar        -Details of the ProgressBar]]                                                         |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                 }                                                                                                                                                                         |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                 function                                                                                                                                                                  |
|                  onCustomText(sender, args)                                                                                                                                               |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                  {                                                                                                                                                                        |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| [ ] [  //args:] []                            |
|                                                                                                                                                                                           |
| [              [//  \_Value                - Value of the ProgressBar]]                                                     |
|                                                                                                                                                                                           |
| [             [// \_ProgressBar        -Details of the ProgressBar   ][]]                             |
|                                                                                                                                                                                           |
| [    ] [        [//  \_Context              -Context of the ProgressBar]] |
|                                                                                                                                                                                           |
| ```                                                                                                                                       |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                       |
|                            //  _Width =  width of the ProgressBar;                                                                                                                        |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                       |
|                            //  _OffsetX = OffsetX of the                                                                                                                                  |
|                 ProgressBar text                                                                                                                                                          |
|                 ;                                                                                                                                                                         |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                       |
|                            //  _OffsetY = OffsetY of the                                                                                                                                  |
|                 ProgressBar text                                                                                                                                                          |
|                 ;                                                                                                                                                                         |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                       |
|                              //  _Height = height of the                                                                                                                                  |
|                 ProgressBar                                                                                                                                                               |
|                 ;                                                                                                                                                                         |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                       |
|                             // _Radius = radius of the                                                                                                                                    |
|                 ProgressBar                                                                                                                                                               |
|                 ;                                                                                                                                                                         |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
|                 }                                                                                                                                                                         |
|                                                                                                                                                                                           |
| ```                                                                                                                                                                                       |
|                                                                                                                                                                                           |
| ```                                                                                                                                                          |
| </script>                                                                                                                                                                                 |
| ```                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

