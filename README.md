# SocialActivity
"SocialActivity" is a plugin developed for QGIS platform, whoose purpose is to plot social activities around a supplied point.
The simple and clean interface gives all the features to retrieve geopoints and plot them on your map. 
All you need to do is to point your favorite place on the map ( "SocialActivity" automatically will catch map coordinates using WGS84 standard) and click on "OK" button.
In two simple steps you are ready to go, but if you need a deeper customization, you'll find some interestings tools in the interface that will help you in that:
- "Max-Range" is useful to define a range around your supplied point, to retrieve all social activities inner that range
- "Num. Points" can be handy if you need to define your favorite number of geopoints to plot.
- "Real Points" flag is used to retrieve proper geographic coordinates from social activities. Keep in mind that just 2-4% of all social activities has real geographic coordinates enclosed, reason why I though that it was handy to have also geocoded points feature.
- "Decoded Points" flag is used to retrieve geocoded points starting from geographic info enclosed in the social activities analized. That means "city of birth", "home town", "visited place" and whatever found in the user's bio is geocoded in geographic coordinates to be ploted.
