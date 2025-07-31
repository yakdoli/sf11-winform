---
title: hidethedefaultcenterportofanode1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\hidethedefaultcenterportofanode1.md
created_at: 2025-07-03
---








  









### Hide the Default Center Port of a Node {#hide-the-default-center-port-of-a-node style="tab-stops: 0pt"}

Each node will have a default center port visibility of this port can be hidden using the following statement.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                           |
|                                                                                                                                                                          |
| []                                                                                                                     |
|                                                                                                                                                                          |
| [            node.Loaded += [new] [RoutedEventHandler](node_Loaded);]                   |
|                                                                                                                                                                          |
| [        [//Hide the Node\'s center port in the Node\'s loaded event.]]                                        |
|                                                                                                                                                                          |
| [        [void] node_Loaded([object] sender, [RoutedEventArgs] e)] |
|                                                                                                                                                                          |
| [        {]                                                                                                                          |
|                                                                                                                                                                          |
| [            [Node] node = sender [as] [Node];]                 |
|                                                                                                                                                                          |
| [            [if] (node.Ports.Count \> 0)]                                                                      |
|                                                                                                                                                                          |
| [            {]                                                                                                                      |
|                                                                                                                                                                          |
| [                node.Ports\[0\].Visibility = [Visibility].Hidden;]                                          |
|                                                                                                                                                                          |
| [            }]                                                                                                                      |
|                                                                                                                                                                          |
| [        }][]                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                      |
| [       ][Private][ node.Loaded += New RoutedEventHandler(AddressOf node_Loaded)]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                      |
| [        [\'Hide the Node\'s center port in the Node\'s loaded event.]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                      |
| [        [Private] [Sub] node_Loaded([ByVal] sender [As] [Object], [ByVal] e [As] [RoutedEventArgs])] |
|                                                                                                                                                                                                                                                                                                                      |
| [            [Dim] node [As] [Node] = [TryCast](sender, [Node])]                                                                                                  |
|                                                                                                                                                                                                                                                                                                                      |
| [            [If] node.Ports.Count \> 0 [Then]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                      |
| [                node.Ports(0).Visibility = Visibility.Hidden]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                      |
| [            [End] [If]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [        [End] [Sub]][]                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


{border="0"} Note:[ ]node.Ports\[0\] refers to the center port. This default center port will be available only after the Node's Template is applied. So you have to change the Visibility accordingly.


[] 

[]{#related-topics}

