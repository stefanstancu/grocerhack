# Grocerhack
An grocery optimization tool for figuring out how to get your macros as cheap as possible.

## Current Support and Future Plan
The project is currently under development.
### Stage 1
Building the scraper for the grocery store Loblaws.
#### Loblaws API 403
The scrapper uses the aiohttp package to substantially increase its throughput over the traditional serial requests. However the API will return 403 if you bombard it with too many requests. Feeling that this is not a unique problem, a tool to probe the api for its fastest stable through-put is under development.
### Stage 2
Build a linear programming model that can choose which foods to eat in order to meet the minimum required macros, for the cheapest possible price.
Restrictions should be placed on the macros and the weight/macro. Lentils are probably the cheapest protein, but you can't eat 1kg of them in a sitting.
### Stage 3
Extend the project and add mutliple grocery store inventories, sales, a notification system, etc.
The options are endless, depending on how useful the core functionality becomes
