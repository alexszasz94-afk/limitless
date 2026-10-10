/** One manual cycle from the command line: `npm run scrape:once`. */
import { loadEnv } from "./env";
loadEnv();

import { runCycle } from "./engine";

runCycle("manual")
  .then((r) => {
    if (r.skippedBecauseLocked) {
      console.log("Another cycle is running right now (scheduler). Try again in a few minutes.");
      process.exit(2);
    }
    process.exit(0);
  })
  .catch((e) => {
    console.error(e);
    process.exit(1);
  });
