---
title: galleryview.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\galleryview.md
created_at: 2025-07-03
---








  









### Gallery View {#gallery-view style="tab-stops: 0pt"}

The Gallery View brings rich user interfaces to your web pages, so that they look like Office 2010. 

Features

[·      ]The number of gallery items to be displayed in the parent block can be customized using the ItemsToShow property.

[·      ]The height of the gallery is customizable.

[·      ]Two different types of display modes are supported: Gallery View and List View.

[·      ]Extra items are supported in the gallery view.

[·      ]Server-side click event can be handled for the items in the Gallery View.

 

Use-Case Scenarios

The large number of galleries can be viewed in a single gallery window, so you can easily add a number of items and commands in a single view.

 

Appearance and Structure of the control

 

{border="0"}

Figure 369: Gallery View Control

 

[·      ]The Gallery View contains Gallery Item and Gallery Extra Items

[·      ]The Gallery Window opens when you click on the Gallery drop down button

[·      ]The items in the Gallery Window can be moved down or up by clicking on the respective buttons

[·      ]The height of the gallery items area can be customized using the Height property**.**

 

Properties

 

+-----------------+----------------------------------------------------------------------------+-----------------+-----------------+
| Property        | Description                                                                | Type            | Data Type       |
+-----------------+----------------------------------------------------------------------------+-----------------+-----------------+
|  DisplayType    | Specifies the type of the control. Default value is GalleryView.           | Server-Side     | Enum            |
|                 |                                                                            |                 |                 |
|                 | The Options  included are                                                  |                 |                 |
|                 |                                                                            |                 |                 |
|                 | [·      ]GalleryView                          |                 |                 |
|                 |                                                                            |                 |                 |
|                 | [·      ]ListView                             |                 |                 |
+-----------------+----------------------------------------------------------------------------+-----------------+-----------------+
| Height          | Specifies the height of the Gallery Items Area                             | Server-Side     | Unit            |
+-----------------+----------------------------------------------------------------------------+-----------------+-----------------+
| Width           | Specifies the width of the Gallery View                                    | Server-Side     | Unit            |
+-----------------+----------------------------------------------------------------------------+-----------------+-----------------+
| ItemsToShow     | Specifies the number of items to be displayed in the GalleryView.          | Server-Side     | int             |
+-----------------+----------------------------------------------------------------------------+-----------------+-----------------+
| Text            | Specifies the text of the gallery items                                    | Server-Side     | String          |
+-----------------+----------------------------------------------------------------------------+-----------------+-----------------+
| ImageUrl        | Specifies the ImageUrl to be used for the items in the gallery             | Server-Side     | String          |
+-----------------+----------------------------------------------------------------------------+-----------------+-----------------+
| ClassName       | Specifies the class for the image to be used items in the gallery          | Server-Side     | String          |
+-----------------+----------------------------------------------------------------------------+-----------------+-----------------+
| Name            | Specifies the unique name for the button which may be used to identify it. | Server-Side     | String          |
+-----------------+----------------------------------------------------------------------------+-----------------+-----------------+

 

 

 

Events

 

  Event     Description                                                                               Arguments                                         Type
  --------- ----------------------------------------------------------------------------------------- ------------------------------------------------- -------------
  OnClick   The Event will be triggered when you click on the gallery items or gallery Extra items.   The selected items will be passed as arguments.   Server-Side

 

More:









