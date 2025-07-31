---
title: clientsideevents43.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents43.md
created_at: 2025-07-03
---






#### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

The Toggle-Button supports the Client-Side event handling.

[] 

Use Case Scenarios

[It allows for easy customization of the events to be handled on the Toggle-Button.  ]

[] 

Adding Client-Side Events to an Application

The Client-Side events can be customized by two ways in Toggle-Button.

[·      ]Using Builder

[·      ]Using Properties Model

[] 

**[Using Builder]**

[] 

The following steps guides in handling the Client-Side events through Builder.

[] 

1.   In View, invoke the normal ToggleButton helper with the button id as the first argument followed by the **ClientSideOnChecked, ClientSideOnUnChecked, ClientSideOnClick** and **ClientSideOnLoad** methods.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                              |
|                                                                                                                                                                                     |
| [        [\<%][=]Html.Syncfusion().ToggleButton([\"myToggleButton\"])] |
|                                                                                                                                                                                     |
| [        .Text([\"Save\"])]                                                                                             |
|                                                                                                                                                                                     |
| [        .IsChecked = [true],]                                                                                             |
|                                                                                                                                                                                     |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                        |
|                                                                                                                                                                                     |
| [        .ContentType([ContentTypes].TextAndImage)]                                                                     |
|                                                                                                                                                                                     |
| **[        .ClientSideOnClick([\"OnClick\"])]**                                                                         |
|                                                                                                                                                                                     |
| **[        .ClientSideOnLoad([\"OnLoaded\"])]**                                                                         |
|                                                                                                                                                                                     |
| **[        .ClientSideOnChecked([\"OnCheck\"])]**                                                                       |
|                                                                                                                                                                                     |
| **[        .ClientSideOnUnChecked([\"OnUnCheck\"])]**                                                                   |
|                                                                                                                                                                                     |
| [        [%\>]]                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                            |
|                                                                                                                                                                                     |
| [        [\@{][ ]Html.Syncfusion().ToggleButton([\"myToggleButton\"])] |
|                                                                                                                                                                                     |
| [        .Text([\"Save\"])]                                                                                             |
|                                                                                                                                                                                     |
| [        .IsChecked = [true],]                                                                                             |
|                                                                                                                                                                                     |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                        |
|                                                                                                                                                                                     |
| [        .ContentType([ContentTypes].TextAndImage)]                                                                     |
|                                                                                                                                                                                     |
| **[        .ClientSideOnClick([\"OnClick\"])]**                                                                         |
|                                                                                                                                                                                     |
| **[        .ClientSideOnLoad([\"OnLoaded\"])]**                                                                         |
|                                                                                                                                                                                     |
| **[        .ClientSideOnChecked([\"OnCheck\"])]**                                                                       |
|                                                                                                                                                                                     |
| **[        .ClientSideOnUnChecked([\"OnUnCheck\"])]**                                                                   |
|                                                                                                                                                                                     |
| **[        .]**[Render();]                                                                                  |
|                                                                                                                                                                                     |
| [        [}]]                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In Javascript, use the methods to enable and disable an item as follow[s.]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**[]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                 |
| [        [function] OnLoaded(inst, args) {]                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [            [// inst - instance of button object.]]                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args :    args.\_currentItem   - clickeded button ]]                                                                                                 |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - button id]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnClick(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [            [// inst - instance of button object.]]                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args :    args.\_currentItem   - loaded button ]]                                                                                                    |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - button id]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnCheck(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [            [// inst - instance of button object.]]                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args :    args.\_currentItem   - clickeded button ]]                                                                                                 |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - button id]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnUnCheck(inst, args) {]                                                                                                                           |
|                                                                                                                                                                                                                                 |
| [            [// inst - instance of button object.]]                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args :    args.\_currentItem   - loaded button ]]                                                                                                    |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - button id]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [\</][script][\>][]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Using Properties Model

The following steps guides in handling the Client-Side events through the Properties model.

 

1.   In Controller, create an object for the ToggleButtonModel class and set the **ClientSideOnChecked, ClientSideOnUnChecked, ClientSideOnLoad**, and **ClientSideOnClick** properties. Assign this model class to view data.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                   |
|                                                                                                                                                                                            |
| [        [public] [ActionResult] Index()]                                                                 |
|                                                                                                                                                                                            |
| [        {]                                                                                                                                            |
|                                                                                                                                                                                            |
| [            [ToggleButtonModel] toggleButtonModel = [new] [ToggleButtonModel]()] |
|                                                                                                                                                                                            |
| [            {]                                                                                                                                        |
|                                                                                                                                                                                            |
| [                Text = [\"Save\"],]                                                                                           |
|                                                                                                                                                                                            |
| [                ImageUrl = [\"Content/icon_save.png\"],]                                                                      |
|                                                                                                                                                                                            |
| [                ContentType = [ContentTypes].TextAndImage,]                                                                   |
|                                                                                                                                                                                            |
| [                ImagePosition = [ImagePositions].Right,]                                                                      |
|                                                                                                                                                                                            |
| **[                ClientSideOnClick = [\"OnClick\"],]**                                                                       |
|                                                                                                                                                                                            |
| **[                ClientSideOnLoad = [\"OnLoaded\"]]**                                                                        |
|                                                                                                                                                                                            |
| **[                ClientSideOnChecked = [\"OnCheck\"],]**                                                                     |
|                                                                                                                                                                                            |
| **[                ClientSideOnUnChecked = [\"OnUnCheck\"]]**                                                                  |
|                                                                                                                                                                                            |
| [            };]                                                                                                                                       |
|                                                                                                                                                                                            |
| [            ViewData\[[\"ToggleButtonModel\"]\] = toggleButtonModel;]                                                         |
|                                                                                                                                                                                            |
| [            [return] View();]                                                                                                    |
|                                                                                                                                                                                            |
| [        }]                                                                                                                                            |
|                                                                                                                                                                                            |
| []                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In View, invoke the ToggleButton helper with the button id as the first argument followed by the view data of the **ToggleButtonModel** class.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().ToggleButton([\"btnToggle\"],([ToggleButtonModel])ViewData\[[\"ToggleButtonModel\"]\]) [%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [\@{][ ][Html.Syncfusion().ToggleButton([\"btnToggle\"],([ToggleButtonModel])ViewData\[[\"ToggleButtonModel\"]\]).Render(); [}]] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   In Javascript, define the function to handle the specified events.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**[]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                 |
| [        [function] OnLoaded(inst, args) {]                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [            [// inst - instance of button object.]]                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args :    args.\_currentItem   - clickeded button ]]                                                                                                 |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - button id]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnClick(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [            [// inst - instance of button object.]]                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args :    args.\_currentItem   - loaded button ]]                                                                                                    |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - button id]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnCheck(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [            [// inst - instance of button object.]]                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args :    args.\_currentItem   - clickeded button ]]                                                                                                 |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - button id]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnUnCheck(inst, args) {]                                                                                                                           |
|                                                                                                                                                                                                                                 |
| [            [// inst - instance of button object.]]                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args :    args.\_currentItem   - loaded button ]]                                                                                                    |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - button id]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [\</][script][\>][]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Events

The following table illustrates the events which describes the events of the Toggle-Button.

 

  Event                                           Description                                                                                       Arguments                             Type                                Reference links
  ----------------------------------------------- ------------------------------------------------------------------------------------------------- ------------------------------------- ----------------------------------- -----------------------------
  ClientSideOnLoded[]     This event is raised immediately when the Toggle-Button gets loaded.[]    inst,args[]   [Client ]   [-]
  ClientSideOnClick                               This event is raised when the Toggle-Button is clicked.                                           inst,args                             [Client]    [-]
  ClientSideOnChecked[]   This event is raised immediately when the Toggle-Button gets checked.[]   inst,args[]   [Client ]   [-]
  ClientSideOnUnChecked                           This event is raised immediately when the Toggle-Button gets unchecked.                           inst,args                             [Client]    [-]

[] 

Sample Link

To view the samples, follow the steps below.

1.   Open the Tools sample browser from the dashboard. (Refer to the Samples and Location chapter)

2.   Navigate to **Tools.Mvc -\> Button -\> Client-Side API.**

 

[]{#related-topics}

