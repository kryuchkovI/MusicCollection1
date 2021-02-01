import os
import argparse

from symlinks_handler import *


def mount(path):
    all_path = path + '/' + "All"
    all_path_flag = not os.path.isdir(all_path)

    if all_path_flag:
        os.mkdir(all_path)

    artists_path = path + '/' + "Artists"
    artists_path_flag = not os.path.isdir(artists_path)

    if artists_path_flag:
        os.mkdir(artists_path)

    albums_path = path + '/' + "Albums"
    albums_path_flag = not os.path.isdir(albums_path)
    
    if albums_path_flag:
        os.mkdir(albums_path)

    if all_path_flag and artists_path_flag and albums_path_flag:
        print("Folders are created")
    elif os.path.exists(all_path) and os.path.exists(artists_path) and os.path.exists(albums_path):
        print("Folders already exist")
    else:
        raise SystemError("Something went wrong...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--mount", default=".", type=str, help="Input path for mount")
    parser.add_argument("--create", default="", type=str, help="Input name of symlink")
    parser.add_argument("--origpath", default="", type=str, help="Input absolute path to original file")
    parser.add_argument("--delete", default="", type=str, help="Input name of symlink for delete")
    parser.add_argument("--update", default="", type=str, help="Input name of symlink for update")
    parser.add_argument("--newname", default="", type=str, help="Input new name of symlink")

    args = parser.parse_args()

    mount(args.mount)
    
    path = os.path.abspath("")

    if args.create:
        create(args.origpath, path, args.create)
    elif args.delete:
        delete(path, args.delete)
    elif args.update and args.newname:
        if args.newname:
            update(args.update, args.update, path, args.origpath)
        else:
            update(args.update, args.newname, path, args.origpath)
    else:
        raise RuntimeError("No valid arguments")
