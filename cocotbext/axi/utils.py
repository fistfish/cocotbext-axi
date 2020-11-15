"""

Copyright (c) 2020 Alex Forencich

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

def hexdump_line(data, offset):
    h = ""
    c = ""
    for ch in data[0:16]:
        h += f"{ch:02x} "
        c += chr(ch) if 32 < ch < 127 else "."
    return f"{offset:08x}: {h:48} {c}"

def hexdump(data, start=0, length=None, prefix="", offset=0):
    stop = min(start+length, len(data)) if length else len(data)
    for k in range(start, stop, 16):
        print(prefix+hexdump_line(data[k:min(k+16,stop)], k+offset))

def hexdump_lines(data, start=0, length=None, prefix="", offset=0):
    lines = []
    stop = min(start+length, len(data)) if length else len(data)
    for k in range(start, stop, 16):
        lines.append(prefix+hexdump_line(data[k:min(k+16,stop)], k+offset))
    return lines

def hexdump_str(data, start=0, length=None, prefix="", offset=0):
    return "\n".join(hexdump_lines(data, start, length, prefix, offset))

