---
title: blendability23.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\blendability23.md
created_at: 2025-07-03
---






#### Blendability {#blendability style="tab-stops: 0pt"}

To edit the style of the UpDown control in Expression Blend:

1.   Drag the **UpDown** control to **Design View**. The **UpDown** control appears as shown in the screen shot displayed below.

[] 

{border="0"}

Figure 1157: UpDown Control in Design View

 

2.   Right-click the **UpDown** control, select **Edit Template**, and then select **Edit a Copy**.

 

{border="0"}

Figure 1158: File Menu

After the **Edit a Copy** option is selected, the style of the UpDown control will be generated in the XAML file. You can change the Control Template or some of the brushes of the UpDown control by using the properties exposed by the UpDown control.

In the following code snippet, the BorderBrush color is changed when the IsMouseOver value changes.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][Trigger][ Property][=\"IsMouseOver\"][ Value][=\"True\"\>][]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    \<][Setter][ Property][=\"BorderBrush\"][ TargetName][=\"Border\"][ Value][=\"Red\"/\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][Trigger][\>][]                                                                                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 1159: BorderBrush Set to Red

[]{#related-topics}

