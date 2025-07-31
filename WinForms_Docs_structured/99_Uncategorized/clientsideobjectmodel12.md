---
title: clientsideobjectmodel12.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideobjectmodel12.md
created_at: 2025-07-03
---






##### Client-Side Object Model {#client-side-object-model style="tab-stops: 0pt"}

[] 

The client side methods can be used to control the behavior of the Window control that allows you to interact with it. The various client side methods supported by Window Control are as follows.

[] 


  ------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Method                                                                    Description
  SetHeight()                                                               Sets the height of Window control.
  SetWidth()                                                                Sets the width of Window control.
  SetSource()                                                               Changes URL of window.
  GetSource(url)                                                            Gets the URL of the window.
  SetStatusText()                                                           Displays content in the window status bar.
  GetStatusText()                                                           Gets the content of window status bar.
  SetTitleText(title)                                                       Sets window title.
  GetTitleText()                                                            Gets window title.
  IsOpened()                                                                Returns true if the window is currently Opened.
  IsClosed()                                                                Returns true if the window is currently closed.     
  SetMinWidth(value)                                                        Sets the Minimum width that the Window can be resized to.
  GetMinWidth()                                                             Gets the Minimum width that the Window can be resized to.
  SetMinHeight(value)                                                       Sets the Minimum Height that the Window can be resized to.
  GetMinHeight()                                                            Gets the Minimum Height that the Window can be resized to.
  Open()                                                                    To open the Window.
  Open( this, sText )                                                       To open the Window.
  Close()                                                                   To close the Window.
  Alert(sText, sCaption, nWidth, nHeight)                                   To display Window Control as alert message box.
  Prompt(sText, fnCallbackFunction, sCaption, sDefValue, nWidth, nHeight)   To display Window Control as Prompt message box.
  Confirm( sText, fnCallbackFunction, sCaption, nWidth, nHeight)            To display Window Control as Confirm message box.
  SetTop(value)                                                             Sets relative start position to top coordinate of the window.
  GetTop()                                                                  Gets relative start position to top coordinate of the window.
  SetLeft(value)                                                            Sets relative start position to Left coordinate of the window.
  GetLeft()                                                                 Gets relative start position to top coordinate of the window.
  SetDraggingStyle(value)                                                   Sets the Style to use for dragging Window.
  GetDraggingStyle()                                                        Gets the Style to use for dragging Window.
  GetDraggingMode()                                                         Gets the type of dragging to allow for  Window.
  SetResizeStyle(value)                                                     Sets the style to use for resizing the Window.
  GetResizeStyle()                                                          Gets the style to use for resizing the Window.
  SetIconUrl(url)                                                           Sets the Icon Image Url.
  SetResizeStyle(value)                                                     Sets the style to use for resizing the Window.
  GetContentFrame()                                                         Gets reference to Windows\'s content area (IFRAME).
  PinOn()                                                                   To PinOn the Window control.
  PinOff()                                                                  To PinOff the Window control.
  Minimize()                                                                To Minimize the Window control.
  Maximize()                                                                To Maximize the Window control.
  Restore()                                                                 To Restore the Window control.
  Refresh()                                                                 Sends callback to server without page refreshing and triggers CallbackRefresh server side Window event. To perform callback the EnableCallbacks property must be set to true.
  ------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 

[]{#related-topics}

