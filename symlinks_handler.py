import os
import csv

from get_metadata_mp3 import *


def create(src_path, path, sym_name):
    try:
        artist = get_artist(src_path) 
        album = get_album(src_path)
        
        if not artist:
            artist = sym_name + '_artist'

        if not album:
            album = sym_name + '_album'
     
    except RuntimeError:
        print("This file has no ID3v1 tags")
        return

    all_path = path + '/' + "All" + '/' + sym_name 

    if os.path.isfile(all_path):
        return 
    else:
        os.symlink(src_path, all_path)

        artists_path = path + '/' + "Artists" + '/' + artist
        os.symlink(all_path, artists_path)

        albums_path = path + '/' + "Albums" + '/' + album
        os.symlink(all_path, albums_path)

        write_ligaments(sym_name, artist, album)


def update(sym_name_from, sym_name_to, path, src_path):
    
    delete(path, sym_name_from)
    create(src_path, path, sym_name_to)


def delete(path, sym_name):
    vals = delete_ligaments(sym_name)

    if not vals:
        print("Nothing to delete")
        return 
    
    artist, album = vals

    os.unlink(path + '/Artists/' + artist)
    os.unlink(path + '/Albums/' + album)

    os.unlink(path + '/All/' + sym_name)


def write_ligaments(all, artist, album):
    with open("ligaments.txt", mode='a', encoding='utf-8') as file:
        file.write(' '.join([all, artist, album]) + '\n')
        
def read_ligaments(): 
    ligs = {}
    with open("ligaments.txt") as file:
        for line in file:
            key, *value = line.split()
            ligs[key] = value
        return ligs

def rewrite_ligaments(ligs):
    with open("ligaments.txt", mode='w', encoding='utf-8') as file:
        for all in ligs:
            file.write(' '.join([all, ligs[all][0], ligs[all][1]]) + '\n')

def delete_ligaments(all):
    ligs = read_ligaments()
    artist, album = ligs.pop(all)
    rewrite_ligaments(ligs)
    return artist, album
