---
title: configuringchildcontrols1.md
original_path: WinForms_Docs/99_Uncategorized/configuringchildcontrols1.md
created_at: 2025-08-05
---






##### Configuring Child Controls {#configuring-child-controls style="tab-stops: 0pt"}

 

Deriving from the Layout Manager base, the CardLayout inherits all the functionality that the Layout Manager type exposes.

[] 

For example, when the CardLayout is added to a form, and a Panel control is added to it, then this Panel control acts as Card1, where the user can add the needed controls. Then another Panel control can be added which will act as Card2 and so on. During runtime, only one Card will be visible at a time. You can traverse through these cards by adding buttons and setting the appropriate code.

 

In the following screen shot, Panel control acts as the Container control and Label control acts as a card.

[] 

{border="0"}

[] 

Figure 662: Adding Labels as Cards

 

Image Settings

[] 

In the selected card, you can insert an image using the Child (Label) control property as shown below.

[] 


  ------------------------ --------------------------------------------------------------
  Child Control Property   Description
  Image                    Gets / sets the image that will be displayed on the control.
  ------------------------ --------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [this][.label1.Image = ((System.Drawing.[Bitmap])(resources.GetObject([\"label1.Image\"])));] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [Me][.label1.Image = [DirectCast]((resources.GetObject([\"label1.Image\"])), System.Drawing.Bitmap)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 663: Setting an Image for the Card

[] 

Size

[] 

The preferred size and minimum size of the Child controls can be set using the **PreferredSize** and **MinimumSize** extended properties of the Child controls that are added to the CardLayout. Refer Child Control Settings to know about this topic.

[\
]Layout Mode

[] 

The CardLayout provides two modes to layout the Child controls. The mode can be set using the property given below.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------+
| CardLayout Property               | Description                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------+
| LayoutMode                        | Specifies the layout mode for the Child controls. The default value is set to \'Default\'. |
|                                   |                                                                                            |
|                                   |                                                                                            |
|                                   |                                                                                            |
|                                   | The options included are as follows.                                                       |
|                                   |                                                                                            |
|                                   |                                                                                            |
|                                   |                                                                                            |
|                                   | Default and                                                                                |
|                                   |                                                                                            |
|                                   | Fill.                                                                                      |
+-----------------------------------+--------------------------------------------------------------------------------------------+


 

When the layout mode of CardLayout is set to \'Default\', the Child control is simply centered within the Container when the Container\'s size is bigger than the Child control\'s preferred size. However, if the Container\'s size is smaller than the Child controls\'s preferred size, the Child control\'s size will shrink down to its minimum size. When shrunk, you have an option to specify whether the preferred width / height aspect ratio should be maintained for that Child control, which is specified using the extended **MaintainAspectRatio** property of each Child.

 

When the layout mode is set to \'Fill\', it simply resizes the Child control to fill the entire Container client area.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [this][.cardLayout1.LayoutMode = Syncfusion.Windows.Forms.Tools.[CardLayoutMode].Fill;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [Me][.cardLayout1.LayoutMode = Syncfusion.Windows.Forms.Tools.CardLayoutMode.Fill] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 664: Layout Mode set to \"Fill\"

[] 

See Also

[] 

[Configuring CardLayout]{.UGHyperlink}[, ]{.UGHyperlink}[Child Control Settings]{.UGHyperlink}[, ]{.UGHyperlink}

###### []{#p822}[]{#_Browsing_Through_Cards}3.4.4.3.2.1 Browsing Through Cards {#browsing-through-cards style="tab-stops: 0pt"}

[] 

This section discusses illustrates how to browse through the Cards (Child controls) that have been added to the CardLayout Manager.

[] 

Through Designer

[] 

The selected card can be displayed using the property given below, which simply takes the card name as input.

[] 


  --------------------- ---------------------------------------
  CardLayout Property   Description
  SelectedCard          Gets / sets the current card\'s name.
  --------------------- ---------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [this][.cardLayout1.SelectedCard = [\"Card1\"];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [Me][.cardLayout1.SelectedCard = [\"Card1\"]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 665: Selecting Cards using Design Time Verbs

[] 

You can also browse through the different cards using the methods given below.

[] 


  ---------- -------------------------------------
  Methods    Description
  First      Shows the first card.
  Next       Show the next card in the list.
  Previous   Show the previous card in the list.
  Last       Show the last card in the list.
  ---------- -------------------------------------


[] 


{border="0"} Note: The SmartTag feature (available only in Visual Studio 2005) can also be used to browse through the cards of the CardLayout.


[] 

Through Code

[] 

Drag and drop the ComboBox and the Previous and Next Buttons for viewing the selected card. Use the **Previous()** and **Next()** methods of the CardLayout to see the CardLayout in action inside the Previous and Next Button Clicks.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [private][ [void] Previous_Click([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [this][.cardLayout1.Previous();]                                                                                 |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [private][ [void] Next_Click([object] sender, System.EventArgs e)]     |
|                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [this][.cardLayout1.Next();]                                                                                     |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] Previous_Click([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                    |
| [Me][.cardLayout1.Previous()]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] Next_Click([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)]     |
|                                                                                                                                                                                                                                                                                                                    |
| [Me][.cardLayout1.Next()]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 666: Adding Buttons And ComboBox

 

At run time, cards can be selected using the items in the ComboBox or by Button clicks.

[] 

{border="0"}

[] 

Figure 667: CardLayout showing one Picture at a Time

[] 

See Also

[] 

[Configuring CardLayout]{.UGHyperlink}[, ]{.UGHyperlink}[Configuring Child Controls]{.UGHyperlink}[, ]{.UGHyperlink}[Child Control Settings]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

