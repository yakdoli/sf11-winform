---
title: methods20.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\methods20.md
created_at: 2025-07-03
---








  









### Methods {#methods style="tab-stops: 0pt"}

Table 6: ShapeFileLayer Methods


  -------------------------- -------------------------------------------------------------------------- -------------------------------------------- ------ ------------- ---------------------------------------------------------------------------------------------------
  Method                     Description                                                                Parameters                                   Type   Return Type   Reference links
  Zoom                       This method can be called to zoom the Map                                  Double zoomfactor                            None   None          
  Pan                        This method can be called to Pan the Map                                   Double XCoordinate, and Double YCoordinate   None   None          
  PointToLatitudeLongitude   This method can be called to  convert a Point to Latitude and Longitude    Point point                                  None   Point         
  LatitudeLongitudeToPoint   This method can be called to convert the Latitude and Longitude to point   Point LatLonPoint                            None   Point         
  LoadFromFile               Method can be called to Load the ShapeFile from a location                 String filename                              None   None          
  LoadFromStream             this method can be called to Load a shape file from stream                 FileStream fileStream, and String filename   None   None          
  -------------------------- -------------------------------------------------------------------------- -------------------------------------------- ------ ------------- ---------------------------------------------------------------------------------------------------


 

[]{#related-topics}

