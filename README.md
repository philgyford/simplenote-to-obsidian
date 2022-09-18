# simplenote-to-obsidian

This is a Python 3 command line script to convert a directory of text files [exported](https://simplenote.com/help/#export) from [Simplenote](https://simplenote.com) into a directory of Markdown files suitable for use in [Obsidian](https://obsidian.md).


## What the script does

* Copies all `.txt` files from one directory into another directory
* Replaces the `.txt` extension with `.md`
* If s Simplenote note contains tags (which Simlenote adds when exporting), these are replaced with text that Obsidian interprets as tags


## What the script does not do

* Handle any links between notes. I didn't use this feature of Simplenote, so didn't see if anything was needed to make them work in Obsidian.
* Convert any notes in the `trash` directory of the Simplenote export directory.
* Do anything with the `source/notes.json` file in the Simplenote export directory.


## How the script does it

### Source and destination directories

The script looks for a directory called `notes` in the same directory as the script itself. When you run the script you'll be given the opportunity to choose a different path to a directory of notes.

The script will create a directory called `notes_exported` in the same directory as the script itself. Converted notes will be put in there. If you want to change this, edit the value of `OUTPUT_DIRECTORY` near the start of the script.

### Tags

If a Simplenote note has tags, the exported file will have something like this added as the final two lines:

    Tags:
      Recipes, Todo

This script will replace those two lines with this final line:

	#Recipes #Todo

(Any words that begin with `#` will be interpreted as tags by Obsidian.)

When you run the the script you'll be given the opportunity to enter `end` (the default, above) or `start`, for where the tags should be written.

If you choose `start`, tags will be inserted after the note's title instead. For example, if the above note begins like this:

	Carrot cake

	* 100g light muscovado sugar
	* 100ml sunflower oil
	...

Then the converted note will begin like this:

	Carrot cake

	#Recipes #Todo

	* 100g light muscovado sugar
	* 100ml sunflower oil
	...

Any non-word characters (like space, `:`, `.`, etc) that are in tags in the Simplenote files will be replaced with a hyphen (`-`) so that Obsidian recognises it as a single tag.

## How to run the script

1. Check out or download this repository.

2. Ensure the script can be executed:

        $ chmod +x convert_notes.py

3. Run it:

        $ ./convert_notes.py

If you run the script multiple times then the content of the `notes_exported` directory isn't erased first – any existing notes will be overwritten with new ones, and new notes will be created.

Once complete, copy or move the exported notes into the directory that's your Obsidian vault, then they should appear in Obsidian.

## Contact

Phil Gyford  
phil@gyford.com  
https://www.gyford.com  
https://twitter.com/philgyford  
http://mastodon.social/@philgyford