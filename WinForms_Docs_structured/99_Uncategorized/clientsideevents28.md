---
title: clientsideevents28.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents28.md
created_at: 2025-08-05
---






#### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

The Button control supports the Client-Side event handling.

[] 

Use Case Scenarios

The Button control allows for easy customization of the events to be handled on the button.

[] 

Adding Client-Side Events to an Application

The Client-Side events can be customized by two ways in button.

[·      ]Using Builder

[·      ]Using Properties Model

 

Using Builder

The following steps guide in handling client side events through builder.

1.   In View, invoke the normal Button helper with the button id as the first argument followed by the **ClientSideOnClick** and **ClientSideOnLoad** methods.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                  |
|                                                                                                                                                                         |
| [        [\<%][=]Html.Syncfusion().Button([\"myButton\"])] |
|                                                                                                                                                                         |
| [        .Text([\"Save\"])]                                                                                 |
|                                                                                                                                                                         |
| [        .Skin([Skins].Almond)]                                                                             |
|                                                                                                                                                                         |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                            |
|                                                                                                                                                                         |
| [        .ContentType([ContentTypes].TextAndImage)]                                                         |
|                                                                                                                                                                         |
| **[        .ClientSideOnClick([\"OnClick\"])]**                                                             |
|                                                                                                                                                                         |
| **[        .ClientSideOnLoad([\"OnLoaded\"])]**                                                             |
|                                                                                                                                                                         |
| [        [%\>]]                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                |
|                                                                                                                                                                         |
| [        [\@{][ ]Html.Syncfusion().Button([\"myButton\"])] |
|                                                                                                                                                                         |
| [        .Text([\"Save\"])]                                                                                 |
|                                                                                                                                                                         |
| [        .Skin([Skins].Almond)]                                                                             |
|                                                                                                                                                                         |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                            |
|                                                                                                                                                                         |
| [        .ContentType([ContentTypes].TextAndImage)]                                                         |
|                                                                                                                                                                         |
| **[        .ClientSideOnClick([\"OnClick\"])]**                                                             |
|                                                                                                                                                                         |
| **[        .ClientSideOnLoad([\"OnLoaded\"])]**                                                             |
|                                                                                                                                                                         |
| **[        ]**[.Render();]                                                                      |
|                                                                                                                                                                         |
| [        [}]]                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In Javascript, use the methods to enable and disable an item as follows.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**[]                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| [\<][script][ [type][=\"text/javascript\"\>]]   |
|                                                                                                                                                                                                                                   |
| [        [function] OnLoaded(inst, args) {]                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [            [// inst - Instance of the button object.]]                                                                                                                |
|                                                                                                                                                                                                                                   |
| [            [// args :    args.\_currentItem   - clickeded button ]]                                                                                                   |
|                                                                                                                                                                                                                                   |
| [            [//          args.\_id            - button id]]                                                                                                            |
|                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| [        [function] OnClick(inst, args) {]                                                                                                                               |
|                                                                                                                                                                                                                                   |
| [            [// inst - instance of the button object.]]                                                                                                                |
|                                                                                                                                                                                                                                   |
| [            [//args :    args.\_currentItem   - loaded button ]]                                                                                                       |
|                                                                                                                                                                                                                                   |
| [            [//          args.\_id            - button id]]                                                                                                            |
|                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| [\</][script][\>][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

Using Builder

[] 

The following steps guide you in handling the Client-Side events through the Builder.

1.   In Controller, create an object for the **ButtonModel** class and set the **ClientSideOnLoad**, and **ClientSideOnClick** properties. Assign this model class to view data.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                 |
|                                                                                                                                                                          |
| **[]**                                                                                                                               |
|                                                                                                                                                                          |
| [        [public] [ActionResult] Index()]                                               |
|                                                                                                                                                                          |
| [        {]                                                                                                                          |
|                                                                                                                                                                          |
| [            [ButtonModel] buttonModel = [new] [ButtonModel]()] |
|                                                                                                                                                                          |
| [            {]                                                                                                                      |
|                                                                                                                                                                          |
| [                Text = [\"Save\"],]                                                                         |
|                                                                                                                                                                          |
| [                ImageUrl = [\"Content/icon_save.png\"],]                                                    |
|                                                                                                                                                                          |
| [                Skin = [Skins].Almond,]                                                                     |
|                                                                                                                                                                          |
| [                ContentType = [ContentTypes].TextAndImage,]                                                 |
|                                                                                                                                                                          |
| [                ImagePosition = [ImagePositions].Right,]                                                    |
|                                                                                                                                                                          |
| **[                ClientSideOnClick = [\"OnClick\"],]**                                                     |
|                                                                                                                                                                          |
| **[                ClientSideOnLoad = [\"OnLoaded\"]]**                                                      |
|                                                                                                                                                                          |
| [            };]                                                                                                                     |
|                                                                                                                                                                          |
| [            ViewData\[[\"ButtonModel\"]\] = buttonModel;]                                                   |
|                                                                                                                                                                          |
| [            [return] View();]                                                                                  |
|                                                                                                                                                                          |
| [        }]                                                                                                                          |
|                                                                                                                                                                          |
| []                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

 

2.   In **View**, invoke the normal **Button** helper with the button id as the first argument followed by the view data of the **ButtonModel** class.

 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().Button([\"btnNormal\"],([ButtonModel])ViewData\[[\"ButtonModel\"]\]) [%\>]] |
|                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                |
| [\@{][ ][Html.Syncfusion().Button([\"btnNormal\"],([ButtonModel])ViewData\[[\"ButtonModel\"]\]).Render();[}]] |
|                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

3.   In **Javascript**, define the function to handle the specified events.

 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**[]                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| [\<][script][ [type][=\"text/javascript\"\>]]   |
|                                                                                                                                                                                                                                   |
| [        [function] OnLoaded(inst, args) {]                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [            [// inst - Instance of the button object.]]                                                                                                                |
|                                                                                                                                                                                                                                   |
| [            [// args :    args.\_currentItem   - clickeded button ]]                                                                                                   |
|                                                                                                                                                                                                                                   |
| [            [//          args.\_id            - button id]]                                                                                                            |
|                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| [        [function] OnClick(inst, args) {]                                                                                                                               |
|                                                                                                                                                                                                                                   |
| [            [// inst - Instance of the button object]]                                                                                                                 |
|                                                                                                                                                                                                                                   |
| [            [// args :    args.\_currentItem   - loaded button ]]                                                                                                      |
|                                                                                                                                                                                                                                   |
| [            [//          args.\_id            - button id]]                                                                                                            |
|                                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                   |
| [\</][script][\>][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Events

The following table illustrates the events of button control.

[] 


  Event               Description                                                     Arguments   Type     Reference links
  ------------------- --------------------------------------------------------------- ----------- -------- -----------------
  ClientSideOnLoded   This event is raised immediately when the button gets loaded.   inst,args   Client   \-
  ClientSideOnClick   This event is raised when a button is clicked.                  inst,args   Client   \-


[] 

Sample Link

To view the samples, follow the steps below:

1.   Open the Tools sample browser from the dashboard. (Refer to the [Samples and Location]{.UGHyperlink}[ ]{.UGHyperlink}chapter)

2.   Navigate to **Tools.Mvc -\> Button -\> Client-Side API**.

 

[]{#related-topics}

