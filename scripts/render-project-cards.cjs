// Run with Sharp available (npm install --no-save --package-lock=false sharp).
const path = require("node:path");
const sharp = require("sharp");
const assets = path.resolve(__dirname, "../assets");

Promise.all(["nemu", "barmous"].map((brand) =>
  sharp(path.join(assets, `orbit-${brand}.svg`))
    .resize({ width: 1120 })
    .png({ compressionLevel: 9 })
    .toFile(path.join(assets, `orbit-${brand}.png`))
)).catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
