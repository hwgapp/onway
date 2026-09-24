REG = []


def frame(fid, name, group, platform=None):
    def deco(fn):
        REG.append(dict(id=fid, name=name, group=group, fn=fn, platform=platform))
        return fn
    return deco
