---
title: usingpropertiesmodel80.md
original_path: WinForms_Docs/99_Uncategorized/usingpropertiesmodel80.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model        {#using-properties-model style="tab-stops: 0pt"}

The following steps guide in handling client side events through the Properties model.

[1.   ] [In ]Controller[, create an object for the][ **Mob**]**[ProgressBarPropertiesModel]**[ ][class and set the][ ]**[ClientSide Events]**[. Assign this model class to view data.][ ]


+-------------------------------------------------------------------------------------------------+
| **[\[Controller\]]** [] |
|                                                                                                 |
| ```                                             |
|                   public                                                                        |
|                                                                                                 |
|                   ActionResult                                                                  |
|                    Index()                                                                      |
|                                                                                                 |
| ```                                                                                             |
|                                                                                                 |
| ```                                             |
|                           {                                                                     |
|                                                                                                 |
| ```                                                                                             |
|                                                                                                 |
| ```                                             |
|                                                                                                 |
|                   MobProgressBarPropertiesModel                                                 |
|                    model =                                                                      |
|                   new                                                                           |
|                                                                                                 |
|                   MobProgressBarPropertiesModel                                                 |
|                   ();                                                                           |
|                                                                                                 |
| ```                                                                                             |
|                                                                                                 |
| ```                                             |
|                               model.Value = 50;                                                 |
|                                                                                                 |
| ```                                                                                             |
|                                                                                                 |
| ```                                             |
|                               model.ClientSideOnChange =                                        |
|                                                                                                 |
|                     "onChange"                                                                  |
|                     ;                                                                           |
|                                                                                                 |
|                                                                                                 |
| ```                                                                                             |
|                                                                                                 |
| ```                                             |
|                                                                                                 |
|                                 model.ClientSideOnCreate =                                      |
|                     "onCreate"                                                                  |
|                     ;                                                                           |
|                                                                                                 |
|                                                                                                 |
| ```                                                                                             |
|                                                                                                 |
| ```                                             |
|                                                                                                 |
|                                 model.ClientSideOnComplete =                                    |
|                     "onComplete"                                                                |
|                     ;                                                                           |
|                                                                                                 |
|                                                                                                 |
| ```                                                                                             |
|                                                                                                 |
| ```                                             |
|                                                                                                 |
|                                 model.ClientSideOnCustomTextRendering =                         |
|                     "onCustomText"                                                              |
|                     ;                                                                           |
|                                                                                                 |
|                                                                                                 |
| ```                                                                                             |
|                                                                                                 |
| ```                                             |
|                               ViewData[                                                         |
|                   "ProgressBar"                                                                 |
|                   ] = model;                                                                    |
|                                                                                                 |
| ```                                                                                             |
|                                                                                                 |
| ```                                             |
|                                                                                                 |
|                   return                                                                        |
|                    View();                                                                      |
|                                                                                                 |
| ```                                                                                             |
|                                                                                                 |
| ```                                             |
|                           }                                                                     |
| ```                                                                                             |
+-------------------------------------------------------------------------------------------------+


[] 

2.   In View, invoke the ProgressBar helper with the control id and view data key as arguments.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                            |
| [\<%] [=] [ Html.MobSyncfusion().ProgressBar([\"pBar\"], [\"progressBar\"])[%\>]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| ```                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| ```                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| ```                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| ```                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [\@{] []                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [               ] [Html.MobSyncfusion().ProgressBar([\"pBar\"], [\"progressBar\"])[.Render(); ]] |
|                                                                                                                                                                                                                                                              |
| [}] []                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   [In][ ]**[Javascript]**[, define the function to handle the specified events:]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [\[Javascript\]]                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [\<[script][type]=\"text/javascript\"\>]                                                                                        |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                              |
|                 function                                                                                                                                                                                       |
|                  onComplete(sender, args)                                                                                                                                                                      |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                              |
|                  {                                                                                                                                                                                             |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| [//args:] []                                                                                                         |
|                                                                                                                                                                                                                |
| [       [//  \_Value             - Value of the ProgressBar]]                                                                                    |
|                                                                                                                                                                                                                |
| [      [// \_ProgressBar        -Details of the ProgressBar]]                                                                                    |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                 }                                                                                                                                                                                              |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                 function                                                                                                                                                                                       |
|                  onCreate(sender, args)                                                                                                                                                                        |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                  {                                                                                                                                                                                             |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| [  //args:] []                                                                                                       |
|                                                                                                                                                                                                                |
| [       [//  \_Value             - Value of the ProgressBar]]                                                                                    |
|                                                                                                                                                                                                                |
| [      [// \_ProgressBar        -Details of the ProgressBar]]                                                                                    |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                 }                                                                                                                                                                                              |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                 function                                                                                                                                                                                       |
|                  onChange(sender, args)                                                                                                                                                                        |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                 {                                                                                                                                                                                              |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| [//args:] []                                                                                                         |
|                                                                                                                                                                                                                |
| [       [//  \_Value             - Value of the ProgressBar]]                                                                                    |
|                                                                                                                                                                                                                |
| [      [// \_ProgressBar        -Details of the ProgressBar]]                                                                                    |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                 }                                                                                                                                                                                              |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                 function                                                                                                                                                                                       |
|                  onCustomText(sender, args)                                                                                                                                                                    |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                  {                                                                                                                                                                                             |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| [ ] [  //args:] []                                                 |
|                                                                                                                                                                                                                |
| [    [//  \_Value                - Value of the ProgressBar]]                                                                                    |
|                                                                                                                                                                                                                |
| [   [// \_ProgressBar        -Details of the ProgressBar   ][]]                                                            |
|                                                                                                                                                                                                                |
| [    ] [//  \_Context              -Context of the ProgressBar] [] |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                              |
|                                                                                                                                                                                                                |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                              |
|                                                                                                                                                                                                                |
|                 //  _Width =  width of the                                                                                                                                                                     |
|                 ProgressBar                                                                                                                                                                                    |
|                 ;                                                                                                                                                                                              |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                              |
|                     //  _OffsetX = OffsetX of the                                                                                                                                                              |
|                 ProgressBar text                                                                                                                                                                               |
|                 ;                                                                                                                                                                                              |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                              |
|                     //  _OffsetY = OffsetY of the                                                                                                                                                              |
|                 ProgressBar text                                                                                                                                                                               |
|                 ;                                                                                                                                                                                              |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                              |
|                     //  _Height = height of the                                                                                                                                                                |
|                 ProgressBar                                                                                                                                                                                    |
|                 ;                                                                                                                                                                                              |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                              |
|                     // _Radius = radius of the                                                                                                                                                                 |
|                 ProgressBar                                                                                                                                                                                    |
|                 ;                                                                                                                                                                                              |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                 |
|                 }                                                                                                                                                                                              |
|                                                                                                                                                                                                                |
| ```                                                                                                                                                                                                            |
|                                                                                                                                                                                                                |
| [\</[script\>][]]                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[[ [] ]]{.underline}**  

4.   Build and run the application.

You can observe the handlers getting invoked when the corresponding event is triggered.

 

[]{#related-topics}

