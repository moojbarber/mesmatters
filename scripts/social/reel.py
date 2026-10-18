#!/usr/bin/env python3
"""Turn a carousel's slide PNGs into an Instagram Reel (1080x1920 MP4).

Each slide holds for a few seconds with a soft crossfade, centred on a navy
9:16 canvas. Silent by design: add a trending sound in the Instagram app if you
want one, or leave it silent (the text carries the message).

Usage: python scripts/social/reel.py <slides_dir> <out.mp4> [seconds_per_slide]
"""
import glob
import os
import subprocess
import sys
import tempfile


def make_reel(slides, out, per=3.2, fade=0.5):
    slides = sorted(slides)
    if not slides:
        raise SystemExit("no slides")
    inputs, filters = [], []
    for i, s in enumerate(slides):
        inputs += ["-loop", "1", "-t", f"{per + fade}", "-i", s]
        filters.append(f"[{i}:v]scale=1080:-2,pad=1080:1920:0:(oh-ih)/2:color=0x0a0820,setsar=1,format=yuv420p,fps=30[v{i}]")
    chain, last, offset = [], "v0", per
    for i in range(1, len(slides)):
        tag = f"x{i}"
        chain.append(f"[{last}][v{i}]xfade=transition=fade:duration={fade}:offset={offset:.2f}[{tag}]")
        last, offset = tag, offset + per
    graph = ";".join(filters + chain)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", graph, "-map", f"[{last}]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
           "-r", "30", out]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    d, out = sys.argv[1], sys.argv[2]
    per = float(sys.argv[3]) if len(sys.argv) > 3 else 3.2
    make_reel(glob.glob(os.path.join(d, "*.png")), out, per)
    print("wrote", out)
