---
title: customizationofnavigation1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizationofnavigation1.md
created_at: 2025-07-03
---






##### Customization of Navigation {#customization-of-navigation style="tab-stops: 0pt"}

[] 

The customization of this default navigation can be done by using the properties, methods and events mentioned below.

[] 

Properties

[] 

The following table lists the properties associated with this feature.

[] 


  ----------------------- ------------ ------------------------------------------------------------------------------------------------------ ----------------- ----------------------
  Property                Type         Description                                                                                            Value Accepted    Property Syntax
  IncrementKey            Dependency   Increase the pointer value.                                                                            Key               Propertyname=Key.key
  DecrementKey            Dependency   Decrease the pointer value.                                                                            Key               Propertyname=Key.key
  PointerSelectionBrush   Dependency   Allows differentiation of the pointer when it is focused and unfocused by changing the border color.   SolidColorBrush   Propertyname=color
  ----------------------- ------------ ------------------------------------------------------------------------------------------------------ ----------------- ----------------------


[] 

Methods

[] 

The following table lists the methods associated with this feature.

[] 


  ----------- -----------------------------------------------
  Method      Description
  KeyDown     Changes the value with appropriate key press.
  GotFocus    Selection is made when pointer gets focus.
  LostFocus   Pointer loses focus.
  ----------- -----------------------------------------------


[] 

Events

**[]** 

The following table lists the events associated with this feature.

[] 


  ------------------------------ --------------- ------------------------------------------------------- --------------------------- -----------------------------------
  Event                          Event Trigger   Method Handling Event                                   Event Argument              Purpose
  PointerSelectionBrushChanged   OnGotFocus      CircularPointer_GotFocus and LinearPointer\_ GotFocus   (object, RoutedEventArgs)   Highlights the pointer selection.
  IncreamentKeyChanged           OnKeyDown       CircularPointer_KeyDown and LinearPointer_KeyDown       (object, KeyEventArgs)      Changes the Pointer value.
  DecreamentKeyChanged           OnKeyDown       CircularPointer_KeyDown and LinearPointer_KeyDown       (object, KeyEventArgs)      Changes the Pointer value.
  ------------------------------ --------------- ------------------------------------------------------- --------------------------- -----------------------------------


 

[]{#p97} 

 

[]{#related-topics}

