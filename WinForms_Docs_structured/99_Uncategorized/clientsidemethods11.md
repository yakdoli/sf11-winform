---
title: clientsidemethods11.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsidemethods11.md
created_at: 2025-07-03
---






#### Client-Side Methods {#client-side-methods style="tab-stops: 0pt"}

The Split-Button supports a set of Client-Side methods to control its behavior.

 

Use Case Scenarios

It allows for easy customization of the behavior of the Split-Button.

 

Adding Client-Side Methods[ ]to an Application

The following steps guides you in using the Client-Side methods.

1.   In **View**, invoke the **SplitButton** helper with the button id as the first argument followed by their methods.

[] 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                             |
|                                                                                                                                                                                    |
| [        [\<%][=]Html.Syncfusion().SplitButton([\"mySplitButton \"])] |
|                                                                                                                                                                                    |
| [        .Text([\"Save\"])]                                                                                            |
|                                                                                                                                                                                    |
| [        .Skin([Skins].Almond)]                                                                                        |
|                                                                                                                                                                                    |
| [        .IsChecked = [true],]                                                                                            |
|                                                                                                                                                                                    |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                       |
|                                                                                                                                                                                    |
| [        .ContentType([ContentTypes].TextAndImage)]                                                                    |
|                                                                                                                                                                                    |
| [        [%\>]]                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                           |
|                                                                                                                                                                                    |
| [        [\@{][ ]Html.Syncfusion().SplitButton([\"mySplitButton \"])] |
|                                                                                                                                                                                    |
| [        .Text([\"Save\"])]                                                                                            |
|                                                                                                                                                                                    |
| [        .Skin([Skins].Almond)]                                                                                        |
|                                                                                                                                                                                    |
| [        .IsChecked = [true],]                                                                                            |
|                                                                                                                                                                                    |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                       |
|                                                                                                                                                                                    |
| [        .ContentType([ContentTypes].TextAndImage)]                                                                    |
|                                                                                                                                                                                    |
| [        .Render();]                                                                                                                           |
|                                                                                                                                                                                    |
| [        [}]]                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   In Javascript, use the methods to enable and disable an item as follows.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**[]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][script][ [type][=\"text/javascript\"\>]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [function] DisableButton() {]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            [// Code to disable the Button.]]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            \$find([\"]][mySplitButton][\"][).Disable();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [function] EnableButton() {]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            [// Code to enable the Button.]]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            \$find([\"]][mySplitButton][\"][).Enable();]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [function] DisableItem() {]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            [// Code to disable an item passing the ID as a parameter.]]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            \$find([\"]][mySplitButton][\"][).][ DisableItembyID][([\"Products\"]);][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [function] EnableItem() {]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            [// Code to enable an item passing the ID as a parameter.]]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            \$find([\"myMenu\"]).][ EnableItembyID][([\"Products\"]);][]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [ [\</][script][\>]]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Run the application.

 

The output is shown in the following screenshot.

 

{border="0"}

Figure 251: Split-Button in a disabled state

{border="0"}

Figure 252: Split-Button in an enabled state

**Methods**

 

The following table illustrates the methods which describes the Client-Side methods of the Split-Button.

 

+-----------------+------------------------------------------------------------+---------------------------------------------+-----------+-------------+-----------------+
| Method          | Description                                                | Parameters                                  | Type      | Return Type | Reference links |
+-----------------+------------------------------------------------------------+---------------------------------------------+-----------+-------------+-----------------+
| DisableItembyID | Disables the specified drop-down item in the Split-Button. | itemToDisable -- DOM element to be disabled | Client    | \-          | \-              |
|                 |                                                            |                                             |           |             |                 |
|                 |                                                            |                                             |           |             |                 |
+-----------------+------------------------------------------------------------+---------------------------------------------+-----------+-------------+-----------------+
| EnableItembyID  | Enables the disabled item.                                 | itemToEnable -- DOM element to be enabled   | Client    | \-          | \-              |
|                 |                                                            |                                             |           |             |                 |
|                 |                                                            |                                             |           |             |                 |
+-----------------+------------------------------------------------------------+---------------------------------------------+-----------+-------------+-----------------+
| Disable         | Disables the button.                                       | \-                                          | Client    | \-          | \-              |
+-----------------+------------------------------------------------------------+---------------------------------------------+-----------+-------------+-----------------+
| Enable          | Enables the disabled button.                               | \-                                          | Client    | \-          | \-              |
+=================+============================================================+=============================================+===========+=============+=================+

[] 

 

Sample Link

 

To view the samples, follow the steps below.

1.   Open the Tools sample browser from the dashboard. (Refer to the [Samples and Location]{.UGHyperlink} chapter)

2.   Navigate to **Tools.Mvc -\> Button -\> Client-Side API**.

 

[]{#related-topics}

