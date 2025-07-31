---
title: zoomingandprinting1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\zoomingandprinting1.md
created_at: 2025-07-03
---






#### Zooming and Printing {#zooming-and-printing style="tab-stops: 0pt"}

RichTextBoxAdv allows you to zoom in and out on the content of the document. CTRL + mouse wheel will zoom in and zoom out the content of the RichTextBoxAdv control.

 

{border="0"}

Figure 918: RichTextBoxAdv after Zooming

 

The printing feature permits users to print the content of the document using **PrintDocument()**.

We can also use the **Print** command which will execute the **PrintDocument** method whenever it is hooked to the command property.

 

+--------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                    |
| *[        ]*[RichTextBox.PrintDocument();] |
|                                                                                                                    |
|                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------+

 

Properties

  --------------- ------------------------------------------------------------------------- --------------------- -----------
  Property        Description                                                               Type                  Data Type
  IsZoomEnabled   Decides whether the content of the RichTextBoxAdv can be zoomed or not.   Dependency Property   Boolean
  ZoomFactor      Factor to show the zoomed value. It ranges from 0.1 to 1.                 Dependency Property   Double
  --------------- ------------------------------------------------------------------------- --------------------- -----------

 

Methods

  ----------------- ------------------------------------------- ------------ ------ -------------
  Method            Description                                 Parameters   Type   Return Type
  ResetZooming()    Resets the zoom.                            NA           NA     Void
  PrintDocument()   Prints the content of the RichTextBoxAdv.   NA           NA     Void
  ----------------- ------------------------------------------- ------------ ------ -------------

[]{#related-topics}

