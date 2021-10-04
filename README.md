# PygameSpaceShooter

This is a simple "game" in python using pygame.

I am not a game programmer and this is one of my first games and probably the furthest I have ever gotten. 

At the moment there are only a few resources available as the original resources used were purchased and the license does not allow for distribution. Hopefully I can create/aquire resources that I can make public.

The original resources were named "SpaceShooter Part 1" by Pixel-Boy of https://sparklinlabs.itch.io/superpowers fame.

## Getting things to run.

The main impediment to running this code yourself should be the resoruces. The file `gamedata.json` contains the references the most the resources and by editing the file you can repoint to new resources that you have available. Each object containing a string will require at least one entry to work. For example to use the original ship from the "SpaceShooter Part 1" resource set you would make this change:

```json
    "ShipFly": [
        "resources/Ship/2.png"
    ]

```

Since there original ship only has one frame it will not be animated. 