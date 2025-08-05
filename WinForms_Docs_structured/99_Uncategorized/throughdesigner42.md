---
title: throughdesigner42.md
original_path: WinForms_Docs/99_Uncategorized/throughdesigner42.md
created_at: 2025-08-05
---






#### Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

This topic discusses how to create a simple layout for aligning Child controls through designer.

[] 

Adding Child Controls

[] 

[·      ]Populate the form with the necessary Child controls (here, we are using Buttons), by dragging and dropping them from the toolbox.

[] 

{border="0"}

[] 

Figure 650: Child Controls (Buttons) added to the Form

[] 

Adding Layout Managers

[] 

The Layout Manager can be added before or after adding the Child controls to the Container control.

[] 

[·      ]The Layout Manager can be added to the form by just dragging and dropping the appropriate Layout Manager (for ex: BorderLayout) from the toolbox onto your form, which will be then be automatically added to the component tray.

[] 

{border="0"}

Figure 651: Adding Layout Manager

[] 

Setting Container Control

[] 

[·      ]You can optionally drop the Child controls onto the Container control that you want to layout and the design time will automatically set the **ContainerControl** property in the Layout Manager.

[·      ]Form, Panel or any control that inherits the Container control can be set as a Container control for the Child controls that are added (here, form is set as the Container control).

 


{border="0"} Note: The FlowLayout, CardLayout and GridLayout controls automatically arrange the Child controls of the Container control in a specific manner. When new controls are added, the Layout Manager will ensure that the old layout is not broken and that the existing controls are not messed up.


[] 

Configuring Child Controls

[] 

For BorderLayout and GridBagLayout, it is necessary to configure the Child controls by changing their extended properties via the property grid in the designer so that the Child controls can be aligned properly.

[] 

{border="0"}

[] 

Figure 652: Aligned Child Controls

 

Configuring Layout Manager

 

You can then configure the Layout Manager by changing its properties via the property grid in the designer.

[] 

See Also

[] 

[Through Code]{.UGHyperlink}[, ]{.UGHyperlink}[Concepts and Features]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

