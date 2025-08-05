---
title: ribbonmodaltabs1.md
original_path: WinForms_Docs/04_Controls/Ribbon/ribbonmodaltabs1.md
created_at: 2025-08-05
---






#### Ribbon Modal Tabs {#ribbon-modal-tabs style="tab-stops: 0pt"}

[] 

Modal Tab in Ribbon Control displays a collection of commands that will be used only in a temporary mode. At this point, the core tabs will be disabled.

**[]** 

Use Case Scenarios

[    ]

Print Preview is a Modal Tab which displays Print Preview related commands until you close the Modal Tab.

 

{border="0"}

 

Figure 875: Ribbon with Core Tabs

 

 

{border="0"}

 

Figure 876: Ribbon with Modal Tab

 

Adding Modal Tabs to an Application

You can add the Modal Tab in an application by adding Ribbon Tabs in ModalTabCollection property in Ribbon. You can also add all Ribbon Tabs that you want to use as Modal Tab into ModalTabCollection property.

This is illustrated in the code given below.

**** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            ][\<][syncfusion][:][Ribbon.ModalTabCollection][ \>][]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                ][\<][syncfusion][:][ModalTabCollection][ \>][]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                    ][\<][syncfusion][:][RibbonTab][ Caption][=\"Print Preview\"][ ]                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                                                 Name][=\"printpreviewtab\"\>][]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                        ][\<][syncfusion][:][RibbonBar][ Header][=\"Sample Bar\"\>][]                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                            ][\<][syncfusion][:][RibbonButton][ Label][=\"Close Tab\"][                                                  ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                                         Click][=\"CloseModalTab_Click\"/\>][]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                        ][\</][syncfusion][:][RibbonBar][\>][]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                    ][\</][syncfusion][:][RibbonTab][\>][]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                ][\</][syncfusion][:][ModalTabCollection][\>][]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [            ][\</][syncfusion][:][Ribbon.ModalTabCollection][\>]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

After adding this collection in Ribbon, you can then handle the Modal Tab visibility by using the following methods at any time.

[] 

[] 

Tables for properties, methods

 

Properties

**[]** 

Table 22: ModalTabCollection Table

**[]** 

  -------------------- ----------------------------------------------------------------------- ---------------------- --------------------- -----------------
  Property             Description                                                             Type                   Data Type             Default Value
  ModalTabCollection   Used to store the collection of Ribbon Tabs as Modal Tabs Collection.    Dependency Property   ModalTabsCollection   Null Collection
  -------------------- ----------------------------------------------------------------------- ---------------------- --------------------- -----------------

[] 

Methods

**[]** 

Table 23: ShowModalTab Table

**[]** 


+--------------+-------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| Method       | Description                                                                         | Parameters                                                                          | Return Type | Reference links                                                                                                                    |
+--------------+-------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-------------+------------------------------------------------------------------------------------------------------------------------------------+
| ShowModalTab | This method will show the specific Modal Tab in the Ribbon from ModalTabCollection. | (string arg1)                                                                       | bool        | [[How to Show a ModalTab?]](#HowtohandleModalTabsinRibbon) |
|              |                                                                                     |                                                                                     |             |                                                                                                                                    |
|              |                                                                                     |                                                                                     |             |                                                                                                                                    |
|              |                                                                                     |                                                                                     |             |                                                                                                                                    |
|              |                                                                                     |  arg1- Name of the Ribbon Tab to be displayed as Modal Tab from ModalTabCollection. |             |                                                                                                                                    |
+==============+=====================================================================================+=====================================================================================+=============+====================================================================================================================================+


[] 

Table 24: CloseModalTabs Table


  Method           Description                                                                 Parameters   Return Type   Reference links
  ---------------- --------------------------------------------------------------------------- ------------ ------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  CloseModalTabs   CloseModalTabs method will close the opened Modal Tabs in Ribbon control.    No Params   bool           [[[How to close ModalTabs?]]{.UGHyperlink}](#HowtohandleModalTabsinRibbon)[[]]{.UGHyperlink}


[]{#_How_to_handle} 

[How to handle Modal Tabs in Ribbon?]{#HowtohandleModalTabsinRibbon}

You can add Ribbon Tabs that you want to display as Modal Tabs to ModalTabCollection property in the Ribbon Control. The ShowModalTab and CloseModalTabs methods handle Modal Tabs in the Ribbon control. You can display any Modal Tab from the ModalTabCollection property whenever required.

 

You can call ShowModalTab method to show the specific Modal Tab in Ribbon. This can be done from any event of core Ribbon Tab element.

This is illustrated in the code given below.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [private][ [void] ShowModalTabBtn_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| [            [this].MyRibbon.ShowModalTab([\"printpreviewtab\"]);]                                                                                   |
|                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

CloseModalTabs method will close the currently opened Modal Tab in Ribbon control. This method should be called in any event of currently displaying Modal Tab element.

This is illustrated in the code given below.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                        |
| [private][ [void] CloseModalTabBtn_Click([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                                                                                        |
| [        {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
| [            [this].MyRibbon.CloseModalTabs();]                                                                                                                               |
|                                                                                                                                                                                                                                        |
| [        }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Sample Link

Tools [à] Ribbon  [à] Modal Tabs

 

[]{#related-topics}

