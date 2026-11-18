// news-image-20261118 entrypoint: Node 22, standard library only.
//
// draw.py paints the front page into entry.png next to this file; this
// program copies that image to /output/entry.png for the grader.
// Outside the grader, set MAKEFUN_OUTPUT_DIR instead of /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from "node:fs";
import { join } from "node:path";

const target = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
copyFileSync(new URL("./entry.png", import.meta.url),
             join(target, "entry.png"));
