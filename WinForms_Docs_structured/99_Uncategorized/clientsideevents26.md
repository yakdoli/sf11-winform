---
title: clientsideevents26.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents26.md
created_at: 2025-08-05
---






#### Client Side Events {#client-side-events style="tab-stops: 0pt"}

Accordion supports client side event handling.

Events

+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Name               | Description                                                                                                                                                                                   | Arguments       | Reference Link  |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| ClientSideOnChange | This event is triggered every time the Accordion changes. If the Accordion is animated, the event will be triggered upon completion of the animation. Otherwise, it is triggered immediately. | event,ui        | \-              |
|                    |                                                                                                                                                                                               |                 |                 |
|                    |                                                                                                                                                                                               |                 |                 |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+

 

Using Builder

The following steps explain the handling of client side events through Builder.

1.   In **View**, create the contents of the Accordion with the header and div tags and invoke the Accordion helper with the control ID as the first argument, followed by the ClientSideOnChange method with the desired handler as argument.

 

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [\<][div][ [id][=\"AccordionContents\"] [style][=\"][visibility][: hidden\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][h3][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][a] [href][=\"#\"\>]About Syncfusion[\</][a][\>\</][h3][\>]]                            |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][div][\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Syncfusion, a world leader in software components have thousands of satisfied customers]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                    |
| [              world-wide who have used our products to ship award winning software.]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\</][div][\>]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][h3][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][a] [href][=\"#\"\>]Technology[\</][a][\>\</][h3][\>]]                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][div][\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Syncfusion products are smartly designed to cope with the fast-changing technology]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                environment.]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\</][div][\>]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][h3][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][a] [href][=\"#\"\>]Contact Us[\</][a][\>\</][h3][\>]]                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][div][\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                Company Headquarters[\<][br] [/\>]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][br] [/\>]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                9001 Aerial Center Parkway[\<][br] [/\>]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                Suite 110[\<][br] [/\>]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                Morrisville, NC 27560[\<][br] [/\>]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                USA.]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\</][div][\>]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [        [\</][div][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                    |
| [ \<%][=][Html.Syncfusion().Accordion([\"myAccordion1\"])]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [               .TargetContentId([\"AccordionContents\"])]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [               .ClientSideOnChange([\"OnChangeHandler\"])[%\>]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                    |
| [\<][div][ [id][=\"AccordionContents\"] [style][=\"][visibility][: hidden\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][h3][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][a] [href][=\"#\"\>]About Syncfusion[\</][a][\>\</][h3][\>]]                            |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][div][\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Syncfusion, a world leader in software components have thousands of satisfied customers]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                    |
| [              world-wide who have used our products to ship award winning software.]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\</][div][\>]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][h3][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][a] [href][=\"#\"\>]Technology[\</][a][\>\</][h3][\>]]                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][div][\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Syncfusion products are smartly designed to cope with the fast-changing technology]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                environment.]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\</][div][\>]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][h3][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][a] [href][=\"#\"\>]Contact Us[\</][a][\>\</][h3][\>]]                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][div][\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                Company Headquarters[\<][br] [/\>]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][br] [/\>]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                9001 Aerial Center Parkway[\<][br] [/\>]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                Suite 110[\<][br] [/\>]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                Morrisville, NC 27560[\<][br] [/\>]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                USA.]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\</][div][\>]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [        [\</][div][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                    |
| [\@{][ ][Html.Syncfusion().Accordion([\"myAccordion1\"])]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                    |
| [               .TargetContentId([\"AccordionContents\"])]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [               .ClientSideOnChange([\"OnChangeHandler\"]).Render();]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [       [}]]                                                                                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   In the Javascirpt, define the handler as below:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                        |
| [\<][script][ [type][=\"text/javascript\"\>]        ] |
|                                                                                                                                                                                                                                        |
| [        [function] OnChangeHandler(event, ui) {]                                                                                                                             |
|                                                                                                                                                                                                                                        |
| [            [//event           - object passed by the jQuery event trigger. ]]                                                                                          |
|                                                                                                                                                                                                                                        |
| [            [//ui:]]                                                                                                                                                    |
|                                                                                                                                                                                                                                        |
| [            [//  ui.newHeader  - jQuery object, activated header]]                                                                                                      |
|                                                                                                                                                                                                                                        |
| [            [//  ui.oldHeader  - jQuery object, previous header]]                                                                                                       |
|                                                                                                                                                                                                                                        |
| [            [//  ui.newContent - jQuery object, activated content]]                                                                                                     |
|                                                                                                                                                                                                                                        |
| [            [//  ui.oldContent - jQuery object, previous content]]                                                                                                      |
|                                                                                                                                                                                                                                        |
| [        }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
| [      [\</][script][\>][]]                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**[]** 

**[]** 

[] 

3.   Build and run the application.

 

Using Properties Model

The following steps explain the handling of client side events through Properties model.

1.   In the Controller, create an instance of AccordionModel, define the **ClientSideOnChange** property and pass the instance through view specific data to View as given below: **

*[[]]{.underline}* 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                    |
|                                                                                                                                                                             |
| [public][ [ActionResult] Index()]                              |
|                                                                                                                                                                             |
| [        {]                                                                                                                             |
|                                                                                                                                                                             |
| [            [//Creating new instance of Accordion Model]]                                                        |
|                                                                                                                                                                             |
| [            [AccordionModel] myModel = [new] [AccordionModel]();] |
|                                                                                                                                                                             |
| [            myModel.TargetControlId = [\"AccordionContents\"];]                                                |
|                                                                                                                                                                             |
| [            myModel.ClientSideOnChange = [\"OnChangeHandler\"];               ]                                |
|                                                                                                                                                                             |
| [            ]                                                                                                                          |
|                                                                                                                                                                             |
| [            [//Passing the model through View Data]]                                                             |
|                                                                                                                                                                             |
| [            ViewData\[[\"myAccordion\"]\] = myModel;]                                                          |
|                                                                                                                                                                             |
| [            [return] View();]                                                                                     |
|                                                                                                                                                                             |
| [        }]                                                                                                                             |
|                                                                                                                                                                             |
| []                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*[[]]{.underline}* 

*[[[]]]{.underline}* 

**[]** 

[] 

2.   In **View**, create the contents of the Accordion with header and div tags and invoke the accordion helper with view data key as the control ID.

 

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [\<][div][ [id][=\"AccordionContents\"] [style][=\"][visibility][: hidden\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][h3][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][a] [href][=\"#\"\>]About Syncfusion[\</][a][\>\</][h3][\>]]                            |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][div][\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Syncfusion, a world leader in software components have thousands of satisfied customers]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                    |
| [              world-wide who have used our products to ship award winning software.]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\</][div][\>]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][h3][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][a] [href][=\"#\"\>]Technology[\</][a][\>\</][h3][\>]]                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][div][\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Syncfusion products are smartly designed to cope with the fast-changing technology]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                environment.]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\</][div][\>]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][h3][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][a] [href][=\"#\"\>]Contact Us[\</][a][\>\</][h3][\>]]                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][div][\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                Company Headquarters[\<][br] [/\>]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][br] [/\>]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                9001 Aerial Center Parkway[\<][br] [/\>]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                Suite 110[\<][br] [/\>]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                Morrisville, NC 27560[\<][br] [/\>]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                USA.]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\</][div][\>]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [        [\</][div][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                    |
| [ [\<%][=]Html.Syncfusion().Accordion([\"myAccordion\"])[%\>]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                    |
| [\<][div][ [id][=\"AccordionContents\"] [style][=\"][visibility][: hidden\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][h3][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][a] [href][=\"#\"\>]About Syncfusion[\</][a][\>\</][h3][\>]]                            |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][div][\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Syncfusion, a world leader in software components have thousands of satisfied customers]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                    |
| [              world-wide who have used our products to ship award winning software.]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\</][div][\>]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][h3][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][a] [href][=\"#\"\>]Technology[\</][a][\>\</][h3][\>]]                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][div][\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [Syncfusion products are smartly designed to cope with the fast-changing technology]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                environment.]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\</][div][\>]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][h3][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][a] [href][=\"#\"\>]Contact Us[\</][a][\>\</][h3][\>]]                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\<][div][\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                Company Headquarters[\<][br] [/\>]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                [\<][br] [/\>]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                9001 Aerial Center Parkway[\<][br] [/\>]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                Suite 110[\<][br] [/\>]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                Morrisville, NC 27560[\<][br] [/\>]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| [                USA.]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                    |
| [            [\</][div][\>]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                    |
| [        [\</][div][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                    |
| [ [\@{][ ]Html.Syncfusion().Accordion([\"myAccordion\"]).Render();[}]]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

3.   In the Javascript, define the handlers as given below:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                        |
| [\<][script][ [type][=\"text/javascript\"\>]        ] |
|                                                                                                                                                                                                                                        |
| [        [function] OnChangeHandler(event, ui) {]                                                                                                                             |
|                                                                                                                                                                                                                                        |
| [            [//event           - object passed by the jQuery event trigger. ]]                                                                                          |
|                                                                                                                                                                                                                                        |
| [            [//ui:]]                                                                                                                                                    |
|                                                                                                                                                                                                                                        |
| [            [//  ui.newHeader  - jQuery object, activated header]]                                                                                                      |
|                                                                                                                                                                                                                                        |
| [            [//  ui.oldHeader  - jQuery object, previous header]]                                                                                                       |
|                                                                                                                                                                                                                                        |
| [            [//  ui.newContent - jQuery object, activated content]]                                                                                                     |
|                                                                                                                                                                                                                                        |
| [            [//  ui.oldContent - jQuery object, previous content]]                                                                                                      |
|                                                                                                                                                                                                                                        |
| [        }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
| [\</][script][\>]                                                                 |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

4.   Build and run the application.

You can observe the handler getting invoked when the corresponding event triggers.

 

Adding Handlers at Runtime

Create

This event will be triggered when accordion is created.

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                 |
|                                                                                                                          |
| [\$([\"#myAccordion\"]).accordion({]                         |
|                                                                                                                          |
| [                  create: [function](event, ui) {]             |
|                                                                                                                          |
| [                        alert([\"Accordion is created\"]);] |
|                                                                                                                          |
| [                  }]                                                                |
|                                                                                                                          |
| [        });][  ]                                |
+--------------------------------------------------------------------------------------------------------------------------+

 


Note: Similarly, you can use all the client-side events of the Jquery accordion in Essential Tools for MVC accordion control. For more details, refer to the following link.


[[http://docs.jquery.com/UI/Accordion#events]{.UGHyperlink}](http://docs.jquery.com/UI/Accordion#events)[]{.UGHyperlink}

 

[]{#related-topics}

