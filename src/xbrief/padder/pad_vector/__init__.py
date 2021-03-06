from aryth.bound_vector import max_by
from texting import SP, lange
from veho.vector import duozipper, trizipper

from xbrief.padder.pad_string import to_pad


def pad_vector(text, raw=None, dye=None, ansi=False, fill=SP):
    raw = raw if raw is not None else text
    pad = to_pad(ansi=ansi, fill=fill)
    wd = max_by(text, lange if ansi else len)
    return trizipper(text, raw, dye, lambda tx, va, dy: dy(pad(tx, wd, va))) \
        if dye \
        else duozipper(text, raw, lambda tx, va: pad(tx, wd, va))
