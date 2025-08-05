---
title: superaccelerator1.md
original_path: WinForms_Docs/99_Uncategorized/superaccelerator1.md
created_at: 2025-08-05
---






#### Super Accelerator {#super-accelerator style="tab-stops: 0pt"}

[] 

SuperAccelerator is a component that is used to accelerate the click event of items by using a Single key stroke without mouse hovering on it.

[] 

1.              Drag-and-drop the SuperAccelerator on your form.

[] 

{border="0"}

[] 

Figure 1454: SuperAccelerator in Toolbox

[] 

2.   When the SuperAccelerator component is added to a form, an extended property will be added to the properties of every item in the toolstrip or tabitem in the RibbonControlAdv.

[] 

{border="0"}

[] 

***[]*** 

Figure 1455: SuperAccelerator Extended Property on ToolStripButton Item

[] 

3.   In the appropriate item, use the Accelerator on SuperAccelerator property to set the string value.

[] 

{border="0"}

***[]*** 

Figure 1456: SuperAccelerator Illustrated

[] 

4.   To accelerate the item\'s click event at run time, Press the ALT key. All the specified accelerator strings will be displayed below the items.

[] 

5.   Press the string in the keyboard and the corresponding item\'s click event will be triggered. (Eg. If the accelerator string of Cut is X key, Press ALT key. Once all the accelerator strings are displayed, press X key the Cut item event will be triggered.)

[] 


 

{border="0"} Note: We can make the Accelerator feature to be active or inactive using SuperAccelerator.Active property.


[] 

See Also

[] 

[ ][[How to get or set an accelerator key programmatically]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_get_2)[?]{.UGHyperlink}[]

 

 

 

 

More:





