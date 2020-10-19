# Firekeeper
> "Let these memes, withdrawn from their vessels, Manifestations of disparity, Elucidated by fire, Burrow deep within me, Retreating to a darkness beyond the reach of flame, Let them assume a new master, Inhabiting ash, casting themselves upon new forms.

Firekeeper makes dumb memes on command.

## Commands
- `*died` makes a you died meme
- `*lit` makes a bonfire lit meme
- `*restored` makes a humanity restored meme

## Building
It is reccommended you use `pipenv` to help manage dependencies. This bot requires python3
### Building with `pipenv`:
1. In the root directory run `pipenv install`
2. Create your `secrets.ini` file with your bot's token (see example file for format)
3. Populate the `firekeeper/data/source_images/` folder with images to be used in the generated memes
3. run the bot: `pipenv run bot`
