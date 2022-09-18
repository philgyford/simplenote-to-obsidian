#!/usr/bin/env python3

import glob
import os
import re
import sys


# Where we'll save the converted notes.
OUTPUT_DIRECTORY = "./notes_converted/"


def main():

    ###################################################################
    # 1. Set up.

    path = input("\nEnter path to folder of .txt files (default is './notes'):")

    if path == "":
        path = "./notes"

    if not os.path.isdir(path):
        sys.exit(f"'{path}' is not a valid directory path")

    tag_position = input("\nWhere should tags be put? Either 'start' or 'end' (default is 'end'):")

    if tag_position == "":
        tag_position = "end"

    if tag_position not in ["start", "end"]:
        sys.exit("Enter either 'start' or 'end'.")

    if not os.path.isdir(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)

    ###################################################################
    # 2. Loop through all the notes and create new ones

    files_read = 0
    files_saved = 0

    # Open each .txt file in the directory in turn:
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(filename) as file:

            # Uncomment this to see each filename:
            # print(filename)

            # Get all the lines in the file:
            lines = file.read().splitlines()

            # What we'll write to the new file by default - same as the old file
            new_lines = lines

            # Is the file long enough to have tags?
            if len(lines) >= 2:
                # See what the penultimate lines of the file is:
                if lines[-2] == "Tags:":
                    # There are probably some tags!

                    last_line = lines[-1]

                    # Split the line into a list of individual tags:
                    tags = [tag.strip() for tag in last_line.split(", ")]

                    if len(tags) > 0:
                        # There are tags!

                        # Replace any non-word characters in each tag with a hyphen:
                        tags = [re.sub(r'\W+', '-', tag) for tag in tags]

                        # Prefix tags with # so obsidian recognises them as tags:
                        tags = ["#"+tag for tag in tags]

                        # Remove the tags lines from the end of the note:
                        new_lines = lines[:-2]

                        # The new line of tags we'll add to the note:
                        tag_line = " ".join(tags)

                        if tag_position == "start":
                            new_lines.insert(1, "")
                            new_lines.insert(2, tag_line)
                        else:
                            new_lines.append(tag_line)

            # Write the file to the new directory as a .md file

            new_filename = os.path.splitext(os.path.basename(filename))[0] + ".md"

            with open(os.path.join(OUTPUT_DIRECTORY, new_filename), "w") as outfile:
                outfile.write("\n".join(new_lines))
                files_saved += 1

        files_read += 1

    print(f"\n{files_read} .txt file(s) were found in {path}")
    print(f"{files_saved} .md  file(s) were saved to {OUTPUT_DIRECTORY}")


if __name__ == "__main__":
    main()