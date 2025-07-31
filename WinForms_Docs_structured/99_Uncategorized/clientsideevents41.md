---
title: clientsideevents41.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents41.md
created_at: 2025-07-03
---






#### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

The Split-Button supports Client-Side event handling.

 

Use Case Scenarios

It allows for easy customization of the events to be handled on the split-button.

 

Adding Client-Side Events[ ]to an Application

The Client-Side events can be customized by two ways in the Split-Button.

[·      ]Using Builder

[·      ]Using Properties Model

 

Using Builder

The following steps guides you in handling the Client-Side events through the Builder.

1.   In **View**, invoke the normal **SplitButton** helper with the button id as the first argument followed by the **ClientSideOnChecked, ClientSideOnUnChecked, ClientSideOnClick** and **ClientSideOnLoad** methods.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                            |
|                                                                                                                                                                                   |
| [        [\<%][=]Html.Syncfusion().SplitButton([\"mySplitButton\"])] |
|                                                                                                                                                                                   |
| [        .Text([\"Save\"])]                                                                                           |
|                                                                                                                                                                                   |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                      |
|                                                                                                                                                                                   |
| [        .ContentType([ContentTypes].TextAndImage)]                                                                   |
|                                                                                                                                                                                   |
| **[        .ClientSideOnClick([\"OnClick\"])]**                                                                       |
|                                                                                                                                                                                   |
| **[        .ClientSideOnLoad([\"OnLoaded\"])]**                                                                       |
|                                                                                                                                                                                   |
| **[        .ClientSideOnMenuItemClick([\"OnItemClick\"])]**                                                           |
|                                                                                                                                                                                   |
| **[        .ClientSideOnMouseOut([\"OnMouseOut\"])]**                                                                 |
|                                                                                                                                                                                   |
| **[        .ClientSideOnMouseOver([\"OnMouseOver\"])]**                                                               |
|                                                                                                                                                                                   |
| [        [%\>]]                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                          |
|                                                                                                                                                                                   |
| [        [\@{][ ]Html.Syncfusion().SplitButton([\"mySplitButton\"])] |
|                                                                                                                                                                                   |
| [        .Text([\"Save\"])]                                                                                           |
|                                                                                                                                                                                   |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                      |
|                                                                                                                                                                                   |
| [        .ContentType([ContentTypes].TextAndImage)]                                                                   |
|                                                                                                                                                                                   |
| **[        .ClientSideOnClick([\"OnClick\"])]**                                                                       |
|                                                                                                                                                                                   |
| **[        .ClientSideOnLoad([\"OnLoaded\"])]**                                                                       |
|                                                                                                                                                                                   |
| **[        .ClientSideOnMenuItemClick([\"OnItemClick\"])]**                                                           |
|                                                                                                                                                                                   |
| **[        .ClientSideOnMouseOut([\"OnMouseOut\"])]**                                                                 |
|                                                                                                                                                                                   |
| **[        .ClientSideOnMouseOver([\"OnMouseOver\"])]**                                                               |
|                                                                                                                                                                                   |
| [        .Render();]                                                                                                                          |
|                                                                                                                                                                                   |
| [        [}]]                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In Javascript, use the methods to enable and disable an item as follows.

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
| [            [//args :    args.\_currentItem   - clickeded button ]]                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - button id]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnClick(inst, args) {]                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [            [// inst - instance of button object.]]                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentItem   - loaded button ]]                                                                                                     |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - button id]]                                                                                                          |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnMouseOver(inst, args) {][]                                                                       |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of menu object.]][]                                                                   |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentItem   - current drop-down item]][]                                           |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - drop-down item id]][]                                                |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_text          - text of the current drop-down item                  ]][]             |
|                                                                                                                                                                                                                                 |
| [        }][]                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [        [function] OnMouseOut(inst, args) {][]                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of menu object.]][]                                                                   |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentItem   - current drop-down item ]][]                                          |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - drop-down id]][]                                                     |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_text          - text of the current drop-down item ]][]                              |
|                                                                                                                                                                                                                                 |
| [        }][]                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [        [function] OnItemClick(inst, args) {][]                                                                       |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of drop-down item object.]][]                                                         |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentItem   - current drop-down item ]][]                                          |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - drop-down id]][]                                                     |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_text          - text of the current drop-down item ]][]                              |
|                                                                                                                                                                                                                                 |
| [        }][]                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [\</][script][\>][]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Using Builder

The following steps guide in handling client side events through builder.

 

1.   In **Controller**, create an object for the **SplitButtonModel** class and set **ClientSideOnChecked, ClientSideOnUnChecked, ClientSideOnLoad**, and **ClientSideOnClick** properties. Assign this model class to view data.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                |
|                                                                                                                                                                                         |
| [        [public] [ActionResult] Index()]                                                              |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            [SplitButtonModel] splitButtonModel = [new] [SplitButtonModel]()] |
|                                                                                                                                                                                         |
| [            {]                                                                                                                                     |
|                                                                                                                                                                                         |
| [                Text = [\"Save\"],]                                                                                        |
|                                                                                                                                                                                         |
| [                ImageUrl = [\"Content/icon_save.png\"],]                                                                   |
|                                                                                                                                                                                         |
| [                ContentType = [ContentTypes].TextAndImage,]                                                                |
|                                                                                                                                                                                         |
| [                ImagePosition = [ImagePositions].Right,]                                                                   |
|                                                                                                                                                                                         |
| **[                ClientSideOnClick = [\"OnClick\"],]**                                                                    |
|                                                                                                                                                                                         |
| **[                ClientSideOnLoad = [\"OnLoaded\"]]**                                                                     |
|                                                                                                                                                                                         |
| **[                ClientSideOnMenuItemClick = [\"OnItemClick\"],]**                                                        |
|                                                                                                                                                                                         |
| **[                ClientSideOnMouseOut = [\"OnMouseOut\",]]**                                                              |
|                                                                                                                                                                                         |
| **[                ClientSideOnMouseOver = [\"OnMouseOver\"]]**                                                             |
|                                                                                                                                                                                         |
| [            };]                                                                                                                                    |
|                                                                                                                                                                                         |
| [            ViewData\[[\"SplitButtonModel\"]\] = splitButtonModel;]                                                        |
|                                                                                                                                                                                         |
| [            [return] View();]                                                                                                 |
|                                                                                                                                                                                         |
| [        }]                                                                                                                                         |
|                                                                                                                                                                                         |
| []                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, invoke the normal **SplitButton** helper with the button id as the first argument followed by the view data of the **SplitButtonModel** class.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().SplitButton([\"btnSplit\"],([SplitButtonModel])ViewData\[[\"SplitButtonModel\"]\]) [%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [\@{][ ][Html.Syncfusion().SplitButton([\"btnSplit\"],([SplitButtonModel])ViewData\[[\"SplitButtonModel\"]\]).Render(); [}]] |
|                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   In **Javascript**, define the function to handle specified events.

 

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
| [        [function] OnMouseOver(inst, args) {][]                                                                       |
|                                                                                                                                                                                                                                 |
| [            [// inst - instance of menu object.]][]                                                                  |
|                                                                                                                                                                                                                                 |
| [            [// args :    args.\_currentItem   - current drop-down item.]][]                                         |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - drop-down item id]][]                                                |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_text          - text of the current drop-down item                  ]][]             |
|                                                                                                                                                                                                                                 |
| [        }][]                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [        [function] OnMouseOut(inst, args) {][]                                                                        |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of menu object.]][]                                                                   |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentItem   - current drop-down item ]][]                                          |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - drop-down id]][]                                                     |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_text          - text of the current drop-down item ]][]                              |
|                                                                                                                                                                                                                                 |
| [        }][]                                                                                                                               |
|                                                                                                                                                                                                                                 |
| [        [function] OnItemClick(inst, args) {][]                                                                       |
|                                                                                                                                                                                                                                 |
| [            [// inst - instance of drop-down item object.]][]                                                        |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.\_currentItem   - current drop-down item ]][]                                          |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_id            - drop-down id]][]                                                     |
|                                                                                                                                                                                                                                 |
| [            [//          args.\_text          - text of the current drop-down item ]][]                              |
|                                                                                                                                                                                                                                 |
| [        }][]                                                                                                                               |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [\</][script][\>][]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Events

The following table illustrates events of the Split-Button.

 

 

 

  Event                       Description                                                           Arguments   Type     Reference links
  --------------------------- --------------------------------------------------------------------- ----------- -------- -----------------
  ClientSideOnLoded           This event is raised immediately when the Split-Button gets loaded.   inst,args   Client   \-
  ClientSideOnClick           This event is raised when the Split-Button is clicked.                inst,args   Client   \-
  ClientSideOnMenuItemClick   This event is raised when the menu item is clicked.                   inst,args   Client   \-
  ClientSideOnMouseOver       This event is raised on mouse over a menu item.                       inst,args   Client   \-
  ClientSideOnMouseOut        This event is raised on mouse over a menu item.                       inst,args   Client   \-

[] 

Sample Link

To view the samples, follow the steps below.

1.   Open the Tools sample browser from the dashboard. (Refer to the Samples and Location chapter)

2.   Navigate to **Tools.Mvc -\> Button -\> Client-Side API**.

[] 

[]{#related-topics}

