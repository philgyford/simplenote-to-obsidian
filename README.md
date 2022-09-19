# simplenote-to-obsidian

This is a Python 3 command line script to convert an [export][export]() of notes from [Simplenote][sn] into a directory of Markdown files suitable for use in [Obsidian][ob].

[export]: https://simplenote.com/help/#export
[sn]: https://simplenote.com
[ob]: https://obsidian.md

## Why you might or might not need this script

Your export of Simplenote `.txt` files can be imported into Obsidian by [changing the file extensions][ext] to `.md`.

[ext]: https://osxdaily.com/2016/11/08/batch-change-file-extensions-mac/

But if you used tags in Simplenote you will lose them in Obsidian, because in the exported Simplenote files they appear like this at the end of each one:

    Tags:
      Recipes, Todo

Obsidian won't recognise these as tags – they each need to be prefixed with `#`.

So, if you used tags, this script will help.


## What the script does

* Reads the original note data from the exported JSON file
* Creates a new directory of `.md` text files, one per note.
* If s Simplenote note had tags, the new file will contain those tags prefixed with `#`, which Obsidian interprets as tags
* Sets the last-modified time of each new file to the last-modified time of the Simplenote note.
* Sets the creation time of each new file to the creation time of the Simplenote note (only works on macOS with Xcode installed; see below).


## What the script does not do

* Handles any links between notes. I didn't use this feature of Simplenote, so didn't see if anything was needed to make them work in Obsidian.
* Converts any notes in Simplenote's trash.


## How the script does it

### Source file and destination directory

The script looks for a `notes.json` file in the same directory as the script itself.

The script will create a directory called `notes_converted` in the same directory as the script itself. Text files will be created in there. If you want to change this, edit the value of `OUTPUT_DIRECTORY` near the start of the script.

### Tags

If a Simplenote note has tags, these will be indicated in the JSON file like this:

    "tags": [
      "Recipes",
      "Todo"
    ]

This script will addd a line to the end of the created file like this:

    #Recipes #Todo

(Any words that begin with `#` are interpreted as tags by Obsidian.)

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

Any non-word characters (like space, `:`, `.`, etc) that are in a Simplenote tag will be replaced with a hyphen (`-`) so that Obsidian recognises it as a single tag.

### Creation times

By default the script will set the creation times of each created file to the original note's creation time.

BUT this only works on macOS with Xcode installed. If this is not the case for you, set `KEEP_ORIGINAL_CREATION_TIME` to `False` at the top of the script, or you'll see a lot of errors.

### Last-modified times

By default the script will set the last-modified time of each created file to the original note's last-modified time.

If you don't want this, change `KEEP_ORIGINAL_MODIFIED_TIME` near the start of the script to `False`.


## How to run the script

1. Check out or download this repository.

2. Ensure the script can be executed:

        $ chmod +x convert_notes.py

3. If you're not on macOS with Xcode installed, set `KEEP_ORIGINAL_CREATION_TIME` near the top of the script to `False` and save the file.

4. In the directory of notes you exported from Simplenote, find the `source/` directory, and the `notes.json` file within that. Copy or move that `notes.json` file to the same directory as the script.

5. Run the script:

        $ ./convert_notes.py

If you run the script multiple times then the content of the `notes_converted` directory isn't erased first – any existing notes will be overwritten with new ones, and new notes will be created.

Once complete, copy or move the exported notes into the directory that's your Obsidian vault, then they should appear in Obsidian.


## Contact

Phil Gyford  
phil@gyford.com  
https://www.gyford.com  
https://twitter.com/philgyford  
http://mastodon.social/@philgyford