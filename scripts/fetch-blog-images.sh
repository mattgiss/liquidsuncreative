#!/usr/bin/env bash
# fetch-blog-images.sh -- download all blog post images from Squarespace CDN
# into their local /blog/<slug>/ folders.
#
# Run this from the repo root on a machine with internet access to Squarespace.
# Safe to re-run -- skips files that already exist.

set -euo pipefail

cd "$(dirname "$0")/.."

failed=0
fetched=0
skipped=0

fetch() {
  local url="$1"; local out="$2"
  if [[ -s "$out" ]]; then
    skipped=$((skipped+1)); return
  fi
  mkdir -p "$(dirname "$out")"
  if curl -fsSL --max-time 30 -o "$out" "$url"; then
    fetched=$((fetched+1))
    echo "  ok   $out"
  else
    failed=$((failed+1))
    echo "  FAIL $url" >&2
    rm -f "$out"
  fi
}

echo "Downloading blog images..."

fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/2c5f84f8-7ead-4e6a-a383-202e46887239/DSC04311.jpg?format=original" "blog/s4u24/DSC04311.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/40e87651-099b-480c-b967-61ad62dd0105/signature.PNG?format=original" "blog/s4u24/signature.PNG"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/db2b68cd-5e3b-4cc4-b6f4-1b2109623d52/DSC04006.jpg?format=original" "blog/s4u23/DSC04006.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/274083c5-3312-4d7e-aca9-56c90cb8e573/DSC03967.jpg?format=original" "blog/s4u23/DSC03967.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/79968c60-7bc6-4cf7-bea1-9d929367d35e/DSC03700.jpg?format=original" "blog/s4u22/DSC03700.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/3ee05f39-d9d4-440f-b1c1-2093481fd590/DSC03793-2.jpg?format=original" "blog/s4u22/DSC03793-2.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/7c6a0c43-6f10-4727-baa2-41f7d3621403/DSC03362.jpg?format=original" "blog/s4u21/DSC03362.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/997fadf3-50b0-4d98-8b25-532db52b2b4e/DSC03508.jpg?format=original" "blog/s4u20/DSC03508.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/9fb230ef-5e88-4b90-955a-f3ed34c7d3ba/DSC03500.jpg?format=original" "blog/s4u20/DSC03500.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/7db8d4e1-48d4-4d04-8e12-328f71f158a3/LSC01131.jpg?format=original" "blog/s4u19/LSC01131.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/1750726991013-5WWRJHUQGDQ62174FEE3/DSC03093.jpg?format=original" "blog/s4u18/DSC03093.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/967e47ea-3b43-4271-8de6-c1a85f8aa45d/LSC01648.jpeg?format=original" "blog/s4u17/LSC01648.jpeg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/7e5d4220-7184-40c7-9851-2449deea8a07/DSC03087.jpg?format=original" "blog/s4u16/DSC03087.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/9349aecb-cbea-42ba-aa1d-d13869a07000/DSC03153-2.jpg?format=original" "blog/s4u15/DSC03153-2.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/211af623-a297-45cd-a2f0-e69532ea4a65/DSC03143.jpg?format=original" "blog/s4u15/DSC03143.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/3c638e0e-9de4-45a2-b694-4a360cd3d993/IMG_0381.JPG?format=original" "blog/s4u14/IMG_0381.JPG"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/dfb0800e-7bc6-43bc-853e-3247ded98ea1/C870D33C-FCC0-4827-B7BB-417106BB5017-9238-0000040F7DC6C178.jpg?format=original" "blog/s4u13/C870D33C-FCC0-4827-B7BB-417106BB5017-9238-0000040F7DC6C178.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/0fee1402-f78c-42b6-ac28-fabab83cb9ca/LSC09457.jpg?format=original" "blog/s4u13/LSC09457.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/919a85b0-692d-4e2e-b5dd-6be14046b442/LSC01247-4.jpg?format=original" "blog/s4u12/LSC01247-4.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/a28c07fe-2e79-4a90-b18c-cbc24bd1c3d9/summitlake.JPG?format=original" "blog/s4u11/summitlake.JPG"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/1745359376431-PHYQINYL0TBDWO5PH5KF/LSC01300.jpg?format=original" "blog/s4u10/LSC01300.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/e1b662f7-019e-4039-bf79-1570e7f4ce32/LSC01294.jpg?format=original" "blog/s4u10/LSC01294.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/cfe60d03-5d2a-416f-95e7-9f96c6d402f3/IMG_0390.jpeg?format=original" "blog/s4u9/IMG_0390.jpeg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/34776c83-2114-4b86-a871-79118f594357/IMG_0770.jpeg?format=original" "blog/s4u9/IMG_0770.jpeg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/e5206460-624c-4505-b5d2-7e9dedf31c97/LSC09222.jpg?format=original" "blog/s4u8/LSC09222.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/3a1b5ab3-8294-43c7-b999-e6deabfd6852/IMG_0940.JPG?format=original" "blog/s4u8/IMG_0940.JPG"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/13ce59f6-94c8-4c12-92a7-a58840720516/IMG_7714.JPG?format=original" "blog/s4u7/IMG_7714.JPG"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/c4313b9d-90b9-4e99-9871-65148f29bca1/IMG_7708+2.JPG?format=original" "blog/s4u7/IMG_7708_2.JPG"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/4e0e3f0f-5bfe-4c19-8ea5-934fe2f43ef0/tempImagesqYpgs.jpg?format=original" "blog/s4u6/tempImagesqYpgs.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/911719c5-2ca0-43cb-9e9f-b62570ad7d9c/IMG_0783.jpeg?format=original" "blog/s4u6/IMG_0783.jpeg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/5432a444-59c2-4ab7-b350-bc4d3f3b65b2/IMG_2319.jpg?format=original" "blog/s4u5/IMG_2319.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/e96553c5-988d-4eb2-bb84-9bac03599114/IMG_6728.jpg?format=original" "blog/s4u5/IMG_6728.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/6c0168a6-bb04-4c28-8351-6881d42a7c55/DSCF5222.jpg?format=original" "blog/s4u4/DSCF5222.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/8cab9461-c9df-46ed-9e3d-ba3d2af8a499/DSCF5229mobile1.jpg?format=original" "blog/s4u4/DSCF5229mobile1.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/c5e9368e-a9f8-4408-b18d-39a35f21c472/DSCF5229.jpg?format=original" "blog/s4u4/DSCF5229.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/04e35f74-bd76-4651-8cff-eb3b71cdc0b0/LSC06624.jpg?format=original" "blog/s4u3/LSC06624.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/f120f5ab-f522-4f1b-8ed2-3dc3387ed5d6/LSC06760mobile.jpg?format=original" "blog/s4u3/LSC06760mobile.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/cd421927-7e9c-4b0d-b681-8bf097c811f0/LSC06760.jpg?format=original" "blog/s4u3/LSC06760.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/1739818089020-OPGKZLJ5CGF8D638T1P3/MFG02891.jpg?format=original" "blog/s4u2/MFG02891.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/d3074011-32a1-45ff-8fc7-686e893e8d49/MFG02944+3.jpg?format=original" "blog/s4u2/MFG02944_3.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/78b027ef-6860-4555-b70c-205d3da23b1a/MFG02944.jpg?format=original" "blog/s4u2/MFG02944.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/1739813560475-KMKNL626TSS9C9W20ZC2/MFG02461.jpg?format=original" "blog/s4u1/MFG02461.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/567cf8c9-6e2c-4d23-a718-63cdbef200a1/MFG02511.jpg?format=original" "blog/s4u1/MFG02511.jpg"
fetch "https://images.squarespace-cdn.com/content/v1/6740cb4588b08d2a45fa92a7/86dbff23-9166-4b63-abc5-2531d6838199/MFG02511+4.JPG?format=original" "blog/s4u1/MFG02511_4.JPG"

echo
echo "Done. fetched=$fetched skipped=$skipped failed=$failed"
if [[ $failed -gt 0 ]]; then exit 1; fi