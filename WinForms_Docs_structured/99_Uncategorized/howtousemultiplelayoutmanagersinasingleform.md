---
title: howtousemultiplelayoutmanagersinasingleform.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtousemultiplelayoutmanagersinasingleform.md
created_at: 2025-07-03
---






#### How to use multiple Layout Managers in a single form {#how-to-use-multiple-layout-managers-in-a-single-form style="tab-stops: 0pt"}

[] 

It is very simple to use more than one Layout Manager in a single form.

[] 

[·      ]Drag-and-drop the **FlowLayout** Manager from the toolbox onto the form setting it as the Container control.

[] 

{border="0"}

[] 

Figure 702: FlowLayout in Designer

[] 

[·      ]Add Panels as Child controls onto the form. The FlowLayout Manager will automatically layout the Child components as shown below.

[] 

{border="0"}

[] 

Figure 703: FlowLayout with Child Controls

[] 

[·      ]Drag and drop the **GridLayout** Manager onto the Panel1 and add Button controls as Child controls. This will be arranged as follows.

[] 

{border="0"}

[] 

Figure 704: GridLayout with Panel1 as Container Control

[] 

[·      ]We can also make Panel2 as the Container control for **GridBagLayout** Manager. This will arrange it\'s Child controls (Buttons) in a single row as shown below.

**[]** 

{border="0"}

[] 

Figure 705: GridBagLayout with Panel2 as Container Control

[] 

[·      ]Finally make Panel3 as the Container control for the **BorderLayout** Manager which will arrange the Child controls (Buttons) as follows.

[] 

{border="0"}

**[]** 

Figure 706: Panel3 as container control with BorderLayout

[] 

[·      ]The final output of the application with all the Layout Managers arranged in the above said fashion is shown below.

[] 

{border="0"}

[] 

Figure 707: Form with Multiple Layout Managers

[] 

See Also

[] 

[Creating a Simple Layout]{.UGHyperlink}[, ]{.UGHyperlink}[How to programmatically nest various layouts]{.UGHyperlink}[?]{.UGHyperlink}

[]{#related-topics}

