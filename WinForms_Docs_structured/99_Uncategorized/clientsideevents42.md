---
title: clientsideevents42.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents42.md
created_at: 2025-08-05
---






#### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

The tab control supports client-side event handling to modify the control's behavior.

 

Events

 

  --------------------- ---------------------------------------------------------------------------- ----------- ----------------
  Name                  Description                                                                  Arguments   Reference Link
  ClientSideOnShow      This event is triggered when a tab is shown.                                 event,ui    NA
  ClientSideOnSelect    This event is triggered when clicking a tab.                                 event,ui    NA
  ClientSideOnDisable   This event is triggered when a tab is disabled.                              event,ui    NA
  ClientSideOnEnable    This event is triggered when a tab is enabled.                               event,ui    NA
  ClientSideOnLoad      This event is triggered after the content of a remote tab has been loaded.   event,ui    NA
  ClientSideOnAdd       This event is triggered when a tab is added.                                 event,ui    NA
  ClientSideOnRemove    This event is triggered when a tab is removed.                               event,ui    NA
  --------------------- ---------------------------------------------------------------------------- ----------- ----------------

*[[]]{.underline}* 

Using Builder

The following steps explain how to set jQuery themes for the tab control through builder.

1.   In **View**, create the contents of the tab with *ul* and *li* (for headers) and *div* tags (for content), and invoke the tab helper with the control ID as the first argument, followed by the **AutoFormat** method with the desired theme as an argument.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][div][ [id][=\"tabContents\"] [style][=\"][visibility][: hidden\"\>]]                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][ul][\>]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#tools\"\>]Essential Tools[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#chart\"\>]Essential Chart[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#grid\"\>]Essential Grid[\</][a][\>\</][li][\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][ul][\>]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"tools\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Tools is a collection of user-interface components used to create interactive ASP.NET MVC applications.]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"chart\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Chart is a business-oriented charting component. Essential Chart features an advanced styles architecture that makes complex multi-level formatting very easy.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"grid\"\>]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Grid MVC offers a full-featured grid control with extensive support for grouping and displaying hierarchical data.]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [       [\</][div][\>]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().Tab([\"myTab1\"])]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [.TargetControlId([\"tabContents\"])]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                  .ClientSideOnSelect([\"OnSelect\"])]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [.ClientSideOnShow([\"OnShow\"])[%\>]]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][div][ [id][=\"tabContents\"] [style][=\"][visibility][: hidden\"\>]]                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][ul][\>]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#tools\"\>]Essential Tools[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#chart\"\>]Essential Chart[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#grid\"\>]Essential Grid[\</][a][\>\</][li][\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][ul][\>]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"tools\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Tools is a collection of user-interface components used to create interactive ASP.NET MVC applications.]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"chart\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Chart is a business-oriented charting component. Essential Chart features an advanced styles architecture that makes complex multi-level formatting very easy.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"grid\"\>]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Grid MVC offers a full-featured grid control with extensive support for grouping and displaying hierarchical data.]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [       [\</][div][\>]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\@{][ Html.Syncfusion().Tab([\"myTab1\"])]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [.TargetControlId([\"tabContents\"])]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                  .ClientSideOnSelect([\"OnSelect\"])]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [.ClientSideOnShow([\"OnShow\"]).Render();[}]]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In JavaScript, define the handlers.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [        [function] OnSelect(event, ui) {]                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//event     - object passed by the jQuery event trigger. ]]                                                                                        |
|                                                                                                                                                                                                                                |
| [            [//ui:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//  index   - index of the current tab]]                                                                                                           |
|                                                                                                                                                                                                                                |
| [            [//  panel   - current panel as a DOM element]]                                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//  tab     - current tab as a DOM element]]                                                                                                       |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnShow(event, ui) {]                                                                                                                              |
|                                                                                                                                                                                                                                |
| [            [//event     - object passed by the jQuery event trigger. ]]                                                                                        |
|                                                                                                                                                                                                                                |
| [            [//ui:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//  index   - index of the current tab]]                                                                                                           |
|                                                                                                                                                                                                                                |
| [            [//  panel   - current panel as a DOM element]]                                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//  tab     - current tab as a DOM element]]                                                                                                       |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [      [\</][script][\>]]                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

Using Properties Model

The following steps explain how to set Syncfusion themes for the tab control through the properties model.

1.   In the controller, create an instance of **TabModel**.**

2.   Define the **AutoFormat** property and pass the instance through the **view-specific data** to the **view**.**

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                        |
|                                                                                                                                                                 |
| [public][ [ActionResult] Index()]                  |
|                                                                                                                                                                 |
| [        {]                                                                                                                 |
|                                                                                                                                                                 |
| [            [//Create an instance of TabModel.]]                                                     |
|                                                                                                                                                                 |
| [            [TabModel] myModel = [new] [TabModel]();] |
|                                                                                                                                                                 |
| [            myModel.TargetControlId = [\"tabContents\"];]                                          |
|                                                                                                                                                                 |
| [            **myModel.ClientSideOnSelect = [\"OnSelect\"];**]                                      |
|                                                                                                                                                                 |
| **[           myModel.ClientSideOnShow = [\"OnShow\"];]**                                           |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [            [//Pass the instance through the view data to the view.]]                                |
|                                                                                                                                                                 |
| [            ViewData\[[\"myTab\"]\] = myModel;]                                                    |
|                                                                                                                                                                 |
| [            [return] View();]                                                                         |
|                                                                                                                                                                 |
| [        }]                                                                                                                 |
|                                                                                                                                                                 |
| []                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

***[[[]]]{.underline}*** 

3.   In **View**, create the contents of the tabs with *ul* and *li* (for headers) and *div* tags (for content), and invoke the tab helper with the view data key as the control ID.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][div][ [id][=\"tabContents\"] [style][=\"][visibility][: hidden\"\>]]                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][ul][\>]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#tools\"\>]Essential Tools[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#chart\"\>]Essential Chart[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#grid\"\>]Essential Grid[\</][a][\>\</][li][\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][ul][\>]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"tools\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Tools is a collection of user-interface components used to create interactive ASP.NET MVC applications.]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"chart\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Chart is a business-oriented charting component. Essential Chart features an advanced styles architecture that makes complex multi-level formatting very easy.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"grid\"\>]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Grid MVC offers a full-featured grid control with extensive support for grouping and displaying hierarchical data.]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [       [\</][div][\>]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().Tab([\"myTab\"])[%\>]]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][div][ [id][=\"tabContents\"] [style][=\"][visibility][: hidden\"\>]]                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][ul][\>]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#tools\"\>]Essential Tools[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#chart\"\>]Essential Chart[\</][a][\>\</][li][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][li][\>\<][a] [href][=\"#grid\"\>]Essential Grid[\</][a][\>\</][li][\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][ul][\>]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"tools\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Tools is a collection of user-interface components used to create interactive ASP.NET MVC applications.]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"chart\"\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Chart is a business-oriented charting component. Essential Chart features an advanced styles architecture that makes complex multi-level formatting very easy.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [id][=\"grid\"\>]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Essential Grid MVC offers a full-featured grid control with extensive support for grouping and displaying hierarchical data.]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [       [\</][div][\>]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\@{][ Html.Syncfusion().Tab([\"myTab\"]).Render();[}]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

4.   In JavaScript, define the handlers.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [        [function] OnSelect(event, ui) {]                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//event     - object passed by the jQuery event trigger]]                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//ui:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//  index   - index of the current tab]]                                                                                                           |
|                                                                                                                                                                                                                                |
| [            [//  panel   - current panel as a DOM element]]                                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//  tab     - current tab as a DOM element]]                                                                                                       |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnShow(event, ui) {]                                                                                                                              |
|                                                                                                                                                                                                                                |
| [            [//event     - object passed by the jQuery event trigger. ]]                                                                                        |
|                                                                                                                                                                                                                                |
| [            [//ui:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//  index   - index of the current tab]]                                                                                                           |
|                                                                                                                                                                                                                                |
| [            [//  panel   - current panel as a DOM element]]                                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//  tab     - current tab as a DOM element]]                                                                                                       |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [      [\</][script][\>]]                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

5.   Build and run the application.

After performing the above steps, you can observe the handlers being invoked when the corresponding events are raised.

 

 

Adding handlers at run time

Load

This event is triggered after the content of a remote tab has been loaded.

+-------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                          |
|                                                                                                                   |
| [ \$([\"#myTab\"]).tabs({]                            |
|                                                                                                                   |
| [                  load: [function](event, ui) {]        |
|                                                                                                                   |
| [                        alert([\"Tab is loaded\"]);] |
|                                                                                                                   |
| [                  }]                                                         |
|                                                                                                                   |
| [        });]                                                                 |
+-------------------------------------------------------------------------------------------------------------------+

***[]*** 


Note: Similarly, you can use all the client-side events of Jquery tabs in Essential Tools for MVC Tabs control. For more details, refer to the following link.


 

[[http://docs.jquery.com/UI/Tabs#events]{.UGHyperlink}](http://docs.jquery.com/UI/Tabs#events)[]{.UGHyperlink}

 

[]{#related-topics}

