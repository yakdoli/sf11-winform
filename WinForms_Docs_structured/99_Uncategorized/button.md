---
title: button.md
original_path: WinForms_Docs/99_Uncategorized/button.md
created_at: 2025-08-05
---






#### Button {#button style="tab-stops: 0pt"}

The Button Advanced control is fully customizable and gives your pages a sleek look.

**Features**

[·      ]Custom Styles:   The  look and feel of the button control can be customized and enhanced using .CSS styles

[·      ]Supports both server-side, and client-side events.

[·      ]You have four different types of buttons to perfect the customization.

[·      ]Menu Items: rendering with sub-menus is supported.

Use Case Scenarios

The Button Advanced control can be easily styled by using the CustomStyle property, to enhance the way the control appears.

Appearance and Structure of the control

This is how the Button Advanced control looks:

{border="0"}

Figure 152: Button

 

The Button Advanced Control follows one of the two structures-

[·      ]Image or Text, or

[·      ]Image and Text

The four different types of button advanced control spawned from the two structures are -

1.  Image Before Text

2.  Image Only

3.  Text Only

4.  Image Above Text

The Types can be chosen form the DisplayType property. These buttons can also be used as sub-menu buttons.

 

Properties

 


+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Property        | Description                                                                                                                                         | Type            | Data Type       |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+
|  DisplayType    | Specifies the type of the button control used. Default value is **ImageBeforeText**.                                                                | Server-Side     | Enum            |
|                 |                                                                                                                                                     |                 |                 |
|                 | The Options included are                                                                                                                            |                 |                 |
|                 |                                                                                                                                                     |                 |                 |
|                 | [·      ]ImageBeforeText                                                                                               |                 |                 |
|                 |                                                                                                                                                     |                 |                 |
|                 | [·      ]ImageAboveText                                                                                                |                 |                 |
|                 |                                                                                                                                                     |                 |                 |
|                 | [·      ]ImageOnly                                                                                                     |                 |                 |
|                 |                                                                                                                                                     |                 |                 |
|                 | [·      ]TextOnly                                                                                                      |                 |                 |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Text            | Shows the text of the button                                                                                                                        | Server-Side     | String          |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| ImageUrl        | Specifies the ImageUrl for the image used in the button                                                                                             | Server-Side     | String          |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| ClassName       | Specifies the .css class name for the image used in the button                                                                                      | Server-Side     | String          |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| CustomClass     | Specifies the class for the background of the button which can be used to set the style and background color of the button.                         | Server-Side     | String          |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Enabled         | Gets and sets the Boolean value, to allow the button to be enabled or disabled. Default Value is **True,** (thus allowing the button to be enabled) | Server-Side     | Boolean         |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| ExtraText       | Shows the extra text in the button                                                                                                                  | Server-Side     | String          |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+
| Name            | Specifies the unique name for the button which can be used as to identify it from the others.                                                       | Server-Side     | String          |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-----------------+


 

Events

 


  Event           Description                                                 Arguments                                                                                                                            Type
  --------------- ----------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------ -------------
  OnClientClick   The Event will be triggered when you click on the button    The text or name of the button will be passed as an argument.                                                                        Client-Side
  OnClick         The Event will be triggered when you click on the button    The text or name of the button will be passed as an argument. For buttons with submenus, the selected submenu item will be passed.   Server-Side


[]{#related-topics}

