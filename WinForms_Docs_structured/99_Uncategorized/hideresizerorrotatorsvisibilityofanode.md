---
title: hideresizerorrotatorsvisibilityofanode.md
original_path: WinForms_Docs/99_Uncategorized/hideresizerorrotatorsvisibilityofanode.md
created_at: 2025-08-05
---








  









### Hide Resizer or Rotator's Visibility of a Node {#hide-resizer-or-rotators-visibility-of-a-node style="tab-stops: 0pt"}

Gripper or Rotator Visibility can be hidden using the following code snippet.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        node.Loaded += [new] [RoutedEventHandler](node_Loaded);]                                                                                   |
|                                                                                                                                                                                                                                      |
| [        //Hide the Node\'s Resizer and Rotator in the Node\'s loaded event.]                                                                                                      |
|                                                                                                                                                                                                                                      |
| [        [void] node_Loaded([object] sender, [RoutedEventArgs] e)]                                                             |
|                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [            [Node] node = sender [as] [Node];]                                                                             |
|                                                                                                                                                                                                                                      |
| [            [//node.Template will be null if it\'s template is not applied.]]                                                                                             |
|                                                                                                                                                                                                                                      |
| [            [if] (node != [null] && node.Template != [null])]                                                                    |
|                                                                                                                                                                                                                                      |
| [            {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                      |
| [                [//To hide the Resizer.]]                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [                (node.Template.FindName([\"PART_Resizer\"], node) [as] [Control]).Template = [null];] |
|                                                                                                                                                                                                                                      |
| [                [//To hide the Rotator.]]                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [                (node.Template.FindName([\"PART_Rotator\"], node) [as] [Control]).Template = [null];] |
|                                                                                                                                                                                                                                      |
| [            }]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                      |
| [        }][]                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                 |
| [  ][Private][ node.Loaded += New RoutedEventHandler(AddressOf node_Loaded)]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                 |
| [  [\'Hide the Node\'s Resizer and Rotator in the Node\'s loaded event.]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [   [Private] [Sub] node_Loaded([ByVal] sender [As] [Object], [ByVal] e [As] [RoutedEventArgs])] |
|                                                                                                                                                                                                                                                                                                                 |
| [      [Dim] node [As] [Node] = [TryCast](sender, [Node])]                                                                                                   |
|                                                                                                                                                                                                                                                                                                                 |
| [      [\'node.Template will be null if it\'s template is not applied.]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                 |
| [      [If] node [IsNot] [Nothing] [AndAlso] node.Template [IsNot] [Nothing] [Then]]                                     |
|                                                                                                                                                                                                                                                                                                                 |
| [        [\'To hide the Resizer.]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                 |
| [        [TryCast](node.Template.FindName([\"PART_Resizer\"], node), [Control]).Template = [Nothing]]                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [        [\'To hide the Rotator.]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                 |
| [        [TryCast](node.Template.FindName([\"PART_Rotator\"], node), [Control]).Template = [Nothing]]                                                                             |
|                                                                                                                                                                                                                                                                                                                 |
| [      [End] [If]]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                 |
| [    [End] [Sub]][]                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


{border="0"} Note:[ ]Node's Template will be available only after its template is applied, so if you try to do these operations before it will not give an expected result.


[] 

[]{#related-topics}

