#!/bin/bash

set -eo pipefail
cd "$(dirname "$0")"

for fn in config/{config.sh,aur_key,signer.key}; do
	if ! [ -f "$fn" ]; then
		echo "ERROR: $fn is missing!"
		exit 1
	fi
done

if [ -z "$GPG_KEY_ID" ] || [ -z "$GITHUB_TOKEN" ]; then
	echo "ERROR: The config.sh file is missing either GPG_KEY_ID or GITHUB_TOKEN!"
	exit 1
fi]

if ! which githubrelease > /dev/null; then
	echo "githubrelease is missing!"
	exit 1
fi

echo "==> Preparing platforms..."
for plat in arch freebsd macos ubuntu windows; do
	"./$plat/prepare.sh"
done

echo "==> Preparing release..."
git checkout master
git merge develop

sed -Ei "s#VERSION = '([0-9\.]+)-dev'#VERSION = '\1'#" knossos/center.py
VERSION="$(cd ..; python setup.py get_version)"

git commit -am "Release $VERSION"
git tag "v$VERSION"


export RELEASE=y
echo "==> Building Windows..."
./windows/build.sh

echo "==> Building macOS..."
./macos/build.sh


echo "==> Pushing to GitHub..."
#git push
#git push --tags

echo "==> Building Ubuntu packages..."
./ubuntu/build.sh

echo "==> Building ArchLinux package..."
./arch/build.sh

echo "==> Building PyPi package..."
./pypi/build.sh

echo "==> Uploading artifacts to GitHub..."
mv windows/
githubrelease release ngld/knossos create "v$VERSION" --name "Knossos $VERSION" --publish windows/dist/{Knossos,update}-"$VERSION".exe macos/dist/Knossos-"$VERSION".dmg

echo "==> Done."
