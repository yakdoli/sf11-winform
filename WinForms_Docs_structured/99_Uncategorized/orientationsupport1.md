---
title: orientationsupport1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\orientationsupport1.md
created_at: 2025-07-03
---






#### Orientation Support {#orientation-support style="tab-stops: 0pt"}

The MenuAdv control can align its content vertically and horizontally by using the Orientation property of the MenuAdv class.

When the value of the Orientation property is set to Horizontal, the Items of MenuAdv will be arranged horizontally.

**[]** 

{border="0"}

Figure 722: Orientation - Horizontal

 

Similarly, when the value of the Orientation property is set to Vertical, the Items of MenuAdv will be arranged vertically.

{border="0"}

Figure 723: Orientation -- Vertical

 

Use Case Scenarios

MenuAdv helps users to set the Menu items in Horizontal or Vertical orientations.

Adding the Orientation Support to an Application

Users can add the Orientation support to MenuAdv used in the application as mentioned in the code snippet below.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][shared][:][MenuAdv][ x][:][Name][=\"Menu\" ][ Orientation][=\"Horizontal"/\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\<][shared][:][MenuItemAdv][ Header][=\"File\"\>][]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                    ][\<][shared][:][MenuItemAdv][ Header][=\"New\"\>][]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                        ][\<][shared][:][MenuItemAdv.Icon][\>][]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                            ][\<][Image][ Source][=\"/MenuControlDemo;component/Images/NewIcon.jpg\"/\>][]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                        ][\</][shared][:][MenuItemAdv.Icon][\>][]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                    ][\</][shared][:][MenuItemAdv][\>][]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                    ][\<][shared][:][MenuItemAdv][ Header][=\"Copy\"\>][]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                        ][\<][shared][:][MenuItemAdv.Icon][\>][]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                            ][\<][Image][ Source][=\"/MenuControlDemo;component/Images/CopyIcon.jpg\"/\>][]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                        ][\</][shared][:][MenuItemAdv.Icon][\>][]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                    ][\</][shared][:][MenuItemAdv][\>][]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                    ][\<][shared][:][MenuItemAdv][ Header][=\"Cut\"\>][]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                        ][\<][shared][:][MenuItemAdv.Icon][\>][]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                            ][\<][Image][ Source][=\"/MenuControlDemo;component/Images/CutIcon.jpg\"/\>][]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                        ][\</][shared][:][MenuItemAdv.Icon][\>][]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                    ][\</][shared][:][MenuItemAdv][\>][]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\</][shared][:][MenuItemAdv][\>][]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\<][shared][:][MenuItemAdv][ Header][=\"Edit\"/\>][]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][shared][:][MenuAdv][\>][]                                                                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Properties

The property for the Orientation support is described in the following tabulation:

Table 64: Property Table

  ------------- ------------------------------------------ -------------------- ------------------------- -----------------
  Property      Description                                Type                 Data Type                 Reference links
  Orientation   Gets or sets the Orientation of MenuAdv.   DependencyProperty   Orientation(Horizontal)   
  ------------- ------------------------------------------ -------------------- ------------------------- -----------------

 

Sample Link

WPF Sample Browser-\> Tools -\> MenuAdv -\> MenuAdv Demo

[]{#related-topics}

