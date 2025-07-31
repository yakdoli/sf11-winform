---
title: basicconcepts.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\basicconcepts.md
created_at: 2025-07-03
---








  









## Basic Concepts {#basic-concepts style="tab-stops: 0pt"}

 

Object model of Microsoft Word document is dendritic. WordDocument is the root of such a tree. Base, simplified hierarchy of document content can be shown as follows.

 

{border="0"}

Figure 22: Object Model of Word Document

 

WordDocument and the rest of the nodes in such a tree (which are containers for content: text or graphics), are inherited from the abstract class, Entity. This class has the **EntityType** property, which defines the type of the node. Such an approach gives an opportunity to generalize the work with the nodes of the WordDocument tree.

 

Every element of a tree has a reference to the document it refers. Elements also have the **Owner** property, which shows whether the current element is attached to the document. If an element is not attached to the document, it won\'t be available in the resultant document after saving the document.

 

Composite Design Patterns

 

Overview

 

Object model of Word document in DocIO uses the idea of \"Composite Design\" pattern. The following screen shot illustrates the classic structure of the Composite Design pattern.

 

{border="0"}

Figure 23: Composite Design Pattern

**** 

IEntity

 

**IEntity** interface represents the \"Component\" block in DocIO. IEntity interface supports all the elements which have content. Composite block is represented by the **ICompositeEntity** interface. Composite block has child nodes. Classes which implement only the IEntity (which don\'t have child nodes) are \"leafs\" for DocIO.

 

IEntity interface has some specific properties.

 

[·      ]**IsComposite**: defines whether the current element is composite (elements which have child nodes are composite).

[·      ]**NextSibling**: returns the next sibling. For example, in the following screen shot, the **NextSibling** property for Child node 2 will return Child node 3 element.

[·      ]**PreviousSibling**: returns the previous sibling. For example, in the following screen shot, the **PreviousSibling** property for Child node 2 will return Child node 1 element.

 

{border="0"}

Figure 24: IEntity Interface

 

IEntity Public Properties

 


  ----------------- ---------------------------------------------------------------
  **Name**          **Description**
  Document          Gets document of this entity.
  EntityType        Gets the type of the entity.
  IsComposite       Gets a value indicating whether this instance is composite.  
  NextSibling       Gets the next sibling.
  Owner             Gets owner of this entity.
  PreviousSibling   Gets the previous sibling.  
  ----------------- ---------------------------------------------------------------


 

IEntity Public Methods

 


  ---------- --------------------------------------
  **Name**   **Description**
  Clone      Creates a duplicate of the entity.  
  ---------- --------------------------------------


 

ICompositeEntity

 

**ICompositeEntity** interface represents an element which has \"children\". A child element is an element that supports the ICompositeEntity (and also has children) or a \"leaf\" (element without children).

 

ICompositeEntity Public Property

 


  --------------- ----------------------------
  **Name**        **Description**
  ChildEntities   Gets the child entities.  
  --------------- ----------------------------


[]{#p26}[]{#_Word_Document}[]{#p34}[]{#_Section} 

 

[]{#related-topics}

