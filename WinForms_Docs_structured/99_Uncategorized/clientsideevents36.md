---
title: clientsideevents36.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents36.md
created_at: 2025-08-05
---






##### Client-side events {#client-side-events style="tab-stops: 0pt"}

 

  --------------------------------- --------------------------------------------------------------------------------------------- ------------ -----------------
  Name                              Description                                                                                   Arguments    Reference Links
  ClientSideOnCreate                This event is triggered when progressbar is created.                                          event,args   NA
  ClientSideOnChange                This event is triggered when the value of the progressbar changes.                            event,args   NA
  ClientSideOnComplete              This event is triggered when the value of the progressbar reaches the maximum value of 100.   event,args   NA
  ClientSideOnCustomTextRendering   This event is triggered when the custom value is added with the progressbar value.            event,args   NA
  --------------------------------- --------------------------------------------------------------------------------------------- ------------ -----------------

 

You can handle client-side events using the following two ways-

 

**[Using Builder]**

The following steps guide in handling client side events through Builder:

1.   In **View**, [invoke the ProgressBar helper with the **ProgressBar** **id** as the first argument ]followed[ by the **Client side events**.][ ]

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                 |
|                                                                                                                                    |
| [\<%][{]                                                           |
|                                                                                                                                    |
| [      Html.Syncfusion().ProgressBar(][\"Progress\"][)]        |
|                                                                                                                                    |
| [      .Height(22)]                                                                                          |
|                                                                                                                                    |
| [      .Width(700)]                                                                                          |
|                                                                                                                                    |
| [      .Value(50)]                                                                                           |
|                                                                                                                                    |
| [      .AllowCustomText(][true][)]                                |
|                                                                                                                                    |
| [      .Orientation(][ProgressBarOrientation][.Horizontal)]    |
|                                                                                                                                    |
| [      .Minimum(10)]                                                                                         |
|                                                                                                                                    |
| [      .Maximum(100)]                                                                                        |
|                                                                                                                                    |
| [      .ClientSideOnChange(][\"onChange\"][)]                  |
|                                                                                                                                    |
| [      .ClientSideOnCreate(][\"onCreate\"][) ]                 |
|                                                                                                                                    |
| [      .ClientSideOnComplete(][\"onComplete\"][)      ]        |
|                                                                                                                                    |
| [      .ClientSideOnCustomTextRendering(][\"onCustomText\"][)] |
|                                                                                                                                    |
| [      .Render() ;]                                                                                          |
|                                                                                                                                    |
| [  } [%\>]]                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| [ ][\[Razor\]]                                                  |
|                                                                                                                                    |
| []                                                                                       |
|                                                                                                                                    |
| [\@{][   ]   |
|                                                                                                                                    |
| [      Html.Syncfusion().ProgressBar(][\"Progress\"][)]        |
|                                                                                                                                    |
| [      .Height(22)]                                                                                          |
|                                                                                                                                    |
| [      .Width(700)]                                                                                          |
|                                                                                                                                    |
| [      .Value(50)]                                                                                           |
|                                                                                                                                    |
| [      .AllowCustomText(][true][)]                                |
|                                                                                                                                    |
| [      .Orientation(][ProgressBarOrientation][.Horizontal)]    |
|                                                                                                                                    |
| [      .Minimum(10)]                                                                                         |
|                                                                                                                                    |
| [      .Maximum(100)]                                                                                        |
|                                                                                                                                    |
| [      .ClientSideOnChange(][\"onChange\"][)]                  |
|                                                                                                                                    |
| [      .ClientSideOnCreate(][\"onCreate\"][) ]                 |
|                                                                                                                                    |
| [      .ClientSideOnComplete(][\"onComplete\"][)      ]        |
|                                                                                                                                    |
| [      .ClientSideOnCustomTextRendering(][\"onCustomText\"][)] |
|                                                                                                                                    |
| [      .Render() ;]                                                                                          |
|                                                                                                                                    |
| [}][]      |
|                                                                                                                                    |
| []                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

[2.   [In Javascript, use the methods to enable and disable an item as follows:]]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**[]                                                                                           |
|                                                                                                                                                                                          |
| [\<[script] [type]=\"text/javascript\"\>]                                                                 |
|                                                                                                                                                                                          |
| [function][ onComplete(sender, args)]                                                                                                         |
|                                                                                                                                                                                          |
| [ {]                                                                                                                                                               |
|                                                                                                                                                                                          |
| [            //args:]                                                                                                                                          |
|                                                                                                                                                                                          |
|             [//  \_Value             - Value of the ProgressBar]                                                                                               |
|                                                                                                                                                                                          |
|             [// \_ProgressBar        -Details of the ProgressBar][]                                                                      |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                          |
| [function][ onCreate(sender, args)]                                                                                                           |
|                                                                                                                                                                                          |
| [ {]                                                                                                                                                               |
|                                                                                                                                                                                          |
| [            //args:][]                                                                        |
|                                                                                                                                                                                          |
| [            [//  \_Value             - Value of the ProgressBar]]                                                         |
|                                                                                                                                                                                          |
| [            [// \_ProgressBar        -Details of the ProgressBar]]                                                        |
|                                                                                                                                                                                          |
| []                                                                                                                                                                 |
|                                                                                                                                                                                          |
| []                                                                                                                                                                 |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                          |
| [function][ onChange(sender, args) ]                                                                                                          |
|                                                                                                                                                                                          |
| [{]                                                                                                                                                                |
|                                                                                                                                                                                          |
| [            //args:][]                                                                        |
|                                                                                                                                                                                          |
| [            [//  \_Value             - Value of the ProgressBar]]                                                         |
|                                                                                                                                                                                          |
| [            [// \_ProgressBar        -Details of the ProgressBar]]                                                        |
|                                                                                                                                                                                          |
| []                                                                                                                                                                 |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                          |
| [function][ onCustomText(sender, args)]                                                                                                       |
|                                                                                                                                                                                          |
| [ {]                                                                                                                                                               |
|                                                                                                                                                                                          |
| [ ][  //args:][]                             |
|                                                                                                                                                                                          |
| [              [//  \_Value                - Value of the ProgressBar]]                                                    |
|                                                                                                                                                                                          |
| [             [// \_ProgressBar        -Details of the ProgressBar   ][]]                            |
|                                                                                                                                                                                          |
| [    ][        [//  \_Context              -Context of the ProgressBar]] |
|                                                                                                                                                                                          |
| []                                                                                                                                                                 |
|                                                                                                                                                                                          |
| [    ]       [//  \_Width =  width of the ][ProgressBar][;]                              |
|                                                                                                                                                                                          |
| [           //  \_OffsetX = OffsetX of the ][ProgressBar text][;]                                              |
|                                                                                                                                                                                          |
| [           //  \_OffsetY = OffsetY of the ][ProgressBar text][;]                                              |
|                                                                                                                                                                                          |
| [             //  \_Height = height of the ][ProgressBar][;]                                                   |
|                                                                                                                                                                                          |
| [            // \_Radius = radius of the ][ProgressBar][;]                                                     |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                          |
| \</[script\>]                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Using Properties Model

The following steps guide in handling client side events through the Properties model.

1.   [In ]Controller[, create an object for the **ProgressBarModel** class and set the **ClientSide Events**. Assign this model class to view data.][ ]

[] 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[]                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [public][ ][ActionResult][ Index()]                                                                                                                                |
|                                                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [            ][ProgressBarPropertiesModel][ model = ][new][ ][ProgressBarPropertiesModel][();] |
|                                                                                                                                                                                                                                                             |
| [            model.Height = 22;]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [            model.Width = 700;]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [            model.Value = 50;]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [            model.AllowCustomText = ][true][;]                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| [            model.Orientation = ][ProgressBarOrientation][.Horizontal;]                                                                                                                |
|                                                                                                                                                                                                                                                             |
| [            model.Minimum = 10;]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [            model.Maximum = 100;]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [            model.ClientSideOnChange = ][\"onChange\"][;]                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [            model.ClientSideOnCreate = ][\"onCreate\"][;]                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [            model.ClientSideOnComplete = ][\"onComplete\"][;]                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| [            model.ClientSideOnCustomTextRendering = ][\"onCustomText\"][;]                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [            ViewData\[][\"Progress\"][\] = model;]                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [            ][return][ View();]                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

[2.   ]In View, invoke the ProgressBar helper with the view data key as the control ID[.][]

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[View\]]**[]                                        |
|                                                                                                                                 |
| [\<%][{]                                                        |
|                                                                                                                                 |
| [      Html.Syncfusion().ProgressBar(][\"Progress\"][)]     |
|                                                                                                                                 |
| [      .Render();]                                                                                        |
|                                                                                                                                 |
| [  } [%\>]][] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 


+----------------------------------------------------------------------------------------------------------------------------------+
| [ ][\[Razor\]]                                                |
|                                                                                                                                  |
| []                                                                                     |
|                                                                                                                                  |
| [\@{][   ] |
|                                                                                                                                  |
| [      Html.Syncfusion().ProgressBar(][\"Progress\"][)]      |
|                                                                                                                                  |
| [      .Render();]                                                                                         |
|                                                                                                                                  |
| [}][]    |
+----------------------------------------------------------------------------------------------------------------------------------+


[] 

[3.   ]In **[Javascript]**[, define the function to handle the specified events:][]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [\[Javascript\]]                                                                                                                                     |
|                                                                                                                                                                                          |
| [\<[script] [type]=\"text/javascript\"\>]                                                                 |
|                                                                                                                                                                                          |
| [function][ onComplete(sender, args)]                                                                                                         |
|                                                                                                                                                                                          |
| [ {]                                                                                                                                                               |
|                                                                                                                                                                                          |
| [            //args:][]                                                                        |
|                                                                                                                                                                                          |
| [            [//  \_Value             - Value of the ProgressBar]]                                                         |
|                                                                                                                                                                                          |
| [            [// \_ProgressBar        -Details of the ProgressBar]]                                                        |
|                                                                                                                                                                                          |
| []                                                                                                                                                                 |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                          |
| [function][ onCreate(sender, args)]                                                                                                           |
|                                                                                                                                                                                          |
| [ {]                                                                                                                                                               |
|                                                                                                                                                                                          |
| [            //args:][]                                                                        |
|                                                                                                                                                                                          |
| [            [//  \_Value             - Value of the ProgressBar]]                                                         |
|                                                                                                                                                                                          |
| [            [// \_ProgressBar        -Details of the ProgressBar]]                                                        |
|                                                                                                                                                                                          |
| []                                                                                                                                                                 |
|                                                                                                                                                                                          |
| []                                                                                                                                                                 |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                          |
| [function][ onChange(sender, args) ]                                                                                                          |
|                                                                                                                                                                                          |
| [{]                                                                                                                                                                |
|                                                                                                                                                                                          |
| [            //args:][]                                                                        |
|                                                                                                                                                                                          |
| [            [//  \_Value             - Value of the ProgressBar]]                                                         |
|                                                                                                                                                                                          |
| [            [// \_ProgressBar        -Details of the ProgressBar]]                                                        |
|                                                                                                                                                                                          |
| []                                                                                                                                                                 |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                          |
| [function][ onCustomText(sender, args)]                                                                                                       |
|                                                                                                                                                                                          |
| [ {]                                                                                                                                                               |
|                                                                                                                                                                                          |
| [ ][  //args:][]                             |
|                                                                                                                                                                                          |
| [              [//  \_Value                - Value of the ProgressBar]]                                                    |
|                                                                                                                                                                                          |
| [             [// \_ProgressBar        -Details of the ProgressBar   ][]]                            |
|                                                                                                                                                                                          |
| [    ][        [//  \_Context              -Context of the ProgressBar]] |
|                                                                                                                                                                                          |
| []                                                                                                                                                                 |
|                                                                                                                                                                                          |
| [    ]       [//  \_Width =  width of the ][ProgressBar][;]                              |
|                                                                                                                                                                                          |
| [           //  \_OffsetX = OffsetX of the ][ProgressBar text][;]                                              |
|                                                                                                                                                                                          |
| [           //  \_OffsetY = OffsetY of the ][ProgressBar text][;]                                              |
|                                                                                                                                                                                          |
| [             //  \_Height = height of the ][ProgressBar][;]                                                   |
|                                                                                                                                                                                          |
| [            // \_Radius = radius of the ][ProgressBar][;]                                                     |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                                |
|                                                                                                                                                                                          |
| [\</[script\>][]]                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

