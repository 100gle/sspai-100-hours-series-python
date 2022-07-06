# text watermark
watermark text \
    --font-name=./PingFang.ttc \
    --font-size=30 \
    --color=red \
    --alpha=0.5 \
    --location=all \
    --offset=30 \
    -v "@少数派 sspai" ./testdata/banner.png

# image watermark
watermark image \
    --image-watermark-path ./testdata/logo.png \
    --zoom=0.8 \
    --alpha=0.8 \
    --location=bottom \
    --offset=30 \
    -v ./testdata/banner.png