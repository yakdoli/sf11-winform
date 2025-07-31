---
title: nodecontent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\nodecontent.md
created_at: 2025-07-03
---








  









### Node Content {#node-content style="tab-stops: 0pt"}

 

Node is used to visually represent any UIElemnts using the Content property. The user can host any content inside the node using the **Content** property. Node supports control template, by the defined template for the nodes. Business object can be assigned as Node's Content and the template will look after the representation of the business object.

[] 


{border="0"} Note:[ ]A Node can have both Content and Shape at the same time. In doing so, Content will be placed over the Shape.


 

Properties\
\

Property


Description

Type of the property

Value it Accept

Any other dependencies/ sub properties associated

Content

Gets or sets the node\'s content

Dependency property

object

No[]

HorizontalContentAlignment

Specifies the horizontal alignment for the node content

Dependency property

HorizontalAlignment.Center

HorizontalAlignment.Left

HorizontalAlignment.Right

HorizontalAlignment.Stretch

No

VerticalContentAlignment

Specifies the vertical alignment for the node content

Dependency property

VerticalAlignment.Bottom

VerticalAlignment.Center

VerticalAlignment.Stretch

VerticalAlignment.Top

No

 

More:






