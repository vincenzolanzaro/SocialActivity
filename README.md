# SocialActivity
"SocialActivity" is a plugin developed for QGIS platform, whose purpose is to plot social activities around a supplied point.
The simple and clean interface gives all the features to retrieve geopoints and plot them on your map. 
All you need to do is to point your favourite place on the map ( "SocialActivity" automatically will catch map coordinates using WGS84 standard) and click on "OK" button ;) 
In two simple steps you are ready to go, but if you need a deeper customization, you'll find some interesting tools in the interface that will help you in that:
- "Max-Range" is useful to define a range around your supplied point, to retrieve all social activities inner that range
- "Num. Points" can be handy if you need to define your favourite number of geopoints to plot.
- "Real Points" flag is used to retrieve proper geographic coordinates from social activities. Keep in mind that just 2-4% of all social activities have real geographic coordinates enclosed, reason why I thought that it was handy to have also geocoded points feature.
- "Decoded Points" flag is used to retrieve geocoded points starting from geographic info enclosed in the social activities analyzed. That means "city of birth", "home town", "visited place" and whatever found in the user's bio is geocoded in geographic coordinates to be plotted.

Because of all that, I thought that was not enough, I added another feature :P
- "Keyword - @Name - #Tag" is a powerful field with which you can define an argument, a subject, a place, or whatever is spoken in social networks to trace its geographic activity and propagation starting from a supplied point :D Be aware that "with great power comes great responsibility", so use it in a savvy manner ;)

Why "Settings..."?
- Well to make all that working, for each social network you'll need to gain you "API Credentials" or "API Access Tokens". At the moment "SocialActivity" plugin works with Twitter API reason why you'll see available just "Twitter Setting Page", but in future releases will be integrated also others social network.

Some info on "SocialActivity" plugin: 
- "SocialActivity" at the moment use "geopy" library for it's geocode subservice. User, differently to other plugins, doesn't need to install any additional package because all is enclosed with plugin.

![Alt text](https://github.com/vincenzolanzaro/SocialActivity/raw/master/pictures/Screenshot-0.jpg?raw=true "SocialActivity settings")
