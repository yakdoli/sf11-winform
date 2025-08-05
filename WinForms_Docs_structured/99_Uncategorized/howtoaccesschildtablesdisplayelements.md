---
title: howtoaccesschildtablesdisplayelements.md
original_path: WinForms_Docs/99_Uncategorized/howtoaccesschildtablesdisplayelements.md
created_at: 2025-08-05
---






#### How to access child table\'s display elements {#how-to-access-child-tables-display-elements style="tab-stops: 0pt"}

[] 

This can be done using the below code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [//Loop for the number of elements in the display elements.]                                                                                                         |
|                                                                                                                                                                                                                        |
| [for][([int] i = 0; i \< [this].gridGroupingControl1.Table.DisplayElements.Count; i++)] |
|                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                |
|                                                                                                                                                                                                                        |
| [      Element el = [this].gridGroupingControl1.Table.DisplayElements\[i\];]                                                                                  |
|                                                                                                                                                                                                                        |
| [      [// If the element is a nested table]]                                                                                                                |
|                                                                                                                                                                                                                        |
| [      [if](el.Kind == DisplayElementKind.NestedTable)]                                                                                                       |
|                                                                                                                                                                                                                        |
| [      {]                                                                                                                                                                          |
|                                                                                                                                                                                                                        |
| [            [// Displaying the nested table elements.]]                                                                                                     |
|                                                                                                                                                                                                                        |
| [            GridNestedTable nt = (GridNestedTable) el;]                                                                                                                           |
|                                                                                                                                                                                                                        |
| [            [foreach](Element el1 [in] nt.ChildTable.NestedDisplayElements)]                                                            |
|                                                                                                                                                                                                                        |
| [            {]                                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [                  System.Diagnostics.Trace.WriteLine(el1);]                                                                                                                       |
|                                                                                                                                                                                                                        |
| [            }]                                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [            i += (nt.ChildTable.NestedDisplayElements.Count - 1);]                                                                                                                |
|                                                                                                                                                                                                                        |
| [      }]                                                                                                                                                                          |
|                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [\'Loop for the number of elements in the display elements.]                                                                                              |
|                                                                                                                                                                                                             |
| [Dim][ i [As] [Integer] = 0]                                                 |
|                                                                                                                                                                                                             |
| [Do][ [While] i \< [Me].gridGroupingControl1.Table.DisplayElements.Count]    |
|                                                                                                                                                                                                             |
| [Dim][ el [As] Element = [Me].gridGroupingControl1.Table.DisplayElements(i)] |
|                                                                                                                                                                                                             |
| [\' If the element is a nested table]                                                                                                                     |
|                                                                                                                                                                                                             |
| [    [If] el.Kind = DisplayElementKind.NestedTable [Then]]                                                                    |
|                                                                                                                                                                                                             |
| [\' Displaying the nested table elements.]                                                                                                                |
|                                                                                                                                                                                                             |
| [Dim][ nt [As] GridNestedTable = [CType](el, GridNestedTable)]               |
|                                                                                                                                                                                                             |
| [        [For] [Each] el1 [As] Element [In] nt.ChildTable.NestedDisplayElements]    |
|                                                                                                                                                                                                             |
| [            System.Diagnostics.Trace.WriteLine(el1)]                                                                                                                   |
|                                                                                                                                                                                                             |
| [        [Next] el1]                                                                                                                               |
|                                                                                                                                                                                                             |
| [        i += (nt.ChildTable.NestedDisplayElements.Count - 1)]                                                                                                          |
|                                                                                                                                                                                                             |
| [    [End] [If]]                                                                                                              |
|                                                                                                                                                                                                             |
| [    i += 1]                                                                                                                                                            |
|                                                                                                                                                                                                             |
| [Loop]                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p658} 

 

[]{#related-topics}

