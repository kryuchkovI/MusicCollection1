import eyed3

def get_metadata(path):
    ext = path.split('.')

    if ext[-1] != "mp3":
        raise RuntimeError("Unsupportable format")

    audiofile = eyed3.load(path)

    return audiofile 

def get_artist(path):
    return get_metadata(path).tag.artist

def get_album(path):
    return get_metadata(path).tag.album